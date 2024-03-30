pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the main branch of the Git repository
                git branch: 'main', url: 'https://github.com/msubhanahmed/MLOPS-A1.git'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    dockerImage = docker.build('jawad151/price-predictor')
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    // Login to Docker Hub
                    docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials-id') {
                        dockerImage.push("${env.BUILD_NUMBER}")
                        dockerImage.push("latest") 
                    }
                }
            }
        }
    }
}
