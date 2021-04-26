'''
NAME:
      example_showGlossarySummary.py
DESC:
      This code is part of series of examples on how to use the Oracle Cloud Infrastructure OCI SDK for python in
      combination with the Oracle Cloud Data Catalog service. This code is NOT official Oracle code and is developed
      outside of Oracle and is just for educational example use. Please refer to the license as mentioned below. This
      specific code has been developed/tested with Python 3.7
INTEND:
      The intend of this code is to provide example code to list a summary of the content of a glossary as part of the
      Oracle Data Catalog
LICENSE:
      Copyright (C) 2021  Johan Louwers
      This code is free software; you can redistribute it and/or modify it under the terms of the GNU General Public
      License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any
      later version.

      This code is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
      warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
      details.

      You should have received a copy of the GNU General Public License along with this code; if not, write to the
      Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
'''

import oci
from oci.config import from_file

# Populate the below variables with the appropriate values for your specific situation.
ociConfigFile = ("/ociExampels/DataCatalog/dataCatalogExamples.config")
ociDataCatalogId = ("ocid1.datacatalog.oc1.eu-frankfurt-1.xxxxxxxxxxxx")
ociGlossaryId = ("xxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx")

# load the configuration content from the file defined in var ociConfigFile into var ociConfig
ociConfig = from_file(file_location=ociConfigFile)

# Initiate the client to interact with the Oracle Cloud Data Catalog.
catalogClient = oci.data_catalog.DataCatalogClient(ociConfig)

# get the summary of the glossary identified by ociDataCatalogId and ociGlossaryId 
glossarySummaryList = catalogClient.expand_tree_for_glossary(ociDataCatalogId, ociGlossaryId).data

# print the summary of the glossary 
print (glossarySummaryList)
