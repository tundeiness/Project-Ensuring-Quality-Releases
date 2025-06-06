resource "random_id" "unique" {
  byte_length = 4
}

resource "azurerm_app_service_plan" "test" {
  name                = "${var.application_type}-${var.resource_type}-${random_id.unique.hex}"
  location            = "West Europe"
  resource_group_name = var.resource_group

  sku {
    tier = "Free"
    size = "F1"
  }
}

resource "azurerm_app_service" "test" {
  name                = "${var.application_type}-${var.resource_type}-${random_id.unique.hex}"
  location            = "West Europe"
  resource_group_name = var.resource_group
  app_service_plan_id = azurerm_app_service_plan.test.id

  app_settings = {
    "WEBSITE_RUN_FROM_PACKAGE" = 0
  }
}
