pipeline {
    agent any

    stages {
        stage('Pull Code') {
            steps {
                git branch: 'main', url: 'https://github.com/itstechiepavan/Practice-Project---Cellpay.git'
            }
        }

        stage('Install Requirements') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Flask App') {
            steps {
                sh 'nohup python3 app.py &'
            }
        }

        stage('Docker Build') {
            steps {
                script {
                    echo "Building Docker Image..."
                    sh 'docker build -t cellpay-app .'
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    echo "Running Docker Container..."
                    // Optional: remove old container if already exists
                    sh 'docker rm -f cellpay-container || true'
                    // Start new container
                    sh 'docker run -d -p 5000:5000 --name cellpay-container cellpay-app'
                }
            }
        }
    }
}
