pipeline {
    agent none
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh 'pip install requests'
                sh 'python script.py'
            }
        }
    }
}
