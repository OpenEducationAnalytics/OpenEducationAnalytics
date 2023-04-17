# Test data

This module includes artifically generated data which matches the format of the four [i-Ready Diagnostic and Personalized Instruction Assessment Reports](https://www.curriculumassociates.com/programs/i-ready-assessment) for both ELA and Math subjects, resulting in a total of eight tables.
- <strong>Comprehensive Student Lesson Activity with Standards Report</strong> provides incremental assessment data on student learning per lesson completed. i-Ready summarizes this data by:
    - the lesson subject area (ELA or Math), 
    - the lesson domain (e.g. phonics, algebra), 
    - additional lesson details (e.g. lesson grade-level), 
    - whether a student passed or failed a particular lesson, 
    - some forms of SIS data (school the student attends, student name, etc.), and
    - lesson correlations with an education system's state standards.
- <strong>Personalized Instruction by Lesson Report</strong> provides the results surrounding student personalized instruction assessments. This table essentially serves as an overview of the <em>Comprehensive Student Lesson Activity with Standards</em> tables, without the matching of state standards.
- <strong>Diagnostic and Instruction YTD Window</strong> provides a year-long snapshot of assessment data on student learning diagnostics. These assessments can be used to identify students who may be at risk for reading/math difficulties. The assessment data also provides test results in specific areas of student-learning domains within ELA and Math. 
- <strong>Diagnostic Results Report</strong> provides the implications and iReady analyses of student diagnostic assessments. These include metrics used for gauging the successes/struggles of student learning (e.g. [Annual Stretch Growth Measure](https://www.curriculumassociates.com/access-and-equity/providing-a-path-to-proficiency-for-every-student)). The assessment data also provides test results in specific areas of student-learning domains within ELA and Math. 

## Data dictionary

### [Comprehensive Student Lesson Activity with Standards ELA Table](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/iReady/test_data/test_data/comprehensive_student_lesson_activity_with_standards_ela/ela.csv)
### [Comprehensive Student Lesson Activity with Standards Math Table](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/iReady/test_data/test_data/comprehensive_student_lesson_activity_with_standards_math/math.csv)

<details><summary>Expand Data Dictionary for: Comprehensive Student Lesson Activity with Standards</summary>
<p>

|Column Name | Data Type | Description |
|-----------|-----------|-----------|
| Last Name | String | The surname of the student. |
| First Name | String | The given name of the student. |
| Student ID | String | The student ID of the student. |
| Student Grade | String | The grade of the student in the education system (e.g. K, 1, 2). |
| Academic Year | String | The academic year of the student at the time of lesson completion. |
| School | String | The name of the school attended by the student. |
| Subject | String | The subject of the lesson (defaulted to "Reading" or "Math" depending on the table). |
| Domain | String | The domain of the lesson; area of learning in the context of the subject area (i.e. Phonics, Comprehension, High-Frequency Words, Phonological Awareness, Vocabulary, Numbers and Operations, Algebra, Measurement and Data, or Geometry). |
| Lesson Grade | String | The iReady-identified grade-level of the lesson. |
| Lesson Level | String | An indicator ("Early", "Mid", "Late", or "Extra") of how the lesson compares to the student, based on the student's grade and the lesson's grade-level. |
| Lesson ID | String | The iReady ID of the associated lesson. |
| Lesson Name | String | The name of lesson. |
| Lesson Objective | String | The learning objective(s) outlined from the lesson. |
| Completion Date | Date | Date the lesson was completed by the student. |
| Total Time on Lesson (min) | Integer | The total number of minutes the student spent on the lesson. |
| Score | Integer | The final score of the student upon completion of the lesson. |
| Passed or Not Passed | String | An indicator ("Passed" or "Not Passed") of whether the student passed the lesson, based on their score exceeds or fails to meet the lesson-score-threshold. |
| Teacher-Assigned Lesson | String | An indicator ("Y" or "N") of whether the student's teacher assigned the lesson to the student. |
| State Standards | String | An abbreviation of the education system's state standards based on their state of residence (e.g. "CA-ELA"). |
| Type of Standard | String | An indicator ("Direct", "Related", "Partial", or "N/A") of whether the lesson belongs or correlates with state standards. |
| Standard Code | String | An abbreviated code for the state standard, to which the the lesson belongs. |
| Standard Text | String | A more in-depth identification of the specific standard, to which the lesson belongs. |

| Comprehensive Student Lesson Activity with Standards Test Data  | 
|:-------------------------:|
| ![](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/iReady/docs/images/test_data_screenshots/iReady_test_data_snapshot_comprehensive.png)  |

Notes: 

1) The "Comprehensive Student Lesson Activity with Standards ELA Table" and "Comprehensive Student Lesson Activity with Standards Math Table" have the exact same columns, though the data pertaining to the subject areas differ.

</p>
</details>

### [Personalized Instruction by Lesson ELA Table](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/iReady/test_data/test_data/personalized_instruction_by_lesson_ela/ela.csv)
### [Personalized Instruction by Lesson Math Table](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/iReady/test_data/test_data/personalized_instruction_by_lesson_math/math.csv)

<details><summary>Expand Data Dictionary for: Personalized Instruction by Lesson</summary>
<p>

|Column Name | Data Type | Description |
|-----------|-----------|-----------|
| Last Name | String | The surname of the student. |
| First Name | String | The given name of the student. |
| Student ID | String | The student ID of the student. |
| Student Grade | String | The grade of the student in the education system (e.g. K, 1, 2). |
| Academic Year | String | The academic year of the student at the time of lesson completion. |
| School | String | The name of the school attended by the student. |
| Subject | String | The subject of the lesson (defaulted to "Reading" or "Math" depending on the table). |
| Domain | String | The domain of the lesson; area of learning in the context of the subject area (i.e. Phonics, Comprehension, High-Frequency Words, Phonological Awareness, Vocabulary, Numbers and Operations, Algebra, Measurement and Data, or Geometry). |
| Lesson Grade | String | The iReady-identified grade-level of the lesson. |
| Lesson Level | String | An indicator ("Early", "Mid", "Late", or "Extra") of how the lesson compares to the student, based on the student's grade and the lesson's grade-level. |
| Lesson ID | String | The iReady ID of the associated lesson. |
| Lesson Name | String | The name of lesson. |
| Lesson Objective | String | The learning objective(s) outlined from the lesson. |
| Lesson Language | String | The language in which the lesson was taught. |
| Completion Date | Date | Date the lesson was completed by the student. |
| Total Time on Lesson (min) | Integer | The total number of minutes the student spent on the lesson. |
| Score | Integer | The final score of the student upon completion of the lesson. |
| Passed or Not Passed | String | An indicator ("Passed" or "Not Passed") of whether the student passed the lesson, based on their score exceeds or fails to meet the lesson-score-threshold. |
| Teacher-Assigned Lesson | String | An indicator ("Y" or "N") of whether the student's teacher assigned the lesson to the student. |

| Personalized Instruction by Lesson Test Data  | 
|:-------------------------:|
| ![](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/iReady/docs/images/test_data_screenshots/iReady_test_data_snapshot_personalized.png)  |

Notes: 

1) The "Personalized Instruction by Lesson ELA Table" and "Personalized Instruction by Lesson Math Table" have the exact same columns, though the data pertaining to the subject areas differ.

</p>
</details>

### [Diagnostic and Instruction ELA YTD Window Table](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/iReady/test_data/test_data/diagnostic_and_instruction_ela_ytd_window/ela.csv)
### [Diagnostic and Instruction Math YTD Window Table](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/iReady/test_data/test_data/diagnostic_and_instruction_math_ytd_window)

<details><summary>Expand Data Dictionary for: Diagnostic and Instruction YTD Window</summary>
<p>

|Column Name | Data Type | Description |
|-----------|-----------|-----------|
| Last Name | String | The surname of the student. |
| First Name | String | The given name of the student. |
| Student ID | String | The student ID of the student. |
| Enrolled | String | An indicator ("Enrolled" or "Not Enrolled") of whether the student is still enrolled at a school. |
| Student Grade | String | The grade of the student in the education system (e.g. K, 1, 2). |
| Academic Year | String | The academic year of the student at the time of lesson completion. |
| School | String | The name of the school attended by the student. |
| Subject | String | The subject of the lesson (defaulted to "Reading" or "Math" depending on the table). |
| User Name | String | The email of the student. |
| Gender | String |	An indicator ("male" or "female") of the student's gender. |
| Hispanic or Latino | String |	An indicator ("Y" or "N") of whether the student is Hispanic or Latino. |
| Race | String | An indicator of the student's racial demographics. |
| English Language Learner | String | An indicator of whether the student is an English language learner. |
| Special Education | String | An indicator of whether the student is in special education. |
| Economically Disadvantaged | String | An indicator of whether the student is economically disadvantaged. |
| Migrant | String | An indicator of whether the student is a migrant. |
| Class(es) | String | An expression for the class(es) that the student is taking. |
| Class Teacher(s) | String | An expression for the teacher(s) that the student has for their class(es). |
| Report Group(s) | String | An expression for the group(s) that the student is associated with at the time of the report generation. |
| Number of Completed Diagnostics during the time frame | Integer | The total number of diagnostic assessments taken at the time of the report generation. |
| Annual Typical Growth Measure | Integer |	An indicator of the yearly expected typical growth. |
| Annual Stretch Growth Measure | Integer |	An indicator of the yearly expected stretch growth. |
| Diagnostic Gain (Note: negative gains=zero) | Integer | An indicator of the general diagnostic assessment growth seen from the student since the latest-previous diagnostic assessment. |
| Diagnostic: Start Date (x) | Date | The start date of the diagnostic assessment. |
| Diagnostic: Completion Date (x) | Date | The completion date of the diagnostic assessment. |
| Diagnostic: Time on Task (min) (x) | Integer | The total time spent on the diagnostic assessment (in minutes). |
| Diagnostic: Rush Flag (x) | String | An indicator of the rush flag association with the student after completion of the diagnostic assessment. |
| Diagnostic: Overall Scale Score (x) | Integer | The overall resulting scale score of the student from the diagnostic assessment (i.e. considering all subject domain scale scores). |
| Diagnostic: Overall Placement (x) | String | The overall resulting i-Ready-identified placement of the student from the diagnostic assessment (i.e. considering all subject domain scale scores). |
| Diagnostic: Percentile (x) | Integer | The percentile associated with the student from the diagnostic assessment results. |
| Diagnostic: Overall Relative Placement (x) | String | The overall resulting i-Ready-identified relative placement of the student from the diagnostic assessment (i.e. considering all subject domain scale scores). |
| Diagnostic: Tier (x) | String | The tier associated with the student from the diagnostic assessment results. |
| xxxxx | xxxxx | xxxxx |
| Diagnostic: (_) Measure (x) | String | The overall Lexile or Quantile measure (depending on whether the ELA or Math table, respectively) of the student, based on those diagnostic assessment results. |
| Diagnostic: (_) Range (x) | String | The overall Lexile or Quantile range (depending on whether the ELA or Math table, respectively) of the student, based on those diagnostic assessment results. |
| Diagnostic: Grouping (x) | String | The grouping of the student, based on those diagnostic assessment results.  |
| Diagnostic: Language (x) | String | The language in which the student took the diagnostic assessment. |
| Diagnostic: <strong>(Subject Domain)</strong> Scale Score (x) | Integer | The resulting scale score of the student, in that particular subject domain from the diagnostic assessment. |
| Diagnostic: <strong>(Subject Domain)</strong> Placement (x) | String | The resulting i-Ready-identified placement of the student, in that particular subject domain from the diagnostic assessment. |
| Diagnostic: <strong>(Subject Domain)</strong> Relative Placement (x) | String | The resulting i-Ready-identified relative placement of the student, in that particular subject domain from the diagnostic assessment. |
| xxxxx | xxxxx | xxxxx |
| Instruction: <strong>(Subject Domain)</strong> Lessons Passed | Integer | The total number of lessons passed by the student, in that subject domain (or overall). |
| Instruction: <strong>(Subject Domain)</strong> Lessons Not Passed | Integer | The total number of lessons not passed by the student, in that subject domain (or overall). |
| Instruction: <strong>(Subject Domain)</strong> Lessons Completed | Integer | The total number of lessons completed by the student, in that subject domain (or overall). |
| Instruction: <strong>(Subject Domain)</strong> Pass Rate (\%) | Integer | The total pass rate percentage of the student in lessons related to that subject domain (or overall).  |
| Instruction: <strong>(Subject Domain)</strong> Time on Task (min) | Integer | The total time, in minutes, spent on the lesson in that subject domain (or overall). |

| Diagnostic and Instruction YTD Window Test Data  | 
|:-------------------------:|
| ![](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/iReady/docs/images/test_data_screenshots/iReady_test_data_snapshot_diagnostic_and_instruction.png)  |

Notes: 

1) Rows in the table marked with "xxxxx" for their section indicate a separate section of the table where column sections are grouped together.
2) Anything in the above table marked with (x) indicates that the "x" is either replaced with "Most Recent", "1", "2", "3", "4", or "5". 
    - There is a section columns corresponding to each diagnostic assessment indicator.
