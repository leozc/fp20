# Defining main function
import requests
import getopt, sys


def getBlock(blockNum: int):
    data = requests.get(f"https://blockchain.info/rawblock/{blockNum}",
                        timeout=2.50)
    return data.json()


def json2rdf(data):

    ## hand code this part for now, and can refactor into generator form
    ## Refer the structure of the block
    ret = [
        #'<{}> <xid> {} .'.format(data['hash'], data['hash']), # Declare the object ID as xid
        #'<{}> <dgraph.type> "ExternalType" .'.format(data['hash']), # Maintain String value of the block hash
        '<{}> <hash> "{}"^^<xs:string> .'.format(data['hash'], data['hash']), # Maintain String value of the block hash
        '<{}> <ver> "{}"^^<xs:int> .'.format(data['hash'], data['ver']),      # Ver is a field (predicate of the block
        '<{}> <prev_block> _:{} .'.format(data['hash'], data['prev_block']),  # Prev block is a reference, we use the hash value as the key
        '_:{} <prev_block_hash> "{}"^^<xs:string>  .'.format(data['prev_block'], data['prev_block']), ## note see how we attach str value hash to the node

        #'_:{} <next_block> [] .'.format(data['hash'], {data['next_block']}),
        '_:{} <mrkl_root> _:{} .'.format(data['hash'], data['mrkl_root']),
        '_:{} <time> "{}"^^<xs:int> .'.format(data['hash'], data['time']),
        '_:{} <dgraph.type> "{}" .'.format(data['hash'], 'Block'),
    ]

    for trx in data['tx']:
        ret.append('_:{} <tx> _:{} .'.format(data['hash'], trx['hash'])) #TODO SKIPPING drill down the trx input and output here
        ret.append('_:{} <tx_hash> "{}"^^<xs:string>  .'.format(trx['hash'], trx['hash']))

    return ret


# Using the special variable
# __name__
if __name__ == "__main__":

    short_options = "hb:v"
    long_options = ["help", "block=", "verbose"]
    try:
        full_cmd_arguments = sys.argv

        argument_list = full_cmd_arguments[1:]
        arguments, values = getopt.getopt(argument_list, short_options,
                                          long_options)
        for current_argument, current_value in arguments:
            if current_argument in ("-v", "--verbose"):
                print("Enabling verbose mode", file=sys.stderr)
            elif current_argument in ("-b", "--block"):
                print ("Looking into Block {}".format(int(current_value)), file=sys.stderr)
                data = getBlock(int(current_value))
                data = json2rdf(data)
                print('\n'.join(data))
            else:
                print("use -b or --block to specify block num")


    except getopt.error as err:
        # Output error, and return with an error code
        print(str(err), file=sys.stderr)
        sys.exit(2)
