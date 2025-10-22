"""
Output exports for the infrastructure
"""
import pulumi
from vpc import (
    vpc,
    igw,
    public_subnets,
    private_subnets,
    nat_eip,
    nat_gw,
    public_rt,
    private_rt
)

# VPC outputs
pulumi.export('vpc_id', vpc.id)
pulumi.export('vpc_cidr', vpc.cidr_block)

# Internet Gateway
pulumi.export('internet_gateway_id', igw.id)

# Public Subnets
for i, subnet in enumerate(public_subnets):
    pulumi.export(f'public_subnet_{i+1}_id', subnet.id)
    pulumi.export(f'public_subnet_{i+1}_az', subnet.availability_zone)

# Private Subnets
for i, subnet in enumerate(private_subnets):
    pulumi.export(f'private_subnet_{i+1}_id', subnet.id)
    pulumi.export(f'private_subnet_{i+1}_az', subnet.availability_zone)

# NAT Gateway
pulumi.export('nat_eip', nat_eip.public_ip)
pulumi.export('nat_gateway_id', nat_gw.id)

# Route Tables
pulumi.export('public_route_table_id', public_rt.id)
pulumi.export('private_route_table_id', private_rt.id)