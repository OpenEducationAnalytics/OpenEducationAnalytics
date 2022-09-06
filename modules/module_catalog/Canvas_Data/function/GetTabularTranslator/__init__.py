# Takes a dict with table name, schema keys and 
# returns an object that maps table name to an Azure Data Factory compatible tabular translator.
# The translator is used to map ordinal columns to named columns and includes type information
# Brodie Hicks, 2021.

import logging

from CanvasApi.DataTypes import CanvasToAdfTypeMap

def main(payload: dict) -> str:
    if "schema" not in payload or "table" not in payload:
        raise ValueError("Payload for GetTabularTranslator must include schema and table keys")
    schema = payload['schema']
    tableName = payload['table']

    logging.info(f"GetTabularTranslator called for table: {tableName}")

    if tableName not in schema:
        raise ValueError(f"Table '{tableName}' not found in schema. Found tables: {','.join(schema.keys())}")

    result = {
        tableName: {
            "type": "TabularTranslator",
            "mappings": [
                { 
                    # If we specify datatype for source it should flow through to parquet.
                    # CanvasToAdfTypeMap returns a mapping object; we just overwrite ordinal to indicate which column
                    "source": {**CanvasToAdfTypeMap[col["type"]], **{"ordinal": index}},
                    "sink": {"name": col["name"]}
                }
                for index, col in enumerate(schema[tableName]['columns'], start=1)
            ]
        }
    }

    logging.info(f"Translator for '{tableName}' complete: {result}")

    return result

