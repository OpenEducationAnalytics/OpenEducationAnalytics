
IF EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.VIEWS WHERE TABLE_SCHEMA = 'analytics' AND TABLE_NAME = 'SchoolCalendarDim')
BEGIN
	DROP VIEW analytics.SchoolCalendarDim
END
GO

CREATE VIEW analytics.SchoolCalendarDim AS
	WITH Calendar AS
	(
		SELECT CalendarCode,
		SchoolId,
		SchoolYear
		FROM
		(
			SELECT CalendarCode,
			SchoolId,
			sy.SchoolYear,
			ROW_NUMBER() OVER (PARTITION BY c.SchoolId, c.SchoolYear ORDER BY c.LastModifiedDate DESC) as [Priority]
			FROM edfi.Calendars c
			INNER JOIN [analytics].[CurrentSchoolYearDim] sy
				ON c.SchoolYear = sy.SchoolYear
			INNER JOIN edfi.CalendarTypeDescriptors ON
				c.CalendarTypeDescriptor = CalendarTypeDescriptors.namespace + '#' +  CalendarTypeDescriptors.codevalue

		) c
		WHERE c.[Priority] = 1
	)
	SELECT	JSON_VALUE(caldate.CalendarReference, '$.schoolId') AS SchoolKey,
			caldate.[Date],
			ced.CodeValue,
			(ROW_NUMBER() OVER (PARTITION BY JSON_VALUE(caldate.CalendarReference, '$.schoolId') ORDER BY caldate.[Date] DESC) - 1) as DaysBack
	FROM Calendar c
	INNER JOIN edfi.CalendarDates caldate
		ON JSON_VALUE(caldate.CalendarReference, '$.calenderCode') = c.CalendarCode
		AND JSON_VALUE(caldate.CalendarReference, '$.schoolId') = c.SchoolId
		AND JSON_VALUE(caldate.CalendarReference, '$.schoolYear') = c.SchoolYear
	INNER JOIN [analytics].[SchoolMinMaxDateDim] mmd
		ON mmd.SchoolKey = JSON_VALUE(caldate.CalendarReference, '$.schoolId')
	LEFT JOIN edfi.Schools s
		ON JSON_VALUE(caldate.CalendarReference, '$.schoolId') = s.SchoolId
	LEFT JOIN edfi.CalendarEventDescriptors ced
		ON JSON_VALUE(caldate.CalendarEvents, '$[0].calendarEventDescriptor') = ced.namespace + '#' +  ced.codevalue
	WHERE
		ced.CodeValue IN ('Instructional day','Make-up day')
		AND caldate.[Date] <= mmd.MaxDate
		-- The MaxDate is determined by the latest date in the attendance event table; that date may be a date in the future
		AND caldate.[Date] <= GETDATE()
GO