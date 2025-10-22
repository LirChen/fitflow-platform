"""
Configuration for FitFlow Platform
"""

# Project settings
PROJECT_NAME = "FitFlow"
ENVIRONMENT = "dev"

# Network settings
VPC_CIDR = "10.0.0.0/16"
AVAILABILITY_ZONES = ["us-east-1a", "us-east-1b"]

# Subnet CIDRs
PUBLIC_SUBNET_CIDRS = ["10.0.1.0/24", "10.0.3.0/24"]
PRIVATE_SUBNET_CIDRS = ["10.0.2.0/24", "10.0.4.0/24"]

# Tags
def get_tags(name: str) -> dict:
    """Generate standard tags for resources"""
    return {
        'Name': f'{PROJECT_NAME}-{name}',
        'Project': PROJECT_NAME,
        'Environment': ENVIRONMENT,
        'ManagedBy': 'Pulumi'
    }