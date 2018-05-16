# vsphere-sddc
Project to deploy complete SDDC stack using Ansible. Initial execution of the workflow will rely upon a hard-coded variables YAML file for ingestion of values.

### Identified holes in Ansible VMware modules
- Migrate a vmkernel interface from a VDS back to a VSS (unwinding).
- Migrate a vmnic on a VSS to a VDS.
- vmware_vmkernel: Add ability to specify the vmk interface (vmk0, vmk1, vmk2, etc.)

### Rollback
- ESXi has a lot of leftover data, may be easier to wipe boot blocks and reinstall using automation.