2) Anything in the above table marked with (\_) indicates that the "\_" is either replaced with "Lexile" or "Quantile" depending on the ELA or Math table, respectively.
3) Anything in the above table marked with <strong>(Subject Domain)</strong> indicates that the entire parenthesis is to be replaced with one of the two sets of domains (the ELA table corresponds with the first set, and the Math table corresponds with the second set):
    - Phonological Awareness, Phonics, High-Frequency Words, Vocabulary, Reading Comprehension: Literature, and Reading Comprehension: Informational Text.
    - Number and Operations, Algebra and Algebraic Thinking, Measurement and Data, and Geometry.
4) With the last "Instruction:" section of columns (outlined above) both tables include an "Overall" section, which precedes the breakdown of subject domains.

</p>
</details>

### [Diagnostic Results ELA Table](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/iReady/test_data/test_data/diagnostic_results_ela/ela.csv)

<details><summary>Expand Data Dictionary for: Diagnostic Results ELA</summary>
<p>

|Column Name | Data Type | Description |
|-----------|-----------|-----------|
| Last Name | String | The surname of the student. |
| First Name | String | The given name of the student. |
| Student ID | String | The student ID of the student. |
| Student Grade | String | The grade of the student in the education system (e.g. K, 1, 2). |
| Academic Year | String | The academic year of the student at the time of lesson completion. |
| School | String | The name of the school attended by the student. |
| Start Date | Date | Date the diagnostic assessment was started by the student. |
| Completion Date | Date | Date the diagnostic assessment was completed by the student. |
| Diagnostic used to establish Growth Measures (Y/N) | String |	An indicator ("Y" or "N") of whether the diagnostic assessment is used to establish growth measures of the student. |
| Most Recent Diagnostic (Y/N) | String | An indicator ("Y" or "N") of whether that particular diagnostic assessment was the most recent diagnostic assessment taken by the student.  |
| Duration (min) | Integer | The total number of minutes the student spent on the diagnostic test. |
| Rush Flag | String | An indicator of the rush flag association with the student after completion of the diagnostic assessment. |
| Overall Scale Score | Integer | The overall resulting scale score of the student from the diagnostic assessment (i.e. considering all subject domain scale scores). |
| Overall Placement | String | The overall resulting i-Ready-identified placement of the student from the diagnostic assessment (i.e. considering all subject domain scale scores). |
| Overall Relative Placement | String | The overall resulting i-Ready-identified relative placement of the student from the diagnostic assessment (i.e. considering all subject domain scale scores). |
| Percentile | Integer | The percentile associated with the student from the diagnostic assessment results. |
| Grouping | String | The grouping of the student, based on those diagnostic assessment results. |
| Lexile Measure | String | The overall Lexile measure of the student, based on those diagnostic assessment results. |
| Lexile Range | String |	The overall Lexile range of the student, based on those diagnostic assessment results. |
| <strong>(Subject Domain)</strong> Scale Score | Integer |	The resulting scale score of the student, in that particular subject domain from the diagnostic assessment. |
| <strong>(Subject Domain)</strong> Placement | String | The resulting i-Ready-identified placement of the student, in that particular subject domain from the diagnostic assessment. |
| <strong>(Subject Domain)</strong> Relative Placement | String | The resulting i-Ready-identified relative placement of the student, in that particular subject domain from the diagnostic assessment. |
| Diagnostic Language | String | The language in which the student took the diagnostic assessment. |
| Annual Typical Growth Measure | Integer |	An indicator of the yearly expected typical growth. |
| Annual Stretch Growth Measure | Integer |	An indicator of the yearly expected stretch growth. |
| Mid On Grade Level Scale Score | Integer | An indicator of the median grade level scale score. |
| Reading Difficulty Indicator (Y/N) |  | An indicator ("Y" or "N") of whether the student has been flagged by i-Ready for having difficulties with reading. |

