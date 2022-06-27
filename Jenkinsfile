pipeline {
    agent { docker { image 'python:3.10.1-alpine' args '-u root' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh 'sudo pip install requests'
                sh 'python script.py'
            }
        }
    }
}
