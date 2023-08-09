pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    def dockerImage = docker.build("sriram21ey/myapp:v1")
                }
            }
        }
        
        stage('Deploy to Kubernetes') {
            steps {
                script {
                    def kubeconfig = credentials('kubeconfig')
                    
                    sh "kubectl --kubeconfig=$kubeconfig apply -f deployment.yaml"
                }
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
    }
}
