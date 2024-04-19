module "service_resource_group_01" {
    
    source = "../../modules/resource-group"

    resource_group_location = var.location
    project_name = var.resource_group_name_prefix
    resource_name = var.resource_name
    resource_number = 1

    environment = var.global_environment_id
    tags = var.basic_tag_information
}