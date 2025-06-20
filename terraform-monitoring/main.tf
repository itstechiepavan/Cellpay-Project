provider "aws" {
  region = "eu-north-1"
}

resource "aws_instance" "monitoring_server" {
  ami           = "ami-0c55b159cbfafe1f0" # Amazon Linux 2 for eu-north-1
  instance_type = "t3.medium"
  key_name      = "your-key-name" # REPLACE with your EC2 key pair name

  tags = {
    Name = "Monitoring-Instance"
  }

  user_data = <<-EOF
              #!/bin/bash
              yum update -y
              yum install -y docker git
              systemctl start docker
              systemctl enable docker

              docker run -d --name prometheus -p 9090:9090 prom/prometheus
              docker run -d --name grafana -p 3000:3000 grafana/grafana
              EOF
}
