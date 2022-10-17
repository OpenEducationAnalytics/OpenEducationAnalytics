CREATE OR ALTER VIEW [analytics].[GradingPeriodDim] AS

	SELECT
		CAST(gpd.charterStatusDescriptorId as NVARCHAR)
			+ '-' + CAST(gp.SchoolId as NVARCHAR)
			+ '-' + CONVERT(NVARCHAR, gp.BeginDate, 112) as GradingPeriodKey,
		CONVERT(NVARCHAR, gp.BeginDate, 112) as GradingPeriodBeginDateKey,
		CONVERT(NVARCHAR, gp.EndDate, 112) as GradingPeriodEndDateKey,
		gpd.CodeValue as GradingPeriodDescription,
		gp.TotalInstructionalDays,
		gp.PeriodSequence,
		CAST(gp.SchoolId AS VARCHAR) as SchoolKey,
		CAST(gp.SchoolYear AS VARCHAR) as SchoolYear,
		gp.LastModifiedDate,
		gp.BeginDate,
		gp.EndDate
	FROM
		edfi.GradingPeriods gp
	INNER JOIN
		edfi.GradingPeriodDescriptors gpd ON
			gp.GradingPeriodDescriptor = gpd.namespace +'#'+ gpd.codeValue
	WHERE gp.BeginDate < GETDATE()
GO
