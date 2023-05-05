# Test data

This module includes artificially generated data which matches the format of [Moodle SQL Database Table Exports](https://www.examulator.com/er/output/index.html).
- 27 tables formatted in CSVs, as described in the Moodle data dictionary. Assets can be adapted to integrate ingestion/refinement functionality for more, different or less tables.

<strong>Note:</strong> This module contains one set of test data - for mock higher education data. This module does not currently contain test data formatted as a K-12 institution.

## Data dictionary

### [HEd Moodle Tables](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Moodle/test_data/hed_test_data)

See full details on the [Moodle SQL Database Table Data Dictionary](https://www.examulator.com/er/output/index.html)

| Domain | Table Name | Description |
|-----------|-----------|-----------|
| Activity/Assignments | [assign](https://www.examulator.com/er/output/tables/assign.html) | Contains overview data per assignment, per course. |
| Activity/Assignments | [assign_grades](https://www.examulator.com/er/output/tables/assign_grades.html) | Grading information about a single assignment submission. |
| Activity/Assignments | [assign_submission](https://www.examulator.com/er/output/tables/assign_submission.html) | Contains data for instances of student assignment submissions. |
| Activity/Assignments | [assignsubmission_file](https://www.examulator.com/er/output/tables/assignsubmission_file.html) | Info about file submissions for assignments. |
| Activity/Assignments | [assign_user_mapping](https://www.examulator.com/er/output/tables/assign_user_mapping.html) | Map assignment IDs to each user in a given class.  |
| Academic Groups | [cohort](https://www.examulator.com/er/output/tables/cohort.html) | Each record represents one cohort (a.k.a. site-wide group). Test data currently uses this table for mapping students to schools. |
| Academic Groups | [course](https://www.examulator.com/er/output/tables/course.html) | Course/class records. Test data currently uses this table for mapping students to classes <strong>(Sections in Insights Module -> Courses in Moodle Module)</strong>. |
| Academic Groups | [course_categories](https://www.examulator.com/er/output/tables/course_categories.html) | Course category records. Test data currently uses this table for mapping students to class categories <strong>(Courses in Insights Module -> Course Categories in Moodle Module)</strong>. |
| Academic Groups | [enrol](https://www.examulator.com/er/output/tables/enrol.html) | User-enrollment in a class. |
| Activity/Forums | [forum](https://www.examulator.com/er/output/tables/forum.html) | Moodle forums contain structured discussions. |
| Activity/Forums | [forum_discussions](https://www.examulator.com/er/output/tables/forum_discussions.html) | Moodle discussions that compose a forum (i.e., discussions contained in a forum). |
| Activity/Forums | [forum_grades](https://www.examulator.com/er/output/tables/forum_grades.html) | Grading data of forum/discussion instances. |
| Activity/Forums | [forum_posts](https://www.examulator.com/er/output/tables/forum_posts.html) | All Moodle forum posts are stored in this table. |
| Activity/Lessons | [lesson](https://www.examulator.com/er/output/tables/lesson.html) | Contains overview data per lesson, per course. |
| Activity/Lessons | [lesson_answers](https://www.examulator.com/er/output/tables/lesson_answers.html) | Contains data around answers to lesson questions. |
| Activity/Lessons | [lesson_attempts](https://www.examulator.com/er/output/tables/lesson_attempts.html) | Contains data per student lesson attempt. |
| Activity/Lessons | [lesson_grades](https://www.examulator.com/er/output/tables/lesson_grades.html) | Grading data of lesson attempt instances. |
| Activity/Lessons | [lesson_pages](https://www.examulator.com/er/output/tables/lesson_pages.html) | Contains data around the pages per lesson. |
| Activity/Lessons | [lesson_timer](https://www.examulator.com/er/output/tables/lesson_timer.html) | Contains timer information for each lesson, per student. |
| Activity/Messaging | [messages](https://www.examulator.com/er/output/tables/messages.html) | <em>No test data at the moment</em> |
| Activity/Messaging | [message_conversations](https://www.examulator.com/er/output/tables/message_conversations.html) | <em>No test data at the moment</em> |
| Activity/Messaging | [message_conversation_members](https://www.examulator.com/er/output/tables/message_conversation_members.html) | <em>No test data at the moment</em> |
| Class Pages | [page](https://www.examulator.com/er/output/tables/page.html) | Each record is one page and its config data. |
| Outcomes/Quizzes | [quiz](https://www.examulator.com/er/output/tables/quiz.html) | Contains overview data per quiz, per course. Documentation says: "The settings for each quiz. For reports see https://docs.moodle.org/en/ad-hoc_contributed_reports#Quiz_Activity". |
| Outcomes/Quizzes | [quiz_attempts](https://www.examulator.com/er/output/tables/quiz_attempts.html) | Contains student attempts at quizzes. |
| Outcomes/Quizzes | [quiz_grades](https://www.examulator.com/er/output/tables/quiz_grades.html) | Grading data of quiz attempt instances. |
| Role | [role](https://www.examulator.com/er/output/tables/role.html) | Contains overview information about each role in the system (e.g., student vs. professor). |
| Role | [role_assignments](https://www.examulator.com/er/output/tables/role_assignments.html) | The relationship mapping between each user and each role per course. |
| People | [user](https://www.examulator.com/er/output/tables/user.html) | Contains the last updated set of information for a given user. |
| Affiliations | [user_enrolments](https://www.examulator.com/er/output/tables/user_enrolments.html) | The relationship between a user and a course. |
