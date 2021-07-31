from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

def execute(api_url: str, query: str, gqlschema = None) -> dict:
  ## this transport can be websock?
  sample_transport=RequestsHTTPTransport(
      url=api_url,
      use_json=True,
      headers={
          "Content-type": "application/json",
      },
      verify=True,
      retries=3,
  )

  client = Client(
      transport=sample_transport,
      # enable one line below
      fetch_schema_from_transport=True,
      #schema=schema 
  )

  query = gql(query)
  return (client.execute(query))
  