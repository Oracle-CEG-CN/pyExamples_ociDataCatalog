'''
NAME:
      example_showCatalogs.py
DESC:
      This code is part of series of examples on how to use the Oracle Cloud Infrastructure OCI SDK for python in
      combination with the Oracle Cloud Data Catalog service. This code is NOT official Oracle code and is developed
      outside of Oracle and is just for educational example use. Please refer to the license as mentioned below. This
      specific code has been developed/tested with Python 3.7
INTEND:
      The intend of this code is to provide example code to list all data catalogs under a specified compartment within
      OCI. The variabel
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

__author__ = "Johan Louwers"
__copyright__ = "Copyright 2021, Johan Louwers"
__license__ = "GPLv3 "
__email__ = "louwersj@gmail.com"



import oci
from oci.config import from_file

# Populate the below variables with the appropriate values for your specific situation.
ociConfigFile = ("/ociExampels/DataCatalog/dataCatalogExamples.config")
ociCompartment = ("ocid1.compartment.oc1.xxxxxxxxxxxxxxxxxx")

# load the configuration content from the file defined in var ociConfigFile into var ociConfig
ociConfig = from_file(file_location=ociConfigFile)

# Initiate the client to interact with the Oracle Cloud Data Catalog.
catalogClient = oci.data_catalog.DataCatalogClient(ociConfig)

# Get a list of all data catalogs in the Oracle Cloud compartment where the ID is defined in the var ociCompartment.
catalogsList = catalogClient.list_catalogs(ociCompartment).data

# print the content of catalogsList to show all catalogs that are available
print (catalogsList)
