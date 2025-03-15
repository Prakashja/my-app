pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = "my-first-flask-app"  // Image name
        DOCKER_TAG = "${env.BUILD_NUMBER}" // Tag the image with Jenkins build number
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image with the build number as the tag
                    sh "docker build -t ${DOCKER_IMAGE_NAME}:${DOCKER_TAG} ."
                }
            }
        }
        stage('Push Docker Image to Docker Hub (optional)') {
            when {
                branch 'main' // Only push to Docker Hub when on the main branch
            }
            steps {
                script {
                    // Docker login - use environment variables or Jenkins secrets for credentials
                    withCredentials([usernamePassword(credentialsId: 'docker', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        sh "docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD"
                    }

                    // Push the image to Docker Hub
                    sh "docker tag ${DOCKER_IMAGE_NAME}:${DOCKER_TAG} sana03/${DOCKER_IMAGE_NAME}:${DOCKER_TAG}"
                    sh "docker push ${DOCKER_IMAGE_NAME}:${DOCKER_TAG}"
                }
            }
        }
    }

    post {
        always {
            // Clean up Docker images to save space (optional)
            sh "docker rmi ${DOCKER_IMAGE_NAME}:${DOCKER_TAG} || true"
        }
    }
}
