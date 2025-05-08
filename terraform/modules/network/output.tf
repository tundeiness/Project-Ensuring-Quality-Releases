output "subnet_id_test" {
  value = "${azurerm_subnet.test.id}"
}

output "subnet_id" {
  value = azurerm_subnet.test.id  # replace with your actual subnet resource name
}
