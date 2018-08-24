nsxv-controllers
=========

Create or delete NSX-v Controllers.

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

vcenter_hostname: 'vcenter.local'
vcenter_username: '{{ vault_vcenter_username }}'
vcenter_password: '{{ vault_vcenter_password }}'
vcenter_datacenter: 'datacenter'
vcenter_datastore: 'vsanDatastore'
vcenter_cluster: 'cluster'

controller_portgroup: 'portgroup'
controller_pool_state: true
controller_state: present
controller_name_prefix: 'prefix-'
controller_password: '{{ vault_controller_password }}'

syslog_server: 'syslog.local'

controller_ippool:
  name: controller_ippool
  start_ip: '192.168.0.251'
  end_ip: 192.168.253'
  prefix_length: '24'
  gw: '192.168.0.254'
  dns1: '8.8.8.8'
  dns2: '8.8.4.4'
```

Dependencies
------------

An Ansible Vault file must exist and include the following variables:

```yaml
vault_vcenter_username: 'administrator@vsphere.local'
vault_vcenter_password: 'password'
vault_nsxv_username: 'admin'
vault_nsxv_password: 'password'
vault_controller_password: 'password'
```

Example Playbook
----------------

```yaml
---
- hosts: all
  connection: local
  gather_facts: false
  
  roles:
    - nsxv-controllers
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
