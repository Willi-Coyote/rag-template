locals {
  resource_name_prefix_dash = "${var.project_name}-${var.resource_name}-${var.environment}"
}

data "azurerm_key_vault_key" "key_vault" {
  name         = "kvl-${local.resource_name_prefix_dash}-${format("%02d", var.resource_number)}"
  key_vault_id = data.azurerm_key_vault.existing.id
}