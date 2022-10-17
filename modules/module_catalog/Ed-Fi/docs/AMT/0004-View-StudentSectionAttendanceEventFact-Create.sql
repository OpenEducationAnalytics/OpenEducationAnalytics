IF EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.VIEWS WHERE TABLE_SCHEMA = 'analytics' AND TABLE_NAME = 'StudentSectionAttendanceEventFact')
BEGIN
	DROP VIEW analytics.StudentSectionAttendanceEventFact
END
GO

CREATE VIEW analytics.StudentSectionAttendanceEventFact AS

	SELECT
		stu.StudentUniqueId as StudentKey
		,ssae.EventDate
		,SSAE.SectionIdentifier
		,SSAE.SessionName
		,ssae.LocalCourseCode
		,ttd.CodeValue as TermDescriptor
		,ssae.SchoolYear
		,aecd.CodeValue as AttendanceEventCategoryDescriptor
		,'' AS AttendanceEventReason
	FROM edfi.Students stu
    INNER JOIN edfi.StudentSectionAttendanceEvents ssae
		ON ssae.studentUniqueId = stu.studentUniqueId
    INNER JOIN edfi.Sections sec
        ON sec.SchoolId = ssae.SchoolId
        AND sec.LocalCourseCode = ssae.LocalCourseCode
        AND sec.SchoolYear = ssae.SchoolYear
        ANd sec.SessionName = ssae.SessionName
        AND sec.SectionIdentifier = ssae.SectionIdentifier
    INNER JOIN edfi.[Sessions] sess
        ON JSON_VALUE(sess.SchoolReference, '$.schoolId') = ssae.SchoolId
        AND JSON_VALUE(sess.SchoolYearTypeReference, '$.schoolId') = ssae.SchoolYear
        AND sess.SessionName = ssae.SessionName
    INNER JOIN edfi.TermDescriptors ttd
		ON sess.TermDescriptor = ttd.namespace + '#' +  ttd.codevalue
    INNER JOIN edfi.AttendanceEventCategoryDescriptors aecd
		ON ssae.AttendanceEventCategoryDescriptor = aecd.namespace + '#' + aecd.codevalue
	INNER JOIN [analytics].[StudentSchoolDim] ssa
			ON ssa.[SchoolKey] = ssae.SchoolId
			AND ssa.StudentKey = stu.studentUniqueId
GO