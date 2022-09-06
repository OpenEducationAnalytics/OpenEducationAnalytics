IF NOT EXISTS (SELECT * FROM sys.external_file_formats WHERE name = 'SynapseDelimitedTextFormat')
	CREATE EXTERNAL FILE FORMAT [SynapseDelimitedTextFormat]
	WITH ( FORMAT_TYPE = DELIMITEDTEXT ,
	       FORMAT_OPTIONS (
			 FIELD_TERMINATOR = ',',
			 USE_TYPE_DEFAULT = FALSE
			))
GO

IF NOT EXISTS (SELECT * FROM sys.external_data_sources WHERE name = 'stage2_stoeacisdedfi1_dfs_core_windows_net')
	CREATE EXTERNAL DATA SOURCE [stage2_stoeacisdedfi1_dfs_core_windows_net]
	WITH (
		LOCATION = 'abfss://stage2@stoeacisdedfi1.dfs.core.windows.net'
	)
GO

CREATE EXTERNAL TABLE [analytics_config].[GradeLevelType] (
	[GradeLevelTypeId] bigint,
	[CodeValue] nvarchar(4000),
	[Description] nvarchar(4000)
	)
	WITH (
	LOCATION = 'Standardized/Transactional/EdFi/v5.3/General/DistrictId=255901/SchoolYear=2017/analytics_config.GradeLevelType/GradeLevelType.csv',
	DATA_SOURCE = [stage2_stoeacisdedfi1_dfs_core_windows_net],
	FILE_FORMAT = [SynapseDelimitedTextFormat]
	)
GO

CREATE EXTERNAL TABLE [analytics_config].[GradingScale](
		[GradingScaleId] [int]  NULL,
		[LocalEducationAgencyId] [int] NULL,
		[GradingScaleName] [nvarchar](50) NULL,
	)
	WITH (
	LOCATION = 'Standardized/Transactional/EdFi/v5.3/General/DistrictId=255901/SchoolYear=2017/analytics_config.GradingScale/GradingScale.csv',
	DATA_SOURCE = [stage2_stoeacisdedfi1_dfs_core_windows_net],
	FILE_FORMAT = [SynapseDelimitedTextFormat]
	)
GO
DROP EXTERNAL TABLE [analytics_config].[GradingScaleGrade]
CREATE EXTERNAL TABLE [analytics_config].[GradingScaleGrade](
			[GradingScaleGradeId] [int]  NULL,
			[GradingScaleId] [int] NULL,
			[Rank] [int] NULL,
			[LetterGrade] [nvarchar](20) NULL,
			[UpperNumericGrade] [decimal](6, 2) NULL,
	)
	WITH (
	LOCATION = 'Standardized/Transactional/EdFi/v5.3/General/DistrictId=255901/SchoolYear=2017/analytics_config.GradingScaleGrade/GradingScaleGrade.csv',
	DATA_SOURCE = [stage2_stoeacisdedfi1_dfs_core_windows_net],
	FILE_FORMAT = [SynapseDelimitedTextFormat]
	)
GO

CREATE EXTERNAL TABLE [analytics_config].[GradingScaleGradeLevel](
		[GradingScaleId] [int] NULL,
		[GradeLevelTypeId] [int] NULL,
		[GradingScaleGradeLevelId] [int] NULL,
		)
	WITH (
	LOCATION = 'Standardized/Transactional/EdFi/v5.3/General/DistrictId=255901/SchoolYear=2017/analytics_config.GradingScaleGradeLevel/GradingScaleGradeLevel.csv',
	DATA_SOURCE = [stage2_stoeacisdedfi1_dfs_core_windows_net],
	FILE_FORMAT = [SynapseDelimitedTextFormat]
	)
GO

CREATE EXTERNAL TABLE [analytics_config].[GradingScaleMetricThreshold](
		[GradingScaleId] [int]  NULL,
		[MetricId] [int]  NULL,
		[Value] [int]  NULL,
		[GradingScaleMetricThresholdId] [int]  NULL,
		)
	WITH (
	LOCATION = 'Standardized/Transactional/EdFi/v5.3/General/DistrictId=255901/SchoolYear=2017/analytics_config.GradingScaleMetricThreshold/GradingScaleMetricThreshold.csv',
	DATA_SOURCE = [stage2_stoeacisdedfi1_dfs_core_windows_net],
	FILE_FORMAT = [SynapseDelimitedTextFormat]
	)
GO
