IF EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.VIEWS WHERE TABLE_SCHEMA = 'analytics' AND TABLE_NAME = 'ProgramDim')
BEGIN
	DROP VIEW analytics.ProgramDim
END
GO

CREATE VIEW [analytics].ProgramDim AS
    SELECT p.educationOrganizationId,
        p.programName,
        pd.codeValue as ProgramType

    FROM edfi.ProgramTypeDescriptors pd
    JOIN edfi.programs p on pd.namespace + '#' +  pd.codevalue = p.programTypeDescriptor
    WHERE pd.CodeValue IN (
                'Section 504 Placement',
                'Bilingual',
                'Bilingual Summer',
                'Career and Technical Education',
                'English as a Second Language (ESL)',
                'Gifted and Talented',
                'Special Education',
                'Title I Part A'
            )
    OR (pd.CodeValue = 'Other' AND p.ProgramName LIKE 'Food Service%')
