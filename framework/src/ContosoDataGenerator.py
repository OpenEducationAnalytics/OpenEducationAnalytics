import datetime
import random
import math
import pandas as pd
from faker import Faker

SUBJECTS = ['Math - Algebra', 'Math - Geometry', 'English Language', 'History - World History',
            'Science Biology', 'Health', 'Technology - Programming', 'Physical Education', 'Art', 'Music']
SCHOOL_TYPES = ['Elementary', 'Middle', 'High']
GRADES = [(0, 'Kindergarten'), (1, 'First'), (2, 'Second'), (3, 'Third'),
          (4, 'Fourth'), (5, 'Fifth'), (6, 'Sixth'), (7, 'Seventh'), (8, 'Eigth')]
ACTIONS = [('ID', 'In-school Suspension'), ('ES', 'Restorative Dialogue'), ('RJ', 'Restorative Justice'), ('EY', 'Expelled Remainder Of School/yr'),
           ('As', 'Tcher/parent/student Conference'), ('IS', 'In-school Detention'), ('LD', 'Lunch Detention'), ('PC', 'Parent Contact'), ('EL', 'Expelled Less Than School Year'),
           ('AC', 'Behavior/Attendance Contract'), ('VB', 'Verbal Warning'), ('SF', 'Suspension 5 Days Or Less'), ('RS', 'Referral To Social Worker'), ('SM', 'Suspension More Than Five Days'),
           ('SS', 'Saturday School'), ('AP', 'Admin/Prnt/Gurdn/Stu Conference'), ('RF', 'Referral To Counseling'), ('DB', 'Detention Before/after School'), ('LP', 'Loss of Privileges'),
           ('IA', 'In-school Alternative'), ('Cn', 'Ref Police - No charges filed'), ('EN', 'Expelled Into Next School Year')]
ATTENDANCE_TYPES = [('V', 'Early Completion'), ('5', 'Parent Request Opt Out Testing'), ('A', 'Absent (unexcused)'), ('F', 'Field Trip'), ('C', 'Counselor'), ('X', 'Excused Tardy'), ('I', 'In School Detention'), ('Q', 'Went Home Ill'), ('O', 'Office'), ('W', 'Weather'),
                    ('6', 'State or District Testing'), ('N', 'Nurse/Infirmary'), ('G', 'Early Release/Parent'), ('H', 'Timeout to Home'), ('Y', 'In a Facility'), ('R', 'Runaway'), ('P', 'Prearranged'), ('S', 'Suspended'), ('L', 'Tutored-District'), ('D', 'Enrolled in Special Program'),
                    ('M', 'SPED ONLY in school no IEP Svcs'), ('J', 'Teacher Excused'), ('E', 'Excused Absence'), ('T', 'Tardy (Unexcused)'), ('Pr', 'Present'), ('K', 'Social Worker'), ('Z', 'In Detention Center (SCYSC)')]
INVOLVEMENTS = [('A', 'Accomplice'), ('W', 'Witness'), ('V', 'Victim'), ('P', 'Perpetrator'), ('N', 'Not Applicable')]
INCIDENTS = [('AA1', 'L1 Unexcused Absences'), ('ALA', 'L2 Abusive Lang w/Staff'), ('ALP', 'L1 Abusive Lang/Intim w/Student'), ('APL', 'L3 Any Act Prohibit by F/S/L Law'),
             ('ASR', 'L2 Altering Sch/Classrm Rcrds'), ('AT3', 'L3 3rd Degree Assault  (by adult'), ('CLM', 'L1 Classroom Misconduct'), ('CLO', 'L2 Continual LEVEL I Infraction'),
             ('CLT', 'L3 Continual LEVEL II Infraction'), ('CP2', 'L2 Campus Misconduct'), ('CPM', 'L1 Campus Misconduct'), ('DEP', 'L3 Destruction/Sch/Emp Prop'), ('DIS', 'L1 Dishonesty'),
             ('DSP', 'L2 Defacing School Prop'), ('FCD', 'L2 Fail Complete Disc Asignmt'), ('FIG', 'L2 Fighting'), ( 'HA3', 'L3 Harassment'), ('HAR', 'L2 Harassment'), ('IDH', 'L1 Inappropriate Dress/Hygiene'),
             ('INS', 'L1 Insubordination'), ('IS2', 'L2 Insubor/open/persist defiance'), ('L1E', 'L1 Inappropriate/Prsnl Elect Dev'), ('L2B', 'L2 Bullying'), ('L2E', 'L2 Inappropriate/Prsnl Elect Dev'),
             ('L2P', 'L2 Phys Mistreatment of Studnt'), ('L2V', 'L2 Violation of AUA'), ('L3A', 'L3 P/U of Alcohol'), ('L3D', 'L3 P/U of Drug Paraphernalia'), ('PSV', 'L2 P/D/S Sched 4 or 5 substances'),
             ('PU4', 'L4 P/U Dangerous Weapon'), ('PUT', 'L2 P/U of  Tobacco/Simulated'), ('PUW', 'L2 Inadvertent  Pos(Stand )Weap'), ('SV2', 'L2 Serious Violations at School'), ('SV3', 'L3 Serious Violations at School'),
             ('THE', 'L2 Theft'), ('ULC', 'L2 Unauthorized Leaving Campus'), ('ULM', 'L3 Unlawful U/P/D/S of Marijuana'), ('UNA', 'L2 Unexcused Absences/Truancy'), ('UNT', 'L1 Unexcused Tardiness'), ('WF3', 'L3 Weapon/Facsimile (Standard)')]

