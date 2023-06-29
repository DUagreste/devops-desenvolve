variable "amis" {
    type = map(string)

    default = {
        "us-east-1" = "ami-053b0d53c279acc90"
        "us-east-2" = "ami-01ba8fe702263d044"
    }
}

variable "cidr_acesso_remoto" {
    type = list(string)

    default = ["177.37.168.129/32", "178.37.168.129/32"]
}

variable "key_name" {
    type = string

    default = "terraform-aws"
}