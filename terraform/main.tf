provider "aws" {
  region = var.aws_region
}

resource "aws_instance" "app_server" {
  ami           = "ami-0ec10929233384c7f"
  instance_type = var.instance_type

  tags = {
    Name = "ExamenModulo3"
  }
}