resource "azurerm_storage_account" "storage_account_01" {
  name                     = "${local.resource_name_storage_no_delimiter}01"
  resource_group_name      = module.service_resource_group_01.name
  location                 = module.service_resource_group_01.location
  account_tier             = "Standard"
  account_replication_type = "LRS"

  tags = merge(var.basic_tag_information, {
    created_by = var.created_by
  })
}

resource "azurerm_storage_container" "storage_container_01" {
  name                  = "tfstate"
  storage_account_name  = azurerm_storage_account.storage_account_01.name
  container_access_type = "private"
}
