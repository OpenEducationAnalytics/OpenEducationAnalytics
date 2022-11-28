
# Data

## Pseudonymization of End User Identifiable Information
To protect students’ identity and comply with GDPR and CCPA requirements, it is required that end user identifiable information like names, email addresses, etc., are pseudonymized. The [OEA framework](https://github.com/microsoft/OpenEduAnalytics/tree/main/framework/synapse) incorporates notebooks and pipelines for pseudonymizing columns in the data sets used for this package. 

The OEA pseudonymization operations are:
- **hash-no-lookup or hnl:** This means that the lookup can be performed against a different table, so no lookup is needed
- **hash or h:** This will hash the column and create a lookup table as well
- **mask or m:** This will mask the column and will not create a lookup table
- **no-op or x:** No operation will be performed so the column will remain as it is
