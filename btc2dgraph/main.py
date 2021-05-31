# Defining main function
import requests
import getopt, sys


def getBlock(blockNum: int):
    block_data = requests.get(f"https://blockchain.info/rawblock/{blockNum}",
                        timeout=2.50)
    return block_data.json()


def json2rdf(block_data):

    ## hand code this part for now, and can refactor into generator form
    ## Refer the structure of the block
    ret = [
        #'<{}> <xid> {} .'.format(block_data['hash'], block_data['hash']), # Declare the object ID as xid
        #'<{}> <dgraph.type> "ExternalType" .'.format(block_data['hash']), # Maintain String value of the block hash
        '_:{} <hash> "{}"^^<xs:string> .'.format(block_data['hash'], block_data['hash']), # Maintain String value of the block hash
        '_:{} <ver> "{}"^^<xs:int> .'.format(block_data['hash'], block_data['ver']),      # Ver is a field (predicate of the block
        '_:{} <prev_block> _:{} .'.format(block_data['hash'], block_data['prev_block']),  # Prev block is a reference, we use the hash value as the key
        '_:{} <prev_block_hash> "{}"^^<xs:string>  .'.format(block_data['prev_block'], block_data['prev_block']), ## note see how we attach str value hash to the node

        '_:{} <mrkl_root> _:{} .'.format(block_data['hash'], block_data['mrkl_root']),
        '_:{} <time> "{}"^^<xs:int> .'.format(block_data['hash'], block_data['time']),
        '_:{} <dgraph.type> "{}" .'.format(block_data['hash'], 'Block'),
    ]
    for nb in block_data['next_block']:
       ret.append('_:{} <next_block> _:{} .'.format(block_data['hash'], nb))

    for trx in block_data['tx']:
        ret.append('_:{} <tx> _:{} .'.format(block_data['hash'], trx['hash'])) # TODO SKIPPING drill down the trx input and output here
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
                block_data = getBlock(int(current_value))
                block_data = json2rdf(block_data)
                print('\n'.join(block_data))
            else:
                print("use -b or --block to specify block num")


    except getopt.error as err:
        # Output error, and return with an error code
        print(str(err), file=sys.stderr)
        sys.exit(2)
