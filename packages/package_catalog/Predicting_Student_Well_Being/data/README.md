
# Data

## Pseudonymization of End User Identifiable Information
To protect students’ identity, it is required that the personal identifiable information of students like names, email addresses, etc., are pseudonymized. The [OEA framework](https://github.com/microsoft/OpenEduAnalytics/blob/main/framework/synapse/notebook/OEA_py.ipynb) incorporates notebooks and pipelines for pseudonymizing columns in the data set. 

The OEA pseudonymization operations are:
- hash-no-lookup or hnl: This means that the lookup can be performed against a different table, so no lookup is needed
- hash or h: This will hash the column and create a lookup table as well
- mask or m: This will mask the column and will not create a lookup table
- no-op or x: No operation will be performed so the column will remain as it is
