
IF EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.VIEWS WHERE TABLE_SCHEMA = 'analytics' AND TABLE_NAME = 'StudentSchoolAttendanceEventFact')
BEGIN
	DROP VIEW analytics.StudentSchoolAttendanceEventFact
END
GO

CREATE VIEW analytics.StudentSchoolAttendanceEventFact AS
		SELECT	stu.StudentUniqueId as StudentKey,
				ssae.EventDate,
				ttd.CodeValue AS TermDescriptor,
				ssae.SchoolYear,
				aecd.CodeValue as AttendanceEventCategoryDescriptor,
				'' AS AttendanceEventReason
		FROM edfi.Students stu
		INNER JOIN edfi.StudentSchoolAttendanceEvents ssae
			ON ssae.studentUniqueId = stu.studentUniqueId
		INNER JOIN edfi.[Sessions] sess
			ON JSON_VALUE(sess.SchoolReference, '$.schoolId') = ssae.SchoolId
			AND JSON_VALUE(sess.SchoolYearTypeReference, '$.schoolYear') = ssae.SchoolYear
			AND sess.SessionName = ssae.SessionName
		INNER JOIN edfi.TermDescriptors ttd
			ON sess.TermDescriptor = ttd.namespace + '#' +  ttd.codevalue
		INNER JOIN edfi.AttendanceEventCategoryDescriptors aecd
			ON ssae.AttendanceEventCategoryDescriptor = aecd.namespace + '#' + aecd.codevalue
		INNER JOIN [analytics].[StudentSchoolDim] ssa
				ON ssa.SchoolKey = ssae.SchoolId
				AND ssa.StudentKey = stu.studentUniqueId
GO