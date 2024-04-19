variable "location" {
  type        = string
  default     = "Southeast Asia"
  description = "Location of the resource group."
}

variable "resource_group_name_prefix" {
  type        = string
  default     = "rag"
  description = "Prefix of the resource group name that's relevant to the project in your Azure subscription."
}

variable "resource_name" {
  type        = string
  description = "The name of the resource"
}

variable "global_environment_id" {
  type        = string
  description = "The current environment. The possible value are 'dev', 'prod'"
}

variable "basic_tag_information" {
  type        = map(string)
  description = "The basic tag information for the resources"
}

variable "created_by" {
  type        = string
  description = "This variable describes who created this resource"
}