IF EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.VIEWS WHERE TABLE_SCHEMA = 'analytics' AND TABLE_NAME = 'StudentDim')
BEGIN
	DROP VIEW analytics.StudentDim
END
GO

CREATE VIEW analytics.StudentDim AS

		WITH AddressPriority ([Order], AddressCodeDescription) AS (
		SELECT 1, 'Home'
		UNION ALL SELECT 2, 'Mailing'
		UNION ALL SELECT 3, 'Work'
		UNION ALL SELECT 4, 'Billing'
		UNION ALL SELECT 5, 'Physical'
		UNION ALL SELECT 6, 'Guardian Address'
		UNION ALL SELECT 7, 'Mother Address'
		UNION ALL SELECT 8, 'Father Address'
		UNION ALL SELECT 9, 'Temporary'
		UNION ALL SELECT 10, 'Other'
		UNION ALL SELECT 11, 'Shipping'
		UNION ALL SELECT 12, 'Shelters, Transitional housing, Awaiting Foster Care'
		UNION ALL SELECT 13, 'Doubled - up (i.e., living with another family)'
		UNION ALL SELECT 14, 'Unsheltered (e.g. cars, parks, campgrounds, temporary trailers including FEMA trailers, or abandoned buildings)'
		UNION ALL SELECT 15, 'Hotels/Motels'
	),
	studentAddress (studentUniqueId, StreetNumberName, ApartmentRoomSuiteNumber, BuildingSiteNumber, City, StateAbbreviationDescriptor, PostalCode, [Priority]) AS (
		SELECT
			t.studentUniqueId
			, t.StreetNumberName
			, t.ApartmentRoomSuiteNumber
			, t.BuildingSiteNumber
			, t.City
			, t.StateAbbreviationDescriptor
			, t.PostalCode
			, ROW_NUMBER() OVER (PARTITION BY t.studentUniqueId ORDER BY t.IsStudentAddress DESC) as [Priority]
		FROM
		(
			SELECT
				1 AS IsStudentAddress
				, sa.studentUniqueId
				, sa.StreetNumberName
				, 0 as ApartmentRoomSuiteNumber
				, 0 as BuildingSiteNumber
				, sa.City
				, sa.StateAbbreviationDescriptor
				, sa.PostalCode
				, ROW_NUMBER() OVER (PARTITION BY sa.studentUniqueId ORDER BY ap.[Order]) as RowNumber
			FROM edfi.StudentEducationOrganizationAssociationAddress sa
				INNER JOIN edfi.AddressTypeDescriptors atd ON sa.AddressTypeDescriptor = atd.namespace +'#'+ atd.codeValue
				INNER JOIN AddressPriority ap ON ap.AddressCodeDescription = atd.codeValue

			UNION ALL

			SELECT
				0 AS IsStudentAddress
				, spa.studentUniqueId
				, pa.StreetNumberName
				, 0 as ApartmentRoomSuiteNumber
				, 0 as BuildingSiteNumber
				, pa.City
				, pa.StateAbbreviationDescriptor
				, pa.PostalCode
				, ROW_NUMBER() OVER (PARTITION BY spa.studentUniqueId ORDER BY spa.LivesWith DESC, spa.PrimaryContactStatus DESC, spa.parentUniqueId, AddressPriority.[Order]) as RowNumber
			FROM edfi.StudentParentAssociations spa
				INNER JOIN edfi.ParentAddress pa ON pa.parentUniqueId = spa.parentUniqueId
				INNER JOIN edfi.AddressTypeDescriptors atd ON pa.AddressTypeDescriptor = atd.namespace +'#'+ atd.codeValue
				INNER JOIN AddressPriority ON AddressCodeDescription = atd.[description]
		) t
		WHERE RowNumber = 1
	)

	select   Student.StudentUniqueId AS StudentKey
			, Student.LastSurname
			, Student.FirstName
			, '' as MiddleName
			, sd.CodeValue as Gender
			, StudentRace.Races
			, StudentCharacteristics.Characteristics
			, StudentIndicators.Indicators
			, 0 as HispanicLatinoEthnicity
			, StudentSchoolDim.SchoolKey
			, StudentSchoolDim.GradeLevel
			, CASE  StudentSchoolDim.GradeLevel
					WHEN 'Early Education' THEN -3
					WHEN 'Infant/toddler' THEN -2
					WHEN 'Preschool/Prekindergarten' THEN -1
					WHEN 'Kindergarten' THEN 0
					WHEN 'First grade' THEN 1
					WHEN 'Second grade' THEN 2
					WHEN 'Third grade' THEN 3
					WHEN 'Fourth grade' THEN 4
					WHEN 'Fifth grade' THEN 5
					WHEN 'Sixth grade' THEN 6
					WHEN 'Seventh grade' THEN 7
					WHEN 'Eighth grade' THEN 8
					WHEN 'Ninth grade' THEN 9
					WHEN 'Tenth grade' THEN 10
					WHEN 'Eleventh grade' THEN 11
					WHEN 'Twelfth grade' THEN 12
					WHEN 'Postsecondary' THEN 13
					WHEN 'Ungraded' THEN 14
					WHEN 'Other' THEN 15
					WHEN 'Grade 13' THEN 16
					WHEN 'Adult Education' THEN 17
					ELSE 18
				END AS [SortOrder]
			   ,CASE StudentSchoolDim.GradeLevel
					WHEN 'Early Education' THEN 'E-E'
					WHEN 'Infant/toddler' THEN 'Inf'
					WHEN 'Preschool/Prekindergarten' THEN 'Pre'
					WHEN 'Kindergarten' THEN 'K'
					WHEN 'First grade' THEN '1st'
					WHEN 'Second grade' THEN '2nd'
					WHEN 'Third grade' THEN '3rd'
					WHEN 'Fourth grade' THEN '4th'
					WHEN 'Fifth grade' THEN '5th'
					WHEN 'Sixth grade' THEN '6th'
					WHEN 'Seventh grade' THEN '7th'
					WHEN 'Eighth grade' THEN '8th'
					WHEN 'Ninth grade' THEN '9th'
					WHEN 'Tenth grade' THEN '10th'
					WHEN 'Eleventh grade' THEN '11th'
					WHEN 'Twelfth grade' THEN '12th'
					WHEN 'Postsecondary' THEN 'Post'
					WHEN 'Ungraded' THEN 'U'
					WHEN 'Other' THEN 'O'
					WHEN 'Grade 13' THEN '13'
					WHEN 'Adult Education' THEN 'A-E'
					ELSE 'Undef'
				END AS [GradeLevelDisplayText]
			, EducationOrganization.NameOfInstitution AS SchoolName
			, scd.CodeValue AS SchoolCategory
			, oed.CodeValue as OldEthnicity
			, sa.StreetNumberName as AddressStreetNumberName
			, sa.ApartmentRoomSuiteNumber as AddressApartmentRoomSuiteNumber
			, sa.BuildingSiteNumber as AddressBuildingSiteNumber
			, sa.City as AddressCity
			, sa.StateAbbreviationDescriptor as AddressState
			, sa.PostalCode as AddressPostalCode
			, Student.BirthDate
			, lepd.CodeValue AS LimitedEnglishProficiency
			, CAST((CASE WHEN EXISTS
					(SELECT 1
					FROM edfi.StudentEducationOrganizationAssociationStudentCharacteristics sc
					INNER JOIN edfi.StudentCharacteristicDescriptors scd
						ON scd.namespace +'#'+ scd.codeValue = sc.StudentCharacteristicDescriptor
					WHERE sc.studentUniqueId = student.studentUniqueId)
					THEN 1
					ELSE 0
					END)
				AS BIT) AS EconomicDisadvantaged
			, CAST((CASE WHEN EXISTS
				(SELECT 1
				FROM edfi.StudentSchoolFoodServiceProgramAssociationSchoolFoodServiceProgramServices sc
				WHERE sc.studentUniqueId = Student.studentUniqueId
					AND sc.SchoolFoodServiceProgramServiceDescriptor IN (
						SELECT sfspsd.namespace +'#'+ sfspsd.codeValue from edfi.SchoolFoodServiceProgramServiceDescriptors sfspsd
						WHERE sfspsd.CodeValue LIKE 'Free%'
						OR sfspsd.CodeValue LIKE 'Reduced Price%'
					))
				THEN 1
				ELSE 0
				END)
			AS BIT) AS HasFreeOrReducedPriceFoodServiceEligibility
			,  StudentSchoolDim.LocalEducationAgencyKey
			, StudentSchoolDim.IsEnrolledToSchool
			, StudentSchoolDim.StudentSchoolAssociationOrderKey
			, StudentSchoolDim.StudentLeaSchoolAssociationOrderKey
	FROM edfi.Students Student
	INNER JOIN analytics.StudentSchoolDim StudentSchoolDim
		ON Student.studentUniqueId=StudentSchoolDim.studentUniqueId
	INNER JOIN edfi.StudentEducationOrganizationAssociations studentEdOrg
		ON Student.studentUniqueId = studentEdOrg.studentUniqueId
	INNER JOIN edfi.Schools EducationOrganization
		ON EducationOrganization.SchoolId = StudentSchoolDim.SchoolKey
	INNER JOIN edfi.SexDescriptors sd
		ON studentEdOrg.SexDescriptor = sd.namespace +'#'+ sd.codeValue
	INNER JOIN edfi.SchoolCategory SchoolCategory
		ON SchoolCategory.SchoolId=StudentSchoolDim.SchoolKey
	INNER JOIN edfi.SchoolCategoryDescriptors scd
		ON scd.namespace +'#'+scd.codeValue=SchoolCategory.SchoolCategoryDescriptor
	LEFT JOIN studentAddress sa ON sa.studentUniqueId = student.studentUniqueId AND sa.[Priority] = 1
	LEFT JOIN (
				SELECT student.studentUniqueId,
						SUBSTRING(
							(SELECT ',' + rd.description
							FROM edfi.StudentEducationOrganizationAssociationRaces sr
							INNER JOIN edfi.RaceDescriptors rd
								ON rd.namespace + '#'+ rd.codeValue = sr.RaceDescriptor
							WHERE sr.studentUniqueId = Student.studentUniqueId
							), 2, 2000000) AS Races
					FROM edfi.Students student
			 ) AS StudentRace
		ON student.studentUniqueId = StudentRace.studentUniqueId
	LEFT JOIN (
				 SELECT	Student.studentUniqueId,
						SUBSTRING(
							(SELECT ',' + scd.codeValue
							FROM edfi.StudentEducationOrganizationAssociationStudentCharacteristics sc
							INNER JOIN edfi.studentCharacteristicDescriptors scd
								ON scd.namespace +'#'+ scd.codeValue = sc.StudentCharacteristicDescriptor
							WHERE sc.studentUniqueId = Student.studentUniqueId
							), 2, 2000000) AS Characteristics
				FROM edfi.Students student
    ) AS StudentCharacteristics ON student.studentUniqueId = StudentCharacteristics.studentUniqueId
	LEFT JOIN (
				 SELECT	Student.studentUniqueId,
						SUBSTRING(
							(SELECT ',' + si.[IndicatorName]
							FROM edfi.[StudentEducationOrganizationAssociationStudentIndicators] si
							WHERE si.studentUniqueId = Student.studentUniqueId
							AND si.Indicator = 'True'
							), 2, 2000000) AS Indicators
				FROM edfi.Students student
    ) AS StudentIndicators ON student.studentUniqueId = StudentIndicators.studentUniqueId
	LEFT JOIN edfi.OldEthnicityDescriptors oed
		ON oed.namespace +'#'+ oed.codeValue = studentEdOrg.OldEthnicityDescriptor
	LEFT JOIN edfi.LimitedEnglishProficiencyDescriptors lepd
        ON studentEdOrg.LimitedEnglishProficiencyDescriptor = lepd.namespace +'#'+ lepd.codeValue
GO