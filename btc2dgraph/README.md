# BTC Block to RDF

It is not a complete nor fully working version, but it should be helpful on illistrating how to convert BTC RPC result to RDF and import to DGraph through RDF.

The following command generate [RDF N-Quad/Triple data](https://dgraph.io/docs/deploy/fast-data-loading/overview/) to `stdout`.

```bash
./pants run btc2dgraph/main.py   -- -b BLOCKHEIGHT # Where the `BLOCKHEIGHT` is the block heigh, output is attached at the end of this doc
```

## Setup

* Install docker and run `docker-compose up` on the project folder (`docker-compose.yml`). After the dockers are up and make sure the ports are accessible.
* Access to `Ratel` locally through `http://localhost:8000/`, and alternatively you can use [DQL playground](https://play.dgraph.io/?latest)
* Run the code to generate RDF triples.
* In `Mutate` tab, paste the triples to insert. (note, you need to use `set` command, please see [DQL Mutations](https://dgraph.io/docs/mutations/triples/) for reference)

## TODOs

* design a schema that allow partitioned import
* Complete the fields.
* Drill down to Transaction (input and output)
* Work on Xid [xid](https://dgraph.io/docs/mutations/external-ids/) and make hash value become the actual node id.
* Test the precision of numbers.
* Exposing DQL type to GraphQL

## Reference and Tutorial

The learning curve of GraphDB is steep, be patient and start out with some reading would be very helpful.

* [DQL Schema](https://dgraph.io/docs/query-language/schema/).
* [DQL Type](https://dgraph.io/docs/query-language/type-system/)
* [DQL Query](https://dgraph.io/docs/query-language/graphql-fundamentals/)

# Here is an example payload for BTC block (400)

```json

{
  "hash": "000000002dd9919f0a67590bb7c945cb57270a060ce39e85d8d37536a71928c3",
  "ver": 1,
  "prev_block": "0000000006a774e00b730eeba018fbca6673c32753fce367a316f5c9be4332bd",
  "mrkl_root": "ec2ba1a3784dacd6962d53e9266d08d6cca40cce60240954bb3448c6acdf568f",
  "time": 1231902179,
  "bits": 486604799,
  "next_block": [
    "000000005bbced8d14a6ec258a8ab28ae980616e9820437cc3b6d3daff3b7d14"
  ],
  "fee": 0,
  "nonce": 2194885122,
  "n_tx": 1,
  "size": 216,
  "block_index": 400,
  "main_chain": true,
  "height": 400,
  "weight": 864,
  "tx": [
    {
      "hash": "ec2ba1a3784dacd6962d53e9266d08d6cca40cce60240954bb3448c6acdf568f",
      "ver": 1,
      "vin_sz": 1,
      "vout_sz": 1,
      "size": 135,
      "weight": 540,
      "fee": 0,
      "relayed_by": "0.0.0.0",
      "lock_time": 0,
      "tx_index": 5043305043249414,
      "double_spend": false,
      "time": 1231902179,
      "block_index": 400,
      "block_height": 400,
      "inputs": [
        {
          "sequence": 4294967295,
          "witness": "",
          "script": "04ffff001d027502",
          "index": 0,
          "prev_out": null
        }
      ],
      "out": [
        {
          "type": 0,
          "spent": false,
          "value": 5000000000,
          "spending_outpoints": [],
          "n": 0,
          "tx_index": 5043305043249414,
          "script": "4104a165ec80efc0b33577c5c60e8b330fd9e91640c9d56392fc8f96d177fa68555ae41ea11d363fd3395eb0b1dae5d7cee7cc94d8d31d3929475797060def38087dac",
          "addr": "1562oGAGjMnQU5VsppQ8R2Hs4ab6WaeGBW"
        }
      ]
    }
  ]
}
```

## Example output RDF

```bash
❯ ./pants run btc2dgraph: -- -b 100000
Looking into Block 100000
_:000000000003ba27aa200b1cecaad478d2b00432346c3f1f3986da1afd33e506 <hash> "000000000003ba27aa200b1cecaad478d2b00432346c3f1f3986da1afd33e506"^^<xs:string> .
_:000000000003ba27aa200b1cecaad478d2b00432346c3f1f3986da1afd33e506 <ver> "1"^^<xs:int> .
_:000000000003ba27aa200b1cecaad478d2b00432346c3f1f3986da1afd33e506 <prev_block> _:000000000002d01c1fccc21636b607dfd930d31d01c3a62104612a1719011250 .
_:000000000002d01c1fccc21636b607dfd930d31d01c3a62104612a1719011250 <prev_block_hash> "000000000002d01c1fccc21636b607dfd930d31d01c3a62104612a1719011250"^^<xs:string>  .
_:000000000003ba27aa200b1cecaad478d2b00432346c3f1f3986da1afd33e506 <mrkl_root> _:f3e94742aca4b5ef85488dc37c06c3282295ffec960994b2c0d5ac2a25a95766 .
_:000000000003ba27aa200b1cecaad478d2b00432346c3f1f3986da1afd33e506 <time> "1293623863"^^<xs:int> .
_:000000000003ba27aa200b1cecaad478d2b00432346c3f1f3986da1afd33e506 <dgraph.type> "Block" .
_:000000000003ba27aa200b1cecaad478d2b00432346c3f1f3986da1afd33e506 <next_block> _:00000000000080b66c911bd5ba14a74260057311eaeb1982802f7010f1a9f090 .
_:000000000003ba27aa200b1cecaad478d2b00432346c3f1f3986da1afd33e506 <tx> _:8c14f0db3df150123e6f3dbbf30f8b955a8249b62ac1d1ff16284aefa3d06d87 .
_:8c14f0db3df150123e6f3dbbf30f8b955a8249b62ac1d1ff16284aefa3d06d87 <tx_hash> "8c14f0db3df150123e6f3dbbf30f8b955a8249b62ac1d1ff16284aefa3d06d87"^^<xs:string>  .
_:000000000003ba27aa200b1cecaad478d2b00432346c3f1f3986da1afd33e506 <tx> _:fff2525b8931402dd09222c50775608f75787bd2b87e56995a7bdd30f79702c4 .
_:fff2525b8931402dd09222c50775608f75787bd2b87e56995a7bdd30f79702c4 <tx_hash> "fff2525b8931402dd09222c50775608f75787bd2b87e56995a7bdd30f79702c4"^^<xs:string>  .
_:000000000003ba27aa200b1cecaad478d2b00432346c3f1f3986da1afd33e506 <tx> _:6359f0868171b1d194cbee1af2f16ea598ae8fad666d9b012c8ed2b79a236ec4 .
_:6359f0868171b1d194cbee1af2f16ea598ae8fad666d9b012c8ed2b79a236ec4 <tx_hash> "6359f0868171b1d194cbee1af2f16ea598ae8fad666d9b012c8ed2b79a236ec4"^^<xs:string>  .
_:000000000003ba27aa200b1cecaad478d2b00432346c3f1f3986da1afd33e506 <tx> _:e9a66845e05d5abc0ad04ec80f774a7e585c6e8db975962d069a522137b80c1d .
_:e9a66845e05d5abc0ad04ec80f774a7e585c6e8db975962d069a522137b80c1d <tx_hash> "e9a66845e05d5abc0ad04ec80f774a7e585c6e8db975962d069a522137b80c1d"^^<xs:string>  .
```
