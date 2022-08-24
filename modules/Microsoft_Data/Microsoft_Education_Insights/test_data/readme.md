# Test data

This module includes artificially generated data which matches the format of the three [Microsoft Insights Data Lake Export](https://docs.microsoft.com/en-us/schooldatasync/enable-education-data-lake-export).
- [Activity Data](https://docs.microsoft.com/en-us/schooldatasync/data-lake-schema-activity) provides data the Insights data lake in their own custom analytics using Azure Data Share services. This includes signal data from O365 applications like Teams, OneNote, OneDrive and Sharepoint. It includes data on education-specific apps like Assignments, Reading Progress, and Reflect.
- [Rostering](https://docs.microsoft.com/en-us/schooldatasync/data-lake-schema-rostering) contains the internal representation of the data that's imported from the institution’s Student Information System (SIS). 
- [Azure Active Directory](https://support.clever.com/hc/s/articles/360049642311?language=en_US#h_7698d144-7ceb-4d63-88b8-e9ca2aa378d2) provides an updated copy of your Azure Active Directory (Azure AD) into the Data Lake. The copy of Azure AD assists with user matching between your SIS / SMS and AAD User object.

## Data dictionary

### [Activity Table](https://github.com/cviddenKwantum/OpenEduAnalytics/blob/main/modules/Microsoft_Data/Microsoft_Education_Insights/test_data/activity/2021-06-02/ApplicationUsage.csv)

See full details on the [icrosoft SDS documentation](https://docs.microsoft.com/en-us/schooldatasync/data-lake-schema-activity)

|Column Name | Data Type | Description |
|-----------|-----------|-----------|

| SignalType | String | M365 app usage signals such as FileDownloaded, CommentCreated, VisitTeamChannel, AssignmentEvent, ReadingSubmission |
| StartTime |	DateTime |	Action time |
| UserAgent |	String |	Device information |
| SignalId | String |	Can be used to remove potential signal duplications |
| SisClassId | String |	Only for tenants running SDS [empty is the sample] |
| ClassId |	String | Office Group ID |
|	ChannelId | String | Optional, the channel in which action took place. In some cases such as AS signal empty==general. In cases of meetings this will identify the channel the meeting took place and hence can be used as a meeting ID. |
|	AppName |	String |	Application used: Assignments, SharePoint Online, Teams, OneDrive for Business, OneNote, TeamsMobile, ReadingProgress, Reflect |
| ActorId |	String | Azure AD Object ID |
| ActorRole |	String | Student – only for tenants running SDS |
| SchemaVersion | Real | Technical, used to track data changes or bugs in the export |
| AssignmentId | String | GUID, identifies the assignment. Can be used to access Graph for more information. |
| SubmissionId | String | GUID, identifies the student submission. Can be used to access Graph for more information. |
| SubmissionCreatedTime	DateTime	Time the submission was created.
| Action | String | Assigned (also for Reading Progress), Updated, Returned, Visited (also for Reading Progress), Submitted, Unsubmitted, Deleted, FeedbackSubmitted (also for Reflect), CardPosted (Reflect), EditMiscue (Reading Progress), Submit (Reading Progress), Attempt (Reading Progress) |
| DueDate |	DateTime | Assignments due date |
| ClassCreationDate | DateTime | Time the class was created |
| Grade | String | Optional. Submission grade points. Example: 100 (when action = Returned) |
| SourceFileExtension | String | For file signals, captures the type of file: aspx, docx, web, mp4, jpg, pptx, etc. |
| Meeting | Duration | TimeSpan	Duration in seconds the student spent in the meeting |
| Meeting Session ID | String | The meeting session ID |
| Meeting type | String | The meeting type |
| ReadingSubmissionWordsPerMinute | Int | Student submission result, reading pace |
| ReadingSubmsssionAccuracyScore | Real | Student submission result, reading progress accuracy score |
| ReadingSubmissionMispronunciationCount | Int | Per student attempt, number of works mispronounced |
| ReadingSubmissionRepetitionsCount | Int | Per student attempt, number of words repeated |
| ReadingSubmissionInsertionsCount | Int | Per student attempt, number of words inserted |
| ReadingSubmissionObmissionCount | Int | Per student attempt, number of works omitted |
| ReadingSubmissionAttemptNumber | Int | Index of student attempts |
| ReadingAssignmentWordCount | Int | Assignment details – number of works in the text of the assignment. Student submission definition – total number of words the user read. |
| ReadingAssignmentFleschKincaidGradeLevel | Real | Only in the Assignment definition signals (not per student attempt) |
| ReadingAssignmentLanguag | String | Only in the assignment definition signals (not per student attempt) |

| Activity Table Test Data  | 
|:-------------------------:|
| ![](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/Digital_Learning_Apps_and_Platforms/Clever/docs/images/test_data_dailypart.png)  |

Notes: 
1) The active use of Clever is currently defined if the user performs any of the following actions:
    - Log into their district Clever account
    - Access an application by clicking on the app icon in the Clever Portal
    - Access an application through an Instant Login Link
    - Logged in to an application using a Log in with Clever button
    - Accessing any link added to the Clever portal by the district, school, or teacher
2) The following columns are pseudonomized in the test data and production data will appear different: sis_id, clerver_user_id, clever_school_id
3) See the [Clever Participation Reports](https://support.clever.com/hc/s/articles/360049642311) documentation for more details.
