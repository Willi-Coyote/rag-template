locals {
  resource_name_prefix_dash = "${var.project_name}-${var.resource_name}-${var.environment}-${var.resource_group_location}"
}

resource "azurerm_user_assigned_identity" "user_assigned_identity" {
  resource_group_name = var.resource_group_name
  location            = var.resource_group_location

  name = "id-${local.resource_name_prefix_dash}-${format("%02d", var.resource_number)}"
}