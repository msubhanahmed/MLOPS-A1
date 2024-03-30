pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the main branch of the Git repository
                git branch: 'main', url: 'https://github.com/msubhanahmed/MLOPS-A1.git'
            }
        }
        
        stage('Checkout Dockerfile Branch') {
            steps {
                // Checkout the branch containing the Dockerfile
                git branch: 'test', url: 'https://github.com/msubhanahmed/MLOPS-A1.git'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    dockerImage = docker.build('jawad-151/price-prediction')
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
    
    post {
        success {
            emailext (
                to: 'mjjawad285@gmail.com',
                subject: "Pipeline Successful",
                body: "Your pipeline has completed successfully.",
            )
        }
    }
}
