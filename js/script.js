// Blog posts data
const blogPosts = [
    {
        id: 1,
        title: "Getting Started with DevOps: A Complete Beginner's Guide",
        excerpt: "Learn the fundamentals of DevOps culture, practices, and tools. Perfect starting point for your DevOps journey.",
        level: "Beginner",
        readTime: "8 min",
        date: "2025-01-15",
        filename: "getting-started-devops"
    },
    {
        id: 2,
        title: "Introduction to Version Control with Git",
        excerpt: "Master Git basics, branching strategies, and collaborative workflows essential for any DevOps engineer.",
        level: "Beginner",
        readTime: "10 min",
        date: "2025-01-14",
        filename: "git-version-control"
    },
    {
        id: 3,
        title: "Linux Fundamentals for DevOps Engineers",
        excerpt: "Essential Linux commands, file systems, and administration skills every DevOps professional needs.",
        level: "Beginner",
        readTime: "12 min",
        date: "2025-01-13",
        filename: "linux-fundamentals"
    },
    {
        id: 4,
        title: "Docker Containerization: From Basics to Production",
        excerpt: "Complete Docker guide covering containers, images, volumes, networks, and best practices.",
        level: "Intermediate",
        readTime: "15 min",
        date: "2025-01-12",
        filename: "docker-containerization"
    },
    {
        id: 5,
        title: "AWS Cloud Fundamentals for DevOps",
        excerpt: "Essential AWS services including EC2, S3, VPC, IAM, and CloudWatch for DevOps workflows.",
        level: "Beginner",
        readTime: "14 min",
        date: "2025-01-11",
        filename: "aws-cloud-fundamentals"
    },
    {
        id: 6,
        title: "CI/CD Pipeline Implementation with Jenkins",
        excerpt: "Build automated CI/CD pipelines using Jenkins, including setup, configuration, and best practices.",
        level: "Intermediate",
        readTime: "18 min",
        date: "2025-01-10",
        filename: "jenkins-cicd-pipeline"
    },
    {
        id: 7,
        title: "Infrastructure as Code with Terraform",
        excerpt: "Learn Terraform basics, resource management, state files, and infrastructure automation.",
        level: "Intermediate",
        readTime: "16 min",
        date: "2025-01-09",
        filename: "terraform-infrastructure-code"
    },
    {
        id: 8,
        title: "Kubernetes Orchestration: Complete Guide",
        excerpt: "Master Kubernetes concepts, deployments, services, ingress, and cluster management.",
        level: "Intermediate",
        readTime: "20 min",
        date: "2025-01-08",
        filename: "kubernetes-orchestration"
    },
    {
        id: 9,
        title: "Monitoring and Logging with Prometheus & Grafana",
        excerpt: "Implement comprehensive monitoring solutions using Prometheus, Grafana, and AlertManager.",
        level: "Intermediate",
        readTime: "17 min",
        date: "2025-01-07",
        filename: "prometheus-grafana-monitoring"
    },
    {
        id: 10,
        title: "Azure DevOps: Complete CI/CD Solution",
        excerpt: "Build end-to-end CI/CD pipelines using Azure DevOps, including repos, pipelines, and artifacts.",
        level: "Intermediate",
        readTime: "19 min",
        date: "2025-01-06",
        filename: "azure-devops-cicd"
    },
    {
        id: 11,
        title: "Docker Compose for Multi-Container Applications",
        excerpt: "Orchestrate multi-container applications using Docker Compose with real-world examples.",
        level: "Intermediate",
        readTime: "13 min",
        date: "2025-01-05",
        filename: "docker-compose-applications"
    },
    {
        id: 12,
        title: "AWS ECS and ECR: Container Management",
        excerpt: "Deploy and manage containerized applications using AWS ECS, ECR, and Fargate.",
        level: "Intermediate",
        readTime: "16 min",
        date: "2025-01-04",
        filename: "aws-ecs-ecr-containers"
    },
    {
        id: 13,
        title: "GitLab CI/CD: Modern DevOps Workflows",
        excerpt: "Implement GitOps workflows using GitLab CI/CD with automated testing and deployment.",
        level: "Intermediate",
        readTime: "15 min",
        date: "2025-01-03",
        filename: "gitlab-cicd-workflows"
    },
    {
        id: 14,
        title: "Helm Charts: Kubernetes Package Management",
        excerpt: "Simplify Kubernetes deployments using Helm charts, templates, and package management.",
        level: "Intermediate",
        readTime: "14 min",
        date: "2025-01-02",
        filename: "helm-kubernetes-packages"
    },
    {
        id: 15,
        title: "Security Best Practices in DevOps (DevSecOps)",
        excerpt: "Integrate security into DevOps workflows with scanning, compliance, and secure practices.",
        level: "Intermediate",
        readTime: "18 min",
        date: "2025-01-01",
        filename: "devsecops-security-practices"
    },
    {
        id: 16,
        title: "Multi-Cloud Strategy and Implementation",
        excerpt: "Design and implement multi-cloud architectures across AWS, Azure, and GCP.",
        level: "Advanced",
        readTime: "22 min",
        date: "2024-12-31",
        filename: "multi-cloud-strategy"
    },
    {
        id: 17,
        title: "Advanced Kubernetes: Service Mesh with Istio",
        excerpt: "Implement service mesh architecture using Istio for microservices communication and security.",
        level: "Advanced",
        readTime: "25 min",
        date: "2024-12-30",
        filename: "kubernetes-istio-service-mesh"
    },
    {
        id: 18,
        title: "Serverless DevOps with AWS Lambda",
        excerpt: "Build serverless CI/CD pipelines and applications using AWS Lambda and serverless framework.",
        level: "Intermediate",
        readTime: "17 min",
        date: "2024-12-29",
        filename: "serverless-aws-lambda"
    },
    {
        id: 19,
        title: "Advanced Terraform: Modules and State Management",
        excerpt: "Master advanced Terraform concepts including modules, remote state, and enterprise patterns.",
        level: "Advanced",
        readTime: "21 min",
        date: "2024-12-28",
        filename: "advanced-terraform-modules"
    },
    {
        id: 20,
        title: "DevOps Career Path: Skills and Certifications",
        excerpt: "Complete roadmap for DevOps career growth, essential skills, and valuable certifications.",
        level: "Beginner",
        readTime: "12 min",
        date: "2024-12-27",
        filename: "devops-career-path"
    }
];

