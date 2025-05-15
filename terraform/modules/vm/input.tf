
variable "location" {}
variable "resource_group" {}
variable "application_type" {}
variable "resource_type" {}
variable "subnet_id" {}
variable "public_ip_address_id" {}

variable "admin_username" {
  default = "azureuser"
}

variable "vm_size" {
  default = "Standard_B1s"
}

variable "vm_name" {}

variable "admin_ssh_key_path" {
  default = "/Users/tunde/Desktop/udrsa/.ssh/id_rsa.pub"
}

variable "network_security_group_id" {}
