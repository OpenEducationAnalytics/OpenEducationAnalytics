# M365 module
This module provides a set of assets for the processing of roster and application usage data received from M365 via Azure Data Share.

Note that the setup of [School Data Sync](https://sds.microsoft.com/) is a prerequisite for being able to receive this type of usage data from your M365 tenant.

Also note the availability of [Insights in Microsoft Teams for Education](https://support.microsoft.com/en-us/office/insights-preview-in-microsoft-teams-for-education-leaders-8738d1b1-4e1c-49bd-9e8d-b5292474c347?ui=en-us&rs=en-us&ad=us) which provides usage analytics available via the Insights app within Teams.

You can find short videos about School Data Sync and the Insights app on the [Microsoft School Data Sync channel](https://www.youtube.com/channel/UCA8ZOC7eTfzLlkcFW3imkHg/featured).

# Update on activity data format
The format for the activity data has been modified to provide more granular signals rather than the previous format which was an hourly aggregate of activity per user.
The assets in this module will be updated to incorporate this change in the coming weeks.
Provided below is the schema for the new format:

|Category   |Column Name        |Description                                                                                                |
|-----------|-------------------|-----------------------------------------------------------------------------------------------------------|
|Common     |SignalType         |'VisitTeamChannel', 'ReactedWithEmoji', 'PostChannelMessage', 'ReplyChannelMessage', 'ExpandChannelMessage', "CallRecordSummarized',FileAccessed', 'FileDownloaded','FileModified', 'FileUploaded', 'ShareNotificationRequested', 'CommentCreated', 'UserAtMentioned', 'AddedToSharedWithMe', 'CommentDeleted', 'Unlike'|
|           |StartTime          |Action time                                                                                                |
|           |UserAgent          |Device information                                                                                         |
|           |SignalId           |Can be used to remove potential signal duplications                                                        |
|           |SisClassId         |Only for tenants running SDS [empty is the sample]                                                         |
|           |ClassId            |Office Group ID                                                                                            |
|           |ChannelId          |Optional, the channel in which action took place. In some cases such as AS signals empty==general.         |
|           |                   |In cases of meetings this identify the channel the meeting took place and hence can be used as a meeting ID|
|           |AppName            |Application used: Assignments, SharePoint Online, Teams, OneDrive for Business, OneNote, TeamsMobile       |
|           |ActorId            |AAD Object ID                                                                                              |
|           |ActorRole          |Student - only for tenants running SDS                                                                     |
|           |SchemaVersion      |technical, used to track data changes or bugs in the export                                                |
|Assignments|AssignmentId       |GUID, identifies the assignment. Can be used to access Graph for additional information.                   |
|           |SubmissionId       |GUID, identifies the student submission. Can be used to access Graph for additional information.           |
|           |Action             |Assigned,Updated,Returned,Visited,Submitted,Unsubmitted,Deleted,FeedbackSubmitted                          |
|           |DueDate            |Assignments due date                                                                                       |
|           |ClassCreationDate  |Time the class was created (might be empty for now)                                                        |
|           |Grade              |Optional. Submission grade points. E.g.: 100 (when action=Returned)                                        |
|Files      |SourceFileExtension|For File* signals, captures the type of file:  Aspx, docx, webm, mp4, .docx, .webm, jpg, pptx etc.         |
|Meeting    |Meeting Duration   |Duration in seconds the student spent in the meeting                                                       |
