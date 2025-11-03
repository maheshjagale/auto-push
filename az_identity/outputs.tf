output "resource_group_name" {
  value = azurerm_resource_group.demo.name
}

output "network_name" {
  value = azurerm_virtual_network.demo.name
}
