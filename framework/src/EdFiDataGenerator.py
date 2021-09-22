import random
import math
from DataGenUtil import *
from faker import Faker

GENDER = ['Male','Female']
BOOLEAN = [True, False]
SCHOOL_YEARS = ['2021','2022','2023','2024','2025']
CITIES = ['Seattle','San Francisco','San Diego','Philadelphia','Chicago','Houston','New York','Los Angeles']
GRADE_LEVEL = ['01','02','03','04','05','06','07','08','09','10','11','12']
SCHOOL_TYPES = ['High School', 'Middle School', 'Elementary School']
COURSE_NAMES = ['Math - Algebra', 'Math - Geometry', 'English Language', 'History - World History',
'Science Biology', 'Health', 'Technology - Programming', 'Physical Education', 'Art', 'Music']
COURSE_TYPES = ['Remedial', 'Basic', 'Honors', 'Ap', 'IB', 'Dual Credit', 'CTE']
ORG_TYPES = ['national organization','school','local education agency','state education agency']

#Placeholders- Need to updated
GRAD_PLAN_TYPE = ['GP_1','GP_2','GP_3']
CREDIT_TYPE = ['CT_1','CT_2','CT_3']
EDUCATION_PLAN = ['EP_1','EP_2','EP_3']
RESIDENCY_STATUS = ['RS_1','RS_2','RS_3']


