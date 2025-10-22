"""
FitFlow Platform Infrastructure
Main entry point - imports all modules
"""
import pulumi

# Import all infrastructure modules
import config
import vpc
import outputs

# Print info
pulumi.log.info(f"Deploying {config.PROJECT_NAME} infrastructure in {config.ENVIRONMENT} environment")