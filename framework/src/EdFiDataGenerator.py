import random
from DataGenUtil import *
import json
from faker import Faker

GENDER = ['Male','Female']
BOOLEAN = [True, False]
OPERATIONAL_STATUS = ['Active','Inactive']
CHARTER_STATUS = ['School Charter', 'Open Enrollment Charter', 'Not a Charter School']
GRADE_LEVEL = ['First Grade','Second Grade','Third Grade','Fourth Grade','Fifth Grade','Sixth Grade','Seventh Grade','Eighth Grade','Ninth Grade','Tenth Grade','Eleventh Grade','Twelfth Grade']
SCHOOL_TYPES = ['High School', 'Middle School', 'Elementary School']
SUBJECT_NAMES = [('Math','Algebra'), ('Math','Geometry'), ('Language','English'), ('History','World History'),('Science','Biology'), ('Science','Health'), ('Technology',' Programming'), ('Physical Education','Sports'), ('Arts','Music')]
LEVELS_OF_EDUCATION = ['Some College No Degree', 'Doctorate', 'Bachelor\'s','Master\'s']
PERSONAL_INFORMATION_VERIFICATION_DESCRIPTIONS = ['Entry in family Bible', 'Other official document', 'State-issued ID', 'Hospital certificate', 'Passport', 'Parents affidavit', 'Immigration document/visa', 'Drivers license']
RACES = ['Asian' , 'Native Hawaiian - Pacific Islander', 'American Indian - Alaska Native', 'White']

