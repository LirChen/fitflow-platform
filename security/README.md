# Security Documentation

## 📁 Contents

- **VULNERABILITY_REPORT.md** - Current vulnerabilities and remediation guide
- **reports/** - Trivy scan results (JSON format)
- **policies/** - OPA policies (future)

## 🔄 Scan Schedule

- **Manual:** On-demand via `trivy image <image>`
- **Automated:** Weekly via GitHub Actions
- **Release:** Before every production deployment

## 🛠️ Quick Commands

\`\`\`bash
# Scan server
trivy image ofirlir/fitflow-server:latest

# Scan client
trivy image ofirlir/fitflow-client:latest

# Full report
trivy image --format json --output reports/scan.json ofirlir/fitflow-server:latest
\`\`\`