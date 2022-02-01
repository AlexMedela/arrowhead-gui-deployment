provider "azurerm" {
  features {}

  subscription_id = var.subscription_id
  tenant_id = var.tenant_id
  client_id = var.client_id
  client_secret = var.client_secret
}

resource "azurerm_resource_group" "default" {
  name     = "arrowhead_framework-rg"
  location = "West Europe"

  tags = {
    environment = "Arrowhead Framework"
  }
}

resource "azurerm_kubernetes_cluster" "default" {
  name                = "arrowhead_framework-aks"
  location            = azurerm_resource_group.default.location
  resource_group_name = azurerm_resource_group.default.name
  dns_prefix          = "arrowhead-k8s"
  kubernetes_version  = "1.20.13"

  default_node_pool {
    name            = "default"
    node_count      = 1
    vm_size         = "Standard_B4ms"
  }

  service_principal {
    client_id     = var.client_id
    client_secret = var.client_secret
  }

  role_based_access_control {
    enabled = true
  }

  tags = {
    environment = "Arrowhead Framework"
  }
}
