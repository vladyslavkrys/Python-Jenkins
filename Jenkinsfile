pipeline {
    agent { docker { image 'python:3.10.1-alpine' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh 'sudo -H pip install requests'
                sh 'python script.py'
            }
        }
    }
}
