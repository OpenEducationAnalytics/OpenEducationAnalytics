IF EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.VIEWS WHERE TABLE_SCHEMA = 'analytics' AND TABLE_NAME = 'StudentAssessmentDim')
BEGIN
	DROP VIEW analytics.StudentAssessmentDim
END
GO

CREATE VIEW [analytics].StudentAssessmentDim AS

	WITH StudentAssessmentPerformanceLevelPrioritized AS
		(
		SELECT
			p.studentUniqueId
			, p.AssessmentIdentifier
			, p.StudentAssessmentIdentifier
			, p.[Namespace]
			, p.AssessmentReportingMethodDescriptorId
			, p.PerformanceLevelDescriptorId
			, p.PerformanceLevelMet
			, ROW_NUMBER() OVER (
				PARTITION BY
					p.studentUniqueId
					, p.AssessmentIdentifier
					, p.StudentAssessmentIdentifier
					, p.[Namespace]
					, p.AssessmentReportingMethodDescriptorId
				ORDER BY
					p.PerformanceLevelMet DESC
					, p.PerformanceLevelDescriptorId DESC
				) AS [Priority]
		FROM edfi.StudentAssessmentPerformanceLevel p
	)
	SELECT
		  stu.StudentUniqueId as StudentKey
		, CAST(s.SchoolId AS VARCHAR) as SchoolKey
		, a.AssessmentIdentifier
		, sa.StudentAssessmentIdentifier
		, AssessmentCategoryDescriptor.CodeValue AS AssessmentCategory
		, LTRIM(RTRIM(a.AssessmentTitle)) AS AssessmentTitle
		, AssessmentAcademicSubjectDescriptor.CodeValue AS AcademicSubject
		, AssessmentAssessedGradeLevelDescriptor.CodeValue AS AssessedGradeLevel
		, a.AssessmentVersion AS [Version]
		, sa.AdministrationDate
		, ReasonNotTestedDescriptor.CodeValue AS ReasonNotTested
		, a.MaxRawScore AS MaxScoreResult
		, sapl.PerformanceLevelDescriptorId AS PerformanceLevel
		, sapl.PerformanceLevelMet
		, a.Namespace
	FROM edfi.Assessments a
		INNER JOIN edfi.AssessmentAcademicSubject aas
			ON aas.AssessmentIdentifier = a.AssessmentIdentifier
			AND aas.[Namespace] = a.[Namespace]
		INNER JOIN edfi.StudentAssessments sa
			ON sa.AssessmentIdentifier = a.AssessmentIdentifier
			AND sa.[Namespace] = a.[Namespace]
		INNER JOIN edfi.AssessmentAssessedGradeLevels aagl
			ON aagl.AssessmentIdentifier = a.AssessmentIdentifier
			AND aagl.[Namespace] = a.[Namespace]
		INNER JOIN	edfi.AssessmentCategoryDescriptors
            ON AssessmentCategoryDescriptors.namespace + '#' + AssessmentCategoryDescriptors.codeValue = a.AssessmentCategoryDescriptor
		INNER JOIN	edfi.AssessmentAcademicSubjectDescriptors
            ON AssessmentAcademicSubjectDescriptors.namespace + '#' + AssessmentAcademicSubjectDescriptors.codeValue = aas.AcademicSubjectDescriptor
		INNER JOIN	edfi.AssessmentAssessedGradeLevelDescriptors
            ON AssessmentAssessedGradeLevelDescriptors.namespace + '#' + AssessmentAssessedGradeLevelDescriptors.codeValue  = aagl.GradeLevelDescriptor
		LEFT JOIN	edfi.ReasonNotTestedDescriptors
            ON ReasonNotTestedDescriptors.namespace + '#' + ReasonNotTestedDescriptors.codeValue  = sa.ReasonNotTestedDescriptor
		LEFT JOIN StudentAssessmentPerformanceLevelPrioritized sapl
			ON sapl.studentUniqueId = sa.studentUniqueId
			AND sapl.AssessmentIdentifier = a.AssessmentIdentifier
			AND sapl.StudentAssessmentIdentifier = sa.StudentAssessmentIdentifier
			AND sapl.[Namespace] = a.[Namespace]
			AND sapl.[Priority] = 1
		INNER JOIN analytics.StudentSchoolDim ON StudentSchoolDim.StudentKey = sa.studentUniqueId
		INNER JOIN edfi.Schools s ON s.SchoolId = StudentSchoolDim.SchoolKey
		INNER JOIN edfi.Students stu ON stu.studentUniqueId = sa.studentUniqueId
GO