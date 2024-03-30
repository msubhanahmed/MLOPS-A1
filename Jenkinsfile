pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the main branch of the Git repository
                git branch: 'main', url: 'https://github.com/your-username/your-repo.git'
            }
        }
    }
}
