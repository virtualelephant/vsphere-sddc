vcenter-cluster
=========

Create, modify or delete a vCenter Server cluster. Enable DRS and HA feature set.

Requirements
------------

pyvmomi

Role Variables
--------------

```yaml
vcenter_hostname: 'vcenter.local'
vcenter_username: '{{ vault_vcenter_username }}'
vcenter_password: '{{ vault_vcenter_password }}'
vcenter_datacenter: 'datacenter'

clusters:
  - name: 'cluster01'
    ha: true
    drs: true
    vsan: true
    state: present
  - name: 'cluster02'
    ha: true
    drs: true
    vsan: true
    state: present
```

Dependencies
------------

An Ansible Vault file must exist and include the following variables:

```yaml
vault_vcenter_username: 'administrator@vsphere.local'
vault_vcenter_password: 'password'
vault_esxi_username: 'root'
vault_esxi_password: 'password'
```

Example Playbook
----------------

```yaml
---
- hosts: all
  connection: local
  gather_facts: false
  
  roles:
    - vcenter-cluster
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
