python_sources ()
resource(name="schema", source="schema.json")

pex_binary(
    name='validator',
    entry_point='pyjsonsigner.jsonSchemaValidator:main',
    dependencies=[
        ':schema',
    ],
    execution_mode="venv",
)