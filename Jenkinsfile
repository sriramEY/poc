pipeline {
    agent any
    
    stages {

        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build Docker Image') {
            steps {
                sh '''
                   docker pull sriram21ey/myapp:v1
                   docker images
                '''
            }
        }
        
        // stage('Deploy to Kubernetes') {                    docker build -t sriram21ey/myapp:v2 .

        //     steps {
        //         script {
        //             //def kubeconfig = credentials('kubeconfig')
                    
        //             sh "kubectl apply -f namespace.yml"
        //         }
        //     }
        // }
    }
    
    post {
        always {
            cleanWs()
        }
    }
}
