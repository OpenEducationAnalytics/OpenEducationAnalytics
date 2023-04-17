IF EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.VIEWS WHERE TABLE_SCHEMA = 'analytics' AND TABLE_NAME = 'StudentLanguageDim')
BEGIN
	DROP VIEW analytics.StudentLanguageDim
END
GO

CREATE VIEW analytics.StudentLanguageDim AS

	SELECT	Student.StudentUniqueId AS StudentKey
			, ld.CodeValue as [Language]
			, ldu.CodeValue as LanguageUse
	FROM edfi.Students Student
		INNER JOIN edfi.StudentEducationOrganizationAssociationLanguages sl
			ON Student.StudentUniqueId = sl.StudentUniqueId
		LEFT JOIN edfi.LanguageDescriptors ld
			ON sl.LanguageDescriptor = ld.namespace +'#'+ ld.codeValue
		LEFT JOIN edfi.studentEducationOrganizationAssociationLanguageUses slu
			ON sl.StudentUniqueId = slu.StudentUniqueId
			AND sl.LanguageDescriptor = slu.LanguageDescriptor
			AND sl.EducationOrganizationId = slu.EducationOrganizationId
		LEFT JOIN edfi.LanguageUseDescriptors ldu
			ON slu.LanguageuseDescriptor = ldu.namespace +'#'+ ldu.codeValue
		LEFT JOIN [analytics].[StudentSchoolDim] StudentSchoolDim
			ON StudentSchoolDim.StudentKey = Student.StudentUniqueId
		LEFT JOIN edfi.Schools School
			ON School.SchoolId = StudentSchoolDim.SchoolKey
		WHERE ld.CodeValue IS NOT NULL
GO