# Verified Credentials Package for Personalized Learner Records

We know that a student’s capabilities cannot be fully represented by a transcript and GPA from a single source. Today’s students learn and acquire capabilities from multiple sources – coursework through institutions, coursework through other curriculum providers (e.g. LinkedIn Learning), internships, and jobs. A comprehensive and personalized picture of their knowledge, capabilities, and skills, will best position students for academic and career success.  

Verified credential solving problem….verification of claims of knowledge and skills, enabling systems to share records between different schools, unified place for learner record 

This complete picture can also be supported by verified credentials that confirm a student’s capabilities by the issuing institution or organization. The combination of a learner’s list of capabilities, supported with verified credentials, creates a record that students can share with potential employers or institutions for applications and background check verification.  

The verifying student learning package allows students to accept and confirm the verified credentials they have earned and that have been issued to them by institutions or organizations. Students can then share the appropriate credentials with another institution or organization for multiple use cases, including school and job applications. The institution or employer can review and verify the skills and credentials the student earned, in support of their application.  

This package will: 

- Allow institutions or schools to easily set up the learner profile data to be able to issue verified credentials to students based on triggered events, such as course completions 
- Allow students to receive and accept skills they have acquired by an issuing organization (e.g. a school) 
- Allow students to maintain and manage a list of the skills they have learned from various organizations (e.g. schools and employers)  
- Allow institutions to issue verified credentials to students, based on the courses they have successfully completed  
- Allow employers to ask for verification of student’s skills 
- Allow students to share verified skills with employer 
- Allow employer to verify that the student has completed the skills required for the job the student is applying for 

This package utilizes student data from an education system’s Student Information System and Microsoft 365 data modules. 

This package was developed by Microsoft Education and Azure Active Directory Verified Credentials. The architecture and reference implementation for this package is built on [Azure Synapse Analytics](https://azure.microsoft.com/en-us/services/synapse-analytics/) - with [Azure Data Lake Storage](https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction) as the storage backbone, and [Azure Active Directory](https://azure.microsoft.com/en-us/services/active-directory/) providing the role-based access control.

To set up the system, please follow these steps: 

- Pipeline of data aggregation from multiple modules 
- Setting up VC service 
- Use Azure fx to write into VC 
- Setting up website for student login/ 3rd party verifier – client API  

The source of data can be replaced with other types of identity access management data the institution uses. The verifying student learning package and its modules [welcomes contributions...](https://github.com/microsoft/OpenEduAnalytics/blob/main/CONTRIBUTING.md).

Here is what this will look like fully set up from the student’s perspective:  
