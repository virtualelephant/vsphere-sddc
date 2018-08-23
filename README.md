# vsphere-sddc
Project to deploy complete SDDC stack using Ansible. Initial execution of the workflow will rely upon a hard-coded variables YAML file for ingestion of values.

## Ansible Roles
esxi-adv-settings     - Configure advanced ESXi settings on ESXi node
esxi-dns-config       - Configure DNS on ESXi node
esxi-ntp-config       - Configure NTP on ESXi node
esxi-services         - Configure ESXi services on ESXi node
esxi-vmk-interfaces   - Create/delete VMkernel interfaces on ESXi node
nsxv-cluster-prep     - Prepare vCenter cluster for NSX-v
nsxv-controllers      - Create/delete NSX-v controllers
nsxv-license          - Assign NSX-v license
nsxv-logical-switch   - Create/delete NSX-v logical switch
nsxv-manager-config   - Configure NSX-v Manager
nsxv-manager-deploy   - Deploy NSX-v Manager OVA to vCenter Server
nsxv-manager-roles    - Configure NSX-v Manager user roles
nsxv-transport-zone   - Create/delete NSX-v transport zone
vcenter-cluster       - Create/delete/modify vCenter cluster
vcenter-datacenter    - Create/delete vCenter datacenter object
vcenter-dvs-migrate   - Migrate ESXi nodes to DVS, including VMkernel interfaces
vcenter-networking    - Create/delete DVS
vcenter-portgroups    - Create/delete port groups
vcsa-deploy           - Deploy vCenter Server Appliance OVA

## Identified holes in Ansible VMware modules
- Migrate a vmkernel interface from a VDS back to a VSS (unwinding).
- Setting up AD authentication for stateful ESXi hosts (https://github.com/vmware/pyvmomi/blob/master/docs/vim/host/ActiveDirectorySpec.rst)
- Creating VMKernel interfaces appears to need to be able to take a datacenter object.
