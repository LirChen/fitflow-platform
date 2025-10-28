"""
Security Groups for EKS
"""
import pulumi
from pulumi_aws import ec2
from config import get_tags
from vpc import vpc
from config import VPC_CIDR

# EKS Security Group
eks_sg = ec2.SecurityGroup('fitflow-eks-sg',
    vpc_id=vpc.id,
    description='Security group for EKS cluster',
    tags=get_tags('EKS-SG')
)

# Allow inbound traffic for Kubernetes API server
eks_api_ingress = ec2.SecurityGroupRule('fitflow-eks-api-ingress',
    security_group_id=eks_sg.id,
    type='ingress',
    from_port=443,
    to_port=443,
    protocol='tcp',
    cidr_blocks=[VPC_CIDR] 
)

# Allow all outbound traffic
eks_egress = ec2.SecurityGroupRule('fitflow-eks-egress',        
    security_group_id=eks_sg.id,
    type='egress',
    from_port=0,
    to_port=0,
    protocol='-1',
    cidr_blocks=['0.0.0.0/0']
)

eks_node_sg = ec2.SecurityGroup('fitflow-eks-node-sg',
    vpc_id=vpc.id,
    description='Security group for EKS nodes',
    tags=get_tags('EKS-Node-SG')
)

# Allow inbound traffic from EKS cluster to nodes
node_to_node = ec2.SecurityGroupRule('fitflow-node-to-node',
    security_group_id=eks_node_sg.id,
    type='ingress',
    from_port=0,
    to_port=65535,
    protocol='-1',
    source_security_group_id=eks_node_sg.id
)

# Allow inbound traffic from EKS cluster security group
cluster_to_node = ec2.SecurityGroupRule('fitflow-cluster-to-node',
    security_group_id=eks_node_sg.id,
    type='ingress',
    from_port=1025,
    to_port=65535,
    protocol='tcp',
    source_security_group_id=eks_sg.id
)

# Allow all outbound traffic from nodes
node_egress = ec2.SecurityGroupRule('fitflow-node-egress',
    security_group_id=eks_node_sg.id,
    type='egress',
    from_port=0,
    to_port=0,
    protocol='-1',
    cidr_blocks=['0.0.0.0/0']
)

# Allow cluster to recieve traffic from nodes
cluster_ingress = ec2.SecurityGroupRule('fitflow-cluster-ingress',
    security_group_id=eks_sg.id,
    type='ingress',
    from_port=443,
    to_port=443,
    protocol='tcp',
    source_security_group_id=eks_node_sg.id
)
