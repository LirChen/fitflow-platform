"""
VPC and networking resources
"""
import pulumi
from pulumi_aws import ec2
from config import (
    VPC_CIDR, 
    AVAILABILITY_ZONES, 
    PUBLIC_SUBNET_CIDRS, 
    PRIVATE_SUBNET_CIDRS,
    get_tags
)

# VPC
vpc = ec2.Vpc('fitflow-vpc',
    cidr_block=VPC_CIDR,
    enable_dns_hostnames=True,
    enable_dns_support=True,
    tags=get_tags('VPC')
)

# Internet Gateway
igw = ec2.InternetGateway('fitflow-igw',
    vpc_id=vpc.id,
    tags=get_tags('IGW')
)

# Public Subnets
public_subnets = []
for i, (az, cidr) in enumerate(zip(AVAILABILITY_ZONES, PUBLIC_SUBNET_CIDRS)):
    subnet = ec2.Subnet(f'fitflow-public-subnet-{i+1}',
        vpc_id=vpc.id,
        cidr_block=cidr,
        availability_zone=az,
        map_public_ip_on_launch=True,
        tags=get_tags(f'Public-Subnet-{i+1}')
    )
    public_subnets.append(subnet)

# Private Subnets
private_subnets = []
for i, (az, cidr) in enumerate(zip(AVAILABILITY_ZONES, PRIVATE_SUBNET_CIDRS)):
    subnet = ec2.Subnet(f'fitflow-private-subnet-{i+1}',
        vpc_id=vpc.id,
        cidr_block=cidr,
        availability_zone=az,
        map_public_ip_on_launch=False,
        tags=get_tags(f'Private-Subnet-{i+1}')
    )
    private_subnets.append(subnet)

# Public Route Table
public_rt = ec2.RouteTable('fitflow-public-rt',
    vpc_id=vpc.id,
    tags=get_tags('Public-RT')
)

# Public Route to Internet
public_route = ec2.Route('fitflow-public-route',
    route_table_id=public_rt.id,
    destination_cidr_block='0.0.0.0/0',
    gateway_id=igw.id
)

# Associate Public Subnets with Public Route Table
for i, subnet in enumerate(public_subnets):
    ec2.RouteTableAssociation(f'fitflow-public-rta-{i+1}',
        subnet_id=subnet.id,
        route_table_id=public_rt.id
    )

# Elastic IP for NAT Gateway
nat_eip = ec2.Eip('fitflow-nat-eip',
    domain='vpc',
    tags=get_tags('NAT-EIP')
)

# NAT Gateway (in first public subnet)
nat_gw = ec2.NatGateway('fitflow-nat-gateway',
    subnet_id=public_subnets[0].id,
    allocation_id=nat_eip.id,
    tags=get_tags('NAT-Gateway')
)

# Private Route Table
private_rt = ec2.RouteTable('fitflow-private-rt',
    vpc_id=vpc.id,
    tags=get_tags('Private-RT')
)

# Private Route to NAT
private_route = ec2.Route('fitflow-private-route',
    route_table_id=private_rt.id,
    destination_cidr_block='0.0.0.0/0',
    nat_gateway_id=nat_gw.id
)

# Associate Private Subnets with Private Route Table
for i, subnet in enumerate(private_subnets):
    ec2.RouteTableAssociation(f'fitflow-private-rta-{i+1}',
        subnet_id=subnet.id,
        route_table_id=private_rt.id
    )