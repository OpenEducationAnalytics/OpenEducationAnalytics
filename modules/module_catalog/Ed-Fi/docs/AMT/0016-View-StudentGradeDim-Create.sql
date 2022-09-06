IF EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.VIEWS WHERE TABLE_SCHEMA = 'analytics' AND TABLE_NAME = 'StudentGradeDim')
BEGIN
	DROP VIEW analytics.StudentGradeDim
END
GO

CREATE VIEW [analytics].StudentGradeDim AS
	SELECT	stu.StudentUniqueId as StudentKey
			, CAST(g.SchoolId AS VARCHAR) as SchoolKey
			, sec.SectionIdentifier
			, sec.SessionName
			, g.LocalCourseCode
			, td.CodeValue AS TermType
			, g.SchoolYear
			, gpd.CodeValue AS GradingPeriodDescription
			, gp.BeginDate AS GradingPeriodBeginDate
			, g.PeriodSequence
			--, g.LetterGradeEarned
			, g.NumericGradeEarned
			, gtd.CodeValue AS GradeType
	FROM edfi.Students stu
    INNER JOIN edfi.Grades g ON g.studentUniqueId = stu.studentUniqueId
    INNER JOIN edfi.GradingPeriods gp
        ON gp.GradingPeriodDescriptor = g.GradingPeriodDescriptor
        AND gp.SchoolId = g.SchoolId
        AND gp.PeriodSequence = g.PeriodSequence
        AND gp.SchoolYear = g.SchoolYear
    INNER JOIN edfi.[Sessions] s
        ON s.SchoolId = g.SchoolId
        AND s.SchoolYear = g.SchoolYear
        AND s.SessionName = g.SessionName
	INNER JOIN analytics.StudentSchoolDim ON StudentSchoolDim.studentUniqueId = g.studentUniqueId AND StudentSchoolDim.SchoolKey = g.SchoolId
    INNER JOIN edfi.Schools sch ON sch.SchoolId = StudentSchoolDim.SchoolKey
    INNER JOIN edfi.GradingPeriodDescriptors gpd ON g.GradingPeriodDescriptor = gpd.namespace +'#'+ gpd.codeValue
    INNER JOIN edfi.Sections sec
        ON sec.SchoolId = g.SchoolId
        AND sec.LocalCourseCode = g.LocalCourseCode
        AND sec.SchoolYear = g.SchoolYear
        AND sec.SessionName = g.SessionName
        AND sec.SectionIdentifier = g.SectionIdentifier
    INNER JOIN edfi.TermDescriptors td
        ON td.namespace +'#'+ td.codeValue = s.TermDescriptor
	INNER JOIN edfi.GradeTypeDescriptors gtd
    ON gtd.namespace +'#'+ gtd.codeValue = g.GradeTypeDescriptor
GO