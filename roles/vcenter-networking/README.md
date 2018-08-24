vcenter-networking
=========

Manage a vCenter Server Distributed Virtual Switch.

Requirements
------------

pyvmomi

Role Variables
--------------

```yaml
vcenter_hostname: 'vcenter.local'
vcenter_username: '{{ vault_vcenter_username }}'
vcenter_password: '{{ vault_vcenter_password }}'
vmware_datacenter: 'datacenter'

switches:
  - name: dvSwitch1
    version: '6.6.0'
    mtu: 9000
    uplink_quantity: 2
    discovery_proto: 'cdp'
    discovery_operation: 'both'
    state: present
  - name: dvSwitch2
    version: '6.6.0'
    mtu: 9000
    uplink_quantity: 2
    discovery_proto: 'cdp'
    discovery_operation: 'both'
    state: present
```

Dependencies
------------

An Ansible Vault file must exist and include the following variables:

```yaml
vault_vcenter_username: 'administrator@vsphere.local'
vault_vcenter_password: 'password'
```

Example Playbook
----------------

```yaml
---
- hosts: all
  connection: local
  gather_facts: false
  
  roles:
    - vcenter-networking
```

License
-------

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.

You may obtain a copy of the License at
   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Author Information
------------------

Created by Chris Mutchler (chris@virtualelephant.com). http://virtualelephant.com
