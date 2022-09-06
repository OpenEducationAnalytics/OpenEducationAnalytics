IF EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.VIEWS WHERE TABLE_SCHEMA = 'analytics' AND TABLE_NAME = 'StudentProgramAssociationDim')
BEGIN
	DROP VIEW analytics.StudentProgramAssociationDim
END
GO

CREATE VIEW [analytics].StudentProgramAssociationDim AS

	SELECT	stu.StudentUniqueId as StudentKey
			, ptd.CodeValue as ProgramType
			, [BeginDate]
			, [EndDate]
			, P.EducationOrganizationId AS EducationOrganizationKey
	FROM edfi.Students stu
		INNER JOIN edfi.StudentProgramAssociations spa ON spa.StudentUniqueId = stu.StudentUniqueId
		INNER JOIN analytics.StudentSchoolDim ssa ON ssa.StudentKey = stu.StudentUniqueId
		INNER JOIN edfi.Schools s ON ssa.SchoolKey = s.SchoolId
		INNER JOIN edfi.ProgramTypeDescriptors ptd on ptd.namespace +'#'+ ptd.codeValue = spa.ProgramTypeDescriptor
		INNER JOIN edfi.Programs p ON p.EducationOrganizationId=s.LocalEducationAgencyId
			AND p.ProgramTypeDescriptor = spa.ProgramTypeDescriptor
			AND p.ProgramName = spa.ProgramName
GO