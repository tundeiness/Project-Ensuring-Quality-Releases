output "public_ip_address_id" {
  value = "${azurerm_public_ip.test.id}"
}

output "public_ip_id" {
  value = azurerm_public_ip.test.id  # replace with your actual public IP resource name
}
