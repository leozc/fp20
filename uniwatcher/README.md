# Readme
This is a simple program to query Uniswap v3 with position Id through (TheGraph)[https://thegraph.com/]
## Before you can run
1. Get API Key through [TheGraph](https://thegraph.com/studio/apikeys/)
2. deposit some GRT to TheGraph so you can use the API

## To Build and Run

```bash
export posid=1234
./pants run uniwatcher/src/python/uniwatcher: -- --posid=$posid --apikey=$THEGRAPHAPIKEY
```

Output

    {
    "position": {
        "collectedFeesToken0": "0.35184979",
        "collectedFeesToken1": "140.010921398202047158",
        "depositedToken0": "4.27571339",
        "depositedToken1": "68.651471069050153191",
        "id": "68571",
        "owner": "xx",
        "pool": {
        "id": "yy",
        "token0": {
            "name": "Wrapped BTC",
            "symbol": "WBTC"
        },
        "token0Price": "0.05867501324469763913850100898824112",
        "token1": {
            "name": "Wrapped Ether",
            "symbol": "WETH"
        },
        "token1Price": "17.04302981287129567441775108425992"
        },
        "transaction": {
        "id": "ff"
        },
        "withdrawnToken0": "0.16489126",
        "withdrawnToken1": "136.771014970764203089"
    }
    }