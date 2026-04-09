pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                sh 'pytest app/tests/test_basic.py' [cite: 29]
            }
        }
        stage('Terraform') {
            steps {
                dir('terraform') { sh 'terraform apply -auto-approve' } [cite: 32]
            }
        }
    }
}