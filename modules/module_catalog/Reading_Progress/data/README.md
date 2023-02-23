# Data
The Reading Progress module includes artificially generated data which were derived from the [Microsoft Education Insights](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights/test_data) data sources.

## Data Dictionary
This module creates 3 tables: [ReadingProgress_activity](
https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Reading_Progress/data/README.md#readingprogress_activity), [Student](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Reading_Progress/data/README.md#student) and Student_lookup (dictionary of mapping hashed/masked fields to raw data).

### ReadingProgress_activity
|Column Name | Data Type | Description |
|-----------|-----------|-----------|
| AadUserId_pseudonym | String | Azure AD User Object ID (pseudonymized) |
| SignalId | String | Unique GUID per signal. Can be used to remove potential signal duplications |
| SignalType | String | Reading Progress usage signals such as ReadingSubmission and ReadingAssignment |
| StartTime |	DateTime |	Action time |
|	AppName |	String |	Application used, which is Reading Progress |
| Action | String | Assigned (also for Reading Progress), Updated, Returned, Visited (also for Reading Progress), Submitted, Unsubmitted, Deleted, EditMiscue (Reading Progress), Submit (Reading Progress), Attempt (Reading Progress) |
| AadGroupId | String | Office Group ID; currently nulled in the Insights K-12 test data and will be updated to include this |
| ReadingSubmissionWordsPerMinute | Int | Student submission result, reading pace |
| ReadingSubmsssionAccuracyScore | Real | Student submission result, reading progress accuracy score |
| ReadingSubmissionRepetitionsCount | Int | Per student attempt, number of words repeated |
| ReadingSubmissionInsertionsCount | Int | Per student attempt, number of words inserted |
| ReadingSubmissionMispronunciationCount | Int | Per student attempt, number of words mispronounced |
| ReadingSubmissionObmissionCount | Int | Per student attempt, number of words omitted |
| ReadingSubmissionAttemptNumber | Int | Index of student attempts |
| ReadingAssignmentWordCount | Int | Assignment details – number of words in the text of the assignment. Student submission definition – total number of words the user read. |
| ReadingAssignmentFleschKincaidGradeLevel | Real | Only in the Assignment definition signals (not per student attempt) |
| ReadingAssignmentLanguage | String | Only in the assignment definition signals (not per student attempt) |
| ReadingSubmissionRepetitionsRate | Int | Per student attempt, rate of words repeated |
| ReadingSubmissionMispronunciationRate | Int | Per student attempt, rate of words mispronounced |
| ReadingSubmissionInsertionsRate | Int | Per student attempt, rate of words inserted |
| ReadingSubmissionObmissionRate | Int | Per student attempt, rate of words omitted |


### Student
|Column Name | Data Type | Description |
|-----------|-----------|-----------|
| PersonId_pseudonym | String | Insights Rostering Person ID (pseudonymized) |
| AadUserId_pseudonym | String | Azure AD User Object ID (pseudonymized) |
| Surname | String | Student's surname |
| GivenName | String | Student's given name |
| MiddleName | String | Student's middle name |
| PersonRole | String | The person's role |
| StudentGrade | String | Student's grade level |
| OrganizationId | String | Organization ID |
| OrganizationName | String | Organization name |

## Data Model
The Reading Progress module is made up of 2 tables where Student is the dimension table and ReadingProgress_activity is the fact table.
![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Reading_Progress/docs/images/rp_module_v0.1_pbi_data_model.png)
