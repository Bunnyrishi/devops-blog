#!/usr/bin/env python3
import os

# Template for blog posts
blog_template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | DevOps Mastery</title>
    <meta name="description" content="{description}">
    <link rel="stylesheet" href="../css/style.css">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
</head>
<body>
    <div class="blog-post">
        <a href="../index.html" class="back-button">
            <i class="fas fa-arrow-left"></i> Back to Blog
        </a>
        
        <article>
            <header class="blog-post-header">
                <h1 class="blog-post-title">{title}</h1>
                <div class="blog-post-meta">
                    <span><i class="fas fa-calendar"></i> January 15, 2025</span>
                    <span><i class="fas fa-clock"></i> {read_time} min read</span>
                    <span><i class="fas fa-tag"></i> {level}</span>
                </div>
            </header>
            
            <div class="blog-post-content">
                <div class="highlight-box">
                    <h2>{emoji} What is {topic}?</h2>
                    <p>{intro_text}</p>
                </div>

                <blockquote>
                    "{quote}" - {quote_author}
                </blockquote>

                <h2>🎯 Key Concepts</h2>
                <div class="info-box">
                    <h3>Essential Points</h3>
                    <ul>
                        {key_points}
                    </ul>
                </div>

                <h2>⚙️ Essential Commands</h2>
                <pre><code>{commands}</code></pre>

                <h2>🏢 Best Practices</h2>
                <div class="highlight-box">
                    <h3>Professional Guidelines</h3>
                    <ul>
                        {best_practices}
                    </ul>
                </div>

                <h2>🎯 Conclusion</h2>
                <p>{conclusion}</p>

                <div class="info-box">
                    <p><strong>Next Steps:</strong> {next_steps}</p>
                </div>
            </div>
        </article>
    </div>
</body>
</html>'''

# Blog configurations
blogs_config = {
    # Missing beginner blogs (need 9 total, have 9, so 0 missing)
    
    # Missing intermediate blogs (need 9 total, have some, need to check)
    "jenkins-advanced-pipeline.html": {
        "title": "Advanced Jenkins CI/CD Pipelines",
        "description": "Master advanced Jenkins pipeline techniques, parallel execution, and enterprise deployment strategies",
        "level": "Intermediate",
        "read_time": "16",
        "emoji": "🔧",
        "topic": "Advanced Jenkins",
        "intro_text": "Advanced Jenkins pipelines enable <strong>sophisticated CI/CD workflows</strong> with parallel execution, conditional logic, and enterprise-grade deployment strategies for complex applications.",
        "quote": "Advanced pipelines are the backbone of enterprise DevOps automation.",
        "quote_author": "Jenkins Community",
        "key_points": '''<li><strong>Pipeline as Code:</strong> Declarative and scripted pipelines</li>
                        <li><strong>Parallel Execution:</strong> Multi-stage parallel builds</li>
                        <li><strong>Conditional Logic:</strong> Dynamic pipeline behavior</li>
                        <li><strong>Enterprise Integration:</strong> LDAP, RBAC, and security</li>
                        <li><strong>Blue-Green Deployment:</strong> Zero-downtime deployments</li>''',
        "commands": '''# Advanced Jenkinsfile
pipeline {
    agent any
    stages {
        stage('Parallel Tests') {
            parallel {
                stage('Unit Tests') {
                    steps { sh 'npm test' }
                }
                stage('Integration Tests') {
                    steps { sh 'npm run test:integration' }
                }
            }
        }
    }
}''',
        "best_practices": '''<li><strong>Pipeline Libraries:</strong> Shared pipeline code</li>
                            <li><strong>Security Scanning:</strong> Automated vulnerability checks</li>
                            <li><strong>Artifact Management:</strong> Proper versioning and storage</li>
                            <li><strong>Monitoring:</strong> Pipeline performance tracking</li>''',
        "conclusion": "Advanced Jenkins pipelines provide <strong>enterprise-grade automation</strong> for complex deployment scenarios.",
        "next_steps": "Implement shared libraries, security scanning, and monitoring for production-ready pipelines."
    },
    
    "ansible-automation.html": {
        "title": "Ansible Automation & Configuration Management",
        "description": "Automate infrastructure provisioning and configuration management with Ansible playbooks and best practices",
        "level": "Intermediate", 
        "read_time": "18",
        "emoji": "🤖",
        "topic": "Ansible Automation",
        "intro_text": "Ansible is a <strong>powerful automation tool</strong> that simplifies configuration management, application deployment, and infrastructure provisioning through simple YAML playbooks.",
        "quote": "Ansible makes complex deployments simple and repeatable.",
        "quote_author": "Red Hat",
        "key_points": '''<li><strong>Agentless:</strong> No software installation on target machines</li>
                        <li><strong>Idempotent:</strong> Safe to run multiple times</li>
                        <li><strong>YAML Syntax:</strong> Human-readable configuration</li>
                        <li><strong>Inventory Management:</strong> Dynamic and static inventories</li>
                        <li><strong>Role-based:</strong> Reusable automation components</li>''',
        "commands": '''# Basic Ansible commands
