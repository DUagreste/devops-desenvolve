# Using a single workspace:
terraform {
  backend "remote" {
    hostname = "app.terraform.io"
    organization = "vitorlabs-cloud"

    workspaces {
      name = "aws-vitorlabs"
    }
  }
}