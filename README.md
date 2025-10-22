# 🏗️ FitFlow Platform - DevOps Infrastructure Project

> **Status:** 🚧 Work in Progress

A production-ready cloud-native fitness application platform built with modern DevOps practices and Infrastructure as Code.

---

## 📋 Project Overview

This project demonstrates advanced DevOps skills by deploying the **FitFlow** application (React + Node.js) on AWS using:
- **Infrastructure as Code** (Pulumi)
- **Kubernetes** (EKS)
- **GitOps** workflows
- **Cloud-Native** tools and best practices

---

## 🎯 Project Goals

- Learn and implement **modern IaC tools** (Pulumi, Crossplane)
- Build **production-grade Kubernetes infrastructure** on AWS
- Implement **Platform Engineering** principles
- Integrate **event-driven architecture** (Kafka)
- Automate everything with **Argo Workflows**

---

## 🏗️ Current Progress

### ✅ Completed (Phase 1)

- [x] Project structure setup
- [x] Pulumi infrastructure initialized
- [x] Modular code architecture (config, vpc, outputs)
- [x] VPC networking design:
  - 2 Public Subnets (us-east-1a, us-east-1b)
  - 2 Private Subnets (us-east-1a, us-east-1b)
  - Internet Gateway
  - NAT Gateway
  - Route Tables with proper associations

### 🚧 In Progress (Phase 2)

- [ ] EKS Cluster setup
- [ ] Karpenter for intelligent autoscaling
- [ ] Security Groups configuration
- [ ] IAM roles and policies

### 📅 Planned

**Phase 3: Kubernetes Tooling**
- [ ] Crossplane installation
- [ ] Kafka deployment (Strimzi Operator)
- [ ] Argo Workflows for CI/CD

**Phase 4: Application Deployment**
- [ ] Helm chart for FitFlow app
- [ ] Integration with Kafka for events
- [ ] Load Balancer and Ingress setup

**Phase 5: Observability & Monitoring**
- [ ] Prometheus + Grafana
- [ ] Logging (ELK/Loki)
- [ ] Alerting setup

---

## 🛠️ Technology Stack

### Infrastructure
- **Cloud Provider:** AWS
- **IaC Tool:** Pulumi (Python)
- **Container Orchestration:** Kubernetes (EKS)
- **Autoscaling:** Karpenter
- **Cloud Resource Management:** Crossplane

### Application
- **Frontend:** React + Vite
- **Backend:** Node.js + Express
- **Database:** MongoDB Atlas
- **Containerization:** Docker

### DevOps Tools
- **GitOps:** ArgoCD
- **CI/CD:** Argo Workflows
- **Messaging:** Apache Kafka (Strimzi)
- **Monitoring:** Prometheus + Grafana

---

## 📁 Project Structure
```
fitflow-platform/
├── app/                          # FitFlow Application
│   ├── client/                   # React frontend
│   ├── server/                   # Node.js backend
│   └── docker-compose.yml
│
├── infrastructure/               # Infrastructure as Code
│   └── pulumi/
│       ├── __main__.py          # Entry point
│       ├── config.py            # Global configuration
│       ├── vpc.py               # VPC & Networking
│       ├── outputs.py           # Export values
│       └── requirements.txt
│
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- AWS Account with $200 credits
- AWS CLI configured
- Pulumi CLI installed
- Python 3.8+
- kubectl
- helm

### Setup Infrastructure
```bash
cd infrastructure/pulumi

# Login to Pulumi (local backend)
pulumi login --local

# Preview infrastructure
pulumi preview

# Deploy infrastructure
pulumi up

# Destroy when done (save costs!)
pulumi destroy -y
```

---

## 💰 Cost Management

**Current Resources:**
- VPC, Subnets, IGW: **$0/month** (Free)
- NAT Gateway: **~$32/month** ($1/day) ⚠️

**Strategy:**
- Using `pulumi destroy` after each session
- Spot instances for EKS nodes
- Single NAT Gateway (not HA)
- Karpenter for aggressive scale-down

**Budget:** $200 AWS credits

---

## 📚 Learning Resources

- [Pulumi Documentation](https://www.pulumi.com/docs/)
- [AWS EKS Best Practices](https://aws.github.io/aws-eks-best-practices/)
- [Karpenter Documentation](https://karpenter.sh/)
- [Crossplane Documentation](https://crossplane.io/)
- [Argo Workflows](https://argoproj.github.io/workflows/)

---

## 🎓 Skills Demonstrated

- **Infrastructure as Code** - Pulumi with modular Python code
- **Cloud Networking** - VPC design with public/private subnets
- **Cost Optimization** - Smart resource management
- **Git Best Practices** - Structured commits, .gitignore, security
- **Documentation** - Clear README and code comments

---

## 👩‍💻 Author

**Lir Chen** - Junior DevOps Engineer

Learning by building! 🚀

---

## 📝 License

This project is for educational purposes.

---

## 🔄 Updates

- **2024-10-22:** Initial VPC infrastructure with Pulumi completed