Role Name
=========

Interface with ESXi services (start, stop, restart, enable, disable)

Requirements
------------

pyvmomi

Role Variables
--------------

vcenter_hostname: 'vcenter.local'
vcenter_username: 'administrator@vsphere.local'
vcenter_password: 'password'
cluster: 'cluster01'
state: present

Dependencies
------------


Example Playbook
----------------
```yaml
---
- hosts: all
  connection: local
  gather_facts: false  
  roles:
    - esxi-services

```
License
-------


Author Information
------------------

Role created by Chris Mutchler (chris@virtualelephant.com)
