# Data
The Reading Progress module includes artificially generated data which were derived from the [Microsoft Education Insights](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights/test_data) data sources.

## Data Dictionary
This module creates 2 tables: [ReadingProgress_pseudo](
https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Reading_Progress/data/README.md#readingprogress_pseudo) and [Student_pseudo](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Reading_Progress/data/README.md#student_pseudo).

### ReadingProgress_pseudo
|Column Name | Data Type | Description |
|-----------|-----------|-----------|
| ActorId_pseudonym | String | Azure AD Object ID (pseudonymized) |
| SignalType | String | Reading Progress usage signals such as ReadingSubmission and ReadingAssignment |
| StartTime |	DateTime |	Action time |
|	AppName |	String |	Application used, which is Reading Progress|
| Action | String | Assigned (also for Reading Progress), Updated, Returned, Visited (also for Reading Progress), Submitted, Unsubmitted, Deleted, EditMiscue (Reading Progress), Submit (Reading Progress), Attempt (Reading Progress) |
| ReadingSubmissionWordsPerMinute | Int | Student submission result, reading pace |
| ReadingSubmissionObmissionRate | Int | Per student attempt, rate of words omitted |
| ReadingAssignmentWordCount | Int | Assignment details – number of words in the text of the assignment. Student submission definition – total number of words the user read. |
| ReadingAssignmentFleschKincaidGradeLevel | Real | Only in the Assignment definition signals (not per student attempt) |
| ReadingAssignmentLanguage | String | Only in the assignment definition signals (not per student attempt) |
| ReadingSubmissionRepetitionsRate | Int | Per student attempt, rate of words repeated |
| ReadingSubmissionMispronunciationRate | Int | Per student attempt, rate of words mispronounced |
| ReadingSubmissionInsertionsRate | Int | Per student attempt, rate of words inserted |
| ReadingSubmsssionAccuracyScore | Real | Student submission result, reading progress accuracy score |
| ReadingSubmissionAttemptNumber | Int | Index of student attempts |

### Student_pseudo
|Column Name | Data Type | Description |
|-----------|-----------|-----------|
| StudentId_internal_pseudonym | String | Student's internal ID (pseudonymized) |
| StudentId_external_pseudonym | String | Student's external ID (pseudonymized) |
| Surname | String | Student's surname |
| GivenName | String | Student's given name |
| MiddleName | String | Student's middle name |
| PersonRole | String | The person's role |
| StudentGrade | String | Student's grade level |
| OrganizationId | String | Organization ID |
| OrganizationName | String | Organization name |
