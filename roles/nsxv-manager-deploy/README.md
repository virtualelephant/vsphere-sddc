nsxv-manager-deploy
=========

A role to deploy the NSX-v Manager OVA to a vCenter Server.

Requirements
------------

pyvmomi
nsxansible (https://github.com/vmware/nsxansible)

Role Variables
--------------

```yaml
ovftool_path: '/usr/bin/ovftool'
ova_path: '/mnt/repo'
ova_file: 'VMware-NSX-Manager-6.4.1-8599035.ova'

vcenter_hostname: 'vcenter.local'
vcenter_username: '{{ vault_vcenter_username }}'
vcenter_password: '{{ vault_vcenter_password }}'
vcenter_datacenter: 'datacenter'
vcenter_cluster: 'cluster'

nsx_manager:
  name: 'nsx-manager'
  fqdn: 'nsx-manager.local'
  ipaddr: '192.168.0.2'
  netmask: '255.255.255.0'
  gw: '192.168.0.254'
  portgroup: 'management'
  admin_password: '{{ vault_nsxv_admin_password }}'
  enable_password: '{{ vault_nsxv_enable_password }}'

domain_name: 'local.domain'
dns_servers:
  - 8.8.8.8
  - 8.8.4.4
ntp_servers:
  - 132.163.96.5
  - 132.163.97.5
```

Dependencies
------------

An Ansible Vault file must exist and include the following variables:

```yaml
vault_vcenter_username: 'administrator@vsphere.local'
vault_vcenter_password: 'password'
vault_nsxv_username: 'admin'
vault_nsxv_password: 'password'
vault_nsxv_enable_password: 'password'
```

Example Playbook
----------------

```yaml
---
- hosts: all
  connection: local
  gather_facts: false
  
  roles:
    - nsxv-manager-deploy
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