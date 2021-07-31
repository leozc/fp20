
from string import Template

QUERY=Template('''
{
  position(id:"$postid") {
    
    id,
    owner,
    depositedToken0,
    depositedToken1,
    withdrawnToken0,
    withdrawnToken1,
    collectedFeesToken0,
    collectedFeesToken1
    pool{
      id,
      token0{
        name,
        symbol
      },
      token0Price,
      token1{
        symbol
        name
      },
      token1Price,
    }
  
    transaction {
      id
    }

    
  }
}
''')


if __name__ == "__main__":
  import datetime
  import argparse
  import importlib.resources
  import json 	
  from uniwatcher import watcher
  
  API_URL="""https://gateway.thegraph.com/api/[api-key]/subgraphs/id/0x9bde7bf4d5b13ef94373ced7c8ee0be59735a298-2"""
  

  parser = argparse.ArgumentParser(description='Fetch stat for the Uniswap position, thegraph API key required')
  parser.add_argument("-i",
                      "--posid",
                      type=int,
                      help="a valid position id",
                      required='True',
                      default=0)
  parser.add_argument("-k",
                      "--apikey",
                      type=str,
                      help="TheGraphAPI Key",
                      required='True',
                      default=0)

  args = parser.parse_args()
  
  if args.posid is None or args.apikey is None:
      exit(-1)

  #OWNER = '0xbecd4fae08d4c6e271b709a6551bf337c6e6060d' # Flash Boy: 0xbec
  q = QUERY.substitute(postid=args.posid)
  API_URL = API_URL.replace("[api-key]", args.apikey)
  
  # turn on/off to print the API url with token 
  #print(API_URL)
  schema = importlib.resources.read_text(__package__, "schema.graphql")

# Serializing json
  r = watcher.execute(API_URL, q, gqlschema = schema)
  r["queryUtcTimeStamp"]=str(datetime.datetime.now())
  json_object = json.dumps(r, indent = 2)


  print(json_object)
