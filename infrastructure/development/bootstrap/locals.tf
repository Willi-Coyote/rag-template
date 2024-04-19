locals {
  resource_name_storage_no_delimiter = "${var.resource_group_name_prefix}${var.resource_name}${var.global_environment_id}"
  resource_name_prefix_dash = "${var.resource_group_name_prefix}-${var.resource_name}-${var.global_environment_id}"
}