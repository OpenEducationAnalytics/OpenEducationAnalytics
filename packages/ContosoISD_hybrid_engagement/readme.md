# Hybrid Student Engagement Package

Student engagement in learning is the starting point for teaching and learning outcomes. Without engagement, learning is blocked. 

As teaching and learning increasingly use digital platforms and tools, and learning takes place outside of schools in digital learning environments, traditional attendance measures are not as representative of students’ actual engagement. Student attendance data is an important metric that schools track and derive insights from. Schools also need a way to measure students' digital activity across the different apps used for learning. With many schools’ transition to hybrid learning, having a way to combine students' in-person attendance in schools and their digital activity will be valuable for school systems. This combination provides a more comprehensive view of student engagement in learning than attendance data alone.

The Hybrid Engagement Package from OEA includes a set of modules for combining in-person attendance and digital activity, providing a more holistic representation of student engagement. This can be used by system and school leaders, and by teachers to identify:
 - Which schools and classes have higher and lower levels of hybrid engagement in learning, and whether expected patterns of engagement are continuing over time. 
 - Which schools and classes have higher and lower levels of in-person attendance or digital activities. This can be used to plan more precisely targeted programs or interventions to increase either attendance or use of digital learning tools, or both. 

The modules in this package can be combined with course completion, academic assessments, competency measures, mastery data, graduation rates, or other outcome data to identify how patterns of engagement relate to learning outcomes. With such combined data, schools and teachers can start to analyze whether new programs or interventions help to improve learning outcomes.  

![image](https://github.com/microsoft/OpenEduAnalytics/blob/64fb4f3b11c225f8c17e486a7174aa8b2684f1b2/packages/ContosoISD_hybrid_engagement/docs/images/hybrid_engagement_overview.png)

This package was developed by Microsoft Education in partnership with Fresno Unified School District in California. The architecture and reference implementation for all modules is built on [Azure Synapse Analytics](https://azure.microsoft.com/en-us/services/synapse-analytics/) - with [Azure Data Lake Storage](https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction) as the storage backbone,  and [Azure Active Directory](https://azure.microsoft.com/en-us/services/active-directory/) providing the role-based access control.

The modules currently represents data from Microsoft Teams for Digital Activities, but that source of data can be replaced with other types of digital activity data or combined with other sources of digital activity data if the school or system has access to those data. 

Modules in the hybrid student engagement package include: 

1. Pipelines for ingesting data from multiple sources into the data lake.
2. Notebooks for cleaning, transforming, anonymizing and enriching data into the data warehouse.
3. PowerBI templates for exploring, visualizing and deriving insights from the data.

The hybrid student engagement package and its modules [welcome contributions.](https://github.com/microsoft/OpenEduAnalytics/blob/main/CONTRIBUTING.md) 

# Legal Notices

Microsoft and any contributors grant you a license to the Microsoft documentation and other content
in this repository under the [Creative Commons Attribution 4.0 International Public License](https://creativecommons.org/licenses/by/4.0/legalcode),
see the [LICENSE](LICENSE) file, and grant you a license to any code in the repository under the [MIT License](https://opensource.org/licenses/MIT), see the
[LICENSE-CODE](LICENSE-CODE) file.

Microsoft, Windows, Microsoft Azure and/or other Microsoft products and services referenced in the documentation
may be either trademarks or registered trademarks of Microsoft in the United States and/or other countries.
The licenses for this project do not grant you rights to use any Microsoft names, logos, or trademarks.
Microsoft's general trademark guidelines can be found at http://go.microsoft.com/fwlink/?LinkID=254653.

Privacy information can be found at https://privacy.microsoft.com/en-us/

Microsoft and any contributors reserve all other rights, whether under their respective copyrights, patents,
or trademarks, whether by implication, estoppel or otherwise.
