# Pipeline

1) Import pipeline/Clever.json
>This pipeline is high level. It will call Copy_all_from_SFTP to ingest new data into stage1np. It will then run the OEA_Connector.ipynb to process the data into stage 2p and stage 2np. Next, the pipeline will create the Lake db and SQL db. 
2) Import pipeline/Copy_all_from_SFTP.json
> This pipeline will call the Copy_from_SFTP for each folder provided in the SftpFolderNames parameter.
3) Import pipeline/Copy_from_SFTP.json
> This pipeline will get the metadata for Clevers SFTP server and then check to see which ones are missing in stage1np. It will then ingest new data into stage1np

# Linked Services
1) Import pipeline/LS_OnPrem_SFTP.json
> This linked service can be used to dynamically connect to SFTP servers using parameters
2) Import pipeline/LS_OnPrem_SFTP_CSV.json
> This linked service is connecting to the datalake and sinking files as csvs