| Diagnostic Results ELA Test Data  | 
|:-------------------------:|
| ![](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/iReady/docs/images/test_data_screenshots/iReady_test_data_snapshot_diagnostic_results.png)  |

Notes:

1) Anything in the above table marked with <strong>(Subject Domain)</strong> indicates that the entire parenthesis is to be replaced with the following set of subject domains:
    - Phonological Awareness, Phonics, High-Frequency Words, Vocabulary, Reading Comprehension: Literature, and Reading Comprehension: Informational Text.
    
</p>
</details>

### [Diagnostic Results Math Table](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/iReady/test_data/test_data/diagnostic_results_math/math.csv)

<details><summary>Expand Data Dictionary for: Diagnostic Results Math</summary>
<p>

|Column Name | Data Type | Description |
|-----------|-----------|-----------|
| Last Name | String | The surname of the student. |
| First Name | String | The given name of the student. |
| Student ID | String | The student ID of the student. |
| Student Grade | String | The grade of the student in the education system (e.g. K, 1, 2). |
| Academic Year | String | The academic year of the student at the time of lesson completion. |
| School | String | The name of the school attended by the student. |
| Start Date | Date | Date the diagnostic assessment was started by the student. |
| Completion Date | Date | Date the diagnostic assessment was completed by the student. |
| Diagnostic used to establish Growth Measures (Y/N) | String |	An indicator ("Y" or "N") of whether the diagnostic assessment is used to establish growth measures of the student. |
| Most Recent Diagnostic (Y/N) | String | An indicator ("Y" or "N") of whether that particular diagnostic assessment was the most recent diagnostic assessment taken by the student.  |
| Duration (min) | Integer | The total number of minutes the student spent on the diagnostic test. |
| Rush Flag | String | An indicator of the rush flag association with the student after completion of the diagnostic assessment. |
| Overall Scale Score | Integer | The overall resulting scale score of the student from the diagnostic assessment (i.e. considering all subject domain scale scores). |
| Overall Placement | String | The overall resulting i-Ready-identified placement of the student from the diagnostic assessment (i.e. considering all subject domain scale scores). |
| Overall Relative Placement | String | The overall resulting i-Ready-identified relative placement of the student from the diagnostic assessment (i.e. considering all subject domain scale scores). |
| Percentile | Integer | The percentile associated with the student from the diagnostic assessment results. |
| Grouping | String | The grouping of the student, based on those diagnostic assessment results. |
| Lexile Measure | String | The overall Lexile measure of the student, based on those diagnostic assessment results. |
| Lexile Range | String |	The overall Lexile range of the student, based on those diagnostic assessment results. |
| <strong>(Subject Domain)</strong> Scale Score | Integer |	The resulting scale score of the student, in that particular subject domain from the diagnostic assessment. |
| <strong>(Subject Domain)</strong> Placement | String | The resulting i-Ready-identified placement of the student, in that particular subject domain from the diagnostic assessment. |
| <strong>(Subject Domain)</strong> Relative Placement | String | The resulting i-Ready-identified relative placement of the student, in that particular subject domain from the diagnostic assessment. |
| Diagnostic Language | String | The language in which the student took the diagnostic assessment. |
| Annual Typical Growth Measure | Integer |	An indicator of the yearly expected typical growth. |
| Annual Stretch Growth Measure | Integer |	An indicator of the yearly expected stretch growth. |
| Mid On Grade Level Scale Score | Integer | An indicator of the median grade level scale score. |

| Diagnostic Results Math Test Data  | 
|:-------------------------:|
| ![](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/iReady/docs/images/test_data_screenshots/iReady_test_data_snapshot_diagnostic_results.png)  |

Notes:

1) Anything in the above table marked with <strong>(Subject Domain)</strong> indicates that the entire parenthesis is to be replaced with the following set of subject domains:
    - Number and Operations, Algebra and Algebraic Thinking, Measurement and Data, and Geometry.
   
</p>
</details>
