# Test data

This module includes artificially generated data which matches the format of the [Canvas API Calls](https://canvas.instructure.com/doc/api/index.html).
- 13 tables formatted in JSONs, as described in the Canvas data dictionary. Assets can be adapted to integrate ingestion/refinement functionality for more, different or less tables.

<strong>Note:</strong> This module contains one set of test data - for mock higher education data. This module does not currently contain test data formatted as a K-12 institution.

## Data dictionary

### [HEd Canvas Tables](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Canvas/test_data/hed_test_data)

See full details on all [Canvas API Table Schemas](https://portal.inshosteddata.com/docs#assignment_dim) and [Canvas Data v2 Schemas](https://docs.google.com/spreadsheets/d/1kqCXAD9K45L0QeEtbuuMAFp2fW8o0oC8EBzJf58SjrY/edit#gid=527545099).

| Domain | Table Name | Description | 
|-----------|-----------|-----------|
| Roster/Accounts | [accounts](https://docs.google.com/spreadsheets/d/1kqCXAD9K45L0QeEtbuuMAFp2fW8o0oC8EBzJf58SjrY/edit#gid=1357702676) | Canvas group accounts associated the education system, courses, sections, etc. |
| Activity/Assignments | [assignments](https://docs.google.com/spreadsheets/d/1kqCXAD9K45L0QeEtbuuMAFp2fW8o0oC8EBzJf58SjrY/edit#gid=878566033) | Attributes of assignments. There is one record in this table for each assignment. |
| Roster/Academic Groups | [courses](https://docs.google.com/spreadsheets/d/1kqCXAD9K45L0QeEtbuuMAFp2fW8o0oC8EBzJf58SjrY/edit#gid=2091525305) | Attributes of courses. |
| Roster/Academic Groups | [course_sections](https://docs.google.com/spreadsheets/d/1kqCXAD9K45L0QeEtbuuMAFp2fW8o0oC8EBzJf58SjrY/edit#gid=263937005) | Attributes of sections (of courses) in Canvas. | 
| Roster/Affiliations | [enrollments](https://docs.google.com/spreadsheets/d/1kqCXAD9K45L0QeEtbuuMAFp2fW8o0oC8EBzJf58SjrY/edit#gid=822574172) | The relationship between a user and a class. That is, a list of users enrolled in a specific course and section. |
| Roster/Affiliations | [enrollment_terms](https://docs.google.com/spreadsheets/d/1kqCXAD9K45L0QeEtbuuMAFp2fW8o0oC8EBzJf58SjrY/edit#gid=1191210023) | The relationship between courses, etc. and their associated enrollment term (e.g. semesters: Fall 2021 and Spring 2022). | 
| Activity/Modules | [modules](https://docs.google.com/spreadsheets/d/1kqCXAD9K45L0QeEtbuuMAFp2fW8o0oC8EBzJf58SjrY/edit#gid=1857332749) | List of modules in a course. |
| Activity/Modules | [module_items](https://docs.google.com/spreadsheets/d/1kqCXAD9K45L0QeEtbuuMAFp2fW8o0oC8EBzJf58SjrY/edit#gid=1715262273) | List of module items in a course. |
| Activity/Quizzes | [quizzes](https://docs.google.com/spreadsheets/d/1kqCXAD9K45L0QeEtbuuMAFp2fW8o0oC8EBzJf58SjrY/edit#gid=189909408) | Attributes of quizzes. One record per quiz in this table. | 
| Activity/Quizzes | [quiz_submissions](https://docs.google.com/spreadsheets/d/1kqCXAD9K45L0QeEtbuuMAFp2fW8o0oC8EBzJf58SjrY/edit#gid=2087146904) | Attributes of quiz submissions. | 
| Roster/Role | [role](https://docs.google.com/spreadsheets/d/1kqCXAD9K45L0QeEtbuuMAFp2fW8o0oC8EBzJf58SjrY/edit#gid=1397725266) | List of roles within an account. See list of Canvas roles [here](https://canvas.instructure.com/doc/api/file.canvas_roles.html). | 
| Outcomes/Grade Results | [submissions](https://docs.google.com/spreadsheets/d/1kqCXAD9K45L0QeEtbuuMAFp2fW8o0oC8EBzJf58SjrY/edit#gid=1148566159) | Holds assignment submission results within a given course or section for users. | 
| Roster/People | [users](https://docs.google.com/spreadsheets/d/1kqCXAD9K45L0QeEtbuuMAFp2fW8o0oC8EBzJf58SjrY/edit#gid=1426195916) | Stores attributes for users (e.g. students, teachers, admins). | 

For the specific v1 API calls for tables, see the table below.

|Table Name | API Call(s) |
|-----------|-----------|
| [accounts](https://canvas.instructure.com/doc/api/accounts.html) |```GET /api/v1/accounts``` |
| [assignments](https://canvas.instructure.com/doc/api/assignments.html) | ```GET /api/v1/courses/:course_id/assignments``` and/or ```GET /api/v1/courses/:course_id/assignment_groups/:assignment_group_id/assignments``` |
| [courses](https://canvas.instructure.com/doc/api/courses.html) | ```GET /api/v1/courses``` |
| [course_sections](https://canvas.instructure.com/doc/api/sections.html) | ```GET /api/v1/courses/:course_id/sections``` |
| [enrollments](https://canvas.instructure.com/doc/api/enrollments.html) | ```GET /api/v1/sections/:section_id/enrollments``` and/or ```GET /api/v1/courses/:course_id/enrollments``` |
| [enrollment_terms](https://canvas.instructure.com/doc/api/enrollment_terms.html) | ```GET /api/v1/accounts/:account_id/terms``` |
| [modules](https://canvas.instructure.com/doc/api/modules.html) | ```GET /api/v1/courses/:course_id/modules``` |
| [module_items](https://canvas.instructure.com/doc/api/modules.html) | ```GET /api/v1/courses/:course_id/modules/:module_id/items``` |
| [quizzes](https://canvas.instructure.com/doc/api/quizzes.html) | ```GET /api/v1/courses/:course_id/quizzes```  |
| [quiz_submissions](https://canvas.instructure.com/doc/api/quiz_submissions.html) | ```GET /api/v1/courses/:course_id/quizzes/:quiz_id/submissions```  |
| [role](https://canvas.instructure.com/doc/api/roles.html) | ```GET /api/v1/accounts/:account_id/roles``` |
| submissions | |
| [users](https://canvas.instructure.com/doc/api/users.html) | ```GET /api/v1/accounts/:account_id/users``` and/or ```GET /api/v1/users/:user_id/profile```|
