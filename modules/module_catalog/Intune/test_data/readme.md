# Test data
As part of this module, we provide a sample data set that you can use to test this module in your own Synapse environment.

## Data dictionary
The test data consists of the following tables and columns:

| Table Name | Column Name | Description |
|-----------|-------------------|-------------|
| devices/\*.csv | DeviceName | Name of the device |
| | ManagedBy | Lists the service that manages the device (for the case of this module, defaulted to "Intune") |
| | Ownership | Lists ownership of the device (e.g. Corporate, Personal, Unknown) |
| | Compliance | Identifies whether the device is compliant |
| | OS | Lists the Operating System of the device (i.e. Windows, macOS, iOS/iPadOS, Android) |
| | OSVersion | Lists the OS version the device is using since the time of the report |
| | LastCheckIn | Timestamp of when the device last communicated with Intune |
| | PrimaryUserUPN | Identifies the primary user's UserPrincipalName (email address) for the user linked to the device |
| | DeviceID | Identifies the device's ID from Intune |

