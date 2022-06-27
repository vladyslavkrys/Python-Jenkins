pipeline {
    agent { docker { image 'python:3.10.5-alpine' } }
    stages {
        stage('build') {
            steps {
                sh 'python3 --version'
                sh '/usr/local/bin/python3 -m pip install --upgrade pip'
                sh 'python3 -m pip install requests --user'
                sh 'python3 script.py'
            }
        }
    }
}
