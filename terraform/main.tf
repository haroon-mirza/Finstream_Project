provider "azurerm" {
  features {}
}

# resource group
resource "azurerm_resource_group" "finstream" {
  name     = "FinStreamResourceGroup"
  location = "eastus"
}

# data factory
resource "azurerm_data_factory" "finstream" {
  name                = "FinStreamDataFactory"
  location            = azurerm_resource_group.finstream.location
  resource_group_name = azurerm_resource_group.finstream.name
}

# databricks workspace
resource "azurerm_databricks_workspace" "finstream" {
  name                = "FinStreamDatabricks"
  resource_group_name = azurerm_resource_group.finstream.name
  location            = azurerm_resource_group.finstream.location
  sku                 = "standard"
}

# log analytics workspace
resource "azurerm_log_analytics_workspace" "finstream" {
  name                = "FinStreamLogAnalytics"
  location            = azurerm_resource_group.finstream.location
  resource_group_name = azurerm_resource_group.finstream.name
  sku                 = "PerGB2018"
}

# data lake storage account
resource "azurerm_storage_account" "finstream" {
  name                     = "finstreamdatalake"
  resource_group_name      = azurerm_resource_group.finstream.name
  location                 = azurerm_resource_group.finstream.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

# data lake storage container
resource "azurerm_storage_container" "finstream" {
  name                  = "content"
  storage_account_name  = azurerm_storage_account.finstream.name
  container_access_type = "private"
}
