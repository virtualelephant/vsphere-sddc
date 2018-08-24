Role Name
=========

Create or delete NSX-v Logical Switches.

Requirements
------------

pyvmomi
nsxansible (https://github.com/vmware/nsxansible)

Role Variables
--------------

```yaml
nsxmanager_spec:
  raml_file: '/path/to/nsxraml/nsxvapi.raml'
  host: 'nsx-manager.local'
  user: '{{ vault_nsxv_username }}'
  password: '{{ vault_nsxv_password }}'

logical_switch:
  name: 'logical-switch'
  tz: 'transport-zone'
  state: present
  control_plane: 'UNICAST_MODE'
  description: 'vxlan logical switch'
```

Dependencies
------------

An Ansible Vault file must exist and include the following variables:

```yaml
vault_nsxv_username: 'admin'
vault_nsxv_password: 'password'
```

Example Playbook
----------------

```yaml
---
- hosts: all
  connection: local
  gather_facts: false
  
  roles:
    - nsxv-logical-switch
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
