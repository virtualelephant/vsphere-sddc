#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: vmware_vcsa_upgrade
short_description: Upgrade a vCenter Server Appliance
description:
    - Using the vCenter Server API, update, stage and upgrade a
      vCenter Server Appliance from an upstream repository.
version_added: 2.6
author:
    - Chris Mutchler (@chrismutchler)
notes:
    - Tested on vSphere 6.7
requirements:
    - "python >= 2.6"
    - pyVmomi
options:
    hostname:
      description:
        - Name of the vCenter Server to update.
      required: True
extends_documentation_fragment: vmware.documentation
'''

EXAMPLES = r'''
- name: Check for VCSA updates
  vmware_vcsa_upgrade:
    hostname: vcenter_hostname
    username: vcenter_root_username
    password: vcenter_root_password
    state: update
    url: download_url

- name: Stage VCSA update
  vmware_vcsa_upgrade:
    hostname: vcenter_hostname
    username: vcenter_root_username
    password: vcenter_root_password
    state: stage

- name: Upgrade the VCSA
  vmware_vcsa_upgrade:
    hostname: vcenter_hostname
    username: vcenter_root_username
    password: vcenter_root_password
    state: upgrade
'''

try:
    from pyVmomi import vim
    HAS_PYVMOMI = True
except ImportError:
    HAS_PYVMOMI = False

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.vmware import *

def main():
    argument_spec = vmware_argument_spec()
    argument_spec.update(dict(
        action=dict(required=True, type='str')
    ))
    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)

    if not HAS_PYVMOMI:
        module.fail_json(msg='pyVmomi is required for this module')

    content = connect_to_api(module=module)

    result = {
            'changed': False
    }

if __name__ == '__main__':
    main()
