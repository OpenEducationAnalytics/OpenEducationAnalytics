# Microsoft Insights
This module provides a set of assets for the processing of roster and application usage data received from M365 via Azure Data Share.

Note that the setup of [School Data Sync](https://sds.microsoft.com/) is a prerequisite for being able to receive this type of usage data from your M365 tenant.

Also note the availability of [Insights in Microsoft Teams for Education](https://support.microsoft.com/en-us/office/insights-preview-in-microsoft-teams-for-education-leaders-8738d1b1-4e1c-49bd-9e8d-b5292474c347?ui=en-us&rs=en-us&ad=us) which provides usage analytics available via the Insights app within Teams.

You can find short videos about School Data Sync and the Insights app on the [Microsoft School Data Sync channel](https://www.youtube.com/channel/UCA8ZOC7eTfzLlkcFW3imkHg/featured).

# App usage data available via Azure Data Share
In order to begin receiving usage data from M365, the first step is to initiate the Data Share feature within School Data Sync. This feature is in Private Preview and is not visible by default - check with your account manager to have the feature enabled for your tenant.

# Setup
In order to install this module, import the MSInsights_py.ipynb and process_MSInsights_data.ipynb notebooks into Synapse Studio, then open the process_MSInsights_data notebook and follow the directions there.

# SignalType data
The current set of signal types coming in the app usage data is:
* UserAtMentioned
* ReactedWithEmoji
* ReplyChannelMessage
* FileAccessed
* VisitTeamChannel
* SubmissionEvent
* ShareNotificationRequested
* ExpandChannelMessage
* PostChannelMessage
* OneNotePageChanged
* FileDownloaded
* CallRecordSummarized
* FileModified
* CommentCreated
* AddedToSharedWithMe
* FileUploaded
* AssignmentEvent
