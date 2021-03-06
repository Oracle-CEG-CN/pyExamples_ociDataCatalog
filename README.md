# OCI Data Catalog / OCI Python SDK - Examples
The examples in this repository are not official Oracle code and should be treated as examples without any waranty and are not intended to be used in any way or form in real code. Please refer to the license file for additional information on warranty, usability and shareability guidance.

This repository contains examples for using the Oracle Cloud Python SDK in combination with Oracle Data Catalog.

## Tech Focus
The examples focus primarily on the below tech components:

### Oracle Data Catalog
Oracle Cloud Infrastructure Data Catalog is a fully managed, self-service data discovery and governance solution for your enterprise data. With Data Catalog, you get a single collaborative environment to manage technical, business, and operational metadata. You can collect, organize, find, access, understand, enrich, and activate this metadata. 
https://docs.oracle.com/en-us/iaas/data-catalog/using/index.htm

### OCI Python SDK
The Oracle Cloud Infrastructure SDK for Python enables you to write code to manage Oracle Cloud Infrastructure resources.
https://pypi.org/project/oci/

## Examples

### example_showCatalogs.py
The intend of this code is to provide example code to list all data catalogs under a specified compartment within OCI. 
See documentation and code [here](/exampleCode/example_showCatalogs.md)

### example_showGlossary.py
The intend of this code is to provide example code to list all glossaries which are part of a given data catalog based upon the Data Catalog ID.
See documentation and code [here](/exampleCode/example_showGlossary.md)

### example_showGlossarySummary.py
The intend of this code is to provide example code to list a summary of the content of a glossary as part of the Oracle Data Catalog See documentation and code [here](/exampleCode/example_showGlossarySummary.md)

### example_showDataAssets.py
The intend of this code is to provide example code to list all data assets which are part of a given data catalog based upon the Data Catalog ID. See documentation and code [here](/exampleCode/example_showDataAssets.md)

### example_plain_rest_api_cmd.py
The intend of this code is to provide example code to access an Oracle Data
Catalog instance using the plain REST API with authentication provided by the
OCI Python API for request signing.[here](/exampleCode/example_plain_rest_api_cmd.md)
