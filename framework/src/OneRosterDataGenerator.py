import math
from faker import Faker


_SUBJECTS = ['Math - Algebra', 'Math - Geometry', 'English Language', 'History - World History', 
             'Science Biology', 'Health', 'Technology - Programming', 'Physical Education', 'Art', 'Music']
_SCHOOL_TYPES = ['Elementary', 'Middle', 'High']

class OneRosterDataGenerator:
  def __init__(self, students_per_school=100, classes_in_student_schedule=6, students_per_section=25, student_teacher_ratio=9, include_optional_fields=True):
    # Set a seed value in Faker so it generates the same values every time it's run
    self.faker = Faker('en_US')
    Faker.seed(1) 

    self.students_per_school = students_per_school
    self.classes_in_student_schedule = classes_in_student_schedule
    self.students_per_section = students_per_section
    self.student_teacher_ratio = student_teacher_ratio
    self.include_optional = include_optional_fields

    self.teachers_per_school = math.ceil(self.students_per_school/self.student_teacher_ratio)
    self.section_id = 1
    self.student_id = 1
    self.teacher_id = 1
    self.course_id = 1
    self.school_id = 1
    self.term_id = 1
    self.domain = '@Classrmtest86.org'

  def create_schools(self, quantity):
    schools = []
    for n in range(quantity):
      school = self.create_school(str(self.school_id))
      schools.append(school)
      self.school_id += 1
    return schools

  def create_school(self, school_id):
    school_info = {
      'sourcedId':f'sch{school_id}',
      'name':f"{self.faker.last_name()} {self.faker.random_element(_SCHOOL_TYPES)}",
      'identifier': school_id if self.include_optional else '',
      'status':'active' if self.include_optional else '',
      'dateLastModified': '2020-04-15T08:30:11.944Z' if self.include_optional else ''
      }

    school_data = {}
    school_data['students'] = self.create_students(school_info['sourcedId'])
    school_data['teachers'] = self.create_teachers(school_info['sourcedId'])
    school_data['courses'] = self.create_courses()
    school_data['terms'] = self.create_terms('2021')
    school_data['student_enrollments'] = self.create_student_enrollments(school_info['sourcedId'], school_data)
    school_data['teacher_enrollments'] = self.create_teacher_enrollments(school_info['sourcedId'], school_data)
    for term in school_data['terms']:
      self.create_sections(term, school_info['sourcedId'], school_data['courses'])

    # Now that all the data is generated across the various entities, we need to extract only what we need for OneRoster's spec
    one_roster_data = {}
    one_roster_data['users'] = school_data['students']
    one_roster_data['users'] += school_data['teachers']
    one_roster_data['courses'] = school_data['courses']

    one_roster_data['classes'] = []
    for term in school_data['terms']:
      term.pop('_section_spots')
      one_roster_data['classes'] += term.pop('_sections')
    one_roster_data['academicSessions'] = school_data['terms']

    return school_info, one_roster_data

  def create_terms(self, school_year):
    terms = []
    terms.append({
      'sourcedId' : 'term' + str(self.term_id),
      'title' : 'Fall Semester',
      'startDate' : '9/1/2020',
      'endDate' : '12/22/2020',
      'type' : 'semester',
      'schoolYear': school_year,
      '_sections' : [],
      '_section_spots' : []  # this is an array of arrays representing the sections and the spots within each section
      })
    self.term_id += 1
    terms.append({
      'sourcedId' : 'term' + str(self.term_id),
      'title' : 'Spring Semester',
      'startDate' : '1/21/2021',
      'endDate' : '5/30/2021',
      'type' : 'semester',
      'schoolYear': school_year,
      '_sections' : [],
      '_section_spots' : []  # this is an array of arrays representing the sections and the spots within each section
      })
    return terms

  def create_courses(self):
    courses = []
    for subject in _SUBJECTS:
      courses.append({
        'sourcedId' : 'course' + str(self.course_id),
        'status': '',
        'dateLastModified':'',
        'Course Name' : subject,
        'courseCode' : str(self.course_id),
        'Course Description' : "Instruction covering " + subject,
        'Course Subject' : subject
        })
      self.course_id += 1
    return courses

  def create_students(self, school_id):
    students = []
    for n in range(self.students_per_school):
      students.append(self.create_user(school_id, self.student_id, 'student'))
      self.student_id += 1
    return students

  def create_teachers(self, school_id):
    teachers = []
    for n in range(self.teachers_per_school):
      teachers.append(self.create_user(school_id, self.teacher_id, 'teacher'))
      self.teacher_id += 1
    return teachers

  def create_user(self, school_id, user_id, user_type):
    id_prefix = 'st' if user_type == 'student' else 't'
    fname = self.faker.first_name()
    lname = self.faker.last_name()
    email = f"{fname.lower()}{lname.lower()}{user_id}{self.domain}"
    user = {
        'userIds': [{"type":"LDAP", "identifier":self.faker.uuid4()}] if self.include_optional else '',
        'enabledUser': True,
        'middleName': self.faker.first_name() if self.include_optional else '',
        'grades': [self.faker.random_element(['9','10','11','12'])] if self.include_optional else '',
        'password': self.faker.password() if self.include_optional else '',
        'username' : f"{fname.lower()}{lname.lower()}{user_id}",
        'givenName' : fname,
        'familyName' : lname,
        'role' : user_type,
        'identifier': str(user_id) if self.include_optional else '',
        'email': email if self.include_optional else '',
        'sms' : self.faker.phone_number(),
        'phone' : self.faker.phone_number(),
        'agents': None,
        'orgs': [ {'href':'http://orgrefhere', 'sourcedId':school_id, 'type':'school'}],
        'sourcedId' : id_prefix + str(user_id),
        'status':'active' if self.include_optional else '',
        'dateLastModified': '2020-04-15T08:30:11.944Z' if self.include_optional else ''
        }
    return user

  def create_sections(self, term, school_id, courses):
    spots_needed = self.students_per_school * self.classes_in_student_schedule
    sections_needed = math.ceil(spots_needed / self.students_per_section) + 1 # determine the number of sections needed
    for n in range(sections_needed):
      course = self.faker.random_element(courses)
      term['_sections'].append({
        'grades': [self.faker.random_element(['9','10','11','12'])] if self.include_optional else '',
        'subjectCodes': ['001'], #todo: populate this
        'periods': ['per1'], #todo: populate this
        'resources': [{'href':'http://resourcerefhere', 'sourcedId': '121212', 'type': 'resource'}], #todo: populate this
        'title' : course['Course Subject'] + " " + str(self.section_id),
        'classCode' : str(self.section_id) if self.include_optional else '',
        'classType': 'scheduled',
        'location' : self.faker.random_element(['room1', 'room2', 'room3', 'room4', 'room5']) if self.include_optional else '',
        'subjects' : [course['Course Subject']] if self.include_optional else '',
        'course' : {'href':'http://courserefhere', 'sourcedId':course['Course SIS ID'], 'type':'course'},
        'school' : {'href':'http://schoolrefhere', 'sourcedId':school_id, 'type':'school'},
        'terms' : [{'href':'http://termrefhere', 'sourcedId':term['sourcedId'], 'type':'academicSession'}],
        'sourcedId' : str(self.section_id),
        'status' : 'active' if self.include_optional else '',
        'dateLastModified': '2020-04-15T08:30:11.944Z' if self.include_optional else ''
        })
      # add section spots   
      spots = []
      for i in range(self.students_per_section):
        spots.append(str(self.section_id))
      term['_section_spots'].append(spots)
      self.section_id += 1

  def create_student_enrollments(self, school_id, school_data):
    enrollments = []
    for student in school_data['students']:
      for term in school_data['terms']:
        num_enrollments = 0
        for section_spots in term['_section_spots']:
          if(len(section_spots) == 0): 
            continue
          else:
            spot_taken = section_spots.pop()
            num_enrollments += 1
            enrollment = self.create_enrollment('student', school_id, student['sourcedId'], spot_taken)
            enrollments.append(enrollment)
          if (num_enrollments >= self.classes_in_student_schedule): break
    return enrollments

  def create_teacher_enrollments(self, school_id, school_data):
    enrollments = []
    for term in school_data['terms']:
      teacher_index = 0
      for section in term['_sections']:
        teacher_id = school_data['teachers'][teacher_index]['sourcedId']
        enrollment = self.create_enrollment('teacher', school_id, teacher_id, section['sourcedId'])
        enrollments.append(enrollment)
        teacher_index += 1
        if (teacher_index == len(school_data['teachers'])): teacher_index = 0 # start over from the beginning of the list of teachers
    return enrollments

  def create_enrollment(self, role, school_id, user_id, section_id):
    enrollment = {
        "beginDate": "2020-04-16T18:22:04.645Z",
        "endDate": "2020-07-16T18:22:04.645Z",
        "role": role,
        "primary": True,
        "user": {
          "href": "http://userhrefhere",
          "sourcedId": user_id,
          "type": "user"
        },
        "school": {
          "href": "http://schoolhrefhere",
          "sourcedId": school_id,
          "type": "org"
        },
        "class": {
          "href": "http://classhrefhere",
          "sourcedId": section_id,
          "type": "class"
        },
        "sourcedId": self.faker.uuid4(),
        "status": "active",
        "dateLastModified": "2020-04-16T18:22:04.647Z"
    }
    return enrollment

##########################
#generate_data()
