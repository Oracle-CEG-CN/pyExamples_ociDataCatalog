'''
NAME:
      example_plain_rest_api_cmd.py
DESC:
      This code is part of series of examples on how to use the Oracle Cloud Infrastructure OCI SDK for python in
      combination with the Oracle Cloud Data Catalog service. This code is NOT official Oracle code and is developed
      outside of Oracle and is just for educational example use. Please refer to the license as mentioned below. This
      specific code has been developed/tested with Python 3.7
INTEND:
      The intend of this code is to provide example code on how to use the plain REST API for Oracle Data Catalog.
      Based on Python's 'cmd' package, it provides a command line to navigate parts of an Oracle Data Catalog instance.
LICENSE:
      Copyright (C) 2021  Stefan Höning
      This code is free software; you can redistribute it and/or modify it under the terms of the GNU General Public
      License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any
      later version.

      This code is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
      warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
      details.

      You should have received a copy of the GNU General Public License along with this code; if not, write to the
      Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
'''


from oci.config import from_file

from oci.signer import Signer

from cmd import Cmd

import requests

import json

_oci_config = from_file()


compartment_id = _oci_config['compartment_id']


auth = Signer(
    tenancy=_oci_config['tenancy'],
    user=_oci_config['user'],
    fingerprint=_oci_config['fingerprint'],
    private_key_file_location=_oci_config['key_file'])


class ODCService:
    def __init__(self, _region, _compartment_id):
        self._region = _region
        self._compartment_id = _compartment_id

    def _get(self, _url_suffix):
        url = 'https://datacatalog.%s.oci.oraclecloud.com/20190325/%s' % (self._region, _url_suffix) 
        response = requests.get(url, auth=auth)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception()

    def catalogs(self):
        return self._get('catalogs?compartmentId=%s' % (self._compartment_id))

    def catalog(self, _key):
        return self._get('catalogs/%s' % (_key))

    def types(self, _catalog_id):
        return self._get('catalogs/%s/types' % (_catalog_id))

    def type(self, _catalog_id, _type_id):
        return self._get('catalogs/%s/types/%s' % (_catalog_id, _type_id))

    def data_assets(self, _catalog_id):
        return self._get('catalogs/{catalog_id}/dataAssets'.format(catalog_id=_catalog_id))

    def data_asset(self, _catalog_id, _data_asset_key):
        return self._get('catalogs/{catalog_id}/dataAssets/{data_asset_key}'.format(catalog_id=_catalog_id, data_asset_key=_data_asset_key))

    def folders(self, _catalog_id, _data_asset_key):
        return self._get('catalogs/{catalog_id}/dataAssets/{data_asset_key}/folders'.format(catalog_id=_catalog_id, data_asset_key=_data_asset_key))

    def folder(self, _catalog_id, _data_asset_key, _folder_key):
        return self._get('catalogs/{catalog_id}/dataAssets/{data_asset_key}/folders/{folder_key}'.format(catalog_id=_catalog_id, data_asset_key=_data_asset_key, folder_key=_folder_key))

    def entities(self, _catalog_id, _data_asset_key):
        return self._get('catalogs/{catalog_id}/dataAssets/{data_asset_key}/entities'.format(catalog_id=_catalog_id, data_asset_key=_data_asset_key))

    def entity(self, _catalog_id, _data_asset_key, _entity_key):
        return self._get('catalogs/{catalog_id}/dataAssets/{data_asset_key}/entities/{entity_key}'.format(catalog_id=_catalog_id, data_asset_key=_data_asset_key, entity_key=_entity_key))

    def attributes(self, _catalog_id, _data_asset_key, _entity_key):
        return self._get('catalogs/{catalog_id}/dataAssets/{data_asset_key}/entities/{entity_key}/attributes'.format(catalog_id=_catalog_id, data_asset_key=_data_asset_key, entity_key=_entity_key))

    def attribute(self, _catalog_id, _data_asset_key, _entity_key, _attribute_key):
        return self._get('catalogs/{catalog_id}/dataAssets/{data_asset_key}/entities/{entity_key}/attributes/{attribute_key}'.format(catalog_id=_catalog_id, data_asset_key=_data_asset_key, entity_key=_entity_key, attribute_key=_attribute_key))


