# BTC Block to RDF

The following command generate [RDF N-Quad/Triple data](https://dgraph.io/docs/deploy/fast-data-loading/overview/) to standard out

```bash
./pants run btc2dgraph/main.py   -- -b BLOCKHEIGHT
```

Where the `BLOCKHEIGHT` is the block heigh.

## TO DO

* design a schema
* Fill more fields
* Drill down to Transaction
* Work on Xid [xid] (https://dgraph.io/docs/mutations/external-ids/) and make hash value become the actual node id.

## Here is an example payload for BTC block (400)

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