class EdFiDataGenerator:
    def __init__(self,number_students_per_school=100, include_optional_fields=True, school_year='2021', credit_conversion_factor = 2.0, number_of_grades_per_school = 5, is_current_school_year = True, graduation_plans_per_school = 10, unique_id_length = 5, number_staffs_per_school = 50):
        # Set a seed value in Faker so it generates same values every run.
        self.faker = Faker('en_US')
        Faker.seed(1)

        self.include_optional_fields = include_optional_fields
        self.graduation_plans_per_school = graduation_plans_per_school
        self.school_year = school_year
        self.country = 'United States of America'
        self.number_students_per_school = number_students_per_school
        self.credit_conversion_factor = credit_conversion_factor
        self.number_of_grades_per_school = number_of_grades_per_school
        self.is_current_school_year = is_current_school_year
        self.unique_id_length = unique_id_length
        self.number_staffs_per_school = number_staffs_per_school

    def get_descriptor_string(self, key, value):
        return "uri://ed-fi.org/{}#{}".format(key,value)

    def generate_data(self, num_of_schools, writer):
        edfi_data = [self.create_school() for _ in range(num_of_schools)]
        edfi_data_formatted = self.format_edfi_data(edfi_data)


        writer.write(f'EdFi/School.json',list_of_dict_to_json(edfi_data_formatted['Schools']))
        writer.write(f'EdFi/Student.json',list_of_dict_to_json(edfi_data_formatted['Students']))
        writer.write(f'EdFi/StudentSchoolAssociation.json',list_of_dict_to_json(edfi_data_formatted['StudentSchoolAssociations']))
        writer.write(f'EdFi/Course.json',list_of_dict_to_json(edfi_data_formatted['Courses']))
        writer.write(f'EdFi/Calendar.json',list_of_dict_to_json(edfi_data_formatted['Calendars']))

    def create_school(self):
        school_type = random.choice(SCHOOL_TYPES)
        school_name = self.faker.city() + ' ' + school_type
        school = {
            'Id': self.faker.uuid4().replace('-',''),
            'SchoolId': self.faker.random_number(digits = self.unique_id_length),
            'NameOfInstitution': school_name,
            'OperationalStatusDescriptor': self.get_descriptor_string('OperationalStatusDescriptor',random.choice(OPERATIONAL_STATUS)),
            'ShortNameOfInstitution': ''.join([word[0] for word in school_name.split()]),
            'Website':''.join(['www.',school_name.lower().replace(' ',''),'.com']),
            'AdministrativeFundingControlDescriptor': self.get_descriptor_string('AdministrativeFundingControlDescriptor',random.choice(['public', 'private']) + ' School'),
            'CharterStatusDescriptor': self.get_descriptor_string('CharterStatusDescriptor',random.choice(CHARTER_STATUS)),
            'SchoolTypeDescriptor': self.get_descriptor_string('SchoolTypeDescriptor','Regular'),
            'TitleIPartASchoolDesignationDescriptor': self.get_descriptor_string('TitleIPartASchoolDesignationDescriptor','Not A Title I School'),
            'Addresses': self.create_address() if self.include_optional_fields else '',
            'EducationOrganizationCategories':[{'EducationOrganizationCategoryDescriptor': self.get_descriptor_string('educationOrganizationCategoryDescriptor','School')}],
            'IdentificationCodes': [
                {
                    'educationOrganizationIdentificationSystemDescriptor': self.get_descriptor_string('educationOrganizationIdentificationSystemDescriptor','SEA'),
                    'identificationCode': self.faker.random_number(digits=10)
                }
            ],
            'InstitutionTelephones': self.create_telephones(),
            'InternationalAddresses': [],
            'SchoolCategories': [
                {
                    'SchoolCategoryDescriptor': self.get_descriptor_string('SchoolCategoryDescriptor',school_type)
                }
            ],
            'gradeLevels': [
                {'gradeLevelDescriptor': self.get_descriptor_string('GradeLevelDescriptor',random.choice(GRADE_LEVEL))} for _ in range(4)
            ]
        }

        school['_SchoolYears'] = self.create_school_years()
        school['_Calendars'] = self.create_calendars(school)
        school['_Students'] = self.create_students()
        school['_Courses'] = self.create_courses(school['SchoolId'],school['Id'],school_name)
        school['_GraduationPlans'] = self.create_graduation_plans(school)
        school['_StudentAssociations'] = self.create_student_school_associations(school)
        school['_Staffs'] = self.create_staffs()
        school['_Sessions'] = self.create_sessions(school)

        return school

    def create_students(self):
        students = []
        for _ in range(self.number_students_per_school):
            gender = random.choice(GENDER)
            fname = self.faker.first_name_male() if gender == 'Male' else self.faker.first_name_female()
            students.append({
                'Id': self.faker.uuid4().replace('-',''),
                'StudentUniqueId': self.faker.random_number(digits = self.unique_id_length),
                "BirthCity": self.faker.city(),
                "BirthDate": str(self.faker.date_between(start_date='-18y',end_date='-5y')),
                "BirthSexDescriptor": self.get_descriptor_string('birthStateAbbreviationDescriptor', gender),
                "FirstName": fname,
                "IdentificationDocuments": [],
                "LastSurname": self.faker.last_name(),
                "OtherNames": [
                    {
                        "OtherNameTypeDescriptor": self.get_descriptor_string('otherNameTypeDescriptor','Nickname'),
                        "FirstName": self.faker.first_name_male() if gender == 'Male' else self.faker.first_name_female(),
                        "PersonalTitlePrefix": 'Mr' if gender == 'Male' else 'Ms'
                    }
                ],
                "PersonalIdentificationDocuments": [],
                "PersonalTitlePrefix": 'Mr' if gender == 'Male' else 'Ms',
                "Visas": [],
                "_etag": self.faker.random_number(digits=10)
        })
        return students


    def create_student_school_associations(self,school):
        result = []
        graduation_plan_ids = [gp['Id'] for gp in school['_GraduationPlans']]
        for student in school['_Students']:
            result.append({
                'Id': self.faker.uuid4().replace('-',''),
                "GraduationPlanReference": {
                    "EducationOrganizationId": school['SchoolId'],
                    "GraduationPlanTypeDescriptor": "uri://ed-fi.org/GraduationPlanTypeDescriptor#Minimum",
                    "GraduationSchoolYear": self.school_year,
                    "Link": {
                        "rel": "GraduationPlan",
                        "href": '/ed-fi/graduationPlans/{}'.format(random.choice(graduation_plan_ids))
                    }
                },
                "SchoolReference": {
                    "SchoolId": school['SchoolId'],
                    "Link": {
                        "rel": "School",
                        "href": '/ed-fi/schools/{}'.format(school['Id'])
                    }
                },
                "StudentReference": {
                    "StudentUniqueId": student['StudentUniqueId'],
                    "Link": {
                        "rel": "Student",
                        "href": "/ed-fi/students/{}".format(student['Id'])
                    }
                },
                "EntryDate": str(self.faker.date_between(start_date='-5y',end_date='today')),
                "EntryGradeLevelDescriptor": "uri://ed-fi.org/GradeLevelDescriptor#{}".format(random.choice(GRADE_LEVEL)),
                "AlternativeGraduationPlans": [],
                "EducationPlans": [],
                "_etag": self.faker.random_number(digits=10)
            })
        return result

    def create_calendars(self,school):
        return {
            'Id': self.faker.uuid4().replace('-',''),
            'CalendarCode':self.faker.random_number(digits = self.unique_id_length),
            "SchoolReference": {
                "SchoolId": school['SchoolId'],
                "Link": {
                    "rel": "School",
                    "href": "/ed-fi/schools/{}".format(school['Id'])
                }
            },
            "SchoolYearTypeReference": {
                "SchoolYear": self.school_year,
                "Link": {
                    "rel": "SchoolYearType",
                    "href": "/ed-fi/schoolYearTypes/{}".format(school['_SchoolYears']['Id'])
                }
            },
            'CalendarTypeDescriptor': self.get_descriptor_string('calendarTypeDescriptor','Student Specific'),
            'GradeLevel': []
        }

    def create_address(self):
        address = []
        state = self.faker.state_abbr()
        for n in ['Physical', 'Mailing']:
            address.append({
                'AddressType':n,
                'City':self.faker.city(),
                'PostalCode':self.faker.postcode(),
                'StateAbbreviation':state,
                'StreetNumberName':self.faker.street_name()
            })
        return address

    def create_courses(self,school_id,id,school_name):
        courses = []
        for subject,course_name in SUBJECT_NAMES:
            courses.append({
                "Id": self.faker.uuid4().replace('-',''),
                "EducationOrganizationReference": {
                    "EducationOrganizationId": school_id,
                    "Link": {
                        "rel": "School",
                        "href": "/ed-fi/schools/{}".format(id)
                    }
                },
                "CourseCode": self.faker.random_number(digits = self.unique_id_length),
                "AcademicSubjectDescriptor": self.get_descriptor_string('academicSubjectDescriptor', subject),
                "CourseDefinedByDescriptor": self.get_descriptor_string('CourseDefinedByDescriptor','SEA'),
                "CourseDescription": 'Description about {}'.format(course_name),
                "CourseGPAApplicabilityDescriptor": self.get_descriptor_string('CourseGPAApplicabilityDescriptor',random.choice(['Applicable','Not Applicable'])),
                "CourseTitle": course_name,
                "HighSchoolCourseRequirement": random.choice(BOOLEAN),
                "NumberOfParts": 1,
                "CompetencyLevels": [],
                "IdentificationCodes": [
                    {
                        "CourseIdentificationSystemDescriptor": self.get_descriptor_string('CourseIdentificationSystemDescriptor','LEA course code'),
                        "CourseCatalogURL": "http://www.{}.edu/coursecatalog".format(school_name.lower().replace(' ','')),
                        "IdentificationCode": '{}-{}'.format(course_name[0:3].upper(),random.choice(range(1,5)))
                    },
                    {
                        "CourseIdentificationSystemDescriptor": self.get_descriptor_string('CourseIdentificationSystemDescriptor','State course code'),
                        "IdentificationCode": self.faker.random_number(digits = self.unique_id_length)
                    }
                ],
                "LearningObjectives": [],
                "LearningStandards": [
                    {
                        "LearningStandardReference": {
                            "LearningStandardId": self.faker.random_number(digits = self.unique_id_length),
                            "Link": {
                                "rel": "LearningStandard",
                                "href": "/ed-fi/learningStandards/{}".format(self.faker.uuid4().replace('-',''))
                            }
                        }
                    }
                ],
                "LevelCharacteristics": [
                    {
                        "CourseLevelCharacteristicDescriptor": self.get_descriptor_string('CourseLevelCharacteristicDescriptor','Core Subject')
                    }
                ],
                "OfferedGradeLevels": [],
                "_etag": self.faker.random_number(digits=10)
            })
        return courses


    def create_graduation_plans(self, school):
        graduation_plans = []
        for _ in range(self.graduation_plans_per_school):
            graduation_plans.append({
                'Id': self.faker.uuid4().replace('-',''),
                "EducationOrganizationReference": {
                    "EducationOrganizationId": school['SchoolId'],
                    "link": {
                        "rel": "School",
                        "href": "/ed-fi/schools/{}".format(school['Id'])
                    }
                },
                "GraduationSchoolYearTypeReference": {
                    "SchoolYear": self.school_year,
                    "Link": {
                        "rel": "SchoolYearType",
                        "href": "/ed-fi/schoolYearTypes/{}".format(school['_SchoolYears']['Id'])
                    }
                },
                "GraduationPlanTypeDescriptor": self.get_descriptor_string('GraduationPlanTypeDescriptor', random.choice(['Minimum','Recommended'])),
                "TotalRequiredCredits": random.choice(range(20,30)),
                "CreditsByCourses": [],
                "CreditsByCreditCategories": [
                    {
                        "CreditCategoryDescriptor": self.get_descriptor_string('CreditCategoryDescriptor','Honors'),
                        "Credits": random.choice(range(5,15))
                    }
                ],
                "CreditsBySubjects": [],
                "RequiredAssessments": [],
                "_etag": self.faker.random_number(digits=10)
            })
        return graduation_plans

    def create_school_years(self):
        return {
            'Id': self.faker.uuid4().replace('-',''),
            'SchoolYear': self.school_year,
            'CurrentSchoolYear': self.is_current_school_year,
            'schoolYearDescription': 'Description about school year',
            '_etag': self.faker.random_number(digits=10)
        }

    def create_telephones(self):
        return [
            {
                'InstitutionTelephoneNumberTypeDescriptor': self.get_descriptor_string('InstitutionTelephoneNumberTypeDescriptor', _),
                "TelephoneNumber": self.faker.phone_number()
            }
            for _ in ['Fax','Main']
        ]

    def create_staffs(self):
        staffs = []
        for _ in range(self.number_staffs_per_school):

            gender = random.choice(GENDER)
            fname = self.faker.first_name_male() if gender == 'Male' else self.faker.first_name_female()
            lname = self.faker.last_name()
            staffs.append({
                "id": self.faker.uuid4().replace('-',''),
                "staffUniqueId": self.faker.random_number(digits = self.unique_id_length),
                "birthDate": str(self.faker.date_between(start_date='-60y',end_date='-30y')),
                "firstName": fname,
                "highestCompletedLevelOfEducationDescriptor": self.get_descriptor_string('LevelOfEducationDescriptor', value = random.choice(LEVELS_OF_EDUCATION)),
                "hispanicLatinoEthnicity": random.choice(BOOLEAN),
                "lastSurname": lname,
                "loginId": '{}{}'.format(fname[0],lname.lower()),
                "personalTitlePrefix": 'Mr' if gender == 'Male' else 'Ms',
                "sexDescriptor": self.get_descriptor_string('SexDescriptor', value = gender),
                "yearsOfPriorProfessionalExperience": random.choice(range(50)),
                "addresses": self.create_address(),
                "ancestryEthnicOrigins": [],
                "credentials": [
                    {
                        "credentialReference": {
                            "credentialIdentifier": self.faker.random_number(digits = 10),
                            "stateOfIssueStateAbbreviationDescriptor": self.get_descriptor_string('StateAbbreviationDescriptor', 'TX'),
                            "link": {
                                "rel": "Credential",
                                "href": "/ed-fi/credentials/" + self.faker.uuid4().replace('-','')
                            }
                        }
                    }
                ],
                "electronicMails": [
                {
                    "electronicMailAddress": "{}{}@edfi.org".format(fname,lname),
                    "electronicMailTypeDescriptor": self.get_descriptor_string('ElectronicMailTypeDescriptor','Work')
                }
                ],
                "identificationCodes": [
                {
                    "staffIdentificationSystemDescriptor": self.get_descriptor_string('StaffIdentificationSystemDescriptor','State'),
                    "identificationCode": self.faker.random_number(digits = self.unique_id_length)
                }
                ],
                "identificationDocuments": [],
                "internationalAddresses": self.create_address(),
                "languages": [],
                "otherNames": [self.faker.first_name_male() if gender == 'Male' else self.faker.first_name_female()],
                "personalIdentificationDocuments": [
                {
                    "identificationDocumentUseDescriptor": "uri://ed-fi.org/IdentificationDocumentUseDescriptor#Personal Information Verification",
                    "personalInformationVerificationDescriptor": self.get_descriptor_string('PersonalInformationVerificationDescriptor', value = random.choice(PERSONAL_INFORMATION_VERIFICATION_DESCRIPTIONS))
                }
                ],
                "races": [
                {
                    "raceDescriptor": self.get_descriptor_string('RaceDescriptor', value = random.choice(RACES))
                }
                ],
                "_etag": self.faker.random_number(digits=10)
            })
        return staffs

    def create_sessions(self, school):

        return [{
            "id": self.faker.uuid4().replace('-',''),
            "schoolReference":{
                "schoolId":school['SchoolId'],
                "link":{
                    "rel":"School",
                    "href":"/ed-fi/schools/{}".format(school['Id'])
                }
            },
            "schoolYearTypeReference": {
                "SchoolYear": self.school_year,
                "link": {
                    "rel": "SchoolYearType",
                    "href": "/ed-fi/schoolYearTypes/{}".format(school['_SchoolYears']['Id'])
                }
            },
            "sessionName": "{} - {} Fall Semester".format(int(self.school_year) - 1, self.school_year ),
            "beginDate": "{}-08-{}".format(int(self.school_year) - 1, random.randint(1,30)),
            "endDate": "{}-12-{}".format(int(self.school_year) - 1, random.randint(1,30)),
            "termDescriptor": self.get_descriptor_string('TermDescriptor', 'Fall Semester'),
            "totalInstructionalDays": random.randint(60,130),
            "gradingPeriods": [
                {
                    "gradingPeriodReference": {
                    "schoolId": school['SchoolId'],
                    "schoolYear": self.school_year,
                    "gradingPeriodDescriptor": "uri://ed-fi.org/GradingPeriodDescriptor#First Six Weeks",
                    "periodSequence": 1,
                    "link": {
                        "rel": "GradingPeriod",
                        "href": "/ed-fi/gradingPeriods/{}".format(self.faker.uuid4().replace('-',''))
                    }
                    }
                },
                {
                    "gradingPeriodReference": {
                    "schoolId": school['SchoolId'],
                    "schoolYear": self.school_year,
                    "gradingPeriodDescriptor": "uri://ed-fi.org/GradingPeriodDescriptor#Second Six Weeks",
                    "periodSequence": 2,
                    "link": {
                        "rel": "GradingPeriod",
                        "href": "/ed-fi/gradingPeriods/{}".format(self.faker.uuid4().replace('-',''))
                    }
                    }
                },
                {
                    "gradingPeriodReference": {
                    "schoolId": school['SchoolId'],
                    "schoolYear": self.school_year,
                    "gradingPeriodDescriptor": "uri://ed-fi.org/GradingPeriodDescriptor#Third Six Weeks",
                    "periodSequence": 3,
                    "link": {
                        "rel": "GradingPeriod",
                        "href": "/ed-fi/gradingPeriods/{}".format(self.faker.uuid4().replace('-',''))
                    }
                    }
                }
            ],
            "_etag": self.faker.random_number(digits=10)
        },
        {
            "id": self.faker.uuid4().replace('-',''),
            "schoolReference":{
                "schoolId":school['SchoolId'],
                "link":{
                    "rel":"School",
                    "href":"/ed-fi/schools/{}".format(school['Id'])
                }
            },
            "schoolYearTypeReference": {
                "SchoolYear": self.school_year,
                "link": {
                    "rel": "SchoolYearType",
                    "href": "/ed-fi/schoolYearTypes/{}".format(school['_SchoolYears']['Id'])
                }
            },
            "sessionName": "{} - {} Spring Semester".format(int(self.school_year) - 1, self.school_year),
            "beginDate": "{}-01-{}".format(self.school_year, random.randint(1,30)),
            "endDate": "{}-05-{}".format(self.school_year, random.randint(1,30)),
            "termDescriptor": self.get_descriptor_string('TermDescriptor', 'Spring Semester'),
            "totalInstructionalDays": random.randint(60,130),
            "gradingPeriods": [
                {
                    "gradingPeriodReference": {
                    "schoolId": school['SchoolId'],
                    "schoolYear": self.school_year,
                    "gradingPeriodDescriptor": "uri://ed-fi.org/GradingPeriodDescriptor#Fourth Six Weeks",
                    "periodSequence": 4,
                    "link": {
                        "rel": "GradingPeriod",
                        "href": "/ed-fi/gradingPeriods/{}".format(self.faker.uuid4().replace('-',''))
                    }
                    }
                },
                {
                    "gradingPeriodReference": {
                    "schoolId": school['SchoolId'],
                    "schoolYear": self.school_year,
                    "gradingPeriodDescriptor": "uri://ed-fi.org/GradingPeriodDescriptor#Fifth Six Weeks",
                    "periodSequence": 5,
                    "link": {
                        "rel": "GradingPeriod",
                        "href": "/ed-fi/gradingPeriods/{}".format(self.faker.uuid4().replace('-',''))
                    }
                    }
                },
                {
                    "gradingPeriodReference": {
                    "schoolId": school['SchoolId'],
                    "schoolYear": self.school_year,
                    "gradingPeriodDescriptor": "uri://ed-fi.org/GradingPeriodDescriptor#Sixth Six Weeks",
                    "periodSequence": 6,
                    "link": {
                        "rel": "GradingPeriod",
                        "href": "/ed-fi/gradingPeriods/{}".format(self.faker.uuid4().replace('-',''))
                    }
                    }
                }
            ],
            "_etag": self.faker.random_number(digits=10)
        }]

    def create_sections(self):
        return {
            "id":"",
            "courseOfferingReference":{
                "localCourseCode": "ALG-1",
                "schoolId": 255901001,
                "schoolYear": 2011,
                "sessionName": "2010-2011 Fall Semester",
                "link": {
                    "rel": "CourseOffering",
                    "href": "/ed-fi/courseOfferings/b8d13c217987448f93f7c2ad9df295a6"
                }
            },
            "locationReference":{
            "classroomIdentificationCode": "220",
            "schoolId": 255901001,
            "link": {
                "rel": "Location",
                "href": "/ed-fi/locations/6e0e2ade0a0e487c80ca8a41f1849450"
            }
            },
            "locationSchoolReference":"",
            "sectionIdentifier":"",
            "availableCredits":"",
            "educationalEnvironmentDescriptor":"",
            "sectionName":"",
            "sequenceOfCourse":"",
            "characteristics":"",
            "classPeriods": [
                {
                "classPeriodReference": {
                "schoolId": 255901001,
                "classPeriodName": "02 - Traditional",
                "link": {
                    "rel": "ClassPeriod",
                    "href": "/ed-fi/classPeriods/1635dc8273a54ed3a4f7be56366b816a"
                }
                }
            }
            ],
            "courseLevelCharacteristics": [],
            "offeredGradeLevels": [],
            "programs": [],
            "_etag": "5249285328760938689"
        }

    def format_edfi_data(self,data):
        result = {
            'Schools':[],
            'Students':[],
            'Calendars':[],
            'Courses':[],
            'StudentSchoolAssociations':[]
        }
        for school in data:
            result['Schools'].append({key: school[key] for key in school if not (key.startswith('_')) })
            result['Students'] += school['_Students']
            result['Courses'] += school['_Courses']
            result['StudentSchoolAssociations'] += school['_StudentAssociations']
            result['Calendars'].append(school['_Calendars'])

        return result
