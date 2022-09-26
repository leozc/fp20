python_sources(
    name="uniwatcher_lib",
    sources=[
        "__init__.py",
        "main.py",
        "watcher.py",
    ],
)

pex_binary(
    dependencies=[":uniwatcher_lib", ":graphql_schema"],
    entry_point="uniwatcher.main",
    name="uniwatcher",
    execution_mode="venv",
)

resources(
    name="graphql_schema",
    # load from https://raw.githubusercontent.com/Uniswap/uniswap-v3-subgraph/main/schema.graphql
    sources=["schema.graphql"],
)
