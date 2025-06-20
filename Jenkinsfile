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
                sh 'pip install -r Practice-Project---Cellpay/requirements.txt'
            }
        }

        stage('Run Flask App') {
            steps {
                sh 'nohup python3 Practice-Project---Cellpay/app.py &'
            }
        }

        stage('Docker Build') {
            steps {
                dir('Practice-Project---Cellpay') {
                    script {
                        echo "Building Docker Image..."
                        sh 'docker build -t cellpay-app .'
                    }
                }
            }
        }
    }
}
