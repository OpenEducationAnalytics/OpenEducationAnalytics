# Test data

This module includes artificially generated data which matches the format of the three [Microsoft Insights Data Lake Exports](https://docs.microsoft.com/en-us/schooldatasync/enable-education-data-lake-export).
- [Activity Data](https://docs.microsoft.com/en-us/schooldatasync/data-lake-schema-activity) provides data the Insights data lake in their own custom analytics using Azure Data Share services. This includes signal data from O365 applications like Teams, OneNote, OneDrive and Sharepoint. It includes data on education-specific apps like Assignments, Reading Progress, and Reflect.
- [Rostering](https://docs.microsoft.com/en-us/schooldatasync/data-lake-schema-rostering) contains the internal representation of the data that's imported from the institution’s Student Information System (SIS). 
- [Azure Active Directory](https://docs.microsoft.com/en-us/schooldatasync/data-lake-schema-azure-ad) provides an updated copy of your Azure Active Directory (Azure AD) into the Data Lake. The copy of Azure AD assists with user matching between your SIS / SMS and AAD User object.

<strong>Note:</strong> This module contains two sets of test data - one set for mock K-12 data, and one set for mock higher education data. You can choose which test data set to ingest via the module pipeline template; for details see the [test data pipeline instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights/pipeline#pipeline-setup-instructions).

## Data dictionary

### [K-12 Activity Table](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/test_data/k12_test_data/activity/2022-01-28/ApplicationUsage.csv) and [HEd Activity Table](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/test_data/hed_test_data/activity/2022-01-28/ApplicationUsage.csv)

See full details on the [Microsoft SDS documentation](https://docs.microsoft.com/en-us/schooldatasync/data-lake-schema-activity)

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
| SubmissionCreatedTime | DateTime | Time the submission was created. |
| Action | String | Assigned (also for Reading Progress), Updated, Returned, Visited (also for Reading Progress), Submitted, Unsubmitted, Deleted, FeedbackSubmitted (also for Reflect), CardPosted (Reflect), EditMiscue (Reading Progress), Submit (Reading Progress), Attempt (Reading Progress) |
| DueDate |	DateTime | Assignments due date |
| ClassCreationDate | DateTime | Time the class was created |
| Grade | String | Optional. Submission grade points. Example: 100 (when action = Returned) |
| SourceFileExtension | String | For file signals, captures the type of file: aspx, docx, web, mp4, jpg, pptx, etc. |
| Meeting | Duration | TimeSpan	Duration in seconds the student spent in the meeting |
| MeetingSessionID | String | The meeting session ID |
| MeetingType | String | The meeting type |
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
| ![](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/testdata_activity.png)  |

### [K-12 Roster Tables](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights/test_data/k12_test_data/roster/2022-01-28T06-16-22) and [HEd Roster Tables](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights/test_data/hed_test_data/roster/2022-01-28T06-16-22)

See full details on the [Microsoft SDS documentation](https://docs.microsoft.com/en-us/schooldatasync/data-lake-schema-rostering)

| Domain | Table Name | Description |
|-----------|-----------|-----------|
| System | SourceSystem | Indicates which external system the data is coming from. |
| System | RefDefinition |  List of Values (ENUMS) used throughout the system. |
| System | RefTranslation | Allows IT to give translated text for Enums that are added to the system. |
| Time | Session | Represents time in the system. Roles, Sections, and other key objects MUST have a session to identify when objects are available in the system. |
| Organizations | Organization | Represents institution entities. Organizations aren't linked to a session. Only the person's association to an organization and role is linked to a session. |
| People | Person | Rrepresents person records. These aren't linked to a session. Only the person's association to an organization and role is linked to a session. |
| People | PersonRelationship | Indicates a relationship between two people. The relationship is stored in one direction. For instance, if the relationship contact is parent/guardian, the child will be represented by the PersonId column while the contact will be represented in the RelatedPersonId column. |
| People | PersonIdentifier | Person can have multiple identifiers from multiple systems. The identifier from the SIS/SMS, Azure AD, etc. are all stored in this table. |
| People | PersonEmailAddress | Contains the last updated set of information for a given Person. |
| People | PersonPhoneNumber | Contains the last updated set of information for a given Person. |
| People | PersonDemographic | Lifetime is tied to the updated cadence of Person; once Person is no longer being updated, no changes will happen to PersonDemographic or any downstream table. |
| People | PersonDemographicEthnicity | Contains the last updated set of information for a given Person. |
| People | PersonDemographicRace | Contains the last updated set of information for a given Person. |
| People | PersonDemographicPersonFlag | Contains the last updated set of information for a given Person. |
| Academic Groups | Section | Course section records. |
| Academic Groups |SectionSession  | Intersection table between Section and Session. The relationship is many to many. |
| Academic Groups | SectionGradeLevel | Contains the last read version of a given subject. |
| Academic Groups | SectionSubject | Contains the last-provided set of subjects for a given section. |
| Academic Groups | Course | Course records. |
| Academic Groups | CourseGradeLevel | Contains the most-recently sourced set of data for a Course. |
| Academic Groups | CourseSubject | Contains the most-recently sourced set of data for a Course. |
| Affiliations | PersonOrganizationRole | The relationship between a Person, Organization and Session (time). |
| Affiliations | Enrollment | The relationship between a Person and a Section. Time (what is current right now) is also important and is determined by the Section Session relationship. The presence of SectionSession table indicates that enrollments span possibly non-contiguous Sessions. |


### [K-12 Azure Active Directory Tables](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights/test_data/k12_test_data/roster/2022-01-28T06-16-22) and [HEd Azure Active Directory Tables](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights/test_data/hed_test_data/roster/2022-01-28T06-16-22)

See full details on the [Microsoft SDS documentation](https://docs.microsoft.com/en-us/schooldatasync/data-lake-schema-azure-ad)

| Table Name | Description |
|-----------|-----------|
| AADUser | Representation of user records for accounts in Azure AD. |
| AADUserPersonMapping | Present only when Roster data is also present. Mapping between AADUser entries and roster Person entries. |
| AADGroup | Representation of group records in Azure AD. |
| AADGroupMembership | Representation of mapping between AADGroup and AADUser in Azure AD. |
