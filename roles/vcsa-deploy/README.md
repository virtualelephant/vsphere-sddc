vcsa-deploy
=========

Deploy a vCenter Server Appliance or Platform Services Controller from OVA to a target ESXi node.

Fork of https://github.com/vmware/ansible-role-vcsa

Requirements
------------

pyvmomi

Role Variables
--------------

```yaml
repo_dir: '/opt/repo'
vcsa_iso: 'VMware-VCSA-all-6.7.0-9451876.iso'
vcsa_task_directory: '/opt/ansible/roles/vcsa-deploy/tasks'

ovftool: '/mnt/vcsa/ovftool/lin64/ovftool'
vcsa_ova: 'vcsa/VMware-vCenter-Server-Appliance-6.7.0.14000-9451876_OVF10.ova'
mount_dir_path: '/mnt'

appliance_type: 'embedded'

net_addr_family: 'ipv4'
network_ip_scheme: 'static'
disk_mode: 'thin'
ssh_enable: true

vcenter_appliance_name: 'vcenter'
vcenter_appliance_size: 'medium'

target_esxi_username: '{{ vault_esxi_username }}'
target_esxi_password: '{{ vault_esxi_password }}'
target_esx_datastore: 'local-t410-3TB'
target_esx_portgroup: 'Management'

time_sync_tools: false

vcenter_password: '{{ vault_vcenter_password }}'
vcenter_fqdn: 'vcenter.local.domain'
vcenter_ip_address: '192.168.0.25'
vcenter_netmask: '255.255.0.0'
vcenter_gateway: '192.168.0.1'
vcenter_net_prefix: '16'

dns_servers: '192.168.0.1,192.168.0.2'
ntp_servers: '132.163.96.1,132.163.97.1'

sso_password: '{{ vault_vcenter_password }}'
sso_site_name: 'Default-Site'
sso_domain_name: 'vsphere.local'
```

Dependencies
------------

An Ansible Vault file must exist and include the following variables:

```yaml
vault_esxi_username: 'root'
vault_esxi_password: 'password'
vault_vcenter_password: 'password'
```

The vCenter Server Appliance ISO must be accessible to the role/playbook.

Example Playbook
----------------

```yaml
---
- hosts: all
  connection: local
  gather_facts: false
  
  roles:
    - vcsa-deploy
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

Modified by Chris Mutchler (chris@virtualelephant.com). http://virtualelephant.com