Note: This module is deprecated - refer to [Microsoft Insights module for the latest](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Microsoft_Insights)

# M365 module (deprecated)
This module provides a set of assets for the processing of roster and application usage data received from M365 via Azure Data Share.

Note that the setup of [School Data Sync](https://sds.microsoft.com/) is a prerequisite for being able to receive this type of usage data from your M365 tenant.

Also note the availability of [Insights in Microsoft Teams for Education](https://support.microsoft.com/en-us/office/insights-preview-in-microsoft-teams-for-education-leaders-8738d1b1-4e1c-49bd-9e8d-b5292474c347?ui=en-us&rs=en-us&ad=us) which provides usage analytics available via the Insights app within Teams.

You can find short videos about School Data Sync and the Insights app on the [Microsoft School Data Sync channel](https://www.youtube.com/channel/UCA8ZOC7eTfzLlkcFW3imkHg/featured).

# App usage data available via Azure Data Share
In order to begin receiving usage data from M365, the first step is to initiate the Data Share feature within School Data Sync. This feature is in Private Preview and is not visible by default - check with your account manager to have the feature enabled for your tenant.

Once your tenant is enabled to access the Data Share feature, you can follow the steps in [modules/M365/docs/M365 Module Guide.pdf](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/M365/docs/M365%20Module%20Guide.pdf) to get it setup.

The format for the activity data that you will receive in your data lake is shown below.
See [modules/M365/docs](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/M365/docs) for more detailed info and see [modules/M365/test-data](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/M365/test-data/m365/DIPData) for an example data set.

|Category   |Column Name        |Description                                                                                                |
|-----------|-------------------|-----------------------------------------------------------------------------------------------------------|
|Common     |SignalType         |'VisitTeamChannel', 'ReactedWithEmoji', 'PostChannelMessage', 'ReplyChannelMessage', 'ExpandChannelMessage', 'CallRecordSummarized',FileAccessed', 'FileDownloaded','FileModified', 'FileUploaded', 'ShareNotificationRequested', 'CommentCreated', 'UserAtMentioned', 'AddedToSharedWithMe', 'CommentDeleted', 'Unlike', 'OneNotePageChanged', 'AssignmentEvent'|
|           |StartTime          |Action time                                                                                                |
|           |UserAgent          |Device information                                                                                         |
|           |SignalId           |Can be used to remove potential signal duplications                                                        |
|           |SisClassId         |Only for tenants running SDS [empty is the sample]                                                         |
|           |ClassId            |Office Group ID                                                                                            |
|           |ChannelId          |Optional, the channel in which action took place. In some cases such as AS signals empty==general. In cases of meetings this identify the channel the meeting took place and hence can be used as a meeting ID|
|           |AppName            |Application used: Assignments, SharePoint Online, Teams, OneDrive for Business, OneNote, TeamsMobile       |
|           |ActorId            |AAD Object ID                                                                                              |
|           |ActorRole          |Student, Teacher (only for tenants running SDS)                                                                     |
|           |SchemaVersion      |technical, used to track data changes or bugs in the export                                                |
|Assignments|AssignmentId       |GUID, identifies the assignment. Can be used to access Graph for additional information.                   |
|           |SubmissionId       |GUID, identifies the student submission. Can be used to access Graph for additional information.           |
|           |Action             |Assigned,Updated,Returned,Visited,Submitted,Unsubmitted,Deleted,FeedbackSubmitted                          |
|           |DueDate            |Assignments due date                                                                                       |
|           |ClassCreationDate  |Time the class was created (might be empty for now)                                                        |
|           |Grade              |Optional. Submission grade points. E.g.: 100 (when SignalType=SubmissionEvent and Action=Returned)                                        |
|Files      |SourceFileExtension|For File signals, captures the type of file:  Aspx, docx, webm, mp4, .docx, .webm, jpg, pptx etc.         |
|Meeting    |Meeting Duration   |Duration in seconds the student spent in the meeting                                                       |
