resource "azurerm_resource_group" "service_resource_group" {
  location = var.resource_group_location
  name     = "rg-${var.project_name}-${var.resource_name}-${var.environment}-${format("%02d", var.resource_number)}"

  tags = var.tags
}