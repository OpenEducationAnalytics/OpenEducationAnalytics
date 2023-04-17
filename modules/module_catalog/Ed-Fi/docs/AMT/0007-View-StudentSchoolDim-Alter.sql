CREATE OR ALTER VIEW [analytics].[StudentSchoolDim]
AS
    SELECT
        CONCAT(Students.StudentUniqueId, '-', StudentSchoolAssociations.SchoolId) AS StudentSchoolKey,
        Students.StudentUniqueId AS StudentKey,
        CAST(StudentSchoolAssociations.SchoolId AS VARCHAR) AS SchoolKey,
        COALESCE(CAST(StudentSchoolAssociations.graduationSchoolYear AS VARCHAR), 'Unknown') AS SchoolYear,
        Students.FirstName AS StudentFirstName,
        '' AS StudentMiddleName,
        COALESCE(Students.LastSurname, '') AS StudentLastName,
        CAST(StudentSchoolAssociations.EntryDate AS NVARCHAR) AS EnrollmentDateKey,
        EntryGradeLevelDescriptors.CodeValue AS GradeLevel,
        COALESCE(CASE
                    WHEN schoolEdOrg.studentUniqueId IS NOT NULL
                    THEN LimitedEnglishDescriptorSchool.CodeValue
                    ELSE LimitedEnglishDescriptorDist.CodeValue
                END, 'Not applicable') AS LimitedEnglishProficiency,
        0 AS IsHispanic,
        COALESCE(CASE
                    WHEN schoolEdOrg.studentUniqueId IS NOT NULL
                    THEN SexTypeSchool.CodeValue
                    ELSE SexTypeDist.CodeValue
                END, '') AS Sex,
        (
            SELECT
                MAX(MaxLastModifiedDate)
            FROM (VALUES
                (Students.LastModifiedDate)
                ,(schoolEdOrg.LastModifiedDate)
                ,(districtEdOrg.LastModifiedDate)
            ) AS VALUE(MaxLastModifiedDate)
        ) AS LastModifiedDate,
		--added
		 StudentSchoolAssociations.[EntryDate],
		 StudentSchoolAssociations.[ExitWithdrawDate] as ExitWithdrawDate,
		 Students.studentUniqueId AS studentUniqueId,
		 GraduationPlanTypeDescriptors.CodeValue AS GraduationPlan,
		 '' AS WithdrawalDescription,
         Schools.LocalEducationAgencyId AS LocalEducationAgencyKey
		 , ROW_NUMBER() OVER (PARTITION BY StudentSchoolAssociations.[studentUniqueId]
            ORDER BY
            StudentSchoolAssociations.[studentUniqueId],
            CASE WHEN StudentSchoolAssociations.ExitWithdrawDate IS NULL THEN 1 ELSE 2 END,
            StudentSchoolAssociations.ExitWithdrawDate DESC,
            StudentSchoolAssociations.[EntryDate] ASC,
            schools.[LocalEducationAgencyId],
            StudentSchoolAssociations.[SchoolId]) AS StudentSchoolAssociationOrderKey
		, ROW_NUMBER() OVER (PARTITION BY StudentSchoolAssociations.[studentUniqueId], Schools.[LocalEducationAgencyId]
			ORDER BY
			StudentSchoolAssociations.[studentUniqueId],
			CASE WHEN StudentSchoolAssociations.ExitWithdrawDate IS NULL THEN 1 ELSE 2 END,
			StudentSchoolAssociations.ExitWithdrawDate DESC,
			StudentSchoolAssociations.[EntryDate] ASC,
			Schools.[LocalEducationAgencyId],
			StudentSchoolAssociations.[SchoolId]) AS StudentLeaSchoolAssociationOrderKey
		,CAST
			(
				(
				CASE
					WHEN
						StudentSchoolAssociations.EntryDate <= mmd.MaxDate
						AND (StudentSchoolAssociations.ExitWithdrawDate IS NULL OR StudentSchoolAssociations.ExitWithdrawDate >= mmd.MaxDate)
					THEN 1
					ELSE 0
				END
				)
			AS BIT
			) AS IsEnrolledToSchool
    FROM
        edfi.Students
    INNER JOIN
        edfi.StudentSchoolAssociations ON
            Students.StudentUniqueId = StudentSchoolAssociations.StudentUniqueId

    INNER JOIN
        edfi.Schools ON
            StudentSchoolAssociations.SchoolId = Schools.SchoolId
    LEFT OUTER JOIN
        edfi.StudentEducationOrganizationAssociations AS schoolEdOrg ON
            Students.StudentUniqueId = schoolEdOrg.StudentUniqueId
            AND StudentSchoolAssociations.SchoolId = schoolEdOrg.educationOrganizationId
    LEFT OUTER JOIN
        edfi.limitedEnglishProficiencyDescriptors AS LimitedEnglishDescriptorSchool ON
            schoolEdOrg.LimitedEnglishProficiencyDescriptor = LimitedEnglishDescriptorSchool.namespace + '#' +  LimitedEnglishDescriptorSchool.codevalue
    LEFT OUTER JOIN
        edfi.sexDescriptors as SexTypeSchool ON
            schoolEdOrg.SexDescriptor = SexTypeSchool.namespace + '#' +  SexTypeSchool.codevalue
	LEFT OUTER JOIN
        edfi.gradeLevelDescriptors EntryGradeLevelDescriptors  ON
            StudentSchoolAssociations.EntryGradeLevelDescriptor = EntryGradeLevelDescriptors.namespace + '#' +  EntryGradeLevelDescriptors.codevalue
    LEFT OUTER JOIN
        edfi.StudentEducationOrganizationAssociations AS districtEdOrg ON
            Students.StudentUniqueId = districtEdOrg.StudentUniqueId
            AND Schools.LocalEducationAgencyId = districtEdOrg.educationOrganizationId
    LEFT OUTER JOIN
        edfi.limitedEnglishProficiencyDescriptors AS LimitedEnglishDescriptorDist ON
            districtEdOrg.LimitedEnglishProficiencyDescriptor = LimitedEnglishDescriptorDist.namespace + '#' +  LimitedEnglishDescriptorDist.codevalue
    LEFT OUTER JOIN
        edfi.SexDescriptors SexTypeDist ON
            districtEdOrg.SexDescriptor = SexTypeDist.namespace + '#' +  SexTypeDist.codevalue
	LEFT OUTER JOIN
        edfi.GraduationPlanTypeDescriptors ON
            StudentSchoolAssociations.GraduationPlanTypeDescriptor = GraduationPlanTypeDescriptors.namespace + '#' +  GraduationPlanTypeDescriptors.codevalue
	LEFT JOIN analytics.SchoolMinMaxDateDim mmd
	 ON mmd.SchoolKey = StudentSchoolAssociations.schoolId
    WHERE(
        StudentSchoolAssociations.ExitWithdrawDate IS NULL
        OR StudentSchoolAssociations.ExitWithdrawDate >= GETDATE());
GO