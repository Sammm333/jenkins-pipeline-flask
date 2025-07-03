pipeline {
  agent any

  environment {
    EC2_HOST = '54.234.136.145'
    EC2_USER = 'ec2-user'
    IMAGE    = 'samvelll/flask-app:latest'
  }

  stages {
    stage('Init') {
      steps {
        echo "Jenkins workspace is already checked out from SCM."
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

    stage('Build & Push Docker Image') {
      steps {
        // build
        sh "docker build -t $IMAGE ."
        // login & push
        withCredentials([usernamePassword(credentialsId: 'dockerhub-creds',
                                         usernameVariable: 'DOCKER_USER',
                                         passwordVariable: 'DOCKER_PASS')]) {
          sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"
          sh "docker push $IMAGE"
        }
      }
    }

    stage('Deploy to EC2') {
      steps {
        sshagent(['ec2-ssh-key']) {
          sh """
            ssh $EC2_USER@$EC2_HOST '
              docker pull $IMAGE &&
              docker stop flask || true &&
              docker rm flask   || true &&
              docker run -d --name flask -p 80:5000 $IMAGE
            '
          """
        }
      }
    }
  }
}
