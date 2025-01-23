# Terraform configuration for creating security groups

resource "aws_security_group" "webserver" {
  name = "Web Server Security Group"
  vpc_id = aws_vpc.main.id

  ingress {
    from_port = 80
    to_port   = 80
    protocol = "tcp"

    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port = 88
    to_port   = 88
    protocol = "tcp"

    cidr_blocks = ["0.0.0.0/0"]
  }
}
