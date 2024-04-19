# Rag Terraform Infrastructure

## Code folder structure

- [**development**](development)
  - [**bootstrap**](development/bootstrap)
  - [**services**](development/services)
    - [**ai-search**](development/services/ai-search)
- [**modules**](modules)
  - [**container-registry**](modules/container-registry)
  - [**key-vault**](modules/key-vault)
  - [**resource-group**](modules/resource-group)
  - [**user-assigned-identity**](modules/user-assigned-identity)
- [**production**](production)

### Overview

Each service will be in it's own terraform module. This is to encourage separate of concern and avoid having one big terraform module that contains everything and result in an messy codebase. To make changes to a service, make the necessary changes and run the terraform plan and apply command in the directory related to the service that you are change.

### Resource naming convention

We will be following the resource naming convention as recommended by Microsoft in the following link: [Azure resource naming convention best practice](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-naming)

In general, this is the format that we should follow:

| Naming Component                          | Description                                                                                                                                                                                                                                                       |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Organization**                          | Top-level name of the organization, normally utilized as the top management group or, in smaller organizations, part of the naming convention. Example: contoso                                                                                                   |
| **Business Unit or Department**           | Top-level division of your company that owns the subscription or the workload that the resource belongs to. In smaller organizations, this component might represent a single corporate, top-level organizational element. Examples: fin, mktg, product, it, corp |
| **Resource Type**                         | An abbreviation that represents the type of Azure resource or asset. This component is often a prefix or suffix in the name. For more information, see Recommended abbreviations for Azure resource types. Examples: rg, vm                                       |
| **Project, Application, or Service Name** | Name of a project, application, or service that the resource is a part of. Examples: navigator, emissions, sharepoint, hadoop                                                                                                                                     |
| **Environment**                           | The stage of the development lifecycle for the workload that the resource supports. Examples: prod, dev, qa, stage, test                                                                                                                                          |
| **Location**                              | The region or cloud provider where the resource is deployed. Examples: westus, eastus2, westeu, usva, ustx                                                                                                                                                        |
| **VM Role**                               | Identifier of the purpose of the VM. Examples: db (database), ws (web server), ps (print server)                                                                                                                                                                  |
| **Instance**                              | The instance count for a specific resource, to differentiate it from other resources that have the same naming convention and naming components. Examples, 01, 001                                                                                                |

Format: `<resource-type>-<project-name>-<environment>-<location>-<vm-role><instance>`

Example: `rg-rag-bootstrap-dev-01`

### development

This folder will contain all the development environment resources.

#### development/bootstrap

This folder will contain all the terraform configurations to setup the basic resources that we will need before setting up other services.

### modules

This folder contains all the terraform modules that we have setup so that we can reuse them in both the development and production infrastructure setup.

The terraform modules also enable us to bootstap some of the details when setting up resources. You can treat the modules as the basic building blocks that will be used by other modules to build up a complete service.

### production

This folder will contain all the production environment resources.

## How to Terraform?

1. **Modify the Terraform Configuration**: Make the necessary modifications to your Terraform configuration files to add, modify, or delete resources as required.

2. **Run the Terraform Plan**: Execute the command `terraform plan` or `terraform plan -var-file="<replace-with-your-variable-file>.tfvars" -out main.tfplan` in the directory where you've made changes. This command generates an execution plan and saves it to a file named `main.tfplan`. This step allows you to review the changes Terraform will make to your infrastructure before applying them.

   If you're using a variable file, replace `<replace-with-your-variable-file>` with the name of your `.tfvars` file. This file should contain the values for any variables your configuration uses.

3. **Apply the Terraform Plan**: Run the command `terraform apply main.tfplan` to apply the changes outlined in your execution plan. After this step, verify that the changes have been successfully implemented in your Azure resources.

Remember to always review the output of `terraform plan` carefully to ensure the changes align with your intentions before running `terraform apply`. This can help prevent unintended modifications to your infrastructure.

## Current Infrastructure

![Current Infrastructure](infra-design-details/current.png)

## Final Infrastructure

![Final Infrastructure](infra-design-details/final-design.png)
