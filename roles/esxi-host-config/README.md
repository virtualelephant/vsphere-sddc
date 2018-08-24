esxi-host-config
=========

Manage ESXi node settings, including hostname, DNS and NTP settings.

Requirements
------------

pyvmomi

Role Variables
--------------

```yaml
esxi_username: '{{ vault_esxi_username }}'
esxi_password: '{{ vault_esxi_password }}'
ntp_state: present

dns_servers:
  - 8.8.8.8
  - 8.8.4.4

ntp_servers:
  - 132.163.96.5
  - 132.163.97.5

change_hostname: false
```

Dependencies
------------

An Ansible Vault file must exist and include the following variables:

```yaml
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
    - esxi-dns-config
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