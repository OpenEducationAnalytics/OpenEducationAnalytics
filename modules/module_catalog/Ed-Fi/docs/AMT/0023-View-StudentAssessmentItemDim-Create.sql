IF EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.VIEWS WHERE TABLE_SCHEMA = 'analytics' AND TABLE_NAME = 'StudentAssessmentItemDim')
BEGIN
	DROP VIEW analytics.StudentAssessmentItemDim
END
GO

CREATE VIEW [analytics].StudentAssessmentItemDim AS
	SELECT	stu.StudentUniqueId as StudentKey
			, CAST(s.SchoolId AS VARCHAR) as SchoolKey
			, a.AssessmentIdentifier
			, a.Namespace
			, sa.StudentAssessmentIdentifier
			, sa.AdministrationDate
			, RTRIM(LTRIM(a.AssessmentTitle)) AS AssessmentTitle
			, aasd.CodeValue AS AcademicSubject
			, gld.CodeValue AS AssessedGradeLevel
			, a.AssessmentVersion AS [Version]
			, aird.CodeValue AS AssessmentItemResult
			, '' as RawScoreResult -- Add to Sai
			, sai.AssessmentResponse
	FROM edfi.Assessments a
    INNER JOIN edfi.AssessmentAcademicSubjects aas
        ON aas.AssessmentIdentifier = a.AssessmentIdentifier
        AND aas.[Namespace] = a.[Namespace]
    INNER JOIN edfi.AssessmentAssessedGradeLevels aagl
        ON aagl.AssessmentIdentifier = a.AssessmentIdentifier
        AND aagl.[Namespace] = a.[Namespace]
    INNER JOIN edfi.StudentAssessments sa
        ON sa.AssessmentIdentifier = a.AssessmentIdentifier
        AND sa.[Namespace] = a.[Namespace]
        -- AND sa.ReasonNotTestedDescriptor IS NULL  -- Reason Not Tested holds precedence over assessment items
    INNER JOIN edfi.StudentAssessmentItems sai
        ON sai.studentUniqueId = sa.studentUniqueId
        AND sai.AssessmentIdentifier = sa.AssessmentIdentifier
        AND sai.[Namespace] = sa.[Namespace]
        AND sai.StudentAssessmentIdentifier = sa.[StudentAssessmentIdentifier]
	INNER JOIN	edfi.AcademicSubjectDescriptors aasd
            ON aas.AcademicSubjectDescriptor = aasd.namespace + '#' + aasd.codeValue
	INNER JOIN	edfi.GradeLevelDescriptors gld
            ON aagl.GradeLevelDescriptor = gld.namespace + '#' + gld.codeValue
	INNER JOIN	edfi.AssessmentItemResultDescriptors aird
            ON sai.AssessmentItemResultDescriptor = aird.namespace + '#' + aird.codeValue
	INNER JOIN analytics.StudentSchoolDim ON StudentSchoolDim.studentUniqueId = sa.studentUniqueId
	INNER JOIN edfi.Schools s ON s.SchoolId = StudentSchoolDim.SchoolKey
    INNER JOIN edfi.Students stu ON stu.studentUniqueId = sai.studentUniqueId
GO