class EdFiDataGenerator:
    def __init__(self,number_students_per_school=100, include_optional_fields=True, school_year='2021', credit_conversion_factor = 2.0):
        # Set a seed value in Faker so it generates same values every run.
        self.faker = Faker('en_US')
        Faker.seed(1)

        self.include_optional_fields = include_optional_fields
        self.school_year = school_year
        self.country = 'United States of America'
        self.number_students_per_school = number_students_per_school
        self.course_set_counter = 1
        self.credit_conversion_factor = credit_conversion_factor

    def generate_data(self, num_of_schools, writer):
        for n in range(num_of_schools):
            school_data = self.create_school(n)
            includeHeaders = True if n==0 else False
            writer.write(f'EdFi/School.csv',obj_to_csv(school_data)+"\n")
            writer.write(f'EdFi/Students.csv',list_of_dict_to_csv(school_data['_Students'],includeHeaders = includeHeaders))
            writer.write(f'EdFi/StudentSchoolAssociation.csv',list_of_dict_to_csv(school_data['_StudentAssociation'], includeHeaders = includeHeaders))
            writer.write(f'EdFi/Courses.csv',list_of_dict_to_csv(school_data['_Courses'], includeHeaders = includeHeaders))

    def create_school(self, school_id):
        school_name = self.faker.city() + ' ' + random.choice(SCHOOL_TYPES)
        school =  {
            'SchoolId': school_id,
            'Address': self.create_address(),
            'EducationOrganizationCategories': ["School"],
            'NameOfInstitution': school_name,
            'ShortNameOfInstitution': ''.join(x[0].upper() for x in school_name.split(' ')),
            'WebSite':'www.'+school_name.lower().replace(' ','')+random.choice(['.com','.org','.info']),
            'AdministrativeFundingControl': random.choice(['public', 'private']) if self.include_optional_fields else '',
            'CharterApprovalSchoolYear': self.school_year if self.include_optional_fields else '',
            'CharterStatus': random.choice(['School Charter', 'Open Enrollment Charter', 'Not a Charter School']) if self.include_optional_fields else '',
            'SchoolCategory': random.choice(SCHOOL_TYPES) if self.include_optional_fields else '',
            'TitleIPartASchoolDesignation': random.choice(['Not A Title I School']) if self.include_optional_fields else '' # Populate this
        }
        school['_Calendar'] = self.create_calendar(school_id)
        school['_Students'] = self.create_students()
        school['_Courses'] = self.create_courses(school_id)
        school['_StudentAssociation'] = self.create_student_school_association(school)
        
        return school

    def create_students(self):
        students = []
        for n in range(self.number_students_per_school):
            isBornInUSA = random.choices(BOOLEAN, weights=(90,10))[0]
            gender = random.choice(GENDER)
            fname = self.faker.first_name_male() if gender == 'Male' else self.faker.first_name_female()
            students.append(self.create_student(n,gender,fname,isBornInUSA))
        
        return students

    def create_student(self, student_id, gender, fname, isBornInUSA):
        return {
            'StudentUniqueId': 'stu_' + str(student_id),
            'BirthData': {
                'BirthCity': random.choice(CITIES),
                'BirthCountry': self.country,
                'BirthDate': str(self.faker.date_between(start_date='-20y',end_date='-5y')),
                'BirthInternationalProvince': '' if isBornInUSA == True else  'India',
                'BirthSex': gender,
                'DateEnteredUS': '' if isBornInUSA == True else str(self.faker.date_between(start_date='-20y',end_date='-1y')),
                'MultipleBirthStatus': random.choice(BOOLEAN)
            },
            'Citizenship': '' if self.include_optional_fields else '',# populate this
            'Name': fname + ' ' + self.faker.last_name(),
            'OtherName': self.faker.first_name() if self.include_optional_fields else ''
        }

    def create_student_school_association(self,school):
        result = []
        for student in school['_Students']:
            start_date = self.faker.date_between(start_date='-5y',end_date='today')
            result.append({
                'EntryDate': str(start_date),
                'SchoolId': school['SchoolId'],
                'StudentId': student['StudentUniqueId'],
                'AlternativeGraduationPlan': self.create_graduation_plan(school),
                'CalendarId': school['_Calendar']['CalendarCode'],
                'ClassOfSchoolYear':random.choice(SCHOOL_YEARS),
                'EducationPlan':random.choice(EDUCATION_PLAN),
                'EmployedWhileEnrolled':random.choice(BOOLEAN),
                'EntryGradeLevel':random.choice(GRADE_LEVEL),
                'EntryGradeLevelReason':'',
                'EntryType':'',
                'ExitWithdrawDate':str(self.faker.date_between(start_date=start_date,end_date='today')),
                'ExitWithdrawType':'',
                'FullTimeEquivalency':f"0.{random.choice(range(9))}{random.choice(range(9))}",
                'GraduationPlan': self.create_graduation_plan(school),
                'PrimarySchool':random.choice(BOOLEAN),
                'RepeatGradeIndicator': random.choice(BOOLEAN),
                'ResidencyStatus':random.choice(RESIDENCY_STATUS),
                'SchoolChoiceTransfer': random.choice(BOOLEAN),
                'SchoolYear': self.school_year,
                'TermCompletionIndicator': random.choice(BOOLEAN),
            })
        return result

    def create_calendar(self,school_id):
        return {
            'CalendarCode':'cal_' + str(school_id),
            'SchoolId':school_id,
            'SchoolYear':self.school_year,
            'CalendarType':'',
            'GradeLevel':random.choice(GRADE_LEVEL)
        }

    def create_address(self):
        address = []
        state = self.faker.state_abbr()
        for n in ['Physical', 'Mailing']:
            address.append({
                'addressType':n,
                'city':self.faker.city(),
                'postalCode':self.faker.postcode(),
                'stateAbbreviation':state,
                'streetNumberName':self.faker.street_name()
            })
        return address

    def create_courses(self,school_id):
        courses = []
        for course_name in COURSE_NAMES:
            courses.append({
                'CourseCode':self.faker.uuid4(),
                'CourseTitle': course_name,
                'EducationOrganizationId': school_id,
                'AcademicSubject': course_name,
                'CourseDefinedBy':random.choice(ORG_TYPES),
                'CourseLevelCharacteristic': random.choice(COURSE_TYPES),
                'CourseDescription': f"A description of the content standards and goals covered in the {course_name} course",
                'HighSchoolCourseRequirement': random.choice(BOOLEAN),
                'OfferedGradeLevel': random.choices(GRADE_LEVEL,k=2),
                'TimeRequiredForCompletion': random.choice(range(100,150)),
                'NumberOfParts': random.choice(range(1,8)),
                'MaximumAvailableCredits': random.choice([3,4,5]),
                'MinimumAvailableCredits': random.choice([1,2,3]),
                'MaxCompletionsForCredit': random.choice([1,2,3]),
                'LearningStandard': '',# Add method for creating learning standard
                'DateCourseAdopted': str(self.faker.date_between(start_date='-5y',end_date='today')),
                'CourseIdentificationCode': '' #Add method for creating course identification system
            })
        return courses


    def create_graduation_plan(self, school):
        self.course_set_counter += 1
        return {
            'EducationOrganizationId':school['SchoolId'],
            'GraduationPlanType': random.choice(GRAD_PLAN_TYPE),
            'GraduationSchoolYear': int(self.school_year) + random.choice(range(1,4)),
            'CreditsByCourse':{
                'CourseSetName':'CourseSet_{self.course_set_counter}',
                'CourseId': [random.choice(school['_Courses'])['CourseCode'] for _ in range(3)],
                'Credits': {
                    'CreditConversion': self.credit_conversion_factor,
                    'CreditType': random.choice(CREDIT_TYPE),
                    'Credits': random.choice(range(2,5))
                }
            },
            'WhenTakenGradeLevel': random.choice(GRADE_LEVEL)
        }
