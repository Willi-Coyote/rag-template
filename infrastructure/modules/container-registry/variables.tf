variable "resource_group_name" {
  type = string
  description = "Name of the resource group container registry belongs in."
}

variable "resource_group_location" {
  type = string
  description = "Location of the resource group container registry belongs in."
}

variable "resource_number" {
  type = number
  default = 1
  description = "Resource number represents the identifier for the resource"
}

variable "environment" {
  type = string
  description = "The environment the resource is working for"
}

variable "resource_name" {
  type = string
  description = "The resource name"
}

variable "project_name" {
  type = string
  description = "The project/group name"
}
variable "tags" {
  type        = map(string)
  description = "The tag information for the resources"
}