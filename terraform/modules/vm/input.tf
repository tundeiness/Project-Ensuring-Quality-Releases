variable "location" {
  type = string
}

variable "resource_group" {
  type = string
}

variable "application_type" {
  type = string
}

variable "resource_type" {
  type = string
}

variable "subnet_id" {
  type = string
}

variable "public_ip_address_id" {
  type = string
}

variable "admin_username" {
  type    = string
  default = "adminuser"
}

variable "vm_size" {
  type    = string
  default = "Standard_B1s"
}

variable "vm_name" {
  type = string
}

variable "admin_ssh_key_path" {
  type    = string
  # default = "/Users/tunde/Desktop/udrsa/.ssh/id_rsa.pub"
  default = "~/.ssh/authorized_keys"
}

variable "network_security_group_id" {
  type = string
}