ansible all -m ping
ansible-playbook site.yml
ansible-galaxy install geerlingguy.nginx

# Playbook example
- hosts: webservers
  tasks:
    - name: Install nginx
      yum: name=nginx state=present''',
        "best_practices": '''<li><strong>Version Control:</strong> Store playbooks in Git</li>
                            <li><strong>Testing:</strong> Use Molecule for playbook testing</li>
                            <li><strong>Secrets Management:</strong> Ansible Vault for sensitive data</li>
                            <li><strong>Documentation:</strong> Clear playbook documentation</li>''',
        "conclusion": "Ansible automation enables <strong>consistent and reliable infrastructure management</strong> at scale.",
        "next_steps": "Create reusable roles, implement testing with Molecule, and integrate with CI/CD pipelines."
    },

    "helm-kubernetes-packages.html": {
        "title": "Helm - Kubernetes Package Manager",
        "description": "Master Helm charts for Kubernetes application packaging, templating, and deployment management",
        "level": "Intermediate",
        "read_time": "15",
        "emoji": "⛵",
        "topic": "Helm",
        "intro_text": "Helm is the <strong>package manager for Kubernetes</strong> that simplifies application deployment through templated charts and release management.",
        "quote": "Helm makes Kubernetes applications as easy to install as mobile apps.",
        "quote_author": "CNCF",
        "key_points": '''<li><strong>Charts:</strong> Packaged Kubernetes applications</li>
                        <li><strong>Templates:</strong> Dynamic YAML generation</li>
                        <li><strong>Releases:</strong> Versioned deployments</li>
                        <li><strong>Repositories:</strong> Chart distribution</li>
                        <li><strong>Hooks:</strong> Lifecycle management</li>''',
        "commands": '''# Helm commands
