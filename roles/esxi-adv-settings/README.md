esxi-adv-settings
=========

Set the Advanced Settings on an ESXi node. The Ansible module `vmware_host_config_manager` is not idempotent.

Requirements
------------

pyvmomi

Role Variables
--------------

```yaml
esxi_username: '{{ vault_esxi_username }}'
esxi_password: '{{ vault_esxi_password }}'

esxi_adv_settings:
  Mem.AllocGuestLargePage: 0
  Mem.ShareForceSalting: 0
  Net.TcpipHeapSize: 32
  Net.TcpipHeapMax: 1024
  Syslog.global.loghost: 'syslog.local'
  UserVars.SuppressShellWarning: 1
  VSAN.SwapThickProvisionDisabled: 1
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
    - esx-adv-settings
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
