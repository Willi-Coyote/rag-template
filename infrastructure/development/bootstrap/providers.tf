terraform {

  required_version = "1.7.5"

  required_providers {
    azurerm = {
      version = "3.98.0"
      source  = "hashicorp/azurerm"
    }    
  }
  backend "azurerm" {
      resource_group_name  = "rg-rag-bootstrap-dev-01"
      storage_account_name = "ragbootstrapdev01"
      container_name       = "tfstate"
      key                  = "terraform-bootstrap.tfstate"
  }
}

provider "azurerm" {
  features {}
}
