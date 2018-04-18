output "Public_IP"{
value = "${azurerm_public_ip.eip.ip_address}"
}

output "VM_Name"{
value = "${azurerm_virtual_machine.vm.name}"
}

output "OS_Name"{
value = "${azurerm_virtual_machine.vm.storage_os_disk.0.os_type}"
}

output "Technical-Owner"{
value = "${azurerm_virtual_machine.vm.tags.technical_owner_tag}"
}

output "Project"{
value = "${azurerm_virtual_machine.vm.tags.project_tag}"
}

output "Cost-Code"{
value = "${azurerm_virtual_machine.vm.tags.cost_code_tag}"
}


output "Schedule-Type"{
value = "${azurerm_virtual_machine.vm.tags.schedule_type_tag}"
}

output "Business-Owner"{
value = "${azurerm_virtual_machine.vm.tags.business_owner_tag}"
}

output "Schedule-Type"{
value = "${azurerm_virtual_machine.vm.tags.schedule_type_tag}"
}

output "VM_Size"{
value = "${azurerm_virtual_machine.vm.vm_size}"
}

output "VM_ID"{
value = "${azurerm_virtual_machine.vm.id}"
}

output "VM_Location"{
value = "${azurerm_virtual_machine.vm.location}"
}

output "Resource_Group_Name"{
value = "${data.azurerm_virtual_network.vnet.resource_group_name}"
}

output "VNet"{
value = "${data.azurerm_virtual_network.vnet.name}"
}

output "Subnet"{
value = "${data.azurerm_virtual_network.vnet.subnets.0}"
}

output "Storage_Disk_Size"{
value = "${azurerm_virtual_machine.vm.storage_os_disk.0.disk_size_gb}"
}

output "OS_Disk_Size" {
value = "${azurerm_virtual_machine.vm.storage_data_disk.0.disk_size_gb}"
}
