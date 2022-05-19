# Static map of Canvas Data Types -> Azure Data Factory Copy Activity types.
# Brodie Hicks, 2021.

from collections import defaultdict

CanvasToAdfTypeMap = defaultdict(lambda: {"type": "string"}, # Default to string for unknown types
    {
        "bigint": {"type": "int64" },
        "varchar": {"type": "string"},
        "int": {"type": "int32"},
        "text": {"type": "string"},
        "timestamp": {"type": "datetimeoffset", "culture": "en-us", "format": "yyyy-MM-dd HH:mm:ss.fff"},
        "double precision": {"type": "double"},
        "boolean": {"type": "boolean"},
        "date": {"type": "datetimeoffset", "culture": "en-us", "format": "yyyy-MM-dd"},
        "integer": {"type": "int32"},
        "enum": {"type": "string"},
        "guid": {"type": "guid"},
        "datetime": {"type": "datetimeoffset", "culture": "en-us", "format": "yyyy-MM-dd HH:mm:ss.fff"}
    }
)