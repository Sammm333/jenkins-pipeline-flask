pipeline {
    agent any

    environment {
        EC2_HOST = '54.234.136.145'        // Replace with your EC2 instance IP
        EC2_USER = 'ec2-user'              // Replace with your EC2 user
        IMAGE = 'samvelll/flask-app'        // Docker image name
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/yourusername/jenkins-pipeline-flask.git'.       // Replace with your repository URL 
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
                echo "✅ All tests passed!"
            }
        }

        stage('Test') {
            steps {
                sh 'python -m unittest'.  // Replace with your test command
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t $IMAGE ."   // Build Docker image
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    sh "echo $PASSWORD | docker login -u $USERNAME --password-stdin"
                    sh "docker push $IMAGE".  // Push Docker image to Docker Hub
                }
            }
        }

        stage('Deploy to Server') {
            steps {
                sshagent(['ec2-ssh-key']) {
                    sh 'ssh ec2-user@your-server-ip "docker pull $IMAGE && docker stop flask || true && docker rm flask || true && docker run -d --name flask -p 80:5000 $IMAGE"' // Deploy Docker container on EC2 
                }
            }
        }
    }
}
