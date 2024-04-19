# Virtual network for resources that are shared across different services.
resource "azurerm_virtual_network" "bootstrap_vnet_01" {
  name                = "vnet-${local.resource_name_prefix_dash}-${module.service_resource_group_01.location}-01"
  address_space       = ["10.0.0.0/16"]
  location            = module.service_resource_group_01.location
  resource_group_name = module.service_resource_group_01.name
  
  tags = merge(var.basic_tag_information, {
    created_by = var.created_by
  })
}

# Subnet for container registry
resource "azurerm_subnet" "bootstrap_subnet_container_registry" {
  name                 = "snet-${local.resource_name_prefix_dash}-${module.service_resource_group_01.location}-01"
  resource_group_name  = module.service_resource_group_01.name
  virtual_network_name = azurerm_virtual_network.bootstrap_vnet_01.name
  address_prefixes     = ["10.0.0.0/24"]

}
