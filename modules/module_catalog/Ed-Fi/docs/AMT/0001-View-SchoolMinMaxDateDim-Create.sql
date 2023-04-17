IF EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.VIEWS WHERE TABLE_SCHEMA = 'analytics' AND TABLE_NAME = 'SchoolMinMaxDateDim')
BEGIN
	DROP VIEW analytics.SchoolMinMaxDateDim
END
GO

CREATE VIEW analytics.SchoolMinMaxDateDim AS

	SELECT	localEducationAgencyId as LocalEducationAgencyKey,
			CAST(Sch.SchoolId AS VARCHAR) as SchoolKey,
			COALESCE(MIN(SS.BeginDate), MIN(gp.BeginDate), '1900/1/1') as MinDate,
			COALESCE(MAX(Att.MaxDate), MAX(cd.[Date]), GETDATE()) as MaxDate,
			COALESCE(MIN(SS.EndDate),'1900/1/1') as SessionEndDate
	FROM edfi.Schools Sch
    LEFT JOIN
    (
        SELECT	a.SchoolId,
            	MAX(a.EventDate) AS MaxDate
        FROM edfi.StudentSectionAttendanceEvents a
		WHERE a.EventDate <= CURRENT_TIMESTAMP
        GROUP BY a.SchoolId

        UNION ALL

        SELECT	a.SchoolId,
				MAX(a.EventDate) AS MaxDate
        FROM edfi.StudentSchoolAttendanceEvents a
		WHERE a.EventDate <= CURRENT_TIMESTAMP
        GROUP BY a.SchoolId
    ) AS Att
        ON Sch.SchoolId = Att.SchoolId

    LEFT JOIN edfi.[Sessions] ss
        ON ss.schoolId = sch.SchoolId

    LEFT JOIN edfi.GradingPeriods gp
        ON gp.SchoolId = sch.SchoolId

    LEFT JOIN edfi.CalendarDates cd
        ON JSON_VALUE(cd.calendarReference, '$.SchoolId') = sch.SchoolId
        AND cd.[Date] <= GETDATE()
	GROUP BY localEducationAgencyId, Sch.SchoolId;
GO

