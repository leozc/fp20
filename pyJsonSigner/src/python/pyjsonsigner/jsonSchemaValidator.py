import json
import jsonschema
import os

schema_path = os.path.dirname(os.path.abspath(__file__)) + '/schema.json'
# Load the JSON schema from an external file
with open(schema_path, 'r') as f:
    schema = json.load(f)

# Example JSON object to validate
json_obj = {
    "community": "chainmedata",
    "version": "openmedata01",
    "revision": 1,
    "schema":
    "https://github.com/openchainmeta/chainmetareader/doc/dataschema/xyz.md",
    "chainmetadata": {
        "provider": {
            "provider_name":
            "chaintool",
            "provider_pubkey":
            "111111",
            "artifact": [{
                "uri": "http://xxxx",
                "fileformat": "json",
                "signature": "xxxxx"
            }, {
                "uri": "http://xxxx",
                "fileformat": "parquet",
                "signature": "yyy"
            }, {
                "uri": "http://xxxx-delta",
                "fileformat": "parquet",
                "signature": "yyy",
                "delta-from": "http://xxxx"
            }]
        }
    }
}

def main():
    try:
        jsonschema.validate(json_obj, schema)
        print("Validation successful!")
    except jsonschema.exceptions.ValidationError as e:
        print("Validation error:", e)


if __name__ == '__main__':
    # Validate the JSON object against the schema
    main()