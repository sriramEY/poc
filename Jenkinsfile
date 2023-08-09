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
                kubernetesDeploy(
                    kubeconfigId: 'kubeconfig',
                    configs: 'deployment.yaml',
                    enableConfigSubstitution: true,
                    namespace: 'python-k8s-poc'
                    // secretName: '',
                    // secretNamespace: ''
                )
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
    }
}
