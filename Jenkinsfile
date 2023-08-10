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
        
        // stage('Build Docker Image') {
        //     steps {
        //         script {
        //             def dockerImage = docker.build("sriram21ey/myapp:${v1}")
        //         }
        //     }
        // }
        
        stage('Deploy to Kubernetes') {
            steps {
                script {
                    //def kubeconfig = credentials('kubeconfig')
                    
                    sh "kubectl apply -f namespace.yml"
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
