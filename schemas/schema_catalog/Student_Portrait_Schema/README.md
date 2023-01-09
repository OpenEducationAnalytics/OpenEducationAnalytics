<img align="right" height="75" src="https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/pics/oea-logo-nobg.png">

# Student Portrait Solution
[Student Portrait](https://www.analytikus.com/learning-analytics) by [Analytikus](https://www.analytikus.com/) is an analytical solution that uses artificial intelligence to get to know all students and support them through personalized messaging. It identifies key student variables and characteristics, then nudges them through short, concise messages, that are personalized and engaging, in a timely manner to maximize student success. 

With the Student Portrait solution, educational institutions can understand how students learn in order to maximize their performance, satisfaction and motivation by delivering personalized nudges through a virtual pedagogical bot. It ensures the best outcomes for students with a 360-degree view of activities and engagement, followed by the provisioning of the right services and support at the optimal time. 

<p align="center">
  <img src="https://github.com/microsoft/OpenEduAnalytics/blob/main/schemas/schema_catalog/Student_Portrait_Schema/docs/images/Student_Portrait_Solution_Overview.png" alt="Student Portrait Solution"/>
</p>

Portrait is operationalized through two AI agents: Emilia, a learning therapist, and Max, an organizational assistant, and uses data from multiple sources including LMS (Moodle, Canvas, Blackboard, etc), SIS, Microsoft Teams, Reflect, etc.

## Data Schema
The Student Portrait data schema has 24 data entities. The Data Entities table below provides the description and update frequency of each data entity.

We are working toward aligning data sources/OEA modules like Canvas and Moodle to the Student Portrait schema, and this will include the creation of the technical assets (notebooks, pipelines, etc) to facilitate this. Please check this folder in a few weeks for updates to the Student Portrait schema.

### Data Entities

|# | Input | Description | Update Frequency |
|-----------|-----------|-----------|-----------|
| 1 | Schools | Faculties Catalog | Start of semester |
| 2 | Programs | Programs catalog | Start of semester |
| 3 | Courses | Course catalog | Start of semester |
| 4 | Term | Catalog of school terms | Start of semester |
| 5 | Classes | Catalog of classes, groups or sections with open registrations for a course and a school term | Start of semester |
| 6 | Users | Catalog of users: students, teachers, coordinators, etc | Start of semester |
| 7 | Student_Enrollments | List of students enrolled by class, group or section | Start of semester |
| 8 | Professor_Enrollments | List of teachers by class, group or section in which they participate | Start of semester |
| 9 | Assignments | List of mandatory assignments | Start of semester |
| 10 | Discussions | List of mandatory forum discussions | Start of semester |
| 11 | Quizzes | List of mandatory quizzes | Start of semester |
| 12 | Lessons | List of lessons or content "objects" that are required | Start of semester |
| 13 | Assignment_Files | List of assignment files submitted by the student | Weekly |
| 14 | Assignment_Attempts | Student attempts to submit an assignment | Weekly |
| 15 | Posts | Student posts in discussion forums | Weekly |
| 16 | Quiz_Attempts | Student Attempts to complete a quiz | Weekly |
| 17 | Lesson_Attempts | Student attempts to complete a lesson or content object | Weekly |
| 18 | Messages | Messages sent by the student | Weekly |
| 19 | Class_Messages | Messages sent by the student associated with a class, group, or section | Weekly |
| 20 | Page_Views | Access to LMS pages | Weekly |
| 21 | Attendance | Student attendance | Weekly |
| 22 | Screener_answers | Answers to the quizzes that Portrait will suggest for certain students | Weekly |
| 23 | Programs_users | Relationship between students and programs in which they are enrolled | Weekly |
| 24 | Courses_programs | Relationship between courses and programs in which they are taught | Weekly |

<p align="center">
  <img src="https://github.com/microsoft/OpenEduAnalytics/blob/main/schemas/schema_catalog/Student_Portrait_Schema/docs/images/Student_Portrait_Input_Entities.png" alt="Student Portrait Schema Input Entities"/>
</p>

### Detailed Information on Data Entities

|Entity id | Property | Type | Description |
|-----------|-----------|-----------|-----------|
| 1 | id | STRING | Faculty identifier |
|  | name | STRING | Faculty abbreviation |
|  | description | STRING | Faculty name |
|  | active | INT | Flag that indicates if the record is active or has been deleted. |
|  | Load_datetime | TIMESTAMP | Date and time of the record upload. |
| 2 | id | STRING | Program identifier |
|  | school_id	 | STRING | Faculty identifier |
|  | name | STRING | Program abbreviation |
|  | description | STRING | Program name |
|  | active | INT | Flag that indicates if the record is active or has been deleted. |
|  | Load_datetime | TIMESTAMP | Date and time of the record upload. |
| 3 | id | STRING | Course identifier |
|  | name | STRING | Course abbreviation |
|  | description | STRING | Course name |
|  | active | INT | Flag that indicates if the record is active or has been deleted. |
|  | Load_datetime | TIMESTAMP | Date and time of the record upload.|
| 4 | id | STRING | Term identifier |
|  | name | STRING | Term name |
|  | start_datetime | TIMESTAMP | Term start date and time |
|  | end_datetime | TIMESTAMP | Term end date and time |
|  | active | INT | Flag that indicates if the record is active or has been deleted. |
|  | Load_datetime | TIMESTAMP | Date and time of the record upload.|
| 5 | id | STRING | Class/group/section identifier |
|  | course_id | STRING | Course identifier |
|  | term_id | STRING | Term identifier |
|  | name | STRING | Class/group/section name |
|  | active | INT | Flag that indicates if the record is active or has been deleted. |
|  | Load_datetime | TIMESTAMP | Date and time of the record upload.|
| 6 | id | STRING | Student, teacher or program director identifier |
|  | last_login | TIMESTAMP | Last date and time of access to the LMS|
|  | active | INT | Flag that indicates if the record is active or has been deleted. |
|  | Load_datetime | TIMESTAMP | Date and time of the record upload.|
| 7 | id | STRING | Enrollment ID |
|  | class_id | STRING | Class/group/section identifier |
|  | user_id | STRING | User ID |
|  | created | TIMESTAMP | Date and time of enrollment |
|  | active | INT | Flag indicating if the registry is active or has been deleted. |
|  | Load_datetime | TIMESTAMP | Date and time of the record creation.|
| 8 | id | STRING | Enrollment ID |
|  | class_id | STRING | Class/group/section identifier |
|  | user_id | STRING | Professor ID |
|  | created | TIMESTAMP | Date and time of enrollment |
|  | Active | INT | Flag indicating if the registry is active or has been deleted. |
|  | Load_datetime | TIMESTAMP | Date and time of the record creation.|
| 9 | id | STRING | Assignment identifier |
|  | class_id | STRING | Class/group/section identifier |
| | start_datetime	| TIMESTAMP	| Assignment start date and time |
| | due_datetime|	TIMESTAMP	| Assignment submission due date and time |
| | name	| STRING	| Assignment name |
| | Active |	INT |	Flag indicating if the registry is active or has been deleted.|
| | Load_datetime	| TIMESTAMP	| Date and time of record creation.|
| 10 | id | STRING | Discussion ID |
|  | class_id | STRING | Class/group/section identifier |
| | start_datetime	| TIMESTAMP	| Discussion start date and time |
| | due_datetime|	TIMESTAMP	| Discussion submission due date and time |
| | name	| STRING	| Discussion/forum name |
| | Active |	INT |	Flag indicating if the registry is active or has been deleted.|
| | Load_datetime	| TIMESTAMP	| Date and time of record creation.|
| 11 | id | STRING | Quiz ID |
|  | class_id | STRING | Class/group/section identifier |
| | start_datetime	| TIMESTAMP	| Quiz start date and time |
| | due_datetime|	TIMESTAMP	| Quiz due date and time |
| | total_questions|	INT	| Total number of questions in quiz |
| | name	| STRING	| Quiz name |
| | Active |	INT |	Flag indicating if the registry is active or has been deleted.|
| | Load_datetime	| TIMESTAMP	| Date and time of record creation.|
| 12 | id | STRING | Lesson identifier |
|  | class_id | STRING | Class/group/section identifier |
| | start_datetime	| TIMESTAMP	| Lesson start date and time |
| | due_datetime|	TIMESTAMP	| Lesson due date and time |
| | total_questions|	INT	| Total number of questions in lesson |
| | name	| STRING	| Lesson or object name |
| | Active |	INT |	Flag indicating if the registry is active or has been deleted.|
| | Load_datetime	| TIMESTAMP	| Date and time of record creation.|
| 13 | id | STRING | Assignment file ID |
|  | assignment_id | STRING | Assignment identifier |
|	| user_id |	STRING |	Student ID |
|	| file_path |	STRING	| Assignment file name and path within AssignmentBinaries |
| | Active |	INT |	Flag indicating if the registry is active or has been deleted.|
| | Load_datetime	| TIMESTAMP	| Date and time of record creation.|
| 14 |	id	| STRING	| Assignment Submission Attempt identifier |
| |	assignment_id	| STRING  |	Assignment identifier |
| |	user_id	| STRING	| Student ID |
| |	attempt_number|	INT	| Assignment Submission attempt number |
| |	created	| TIMESTAMP	| Date and time of submission |
| |	grade	| DECIMAL(18,4)| 	Standardized rating on a scale of 0 to 1, where 0 is the lowest possible grade and 1 is the highest possible grade. |
| | completed	| INT |	Flag indicating whether this attempt completes the task. |
| |	active |	INT |	Flag that indicates if the record is active or has been deleted.|
| |	load_datetime |	TIMESTAMP	| Date and time of the record upload.|
| 15 |	id	| STRING	| Post identifier |
|	| discussion_id |	STRING	| Discussion identifier |
| |	user_id	| STRING	| Student ID |
| |	created	| TIMESTAMP |	Post date and time of publishing |
| | post_text	| STRING	| Post text |
| |	Grade	| DECIMAL(18,4) |	Standardized grade on a scale of 0 to 1, where 0 is the lowest possible grade and 1 is the highest possible grade |
| |	completed |	INT |	Flag indicating whether this attempt completes participation in the forum.|
| |	active |	INT	| Flag that indicates if the record is active or has been deleted.|
| |	load_datetime	| TIMESTAMP |	Date and time of the record upload.|
| 16 |	id| 	STRING	| Quiz attempt identifier |
| |	quiz_id	| STRING	| Quiz ID |
| |	user_id	| STRING	|  Student ID |
|	| attempt_number	| INT	| Quiz attempt number |
|	| created	| TIMESTAMP	| Date and time of attempt start |
|	| modified	| TIMESTAMP |	Date and time of attempt end |
| |	total_answered |	INT	| Total number of questions that were answered by the student |
| |	total_not_answered |	INT	| Total number of questions that were not answered by the student |
| |	correct_answers	| INT |	Total number of questions that were answered correctly by the student |
| |	wrong_answers |	INT	| Total number of questions that were answered incorrectly by the student |
| |	undefined_questions|	INT	| Total number of questions that were answered by the student but haven’t been graded |
| |	grade	|DECIMAL(18,4)|	Standardized grade on a scale of 0 to 1, where 0 is the lowest possible grade and 1 is the highest possible grade |
| |	completed |	INT |	Flag indicating whether this attempt completes participation in the quiz |
| |	active |	INT |	Flag that indicates if the record is active or has been deleted. |
| |	load_datetime	| TIMESTAMP	| Date and time of the record upload.|
| 17 |	id |	STRING	| Lesson attempt identifier |
| |	min_seen_datetime	| TIMESTAMP	| Minimum date and time that the student was seen during the attempt |
| |	max_seen_datetime |	TIMESTAMP |	Maximum date and time that the student was seen during the attempt |
| |	correct_answers	| INT	| Number of correct answers |
| |	user_id	| STRING	| Student ID |
| |	lesson_id	| STRING	| Lesson identifier |
| |	completed	| INT	| Flag indicating whether this attempt completes participation in the lesson |
| |	grade| 	DECIMAL(18,4) |	Standardized grade on a scale of 0 to 1, where 0 is the lowest possible grade and 1 is the highest possible grade |
| |	active	| INT	| Flag that indicates if the record is active or has been deleted.|
| |	load_datetime |	TIMESTAMP |	Date and time of the record upload.|
| 18|	id	| STRING	| Message identifier |
| |	from_user_id |	STRING	| Sender identifier |
| |	to_user_id |	STRING	| Recipient identifier |
| |	created	| TIMESTAMP	| Date and time the message was sent |
| |	message_text |	STRING |	Message text |
|	| active |	INT	| Flag that indicates if the record is active or has been deleted.|
| |	load_datetime |	TIMESTAMP	| Date and time of the record upload.|
| 19	|id	|STRING	| Message identifier |
| |	from_user_id	| STRING	| Sender identifier |
| |	to_user_id	| STRING	| Recipient identifier |
| |	class_id |	STRING |	Class/group/section identifier |
|	| created	| TIMESTAMP |	Date and time the message was sent |
| |	message_text |	STRING |	Message text |
| |	active	| INT	| Flag that indicates if the record is active or has been deleted. |
| |	load_datetime |	TIMESTAMP	| Date and time of the record upload. |
| 20 |	Id	| STRING |	Record identifier |
| |	user_id |	STRING |	Student ID |
| |	class_id | STRING |	Class/group/section identifier |
| |	page_views |	INT	| Total number of pages visited up to the current date |
| |	created	| TIMESTAMP	| Time and date of count |
| |	active	| INT |	Flag that indicates if the record is active or has been deleted.|
| |	load_datetime |	TIMESTAMP |	Date and time of the record upload.|
| 21 |	Id	| STRING	| Record identifier |
| |	user_id	| STRING	| Student ID |
| |	class_id |	STRING |	Class/group/section identifier |
| |	sessions |	INT	| Number of sessions that occurred at the cut |
| |	Attendance_percentage	| DECIMAL(18,4)	| % of attendance at the cut (0 to 1) |
| |	created |	TIMESTAMP	| Date and time of report |
| |	active |	INT |	Flag that indicates if the record is active or has been deleted. |
| |	load_datetime |	TIMESTAMP |	Date and time of the record upload.|
| 22 |	id	| STRING	| Record unique identifier |
| |	user_id	| STRING	| Unique ID for user who provided the answer |
| |	question_id	| INT	| Question identifier |
| |	answer	| INT	| Answer’s numeric code |
| |	created	| TIMESTAMP |	Date and time of answer creation |
| |	active	| INT	| Flag that indicates if the record is active or has been deleted. |
| |	load_datetime	| TIMESTAMP	| Date and time of the record upload. |
| 23 | id	| STRING	| Record unique identifier |
| |	program_id	| STRING	| Program unique ID |
| |	user_id	| STRING	| Student ID |
| |	active	| INT	| Flag that indicates if the record is active or has been deleted.|
| |	load_datetime	| TIMESTAMP	| Date and time of the record upload.|
| 24|	id	| STRING	| Record unique identifier |
| |	course_id |	STRING |	Course unique ID |
|	 | program_id	| STRING |	Program identifier |
| |	active |	INT |	Flag that indicates if the record is active or has been deleted.|
|	| load_datetime	| TIMESTAMP	| Date and time of the record upload.|


# Legal Notices
Microsoft and any contributors grant you a license to the Microsoft documentation and other content
in this repository under the [Creative Commons Attribution 4.0 International Public License](https://creativecommons.org/licenses/by/4.0/legalcode),
see the [LICENSE](LICENSE) file, and grant you a license to any code in the repository under the [MIT License](https://opensource.org/licenses/MIT), see the
[LICENSE-CODE](LICENSE-CODE) file.

Microsoft, Windows, Microsoft Azure and/or other Microsoft products and services referenced in the documentation may be either trademarks or registered trademarks of Microsoft in the United States and/or other countries. The licenses for this project do not grant you rights to use any Microsoft names, logos, or trademarks.
Microsoft's general trademark guidelines can be found at http://go.microsoft.com/fwlink/?LinkID=254653.

Privacy information can be found at https://privacy.microsoft.com/en-us/

Microsoft and any contributors reserve all other rights, whether under their respective copyrights, patents,
or trademarks, whether by implication, estoppel or otherwise.

