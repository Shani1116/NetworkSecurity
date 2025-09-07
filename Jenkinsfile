pipeline {
    agent any

    environment {
        DIRECTORY_PATH = "/var/www/NetworkSecurity"
        TESTING_ENVIRONMENT = "Shanika-Stg-Env"
        PRODUCTION_ENVIRONMENT = "Shanika-Prod-Env"
    }

    stages {
        stage('Build') {
            steps {
                echo "Fetching source code from ${DIRECTORY_PATH}"
                echo "Build the code using Maven and generate build artifacts"
                echo "Example tool - Maven"
                echo "Example code - mvn clean install"
            }
        }

        stage('Unit & Integration Tests') {
            steps {
                echo "Run Unit & Integration Tests"
                echo "Example tool - Surefire"
                echo "Example code - mvn test"
                sh 'echo "Unit & Integration tests executed"' 
            }
        }

        stage('Code Analysis') {
            steps {
                echo "Analyze code quality using SonarQube"
                echo "Example tool - SonarQube"
                sh 'echo "SonarQube scan completed"'
            }
        }

        stage('Security Scan') {
            steps {
                echo "Perform security scan using Trivy"
                echo "Example tool - Trivy"
                sh 'echo "Security scan completed - no critical vulnerabilities found"'
            }
        }

        stage('Deploy to Staging') {
            steps {
                echo "Deploy application to testing environment: ${TESTING_ENVIRONMENT}"
                sh 'echo "Application deployed to staging server"'
            }
        }

        stage('Integration Tests on Staging') {
            steps {
                echo "Run integration tests on the staging environment"
                sh 'echo "Staging environment tests executed successfully"'
            }
        }

        stage('Deploy to Production') {
            steps {
                echo "Deploy application to production environment: ${PRODUCTION_ENVIRONMENT}"
                sh 'echo "Application successfully deployed to production!"'
            }
        }
    }
}