class ODCBaseCommand(Cmd):
    def __init__(self, _odc_service):
        Cmd.__init__(self)
        self._odc_service = _odc_service

    def _show_json(self, _json):
        print(json.dumps(_json, indent=4))

    def do_exit(self, line):
        return True


class ODCCatalogBaseCommand(ODCBaseCommand):
    def __init__(self, _odc_service, _catalog_id):
        ODCBaseCommand.__init__(self, _odc_service)
        self._catalog_id = _catalog_id

    def do_types(self, line):
        if (len(line) > 0):
            self._show_json(self._odc_service.type(self._catalog_id, line))
        else:
            self._show_json(self._odc_service.types(self._catalog_id))


class ODCDataAssetBaseCommand(ODCCatalogBaseCommand):
    def __init__(self, _odc_service, _catalog_id, _data_asset_key):
        ODCCatalogBaseCommand.__init__(self, _odc_service, _catalog_id)
        self._data_asset_key = _data_asset_key


class ODCEntityCommand(ODCDataAssetBaseCommand):
    def __init__(self, _odc_service, _catalog_id, _data_asset_key, _entity_key):
        ODCDataAssetBaseCommand.__init__(self, _odc_service, _catalog_id, _data_asset_key)
        self._entity_key = _entity_key

    def do_attributes(self, line):
        if (len(line) > 0):
            self._show_json(self._odc_service.attribute(self._catalog_id, self._data_asset_key, self._entity_key, line))
        else:
            self._show_json(self._odc_service.attributes(self._catalog_id, self._data_asset_key, self._entity_key))


class ODCDataAssetCommand(ODCDataAssetBaseCommand):
    def __init__(self, _odc_service, _catalog_id, _data_asset_key):
        ODCDataAssetBaseCommand.__init__(self, _odc_service, _catalog_id, _data_asset_key)
        
    def do_folders(self, line):
        if (len(line) > 0):
            self._show_json(self._odc_service.folder(self._catalog_id, self._data_asset_key, line))
        else:
            self._show_json(self._odc_service.folders(self._catalog_id, self._data_asset_key))

    def do_entities(self, line):
        if (len(line) > 0):
            self._show_json(self._odc_service.entity(self._catalog_id, self._data_asset_key, line))
        else:
            self._show_json(self._odc_service.entities(self._catalog_id, self._data_asset_key))

    def do_set_entity(self, line):
        if (len(line) > 0):
            ODCEntityCommand(self._odc_service, self._catalog_id, self._data_asset_key, line).cmdloop()
        else:
            print('No entity key given')


class ODCCatalogCommand(ODCCatalogBaseCommand):
    def __init__(self, _odc_service, _catalog_id):
        ODCCatalogBaseCommand.__init__(self, _odc_service, _catalog_id)
            
    def do_data_assets(self, line):
        if (len(line) > 0):
            self._show_json(self._odc_service.data_asset(self._catalog_id, line))
        else:
            self._show_json(self._odc_service.data_assets(self._catalog_id))

    def do_set_data_asset(self, line):
        if (len(line) > 0):
            ODCDataAssetCommand(self._odc_service, self._catalog_id, line).cmdloop()
        else:
            print('No data asset key given')


class ODCCommand(ODCBaseCommand):
    def __init__(self, _odc_service):
        ODCBaseCommand.__init__(self, _odc_service)
        self._odc_service = _odc_service

    def do_set_catalog(self, line):
        if (len(line) > 0):
            ODCCatalogCommand(self._odc_service, line).cmdloop()
        else:
            print('No catalog_id given')

    def do_catalogs(self, line):
        if (len(line) > 0):
            self._show_json(self._odc_service.catalog(line))
        else:
            self._show_json(self._odc_service.catalogs())

    def do_exit(self, line):
        return True


def main():
    odc_service = ODCService('eu-frankfurt-1', compartment_id)
    ODCCommand(odc_service).cmdloop()


if __name__ == '__main__':
    main()

