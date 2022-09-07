# Power BI Template

The i-Ready module Power BI template enables users to quickly explore iReady Assessment Reports data. There are two options for exploring this module Power BI template.
- [Power BI with test data](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/iReady/powerbi/iReady%20Module%20Dashboard%20TestData.pbix): Power BI templated with module test data imported locally. 
- [Power BI with direct query](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/iReady/powerbi/iReady%20Module%20Dashboard%20DirectQuery.pbix): Power BI template connected to a Synapse workspace data source. See instructions below to setup.

See [Power BI setup instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/iReady/powerbi#power-bi-setup-instructions) below for details.

## Dashboard Explanation

The i-Ready module Power BI template consists of a single dashboard which summarizes student lesson learning progress. 

There are two buttons: the ELA button summarizes the student lesson results in ELA, while the Math button summarizes the student lesson results in Math, independently.

#### Student Lesson Results Summary Dashboard:
- <em>Lesson Results by Lesson Grade-Level compared to Student Grade</em> - shows a table that breaks-down the student grades (i.e. K, 1, 2) compared to the lesson grade-level, by distinctly counting the number of students that passed or failed a lesson.
- <em>Comprehensive Student Lesson Activity Passing by (ELA or Math) Learning Domains</em> - shows a breakdown for the 6 lesson domains of ELA or the 4 lesson domains of Math, showcasing the passing or non-passing lesson results within each domain. The count comes from all lessons taken by all students, and the student results of those lessons.
- <em>(ELA or Math) Lesson Results Breakdown by School</em> - shows the aggregate data lesson results of students, further broken-down by the school in which they attend. This accounts for all students within the education system, unless the School Filter is used.
- <em>Student Lesson Results Over Time</em> - shows the aggregate data for lesson activity results (passed or not passed) of students, over a particular month.

![Student Lesson Results Summary](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/iReady/docs/images/iReady%20Module%20Dashboard%20p1.png)

## Data Model

This Power BI data module consists of the eight i-Ready Diagnostic and Instruction Assessment tables: comprehensive_student_lesson_activity_with_standards_ela_pseudo, comprehensive_student_lesson_activity_with_standards_math_pseudo, diagnostic_and_instruction_ela_ytd_window_pseudo, diagnostic_and_instruction_math_ytd_window_pseudo, diagnostic_results_ela_pseudo, diagnostic_results_math_pseudo, personalized_instruction_by_lesson_ela_pseudo, and personalized_instruction_by_lesson_math_pseudo. 

![Data Model](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/iReady/docs/images/iReady%20Module%20Dashboard%20Data%20Model.png)


## Power BI Setup Instructions

#### [Power BI with test data](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/iReady/powerbi/iReady%20Module%20Dashboard%20TestData.pbix):
- Download the PBIX file with test data here: [LINK](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/iReady/powerbi/iReady%20Module%20Dashboard%20TestData.pbix)
- Open the link locally on your computer and explore module test data. 

#### [Power BI with direct query](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/iReady/powerbi/iReady%20Module%20Dashboard%20DirectQuery.pbix):
- Complete the [module setup instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/iReady#module-setup-instructions).
- Download the PBIX file with direct query here: [LINK](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/iReady/powerbi/iReady%20Module%20Dashboard%20DirectQuery.pbix)
- The dashboard visuals may not load. You will need to switch your Synapse workspace serverless SQL endpoint by:
    - Select menu item File > Options and settings > Data source settings.
<kbd> 
    <img src="https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Clever/docs/images/pbi%20data%20source.png" width="600"> 
</kbd>

    - Select Change Source...
| <img src="https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Clever/docs/images/pbi%20change%20source.png" width="600"> | 
|-|
    - Enter your Synapse workspace SQL server endpoint. This can be found on your Synapse workspace information page in the Azure portal.
<kbd> 
    <img src="https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Clever/docs/images/pbi%20sql%20endpt.png" width="600">
</kbd>
<kbd> 
    <img src="https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Clever/docs/images/synapse%20sql%20enpt.png" width="600"> 
</kbd>
