# Azure GUIDs
variable "subscription_id" {}
variable "client_id" {}
variable "client_secret" {}
variable "tenant_id" {}

# Resource Group/Location
variable "location" {}
variable "resource_group" {}
variable "application_type" {}

# Network
variable "virtual_network_name" {}
variable "address_space" {}
variable "address_prefix_test" {}

# VM
variable "packer_image" {}
variable "admin_username" {}
variable "admin_password" {}
