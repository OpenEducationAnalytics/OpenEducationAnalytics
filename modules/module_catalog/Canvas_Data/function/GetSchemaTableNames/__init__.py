# Helper to extract an object containing tableName -> schema mappings
# Necessary as the default schema format includes object names as the key, not table names.
# Brodie Hicks, 2021.

def main(schema: dict) -> dict:
    return {
        v['tableName']: {**v, **{"entity_name": k}}
        for k, v in schema.items()
    }