class ContosoDataGenerator:
    def __init__(self, students_per_school=100, classes_in_student_schedule=6, students_per_section=25, student_teacher_ratio=9, include_optional_fields=True,
                 fall_semester_start_date='2021-08-15', fall_semester_end_date='2021-12-15', spring_semester_start_date='2022-01-10', spring_semester_end_date='2022-05-10'):
        # Set a seed value in Faker so it generates the same values every time it's run
        self.faker = Faker('en_US')
        Faker.seed(1)

        self.students_per_school = students_per_school
        self.classes_in_student_schedule = classes_in_student_schedule
        self.students_per_section = students_per_section
        self.student_teacher_ratio = student_teacher_ratio
        self.include_optional = include_optional_fields
        self.fall_semester_start_date = fall_semester_start_date
        self.fall_semester_end_date = fall_semester_end_date
        self.spring_semester_start_date = spring_semester_start_date
        self.spring_semester_end_date = spring_semester_end_date

        self.teachers_per_school = math.ceil(self.students_per_school/self.student_teacher_ratio)
        self.section_id = 1
        self.student_id = 1
        self.teacher_id = 1
        self.course_id = 1
        self.school_id = 1
        self.term_id = 1
        self.domain = '@Classrmtest86.org'

    def create_school(self, school_id):
        school_info = {
            'SchoolID': school_id,
            'SchoolName': f"{self.faker.last_name()} {random.choice(SCHOOL_TYPES)}"
        }
        school_data = {}
        school_data['Students'] = self.create_students(school_id)
        school_data['Courses'] = self.create_courses()
        school_data['Terms'] = self.create_terms()
        school_data['Attendance'], school_data['ClassAttendance'], school_data['DailyIncidents'] = self.create_daily_records(school_id, school_data)
        return school_info, school_data

    def create_students(self, school_id):
        students = []
        for n in range(self.students_per_school):
            students.append(self.create_student(
                school_id, self.student_id, 'student'))
            self.student_id += 1
        return students

    def create_student(self, school_id, user_id, user_type):
        grade_num, grade = random.choice(GRADES)
        gender = random.choice(['Male', 'Female'])
        if gender == 'Male': fname = self.faker.first_name_male()
        else: fname = self.faker.first_name_female()

        user = {
            'ID': user_id,
            'Firstname': fname,
            'Lastname': self.faker.last_name(),
            'Gender': gender,
            'FederalRaceCategory': random.choice(['Asian', 'Black', 'White', 'Hispanic', 'American Indian']),
            'PrimaryLanguage': random.choices(['English', 'Spanish', 'German', 'French', 'Japanese'], weights=(85, 10, 2, 2, 1))[0],
            'ELLStatus': random.choices(['', 'English Learner', 'Initially Fluent English Proficient', 'Redesignated Fluent English Proficient'], weights=(80, 10, 5, 5))[0],
            'SpecialEducation': random.choices(['', 'Designated Instruction Service', 'Resource Specialty Program', 'Special Day Class'], weights=(80, 10, 5, 5))[0],
            'LowIncome': random.choices([0, 1], weights=(60, 40))[0],
            'GradeNumber': grade_num,
            'Grade': grade,
            'CumulativeGPA': random.choice([0.523, 0.423, 1.13, 2.63, 2.33, 3.33, 4.0]),
            'StartSchoolYear': self.fall_semester_start_date,
            'EndSchoolYear': self.spring_semester_end_date
        }
        return user

    def create_terms(self):
        terms = []
        terms.append({
            'TermID': self.term_id,
            'TermName': 'Fall Semester',
            'TermStartDate': self.fall_semester_start_date,
            'TermEndDate': self.fall_semester_end_date,
        })
        self.term_id += 1
        terms.append({
            'TermID': self.term_id,
            'TermName': 'Spring Semester',
            'TermStartDate': self.spring_semester_start_date,
            'TermEndDate': self.spring_semester_end_date,
        })
        self.term_id += 1
        return terms

    def create_courses(self):
        courses = []
        for subject in SUBJECTS:
            courses.append({
                'CourseID': self.course_id,
                'CourseName': subject,
                'CourseCode': subject
            })
            self.course_id += 1
        return courses

    def create_daily_records(self, school_id, school_data):
        date_range = pd.date_range(datetime.datetime.strptime(self.fall_semester_start_date, "%Y-%m-%d"), datetime.datetime.strptime(self.spring_semester_end_date, "%Y-%m-%d"))
        daily_attendance = []
        class_attendance = []
        incidents = []
        for student in school_data['Students']:
            for single_date in date_range:
                daily_attendance.append(self.create_daily_attendance_record(school_id, student, single_date))
                class_attendance.append(self.create_class_attendance_record(school_id, student, single_date, school_data['Courses']))
                if (random.randint(1, 100)) <= 10:  # 10% chance of an incident occurring
                    incidents.append(self.create_incident_record(school_id, student['ID'], single_date))
        return (daily_attendance, class_attendance, incidents)

    def create_class_attendance_record(self, school_id, student_id, date_value, courses):
        # todo: fix term id to use the correct term id based on the date
        class_attendance = {
            'SchoolID': school_id,
            'AttendanceDate': date_value.strftime("%Y-%m-%d"),
            'StudentID': student_id,
            'Term': '1',
            'CourseID': random.choice(courses)['CourseID'],
            'AttendTypeID': random.choice(ATTENDANCE_TYPES)[0]
        }
        return class_attendance

    def create_incident_record(self, school_id, student_id, date_value):
        incident_id, incident = random.choice(INCIDENTS)
        involvement_id, incident = random.choice(INVOLVEMENTS)
        action_id, action = random.choice(ACTIONS)
        incident_record = {
            'StudentID': student_id,
            'SchoolID': school_id,
            'IncidentID': incident_id,
            'InvolvementID': involvement_id,
            'IncidentDate': date_value.strftime("%Y-%m-%d"),
            'ActionID': action_id
        }
        return incident_record

    def create_daily_attendance_record(self, school_id, student, date_value):
        possible_periods_in_day = 6
        unexcused_all_day = random.choices([0, 1], weights=(80, 20))[0]
        if unexcused_all_day == 1:
            excused_all_day = 0
        else:
            excused_all_day = random.choices([0, 1], weights=(70, 30))[0]

        attendance_record = {
            'SchoolID': school_id,
            'AttendanceDate': date_value.strftime("%Y-%m-%d"),
            'StudentID': student['ID'],
            'NumofPossiblePeriods': possible_periods_in_day,
            'NumofTardies': random.choices([0, 1, 2, 3, 4, 5, 6], weights=(50, 20, 10, 5, 5, 5, 5))[0],
            'NumofUnexcusedAbsent': random.choices([0, 1, 2, 3], weights=(70, 10, 10, 10))[0],
            'NumofExcusedAbsent': random.choices([0, 1, 2, 3], weights=(60, 20, 10, 10))[0],
            'UnexcusedAllDay': unexcused_all_day,
            'ExcusedAllDay': excused_all_day,
            'Cumulative GPA': student['CumulativeGPA']
        }
        return attendance_record
