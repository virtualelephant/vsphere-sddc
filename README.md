# vsphere-sddc
Project to deploy complete SDDC stack using Ansible. Initial execution of the workflow will rely upon a hard-coded variables YAML file for ingestion of values.

## Ansible Roles
* esxi-adv-settings     - Configure advanced ESXi settings on an ESXi node
* esxi-host-config      - Configure DNS, hostname and NTP settings on an ESXi node
* esxi-services         - Configure ESXi services on an ESXi node
* esxi-vmk-interfaces   - Create/delete VMkernel interfaces on an ESXi node
* nsxv-cluster-prep     - Prepare vCenter cluster for NSX-v
* nsxv-controllers      - Create/delete NSX-v controllers
* nsxv-license          - Assign NSX-v license
* nsxv-logical-switch   - Create/delete NSX-v logical switch
* nsxv-manager-config   - Configure NSX-v Manager
* nsxv-manager-deploy   - Deploy NSX-v Manager OVA to vCenter Server
* nsxv-manager-roles    - Configure NSX-v Manager user roles
* nsxv-transport-zone   - Create/delete NSX-v transport zone
* vcenter-add-hosts	- Add or remove ESXi nodes to vCenter Server
* vcenter-cluster       - Create/delete/modify vCenter cluster
* vcenter-datacenter    - Create/delete vCenter datacenter object
* vcenter-dvs-migrate   - Migrate ESXi nodes to DVS, including VMkernel interfaces
* vcenter-maintenance-mode	- Manage the maintenance mode state of an ESXi node
* vcenter-networking    - Create/delete a Distributed Virtual Switch 
* vcenter-portgroups    - Create/delete port groups
* vcsa-deploy           - Deploy vCenter Server Appliance OVA

## Ansible Playbooks
* esxi_sddc_configure.yml	- Configure ESXi nodes
* nsxv_sddc_deploy		- Deploy and configure NSX-v Manager and controllers

## Identified holes in Ansible VMware modules
* Setting up AD authentication for stateful ESXi hosts
** (https://github.com/vmware/pyvmomi/blob/master/docs/vim/host/ActiveDirectorySpec.rst)
* Support for creating VMkernel interfaces on a DVS.
* Support for NIOC settings
