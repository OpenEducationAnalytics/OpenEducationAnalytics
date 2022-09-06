CREATE OR ALTER VIEW [analytics].[StudentSectionDim]
AS
     SELECT
            CAST(Students.StudentUniqueId AS NVARCHAR) + '-' + CAST(StudentSectionAssociations.SchoolId AS NVARCHAR) + '-' + StudentSectionAssociations.LocalCourseCode + '-' + CAST(StudentSectionAssociations.SchoolYear AS NVARCHAR) + '-' + StudentSectionAssociations.SectionIdentifier + '-' + StudentSectionAssociations.SessionName + '-' + CONVERT(NVARCHAR, StudentSectionAssociations.BeginDate, 112) AS StudentSectionKey,
            Students.StudentUniqueId AS StudentKey,
            CAST(StudentSectionAssociations.SchoolId AS NVARCHAR) + '-' + StudentSectionAssociations.LocalCourseCode + '-' + CAST(StudentSectionAssociations.SchoolYear AS NVARCHAR) + '-' + StudentSectionAssociations.SectionIdentifier + '-' + StudentSectionAssociations.SessionName AS SectionKey,
            StudentSectionAssociations.LocalCourseCode,
            ISNULL(asd.Description, '') AS Subject,
            ISNULL(Courses.CourseTitle, '') AS CourseTitle,

            -- There could be multiple teachers for a Sections - reduce those to a single string.
            -- Unfortunately this means that the Staffs and StaffSectionAssociations
            -- LastModifiedDate values can't be used to calculate this record's LastModifiedDate
            ISNULL(STUFF(
     (
         SELECT
                N', ' + ISNULL(Staffs.FirstName, '') + ' ' + ISNULL(Staffs.LastSurname, '')
         FROM edfi.StaffSectionAssociations
              LEFT OUTER JOIN edfi.Staffs
              ON StaffSectionAssociations.staffUniqueId = Staffs.staffUniqueId
         WHERE StudentSectionAssociations.SchoolId = StaffSectionAssociations.SchoolId
               AND StudentSectionAssociations.LocalCourseCode = StaffSectionAssociations.LocalCourseCode
               AND StudentSectionAssociations.SchoolYear = StaffSectionAssociations.SchoolYear
               AND StudentSectionAssociations.SectionIdentifier = StaffSectionAssociations.SectionIdentifier
               AND StudentSectionAssociations.SessionName = StaffSectionAssociations.SessionName FOR
         XML PATH('')
     ), 1, 1, N''), '') AS TeacherName,
            CONVERT(NVARCHAR, StudentSectionAssociations.BeginDate, 112) AS StudentSectionStartDateKey,
            CONVERT(NVARCHAR, StudentSectionAssociations.EndDate, 112) AS StudentSectionEndDateKey,
            CAST(StudentSectionAssociations.SchoolId AS VARCHAR) AS SchoolKey,
            CAST(StudentSectionAssociations.SchoolYear AS NVARCHAR) AS SchoolYear,
     (
         SELECT
                MAX(MaxLastModifiedDate)
         FROM(VALUES(StudentSectionAssociations.LastModifiedDate), (Courses.LastModifiedDate), (CourseOfferings.LastModifiedDate) ) AS VALUE(MaxLastModifiedDate)
     ) AS LastModifiedDate,

	 --added
	 ISNULL(StudentSectionAssociations.[BeginDate], [Sessions].[BeginDate]) as BeginDate,
	 ISNULL(StudentSectionAssociations.[EndDate], [Sessions].[EndDate]) as EndDate,
     StudentSectionAssociations.[HomeroomIndicator],
     Sections.SectionIdentifier,
	 Sections.SessionName,
     CAST(Sections.Id AS VARCHAR(50)) as SectionId
    FROM edfi.StudentSectionAssociations
    INNER JOIN edfi.Students
        ON StudentSectionAssociations.studentUniqueId = Students.studentUniqueId
	 INNER JOIN edfi.Sections
        ON Sections.SchoolId = StudentSectionAssociations.SchoolId
        AND Sections.LocalCourseCode = StudentSectionAssociations.LocalCourseCode
        AND Sections.SchoolYear = StudentSectionAssociations.SchoolYear
        AND Sections.SessionName = StudentSectionAssociations.SessionName
        AND Sections.SectionIdentifier = StudentSectionAssociations.SectionIdentifier
    INNER JOIN edfi.CourseOfferings
        ON JSON_VALUE(CourseOfferings.SchoolReference, '$.schoolId') = StudentSectionAssociations.SchoolId
        AND JSON_VALUE(CourseOfferings.CourseReference, '$.courseCode') = StudentSectionAssociations.LocalCourseCode
        AND JSON_VALUE(CourseOfferings.SessionReference, '$.schoolYear') = StudentSectionAssociations.SchoolYear
        AND JSON_VALUE(CourseOfferings.SessionReference, '$.sessionName') = StudentSectionAssociations.SessionName
    INNER JOIN edfi.Courses
        ON Courses.CourseCode = JSON_VALUE(CourseOfferings.CourseReference, '$.courseCode')
        AND Courses.EducationOrganizationId = JSON_VALUE(CourseOfferings.SchoolReference, '$.schoolId')
    --Added
    INNER JOIN edfi.[Sessions]
        ON JSON_VALUE(Sessions.SchoolReference, '$.schoolId') = StudentSectionAssociations.SchoolId
        AND JSON_VALUE(Sessions.SchoolYearTypeReference, '$.schoolYear') = StudentSectionAssociations.SchoolYear
        AND [Sessions].SessionName = StudentSectionAssociations.SessionName
    --ends here
    LEFT OUTER JOIN edfi.AcademicSubjectDescriptors asd
        ON courses.AcademicSubjectDescriptor = asd.namespace + '#' + asd.codevalue
GO