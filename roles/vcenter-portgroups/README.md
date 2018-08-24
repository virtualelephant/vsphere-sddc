vcenter-portgroups
=========

Create or delete vCenter / ESXi port groups

Requirements
------------

pyvmomi

Role Variables
--------------

```yaml
vcenter_hostname: 'vcenter.local'
vcenter_username: '{{ vault_vcenter_username }}'
vcenter_password: '{{ vault_vcenter_password }}'

portgroups:
  - name: "management"
    vlan_id: 101
    num_ports: 120
    portgroup_type: 'ephemeral'
    state: present
  - name: "vmotion"
    vlan_id: 103
    num_ports: 120
    portgroup_type: 'ephemeral'
    state: present

network_policy:
  promiscious: yes
  forged_transmits: yes
  mac_changes: yes

port_policy:
  block_override: yes
  ipfix_override: yes
  live_port: yes
  network_rp: yes
  port_config: yes
  security_override: yes
  shaping_override: yes
  traffic_filter: yes
  uplink_teaming: yes
  vendor_config: yes
  vlan_override: yes
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
    - vcenter-portgroups
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