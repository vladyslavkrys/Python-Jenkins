pipeline {
    agent { docker { image 'python:3.10.5-alpine' } }
    stages {
        stage('build') {
            steps {
                sh 'python3 --version'
                sh 'sudo python3 -m pip install requests'
                sh 'python3 script.py'
            }
        }
    }
}
