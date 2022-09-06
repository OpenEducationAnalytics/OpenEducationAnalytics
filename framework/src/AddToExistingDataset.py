import os
import csv
import random

_path = os.path.dirname(__file__)
reader = csv.reader(open(f"{_path}/../../modules/M365/test_data/DIPData/Roster/Person.csv"))
students = []
buffer = 'SIS ID,FederalRaceCategory,PrimaryLanguage,ELLStatus,SpecialEducation,LowIncome\n'
for row in reader:
    sis_id = row[7]
    if sis_id.startswith('st'):
        buffer += sis_id + ','
        buffer += random.choices(['Asian', 'Black', 'White', 'Hispanic', 'American Indian'], weights=(15, 25, 30, 25, 5))[0] + ','
        buffer += random.choices(['English', 'Spanish', 'German', 'French', 'Japanese'], weights=(85, 10, 2, 2, 1))[0] + ','
        buffer += random.choices(['', 'English Learner', 'Initially Fluent English Proficient', 'Redesignated Fluent English Proficient'], weights=(80, 10, 5, 5))[0] + ','
        buffer += random.choices(['', 'Designated Instruction Service', 'Resource Specialty Program', 'Special Day Class'], weights=(80, 10, 5, 5))[0] + ','
        buffer += random.choices(['0', '1'], weights=(60, 40))[0] + '\n'

        student = {
            'SIS ID': sis_id,
            'FederalRaceCategory': random.choices(['Asian', 'Black', 'White', 'Hispanic', 'American Indian'], weights=(15, 25, 30, 25, 5))[0],
            'PrimaryLanguage': random.choices(['English', 'Spanish', 'German', 'French', 'Japanese'], weights=(85, 10, 2, 2, 1))[0],
            'ELLStatus': random.choices(['', 'English Learner', 'Initially Fluent English Proficient', 'Redesignated Fluent English Proficient'], weights=(80, 10, 5, 5))[0],
            'SpecialEducation': random.choices(['', 'Designated Instruction Service', 'Resource Specialty Program', 'Special Day Class'], weights=(80, 10, 5, 5))[0],
            'LowIncome': random.choices([0, 1], weights=(60, 40))[0]
        }    
        students.append(student)


print(buffer)
with open('mycsvfile.csv','w') as f:
    f.write(buffer)
    #w = csv.writer(f)
    #w.writerow(students[0].keys())
    #for student in students: w.writerow(student.values())


"""
for row in csv.DictReader(open(f"{_path}/../../modules/M365/test_data/DIPData/Roster/Person.csv")):
    print(row)

    student_id = row['SIS ID']
    section_id = row['Section SIS ID']
    attendance_code = get_random_attendance()
    attendance_flag = int(attendance_code == 'P')
    attendance_status = 'Present'
    if attendance_code != 'P': attendance_status = 'Absent'
    attendance_csv.write(f"att_{str(index)},{student_id},2021,,{date_str},No,1,{section_id},{attendance_code},{attendance_flag},{attendance_status},ClassSectionAttendance,0\n")
    index += 1
"""