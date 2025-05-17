#!/usr/bin/env bash

# Exit immediately on any error
set -euo pipefail

RAND_SUFFIX=$(openssl rand -hex 6)    # e.g. a1b2c3d4e5f6


RESOURCE_GROUP_NAME="Azuredevops"
STORAGE_ACCOUNT_NAME="tfstate${RAND_SUFFIX}"
CONTAINER_NAME="tfstate"

# This command is not needed in the Udacity provided Azure account. 
# Create resource group
# az group create --name $RESOURCE_GROUP_NAME --location eastus

# Create storage account
# az storage account create --resource-group $RESOURCE_GROUP_NAME --name $STORAGE_ACCOUNT_NAME --sku Standard_LRS --encryption-services blob

echo "Creating storage account '${STORAGE_ACCOUNT_NAME}' in RG '${RESOURCE_GROUP_NAME}'…"
az storage account create \
  --name "${STORAGE_ACCOUNT_NAME}" \
  --resource-group "${RESOURCE_GROUP_NAME}" \
  --location "${LOCATION}" \
  --sku Standard_LRS \
  --kind StorageV2 \
  --encryption-services blob \
  --https-only true

# Get storage account key
ACCOUNT_KEY=$(az storage account keys list --resource-group $RESOURCE_GROUP_NAME --account-name $STORAGE_ACCOUNT_NAME --query '[0].value' -o tsv)
export ARM_ACCESS_KEY=$ACCOUNT_KEY

# Create blob container

echo "Creating blob container '${CONTAINER_NAME}'…"
az storage container create --name $CONTAINER_NAME --account-name $STORAGE_ACCOUNT_NAME --account-key $ACCOUNT_KEY

echo "RESOURCE_GROUP_NAME=$RESOURCE_GROUP_NAME"
echo "STORAGE_ACCOUNT_NAME=$STORAGE_ACCOUNT_NAME"
echo "CONTAINER_NAME=$CONTAINER_NAME"
echo "ACCOUNT_KEY=$ACCOUNT_KEY"