// Load blog posts on page load
document.addEventListener('DOMContentLoaded', function() {
    loadBlogPosts();
    initCategoryFilters();
});

function loadBlogPosts() {
    const blogGrid = document.getElementById('blogGrid');
    if (!blogGrid) return;

    blogGrid.innerHTML = '';
    
    // Load all posts initially
    blogPosts.forEach(post => {
        const blogCard = createBlogCard(post);
        blogGrid.appendChild(blogCard);
    });
}

function initCategoryFilters() {
    const filterButtons = document.querySelectorAll('.filter-btn');
    
    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Remove active class from all buttons
            filterButtons.forEach(btn => btn.classList.remove('active'));
            
            // Add active class to clicked button
            this.classList.add('active');
            
            // Filter posts
            const category = this.getAttribute('data-category');
            filterPosts(category);
        });
    });
}

function filterPosts(category) {
    const blogCards = document.querySelectorAll('.blog-card');
    
    blogCards.forEach(card => {
        if (category === 'all') {
            card.classList.remove('hidden');
        } else {
            const cardLevel = card.querySelector('.blog-level').textContent.toLowerCase();
            if (cardLevel === category) {
                card.classList.remove('hidden');
            } else {
                card.classList.add('hidden');
            }
        }
    });
}

function createBlogCard(post) {
    const card = document.createElement('div');
    card.className = 'blog-card';
    card.onclick = () => openBlogPost(post.filename);
    
    const levelClass = post.level.toLowerCase();
    card.setAttribute('data-category', levelClass);
    
    card.innerHTML = `
        <div class="blog-card-header">
            <span class="blog-level ${levelClass}">${post.level}</span>
            <h3>${post.title}</h3>
        </div>
        <div class="blog-card-body">
            <p>${post.excerpt}</p>
            <div class="blog-meta">
                <span class="blog-date">${formatDate(post.date)}</span>
                <span class="read-time">
                    <i class="fas fa-clock"></i>
                    ${post.readTime} read
                </span>
            </div>
        </div>
    `;
    
    return card;
}

function formatDate(dateString) {
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    return new Date(dateString).toLocaleDateString('en-US', options);
}

function openBlogPost(filename) {
    window.open(`posts/${filename}.html`, '_blank');
}

// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});