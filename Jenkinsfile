pipeline {
    agent {
        docker {
            image 'python:3.9-slim'
        }
    }

    environment {
        EC2_HOST = '54.234.136.145'        // Your EC2 IP
        EC2_USER = 'ec2-user'              // Your EC2 username
        IMAGE = 'samvelll/flask-app:latest' // Your Docker image name
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Sammm333/jenkins-pipeline-flask.git'  // ✔️ Correct repo URL
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'python -m unittest'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t $IMAGE ."
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    sh "echo $PASSWORD | docker login -u $USERNAME --password-stdin"
                    sh "docker push $IMAGE"
                }
            }
        }

        stage('Deploy to Server') {
            steps {
                sshagent(['ec2-ssh-key']) {
                    sh """
                        ssh $EC2_USER@$EC2_HOST '
                        docker pull $IMAGE &&
                        docker stop flask || true &&
                        docker rm flask || true &&
                        docker run -d --name flask -p 80:5000 $IMAGE
                        '
                    """
                }
            }
        }
    }
}
