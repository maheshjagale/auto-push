# Azure managed identity setup

terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~>3.0"
    }
  }
}

# Connect to Azure using Managed Identity
provider "azurerm" {
  features {}
  use_msi = true
}

# Create a Resource Group 
resource "azurerm_resource_group" "demo" {
  name     = "my-rg"
  location = "centralindia"
}

# Create a Virtual Network
resource "azurerm_virtual_net" "demo" {
  name                = "my-first-network"
  address_space       = ["10.0.0.0/16"]
  location            = azurerm_resource_group.demo.location
  resource_group_name = azurerm_resource_group.demo.name

