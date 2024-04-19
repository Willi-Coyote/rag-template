# bootstrap

This directory contains all the initial resources required by the service.

## How to make changes to the service?

1. **Modify the Terraform Configuration**: Make the necessary modifications to your Terraform configuration files to add, modify, or delete resources as required.

2. **Run the Terraform Plan**: Execute the command `terraform plan -out main.tfplan` in the directory where you've made changes. This command generates an execution plan and saves it to a file named `main.tfplan`. This step allows you to review the changes Terraform will make to your infrastructure before applying them.

   Please note that during this step, you'll be prompted to enter a value for the `created_by` variable. Enter your name here; this tags the resources with your name, providing a clear record of who created them.

3. **Apply the Terraform Plan**: Run the command `terraform apply main.tfplan` to apply the changes outlined in your execution plan. After this step, verify that the changes have been successfully implemented in your Azure resources.

Remember to always review the output of `terraform plan` carefully to ensure the changes align with your intentions before running `terraform apply`. This can help prevent unintended modifications to your infrastructure.
