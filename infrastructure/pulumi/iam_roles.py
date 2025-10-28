"""
IAM Roles for EKS Cluster and Nodes
"""
import pulumi
from pulumi_aws import iam
import json
from config import get_tags

# EKS Cluster Role
eks_cluster_role = iam.Role('fitflow-eks-cluster-role',
    assume_role_policy=json.dumps({
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Principal": {"Service": "eks.amazonaws.com"},
            "Action": "sts:AssumeRole"
        }]
    }),
    tags=get_tags('EKS-Cluster-Role')
)

# Attach AWS managed policy to cluster role
eks_cluster_policy = iam.RolePolicyAttachment('fitflow-eks-cluster-policy',
    role=eks_cluster_role.name,
    policy_arn='arn:aws:iam::aws:policy/AmazonEKSClusterPolicy'
)

# EKS Node Role
eks_node_role = iam.Role('fitflow-eks-node-role',
    assume_role_policy=json.dumps({
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Principal": {"Service": "ec2.amazonaws.com"},
            "Action": "sts:AssumeRole"
        }]
    }),
    tags=get_tags('EKS-Node-Role')
)

# Attach policies to node role
eks_worker_node_policy = iam.RolePolicyAttachment('fitflow-eks-worker-node-policy',
    role=eks_node_role.name,
    policy_arn="arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy"
)

ecr_readonly_policy = iam.RolePolicyAttachment('fitflow-ecr-readonly-policy',
    role=eks_node_role.name,
    policy_arn="arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly"
)

eks_cni_policy = iam.RolePolicyAttachment('fitflow-eks-cni-policy',
    role=eks_node_role.name,
    policy_arn="arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy"
)