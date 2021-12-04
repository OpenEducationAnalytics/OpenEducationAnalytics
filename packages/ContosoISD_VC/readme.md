# Verifiable Credentials Package for Digital Learner Records
A learner’s knowledge, skills, and capabilities are often not fully represented by a transcript or a test score. Today, learners acquire knowledge and skills from multiple sources – courses from their schools or colleges, courses from outside providers (e.g. Coursera, EdX, LinkedIn Learning), internships, and throughout life on jobs. Learners need to be able to present a more comprehensive picture of their knowledge, capabilities, and skills  from across these different experiences. 

This OEA Package enables learning organizations that have set up the OEA Azure Synapse environment to combine data from their student information system with the Verifiable Credentials service from Microsoft Azure, so they can more easily issue verifiable credentials to students.  

New technologies such as Distributed Identity and Verifiable Credentials provide a means for a learner to collect credentials from different learning experiences, where those credentials are issued by different schools or learning organizations and can be verified digitally. These digital claims of knowledge and skills enable people and organizations to share learning records, while providing data privacy controls for the learner.  


Use cases in education for Verifiable Credentials include: 

- Schools or universities issuing digital transcripts or credentials for specific course completions to students, who can share them in school admissions processes or potential employers 
- Schools sharing learner records for students who move between schools within a district, state, or country 
- Expanding the range of knowledge and skills that can be represented for a student, beyond standard curriculum or transcripts 

The Verifiable Credentials package allows students to accept and confirm the verified credentials they have earned and that have been issued to them by institutions or organizations. Students can then share the appropriate credentials with another institution or organization, including school and job applications. The institution or employer can then digitally verify the skills and credentials the student earned, in support of their application. 

This OEA package will: 

- Allow institutions or schools to easily set up the learner profile data in their OEA Azure Synapse environment to be able to issue verified credentials to students based on triggered events, such as course completions 
- Allow students to receive and accept verifiable credentials for skills they have acquired by an issuing organization (e.g., a school) 
- Allow students to maintain and manage a collection of the skills they have learned from various organizations (e.g. schools and employers) from their mobile phones 

This package utilizes student data from an education system’s Student Information System their Azure Active Directory identity service. 

This package was developed by Microsoft Education and Azure Active Directory Verified Credentials.  The architecture and reference implementation for this package is built on [Azure Synapse Analytics](https://azure.microsoft.com/en-us/services/synapse-analytics/) - with [Azure Data Lake Storage](https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction) as the storage backbone, and [Azure Active Directory](https://azure.microsoft.com/en-us/services/active-directory/) providing the role-based access control.

To set up the system, please follow these steps: 

- Pipeline of data aggregation from multiple modules 
- Setting up VC service 
- Use Azure fx to write into VC 
- Setting up website for student login/ 3rd party verifier – client API 

The source of data can be replaced with other types of identity access management data the institution uses. The verifying student learning package and its modules [welcomes contributions...](https://github.com/microsoft/OpenEduAnalytics/blob/main/CONTRIBUTING.md).

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