helm create mychart
helm install myapp ./mychart
helm upgrade myapp ./mychart
helm rollback myapp 1
helm list
helm repo add stable https://charts.helm.sh/stable''',
        "best_practices": '''<li><strong>Chart Structure:</strong> Follow Helm best practices</li>
                            <li><strong>Values Files:</strong> Environment-specific configurations</li>
                            <li><strong>Testing:</strong> Helm test for validation</li>
                            <li><strong>Security:</strong> Chart signing and verification</li>''',
        "conclusion": "Helm streamlines <strong>Kubernetes application lifecycle management</strong> with powerful packaging capabilities.",
        "next_steps": "Create custom charts, implement CI/CD integration, and establish chart repositories."
    },

    # Missing advanced blogs
    "microservices-architecture.html": {
        "title": "Microservices Architecture & Design Patterns",
        "description": "Design and implement scalable microservices architectures with modern patterns and best practices",
        "level": "Advanced",
        "read_time": "20",
        "emoji": "🏗️",
        "topic": "Microservices Architecture",
        "intro_text": "Microservices architecture enables <strong>scalable, maintainable applications</strong> through distributed services that communicate via well-defined APIs.",
        "quote": "Microservices are not a silver bullet, but they solve real problems at scale.",
        "quote_author": "Martin Fowler",
        "key_points": '''<li><strong>Service Decomposition:</strong> Domain-driven design principles</li>
                        <li><strong>API Gateway:</strong> Centralized routing and security</li>
                        <li><strong>Service Mesh:</strong> Inter-service communication</li>
                        <li><strong>Data Management:</strong> Database per service pattern</li>
                        <li><strong>Observability:</strong> Distributed tracing and monitoring</li>''',
        "commands": '''# Docker Compose microservices
version: '3.8'
services:
  api-gateway:
    image: nginx:alpine
    ports: ["80:80"]
  user-service:
    build: ./user-service
  order-service:
    build: ./order-service''',
        "best_practices": '''<li><strong>Circuit Breaker:</strong> Fault tolerance patterns</li>
                            <li><strong>Event Sourcing:</strong> Audit trail and replay capability</li>
                            <li><strong>CQRS:</strong> Command Query Responsibility Segregation</li>
                            <li><strong>Security:</strong> Zero-trust architecture</li>''',
        "conclusion": "Microservices architecture provides <strong>scalability and flexibility</strong> for enterprise applications.",
        "next_steps": "Implement service mesh, establish monitoring, and design resilience patterns."
    },

    "service-mesh-istio.html": {
        "title": "Service Mesh with Istio - Advanced Networking",
        "description": "Implement advanced service mesh capabilities with Istio for microservices communication and security",
        "level": "Advanced",
        "read_time": "22",
        "emoji": "🕸️",
        "topic": "Service Mesh",
        "intro_text": "Istio service mesh provides <strong>advanced networking capabilities</strong> for microservices including traffic management, security, and observability.",
        "quote": "Service mesh is the infrastructure layer for microservices communication.",
        "quote_author": "Istio Team",
        "key_points": '''<li><strong>Traffic Management:</strong> Load balancing and routing</li>
                        <li><strong>Security:</strong> mTLS and policy enforcement</li>
                        <li><strong>Observability:</strong> Metrics, logs, and tracing</li>
                        <li><strong>Policy Enforcement:</strong> Rate limiting and access control</li>
                        <li><strong>Fault Injection:</strong> Chaos engineering capabilities</li>''',
        "commands": '''# Istio installation
istioctl install --set values.defaultRevision=default
kubectl label namespace default istio-injection=enabled

# Virtual Service
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: reviews
spec:
  http:
  - route:
    - destination:
        host: reviews''',
        "best_practices": '''<li><strong>Gradual Rollout:</strong> Canary deployments with traffic splitting</li>
                            <li><strong>Security Policies:</strong> Zero-trust networking</li>
                            <li><strong>Performance:</strong> Optimize sidecar resource usage</li>
                            <li><strong>Monitoring:</strong> Comprehensive observability setup</li>''',
        "conclusion": "Istio service mesh enables <strong>enterprise-grade microservices networking</strong> with advanced capabilities.",
        "next_steps": "Implement advanced traffic policies, security configurations, and observability dashboards."
    },

    "gitops-argocd.html": {
        "title": "GitOps with ArgoCD - Declarative Deployments",
        "description": "Implement GitOps workflows with ArgoCD for automated, declarative Kubernetes deployments",
        "level": "Advanced",
        "read_time": "19",
        "emoji": "🔄",
        "topic": "GitOps",
        "intro_text": "GitOps with ArgoCD enables <strong>declarative deployment workflows</strong> where Git repositories serve as the single source of truth for infrastructure and applications.",
        "quote": "GitOps is the path to more secure, compliant, and auditable deployments.",
        "quote_author": "Weaveworks",
        "key_points": '''<li><strong>Declarative:</strong> Desired state in Git repositories</li>
                        <li><strong>Automated:</strong> Continuous deployment and sync</li>
                        <li><strong>Auditable:</strong> Complete deployment history</li>
                        <li><strong>Secure:</strong> Pull-based deployment model</li>
                        <li><strong>Rollback:</strong> Easy reversion to previous states</li>''',
        "commands": '''# ArgoCD CLI
argocd app create myapp --repo https://github.com/user/repo --path manifests --dest-server https://kubernetes.default.svc
argocd app sync myapp
argocd app get myapp
argocd app rollback myapp

# Application manifest
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: myapp''',
        "best_practices": '''<li><strong>Repository Structure:</strong> Separate app and config repos</li>
                            <li><strong>RBAC:</strong> Role-based access control</li>
                            <li><strong>Multi-cluster:</strong> Centralized management</li>
                            <li><strong>Secrets Management:</strong> External secret operators</li>''',
        "conclusion": "GitOps with ArgoCD provides <strong>reliable and auditable deployment workflows</strong> for Kubernetes.",
        "next_steps": "Implement multi-cluster management, RBAC policies, and automated secret management."
    },

    "devsecops-security.html": {
        "title": "DevSecOps - Security in CI/CD Pipelines",
        "description": "Integrate security practices into DevOps workflows with automated scanning and compliance",
        "level": "Advanced",
        "read_time": "21",
        "emoji": "🔒",
        "topic": "DevSecOps",
        "intro_text": "DevSecOps integrates <strong>security practices throughout the development lifecycle</strong>, making security everyone's responsibility with automated tools and processes.",
        "quote": "Security is not a feature, it's a foundation that must be built into every process.",
        "quote_author": "DevSecOps Community",
        "key_points": '''<li><strong>Shift Left:</strong> Early security integration</li>
                        <li><strong>Automated Scanning:</strong> SAST, DAST, and SCA tools</li>
                        <li><strong>Compliance:</strong> Automated policy enforcement</li>
                        <li><strong>Secrets Management:</strong> Secure credential handling</li>
                        <li><strong>Threat Modeling:</strong> Proactive security assessment</li>''',
        "commands": '''# Security scanning pipeline
stages:
  - security-scan:
      script:
        - trivy image myapp:latest
        - sonarqube-scanner
        - snyk test
        - checkov -f Dockerfile
      only:
        - merge_requests''',
        "best_practices": '''<li><strong>Zero Trust:</strong> Never trust, always verify</li>
                            <li><strong>Least Privilege:</strong> Minimal access rights</li>
                            <li><strong>Continuous Monitoring:</strong> Runtime security</li>
                            <li><strong>Incident Response:</strong> Automated security workflows</li>''',
        "conclusion": "DevSecOps ensures <strong>security is built into every aspect</strong> of the development and deployment process.",
        "next_steps": "Implement comprehensive security scanning, establish incident response procedures, and create security metrics."
    },

    "chaos-engineering.html": {
        "title": "Chaos Engineering - Building Resilient Systems",
        "description": "Implement chaos engineering practices to build resilient, fault-tolerant distributed systems",
        "level": "Advanced",
        "read_time": "18",
        "emoji": "🌪️",
        "topic": "Chaos Engineering",
        "intro_text": "Chaos engineering is the <strong>discipline of experimenting on distributed systems</strong> to build confidence in system resilience and discover weaknesses before they cause outages.",
        "quote": "Chaos engineering is not about breaking things, it's about learning how things break.",
        "quote_author": "Netflix",
        "key_points": '''<li><strong>Hypothesis-driven:</strong> Scientific approach to testing</li>
                        <li><strong>Controlled Experiments:</strong> Safe failure injection</li>
                        <li><strong>Blast Radius:</strong> Limited scope of experiments</li>
                        <li><strong>Observability:</strong> Comprehensive monitoring during tests</li>
                        <li><strong>Automation:</strong> Continuous chaos testing</li>''',
        "commands": '''# Chaos Monkey example
chaosmonkey:
  enabled: true
  schedule: "0 10 * * MON-FRI"
  
# Litmus chaos experiment
apiVersion: litmuschaos.io/v1alpha1
kind: ChaosEngine
metadata:
  name: pod-delete
spec:
  experiments:
  - name: pod-delete''',
        "best_practices": '''<li><strong>Start Small:</strong> Begin with non-critical systems</li>
                            <li><strong>Game Days:</strong> Scheduled chaos exercises</li>
                            <li><strong>Runbooks:</strong> Documented response procedures</li>
                            <li><strong>Culture:</strong> Blameless post-mortem culture</li>''',
        "conclusion": "Chaos engineering builds <strong>confidence in system resilience</strong> through controlled failure experiments.",
        "next_steps": "Implement chaos experiments, establish monitoring, and create incident response procedures."
    },

    "platform-engineering.html": {
        "title": "Platform Engineering - Internal Developer Platforms",
        "description": "Build internal developer platforms to improve developer experience and operational efficiency",
        "level": "Advanced",
        "read_time": "23",
        "emoji": "🏭",
        "topic": "Platform Engineering",
        "intro_text": "Platform engineering focuses on <strong>building internal developer platforms</strong> that provide self-service capabilities and improve developer productivity while maintaining operational excellence.",
        "quote": "Platform engineering is about creating the golden path for developers.",
        "quote_author": "Platform Engineering Community",
        "key_points": '''<li><strong>Self-Service:</strong> Developer autonomy and speed</li>
                        <li><strong>Golden Path:</strong> Opinionated, supported workflows</li>
                        <li><strong>Abstraction:</strong> Hide infrastructure complexity</li>
                        <li><strong>Standards:</strong> Consistent tooling and practices</li>
                        <li><strong>Observability:</strong> Platform and application metrics</li>''',
        "commands": '''# Platform API example
kubectl apply -f - <<EOF
apiVersion: platform.io/v1
kind: Application
metadata:
  name: myapp
spec:
  runtime: nodejs
  replicas: 3
  database: postgresql
EOF''',
        "best_practices": '''<li><strong>Product Mindset:</strong> Treat platform as a product</li>
                            <li><strong>Developer Experience:</strong> Focus on usability</li>
                            <li><strong>Gradual Adoption:</strong> Incremental platform rollout</li>
                            <li><strong>Feedback Loops:</strong> Continuous improvement</li>''',
        "conclusion": "Platform engineering creates <strong>scalable developer experiences</strong> that accelerate delivery while maintaining quality.",
        "next_steps": "Design platform APIs, implement self-service capabilities, and establish developer feedback mechanisms."
    }
}

def create_missing_blogs():
    """Create missing blog files"""
    posts_dir = "posts"
    
    if not os.path.exists(posts_dir):
        os.makedirs(posts_dir)
    
    for filename, config in blogs_config.items():
        filepath = os.path.join(posts_dir, filename)
        
        if not os.path.exists(filepath):
            print(f"Creating {filename}...")
            
            content = blog_template.format(**config)
            
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(content)
            
            print(f"Created {filename}")
        else:
            print(f"Skipping {filename} - already exists")

if __name__ == "__main__":
    create_missing_blogs()
    print("Missing blog creation completed!")