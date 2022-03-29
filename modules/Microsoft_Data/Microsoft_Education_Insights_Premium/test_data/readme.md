# Test data
As part of this module, we provide a sample data set that you can use to test this module in your own Synapse environment.

Below contains the data dictionary of all the data that is provided from this test data. This can also be used to better understand what your data provides within the scope of using this module to incorporate your own data.

## Data dictionary
| Table Type | Table Name | Column Name | Description |
|-----------|-------------------|-------------|-------------|
| Activity | Common | SignalType | SharePoint: [Like, Unlike, FileAccessed, FileModified, FileDownloaded, FileUploaded, ShareNotificationRequested, AddedToSharedWithMe, CommentCreated, CommentDeleted, UserAtMentioned] |
| | | | Teams Channel: [PostChannelMessage, ReplyChannelMessage, VisitTeamChannel, ExpandChannelMessage, ReactedWithEmoji] |
| | | | Teams Meetings: [CallRecordSummarized], Assignment Services: [AssignmentEvent, SubmissionEvent], OneNote: [OneNotePageChanged], Reading Progress: [ReadingAssignment, ReadingSubmission], Reflect: [FeedbackSubmitted, CardPosted] |
| | | StartTime | Action time |
| | | UserAgent | Device information |
| | | SignalId | Can only be used to remove potential signal duplications |
| | | SisClassId | Only for tenants running SDS (empty is the sample) |
| | | ClassId | Office Group ID |
| | | ChannelId | Optional, the channel in which action took place. In some cases such as AS signals empty==general. In cases of meetings this identify the channel the meeting took place and hence can be used as a meeting ID |
| | | AppName | Application used: Assignments, SharePoint Online, Teams, OneDrive for Business, OneNote, TeamsMobile |
| | | ActorId | AAD Object ID |
| | | ActorRole | Student - only for tenants running SDS |
| | | SchemaVersion | Technical, used to track data changes or bugs in the export |
| | Assignments | AssignmentId | GUID, identifies the assignment. Can be used to access Graph for additional information |
| | | SubmissionId | GUID, identifies the student submission. Can be used to access Graph for additional information |
| | | SubmissionCreatedTime | The time the submission was created |
| | | Action | Assigned, Updated, Returned, Visited, Submitted, Unsubmitted, Deleted, FeedbackSubmitted |
| | | DueDate | Assignments due date |
| | | ClassCreationDate | Time the class was created (might be empty for now) |
| | | Grade | Optional. Submission grade points. E.g.: 100 (when action=Returned) |
| | Files | SourceFileExtension | For File* signals, captures the type of file:  Aspx, docx, webm, mp4, .docx, .webm, jpg, pptx etc. |
| | Meetings | Meeting Duration | Duration in seconds the student spent in the meeting |
| | Meetings | Meeting session Id  | The meeting session Id  |
| | Meetings | Meeting type  | The meeting type  |
| Roster | AadGroup |  |  |
| | AadGroupMembership | | |
| | AadUser | | |
| | AadUserPersonMapping | | |
| | Course | | |
| | CourseGradeLevel | | |
| | CourseSubject | | |
| | Enrollment | | |
| | Organization | | |
| | Person | | |
| | PersonDemographic | | |
| | PersonDemographicEthnicity | | |
| | PersonDemographicPersonFlag | | |
| | PersonDemographicRace | | |
| | PersonEmailAddress | | |
| | PersonIdentifier | | |
| | PersonOrganizationRole | | |
| | PersonPhoneNumber | | |
| | PersonRelationship | | |
| | RefDefinition | | |
| | Section | | |
| | SectionGradeLevel | | |
| | SectionSession | | |
| | SectionSubject | | |
| | Session | | |
| | SourceSystem | | |
