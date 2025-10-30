"""
EKS Cluster
"""
import pulumi
from pulumi_aws import eks
from config import get_tags
from vpc import private_subnets  
from iam_roles import eks_cluster_role, eks_node_role 
from security_groups import eks_sg

# EKS Cluster
eks_cluster = eks.Cluster('fitflow-eks',
    role_arn=eks_cluster_role.arn, 
    vpc_config={
        'subnet_ids': [s.id for s in private_subnets], 
        'security_group_ids': [eks_sg.id],
        'endpoint_private_access': True,
        'endpoint_public_access': True 
    },
    version='1.31', 
    tags=get_tags('EKS-Cluster')
)

pulumi.export('eks_cluster_name', eks_cluster.name)
pulumi.export('eks_cluster_endpoint', eks_cluster.endpoint)

# EKS Node Group
eks_node_group = eks.NodeGroup('fitflow-node-group',
    cluster_name=eks_cluster.name,
    node_role_arn=eks_node_role.arn,
    subnet_ids=[s.id for s in private_subnets],
    instance_types=['t3.small'],
    capacity_type='ON_DEMAND',
    scaling_config={
        'desired_size': 2,
        'max_size': 4,  
        'min_size': 1
    },
    tags=get_tags('EKS-Node-Group')
)

pulumi.export('eks_node_group_id', eks_node_group.id)