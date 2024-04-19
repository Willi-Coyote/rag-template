resource "azurerm_container_registry" "container_registry_01" {
  name                = "cr${local.resource_name_prefix}${format("%02d", var.resource_number)}"
  resource_group_name = var.resource_group_name
  location            = var.resource_group_location
  sku                 = "Basic"

  tags = var.tags

}
