
### Note: We are currently working on releasing a sample of test data for other technical assets to consume.




# Data

## Pseudonymization of End User Identifiable Information
To protect students’ identity and comply with GDPR and CCPA requirements, it is required that end user identifiable information like names, email addresses, etc., are pseudonymized. The [OEA framework](https://github.com/microsoft/OpenEduAnalytics/tree/main/framework/synapse) incorporates notebooks and pipelines for pseudonymizing columns in the data sets used for this package. 

The OEA pseudonymization operations are:
- **hash-no-lookup or hnl:** This means that the lookup can be performed against a different table, so no lookup is needed
- **hash or h:** This will hash the column and create a lookup table as well
- **mask or m:** This will mask the column and will not create a lookup table
- **no-op or x:** No operation will be performed so the column will remain as it is



## Local Data Source Mapped to Theoretical Construct 
For similar use cases to address students' well-being needs, users should engage and partner with stakeholders to find out what would be the appropriate data items to use. The data items should be collected with consent of relevant stakeholders (e.g. students and families), supported by relevant literature and subject to the local context, regulations, and laws. For the purpose of illustration, we listed data items collected by the Tasmania Department of Education and features used by Microsoft Education under a joint research agreement to proactively address students' well-being needs.  

- **Attendance** – Research shows that unauthorized absence is an indicator of other risk factors

This is where specific fields from available datasets should be mapped to the theoretical constructs important to student well-being.

In the Tasmanian dataset, we create features indicating patterns of student attendance at school: the minimum, average and maximum number of consecutive days of absence and/or presence at school. 

- **Assessment scores** – Reflective of development and academic learning outcomes

This is where specific fields from available datasets should be mapped to the theoretical constructs important to student well-being.

In the Tasmanian dataset, we
-	select assessment scores of certain subjects based on data quality (proportion of missing value, whether an assessment of a subject is mandatory / optional, consistency of assessment criterion).
-	create features represented by the earliest assessment score and latest assessment score for each student.

- **Medical Conditions** – Represents the health context of a student

This is where specific fields from available datasets should be mapped to the theoretical constructs important to student well-being.

In the Tasmanian dataset, we
-	create features indicating seriousness of medical conditions;
-	create features indicating whether the student used to have medical condition that raised alert.

- **Protection Order** – Represents physical well-being

This is where specific fields from available datasets should be mapped to the theoretical constructs important to student well-being.

In the Tasmanian dataset, we count the number of protection orders of each individual.

- **Disability** – Represents additional health context

This is where specific fields from available datasets should be mapped to the theoretical constructs important to student well-being.

In the Tasmanian dataset, we create indicators of whether a student used to have certain disability registered in the system.

- **Disciplinary** – Represents disciplinary sanctions against a student

This is where specific fields from available datasets should be mapped to the theoretical constructs important to student well-being.

In the Tasmanian dataset, we
flag on whether a student had certain disciplinary sanctions;
-	count the number of days a student was under a certain type of sanction.

- **Observed Behaviors** – Represents negative behaviors a student had in a specific timeframe

This is where specific fields from available datasets should be mapped to the theoretical constructs important to student well-being.

In the Tasmanian dataset, we
-	count number of negative behaviors recorded of a student during a specific timeframe;
-	count actions taken against the student during a specific timeframe.



