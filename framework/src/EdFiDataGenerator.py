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
    def __init__(self,number_students_per_school=100, include_optional_fields=True, school_year='2021', credit_conversion_factor = 2.0, number_of_grades_per_school = 5, is_current_school_year = True, graduation_plans_per_school = 10, unique_id_length = 5, number_staffs_per_school = 50, number_sections_per_school = 10):
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
        self.number_sections_per_school = number_sections_per_school

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
        writer.write(f'EdFi/Sessions.json',list_of_dict_to_json(edfi_data_formatted['Sessions']))
        writer.write(f'EdFi/StaffSchoolAssociations.json',list_of_dict_to_json(edfi_data_formatted['StaffSchoolAssociations']))
        writer.write(f'EdFi/Sections.json',list_of_dict_to_json(edfi_data_formatted['Sections']))
        writer.write(f'EdFi/Staffs.json',list_of_dict_to_json(edfi_data_formatted['Staffs']))
        writer.write(f'EdFi/StudentSectionAssociations.json',list_of_dict_to_json(edfi_data_formatted['StudentSectionAssociations']))
        writer.write(f'EdFi/StaffSectionAssociations.json',list_of_dict_to_json(edfi_data_formatted['StaffSectionAssociations']))


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
        school['_StaffSchoolAssociations'] = self.create_staff_school_associations(school)
        school['_Sessions'] = self.create_sessions(school)
        school['_Sections'] = self.create_sections(school)
        school['_StaffSectionAssociations'] = self.create_staff_section_associations(school)
        school['_StudentSectionAssociations'] = self.create_student_section_associations(school)
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
            courseCode = '{}-{}'.format(course_name[0:3].upper(),random.choice(range(1,5)))
            courses.append({
                "Id": self.faker.uuid4().replace('-',''),
                "EducationOrganizationReference": {
                    "EducationOrganizationId": school_id,
                    "Link": {
                        "rel": "School",
                        "href": "/ed-fi/schools/{}".format(id)
                    }
                },
                "CourseCode": courseCode,
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
                        "IdentificationCode": courseCode
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
                "Id": self.faker.uuid4().replace('-',''),
                "StaffUniqueId": self.faker.random_number(digits = self.unique_id_length),
                "BirthDate": str(self.faker.date_between(start_date='-60y',end_date='-30y')),
                "FirstName": fname,
                "HighestCompletedLevelOfEducationDescriptor": self.get_descriptor_string('LevelOfEducationDescriptor', value = random.choice(LEVELS_OF_EDUCATION)),
                "HispanicLatinoEthnicity": random.choice(BOOLEAN),
                "LastSurname": lname,
                "LoginId": '{}{}'.format(fname[0],lname.lower()),
                "PersonalTitlePrefix": 'Mr' if gender == 'Male' else 'Ms',
                "SexDescriptor": self.get_descriptor_string('SexDescriptor', value = gender),
                "YearsOfPriorProfessionalExperience": random.choice(range(50)),
                "Addresses": self.create_address(),
                "AncestryEthnicOrigins": [],
                "Credentials": [
                    {
                        "CredentialReference": {
                            "CredentialIdentifier": self.faker.random_number(digits = 10),
                            "StateOfIssueStateAbbreviationDescriptor": self.get_descriptor_string('StateAbbreviationDescriptor', 'TX'),
                            "Link": {
                                "rel": "Credential",
                                "href": "/ed-fi/credentials/" + self.faker.uuid4().replace('-','')
                            }
                        }
                    }
                ],
                "ElectronicMails": [
                    {
                        "ElectronicMailAddress": "{}{}@edfi.org".format(fname,lname),
                        "ElectronicMailTypeDescriptor": self.get_descriptor_string('ElectronicMailTypeDescriptor','Work')
                    }
                ],
                "IdentificationCodes": [
                    {
                        "StaffIdentificationSystemDescriptor": self.get_descriptor_string('StaffIdentificationSystemDescriptor','State'),
                        "IdentificationCode": self.faker.random_number(digits = self.unique_id_length)
                    }
                ],
                "IdentificationDocuments": [],
                "InternationalAddresses": self.create_address(),
                "Languages": [],
                "OtherNames": [self.faker.first_name_male() if gender == 'Male' else self.faker.first_name_female()],
                "PersonalIdentificationDocuments": [
                    {
                        "IdentificationDocumentUseDescriptor": "uri://ed-fi.org/IdentificationDocumentUseDescriptor#Personal Information Verification",
                        "PersonalInformationVerificationDescriptor": self.get_descriptor_string('PersonalInformationVerificationDescriptor', value = random.choice(PERSONAL_INFORMATION_VERIFICATION_DESCRIPTIONS))
                    }
                ],
                "Races": [
                    {
                        "RaceDescriptor": self.get_descriptor_string('RaceDescriptor', value = random.choice(RACES))
                    }
                ],
                "_etag": self.faker.random_number(digits=10)
            })
        return staffs

    def create_sessions(self, school):

        return [{
            "Id": self.faker.uuid4().replace('-',''),
            "SchoolReference":{
                "SchoolId":school['SchoolId'],
                "Link":{
                    "rel":"School",
                    "href":"/ed-fi/schools/{}".format(school['Id'])
                }
            },
            "SchoolYearTypeReference": {
                "SchoolYear": self.school_year,
                "Link": {
                    "rel": "SchoolYearType",
                    "href": "/ed-fi/schoolYearTypes/{}".format(school['_SchoolYears']['Id'])
                }
            },
            "SessionName": "{} - {} Fall Semester".format(int(self.school_year) - 1, self.school_year ),
            "BeginDate": "{}-08-{}".format(int(self.school_year) - 1, random.randint(1,30)),
            "EndDate": "{}-12-{}".format(int(self.school_year) - 1, random.randint(1,30)),
            "TermDescriptor": self.get_descriptor_string('TermDescriptor', 'Fall Semester'),
            "TotalInstructionalDays": random.randint(60,130),
            "GradingPeriods": [
                {
                    "GradingPeriodReference": {
                    "SchoolId": school['SchoolId'],
                    "SchoolYear": self.school_year,
                    "GradingPeriodDescriptor": "uri://ed-fi.org/GradingPeriodDescriptor#First Six Weeks",
                    "PeriodSequence": 1,
                    "Link": {
                        "rel": "GradingPeriod",
                        "href": "/ed-fi/gradingPeriods/{}".format(self.faker.uuid4().replace('-',''))
                    }
                    }
                },
                {
                    "GradingPeriodReference": {
                    "SchoolId": school['SchoolId'],
                    "SchoolYear": self.school_year,
                    "GradingPeriodDescriptor": "uri://ed-fi.org/GradingPeriodDescriptor#Second Six Weeks",
                    "PeriodSequence": 2,
                    "Link": {
                        "rel": "GradingPeriod",
                        "href": "/ed-fi/gradingPeriods/{}".format(self.faker.uuid4().replace('-',''))
                    }
                    }
                },
                {
                    "GradingPeriodReference": {
                    "SchoolId": school['SchoolId'],
                    "SchoolYear": self.school_year,
                    "GradingPeriodDescriptor": "uri://ed-fi.org/GradingPeriodDescriptor#Third Six Weeks",
                    "PeriodSequence": 3,
                    "Link": {
                        "rel": "GradingPeriod",
                        "href": "/ed-fi/gradingPeriods/{}".format(self.faker.uuid4().replace('-',''))
                    }
                    }
                }
            ],
            "_etag": self.faker.random_number(digits=10)
        },
        {
            "Id": self.faker.uuid4().replace('-',''),
            "SchoolReference":{
                "SchoolId":school['SchoolId'],
                "Link":{
                    "rel":"School",
                    "href":"/ed-fi/schools/{}".format(school['Id'])
                }
            },
            "SchoolYearTypeReference": {
                "SchoolYear": self.school_year,
                "Link": {
                    "rel": "SchoolYearType",
                    "href": "/ed-fi/schoolYearTypes/{}".format(school['_SchoolYears']['Id'])
                }
            },
            "SessionName": "{} - {} Spring Semester".format(int(self.school_year) - 1, self.school_year),
            "BeginDate": "{}-01-{}".format(self.school_year, random.randint(1,30)),
            "EndDate": "{}-05-{}".format(self.school_year, random.randint(1,30)),
            "TermDescriptor": self.get_descriptor_string('TermDescriptor', 'Spring Semester'),
            "TotalInstructionalDays": random.randint(60,130),
            "GradingPeriods": [
                {
                    "GradingPeriodReference": {
                    "SchoolId": school['SchoolId'],
                    "SchoolYear": self.school_year,
                    "GradingPeriodDescriptor": "uri://ed-fi.org/GradingPeriodDescriptor#Fourth Six Weeks",
                    "PeriodSequence": 4,
                    "Link": {
                        "rel": "GradingPeriod",
                        "href": "/ed-fi/gradingPeriods/{}".format(self.faker.uuid4().replace('-',''))
                    }
                    }
                },
                {
                    "GradingPeriodReference": {
                    "SchoolId": school['SchoolId'],
                    "SchoolYear": self.school_year,
                    "GradingPeriodDescriptor": "uri://ed-fi.org/GradingPeriodDescriptor#Fifth Six Weeks",
                    "PeriodSequence": 5,
                    "Link": {
                        "rel": "GradingPeriod",
                        "href": "/ed-fi/gradingPeriods/{}".format(self.faker.uuid4().replace('-',''))
                    }
                    }
                },
                {
                    "GradingPeriodReference": {
                    "SchoolId": school['SchoolId'],
                    "SchoolYear": self.school_year,
                    "GradingPeriodDescriptor": "uri://ed-fi.org/GradingPeriodDescriptor#Sixth Six Weeks",
                    "PeriodSequence": 6,
                    "Link": {
                        "rel": "GradingPeriod",
                        "href": "/ed-fi/gradingPeriods/{}".format(self.faker.uuid4().replace('-',''))
                    }
                    }
                }
            ],
            "_etag": self.faker.random_number(digits=10)
        }]

    def create_sections(self, school):
        sections = []
        for _ in range(self.number_sections_per_school):
            semesterType = random.choice(['Spring', 'Fall'])
            subjectName = random.choice(SUBJECT_NAMES)[1]
            subjectNumber = random.randint(1,5)
            sections.append({
                "Id": self.faker.uuid4().replace('-',''),
                "CourseOfferingReference": {
                    "LocalCourseCode": "{}-{}".format(subjectName[0:3].upper(), subjectNumber),
                    "SchoolId": school['SchoolId'],
                    "SchoolYear": self.school_year,
                    "SessionName": "{} - {} {} Semester".format(int(self.school_year) - 1, semesterType, self.school_year),
                    "Link": {
                        "rel": "CourseOffering",
                        "href": "/ed-fi/courseOfferings/{}".format(self.faker.uuid4().replace('-',''))
                    }
                },
                "LocationReference": {
                    "ClassroomIdentificationCode": self.faker.random_number(digits = 3),
                    "SchoolId": school['SchoolId'],
                    "Link": {
                        "rel": "Location",
                        "href": "/ed-fi/locations/{}".format(self.faker.uuid4().replace('-',''))
                    }
                },
                "LocationSchoolReference": {
                    "SchoolId": school['SchoolId'],
                    "Link": {
                        "rel": "School",
                        "href": "/ed-fi/schools/{}".format(school['Id'])
                    }
                },
                "SectionIdentifier": self.faker.uuid4().replace('-',''),
                "AvailableCredits": random.randint(1,4),
                "EducationalEnvironmentDescriptor": self.get_descriptor_string('EducationalEnvironmentDescriptor','Classroom'),
                "SectionName": "{} {}".format(subjectName, subjectNumber),
                "SequenceOfCourse": random.randint(1,5),
                "Characteristics": [],
                "ClassPeriods": [
                {
                    "ClassPeriodReference": {
                    "SchoolId": school['SchoolId'],
                    "ClassPeriodName": "{} - Traditional".format(random.randint(1,5)),
                    "Link": {
                        "rel": "ClassPeriod",
                        "href": "/ed-fi/classPeriods/{}".format(self.faker.uuid4().replace('-',''))
                    }
                    }
                }
                ],
                "CourseLevelCharacteristics": [],
                "OfferedGradeLevels": [],
                "Programs": [],
                "_etag": self.faker.random_number(digits=10)
            })
        return sections

    def create_student_section_associations(self, school):
        student_section_associations = []
        session = random.choice(school['_Sessions'])
        for student in school['_Students']:
            course = random.choice(school['_Courses'])
            section = random.choice(school['_Sections'])
            student_section_associations.append({
                    "Id": self.faker.uuid4().replace('-',''),
                    "SectionReference": {
                        "LocalCourseCode": course['CourseCode'],
                        "SchoolId": school['SchoolId'],
                        "SchoolYear": self.school_year,
                        "SectionIdentifier": section['SectionIdentifier'],
                        "SessionName": session['SessionName'],
                        "Link": {
                            "rel": "Section",
                            "href": "/ed-fi/sections/{}".format(section['Id'])
                        }
                    },
                    "StudentReference": {
                        "StudentUniqueId": student['StudentUniqueId'],
                        "Link": {
                            "rel": "Student",
                            "href": "/ed-fi/students/{}".format(student['Id'])
                        }
                    },
                    "BeginDate": session['BeginDate'],
                    "EndDate": session['EndDate'],
                    "HomeroomIndicator": random.choice(BOOLEAN),
                    "_etag": self.faker.random_number(digits = 10)
                })
        return student_section_associations

    def create_staff_section_associations(self,school):
        staff_section_associations = []
        for staff in school['_Staffs']:
            session = random.choice(school['_Sessions'])
            section = random.choice(school['_Sections'])
            staff_section_associations.append({
                "Id": self.faker.uuid4().replace('-',''),
                "SectionReference": {
                    "LocalCourseCode": section['CourseOfferingReference']['LocalCourseCode'],
                    "SchoolId": school['SchoolId'],
                    "SchoolYear": self.school_year,
                    "SectionIdentifier": section['SectionIdentifier'],
                    "SessionName": session['SessionName'],
                    "Link": {
                        "rel": "Section",
                        "href": "/ed-fi/sections/{}".format(section['Id'])
                    }
                },
                "StaffReference": {
                    "StaffUniqueId": staff['StaffUniqueId'],
                    "Link": {
                        "rel": "Staff",
                        "href": "/ed-fi/staffs/{}".format(staff['Id'])
                    }
                },
                "BeginDate": session['BeginDate'],
                "ClassroomPositionDescriptor": "uri://ed-fi.org/ClassroomPositionDescriptor#Teacher of Record",
                "EndDate": session['EndDate'],
                "_etag": self.faker.uuid4().replace('-','')
            })
        return staff_section_associations


    def create_staff_school_associations(self, school):
        staff_school_associations = []
        for staff in school['_Staffs']:
            staff_school_associations.append({
                "Id": self.faker.uuid4().replace('-',''),
                "SchoolReference": {
                    "SchoolId": school['SchoolId'],
                    "Link": {
                        "rel": "School",
                        "href": "/ed-fi/schools/{}".format(school['Id'])
                    }
                },
                "StaffReference": {
                    "StaffUniqueId": staff['StaffUniqueId'],
                    "Link": {
                        "rel": "Staff",
                        "href": "/ed-fi/staffs/{}".format(staff['Id'])
                    }
                },
                "ProgramAssignmentDescriptor": self.get_descriptor_string('ProgramAssignmentDescriptor','Regular Education'),
                "AcademicSubjects": [
                    {
                        "AcademicSubjectDescriptor": self.get_descriptor_string('AcademicSubjectDescriptor',random.choice(SUBJECT_NAMES)[0])
                    }
                ],
                "GradeLevels": [
                    {'GradeLevelDescriptor': self.get_descriptor_string('GradeLevelDescriptor',random.choice(GRADE_LEVEL))} for _ in range(4)
            ],
                "_etag": self.faker.random_number(digits=10)
            })
        return staff_school_associations

    def format_edfi_data(self,data):
        result = {
            'Schools':[],
            'Students':[],
            'Calendars':[],
            'Courses':[],
            'StudentSchoolAssociations':[],
            'Staffs':[],
            'Sections': [],
            'StaffSchoolAssociations':[],
            'Sessions':[],
            'StudentSectionAssociations':[],
            'StaffSectionAssociations':[]

        }
        for school in data:
            result['Schools'].append({key: school[key] for key in school if not (key.startswith('_')) })
            result['Students'] += school['_Students']
            result['Courses'] += school['_Courses']
            result['StudentSchoolAssociations'] += school['_StudentAssociations']
            result['Calendars'].append(school['_Calendars'])
            result['Staffs'] += school['_Staffs']
            result['Sections'] += school['_Sections']
            result['StaffSchoolAssociations'] += school['_StaffSchoolAssociations']
            result['Sessions'] += school['_Sessions']
            result['StudentSectionAssociations'] += school['_StudentSectionAssociations']
            result['StaffSectionAssociations'] += school['_StaffSectionAssociations']


        return result
