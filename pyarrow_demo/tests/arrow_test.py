import pyarrow.parquet as pq
import numpy as np
import pandas as pd
import pyarrow as pa

import pytest


def test_df():
    df = pd.DataFrame({'one': [-1, np.nan, 2.5],
                    'two': ['foo', 'bar', 'baz'],
                    'three': [True, False, True]},
                    index=list('abc'))

    table = pa.Table.from_pandas(df)

    import pyarrow.parquet as pq
    pq.write_table(table, 'example.parquet')
    assert pq.read_table('example.parquet').equals(table)

# write a unit test for printing helliworld
def test_hello_world():
    print("Hello World")
