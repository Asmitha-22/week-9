pipeline {
    agent any
    stages {
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t registration:v1 .'
            }
        }
        stage('Push to Docker Hub') {
            steps {
                bat 'docker tag registration:v1 asmithayarkala/registration:v1'
                bat 'docker push asmithayarkala/registration:v1'
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                bat 'kubectl apply -f deployment.yaml'
                bat 'kubectl apply -f service.yaml'
            }
        }
        stage('Automated UI Test') {
            steps {
                bat 'python D:/DevOps/week-2/test_registration.py'
            }
        }
    }
}


