module "container_registry_01" {
    
    source = "../../modules/container-registry"

    resource_group_name = module.service_resource_group_01.name
    resource_group_location = var.location
    project_name = var.resource_group_name_prefix
    resource_name = var.resource_name
    resource_number = 1

    environment = var.global_environment_id
    tags = merge(var.basic_tag_information, {
        created_by = var.created_by
    })
}