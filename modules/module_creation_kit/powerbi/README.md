> In this folder, you will find a draft Power BI dashboard template . Download this template and use it for your module’s visualization. When done, upload the updated .pbix files back to this folder: one for the dashboard template using Import, and one for the dashboard template using DirectQuery. Please provide descriptions of each page and visuals, as well as screenshots of the Power BI dashboard and the data model in this README.md file.

# Power BI Template
The [name of module] module Power BI template enables users to quickly explore [name of module and tables processed] data. There are two options for exploring this module's Power BI template:
 - [Power BI with test data](insert hyperlink to Imported PBIX dashboard template): Power BI template with module test data imported locally.
 - [Power BI with direct query](insert hyperlink to DirectQuery PBIX dashboard template): Power BI template connected to a Synapse workspace data source. See instructions below to setup.

See [Power BI setup instructions](insert hyperlink to instructions) below for details.

## Dashboard Explanation
The [name of module] Power BI template consists of [number] pages, which [insert brief description of how the dashboard enables users]: 

1. **Page 1:** description of page.
- visual 1 name - description of visual
- visual 2 name - description of visual
- visual 3 name - description of visual

2. **Page 2:** description of page.
- visual 1 name - description of visual
- visual 2 name - description of visual
- visual 3 name - description of visual

3. **Page 3:** description of page.
- visual 1 name - description of visual
- visual 2 name - description of visual
- visual 3 name - description of visual

![image](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_creation_kit/docs/images/Module_Dashboard_Page1_Sample.png)
NB: This can be an image of one of the PowerBI pages.

## Data Model
This Power BI data model consists of  the [name of module] tables: [list table names]. The dimension table is [name of dimension table] and the fact tables are [list of fact tables].

![image](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_creation_kit/docs/images/Sample_PowerBI_Semantic_Model.png)

## Power BI Setup Instructions
### Power BI with imported test data:
- Download the PBIX file with test data here: [LINK](insert hyperlink to Imported PBIX dashboard template).
- Open the link locally on your computer and explore module test data.

### Power BI with direct query of data on your data lake:
- Complete the [module setup instructions](insert hyperlink to module landing page README to the module setup instructions).
- Download the PBIX file with direct query here: [LINK](insert hyperlink to DirectQuery PBIX dashboard template).

[Insert the rest of the instructions relevant applying DirectQuery to the module dashboard template; see the [Clever module](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Clever/powerbi) as an example.]
