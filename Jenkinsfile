pipeline {
    agent any

    environment {
        PYTHON = 'C:\\Users\\Fran\\AppData\\Local\\Programs\\Python\\Python313\\python.exe'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install') {
            steps {
                bat '"%PYTHON%" -m venv venv'
                bat 'venv\\Scripts\\python.exe -m pip install --upgrade pip'
                bat 'venv\\Scripts\\pip.exe install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                bat 'venv\\Scripts\\pytest.exe --junitxml=rezultati.xml'
            }
            post {
                always {
                    junit 'rezultati.xml'
                }
            }
        }

        stage('Deploy') {
            steps {
                bat 'venv\\Scripts\\python.exe deploy.py'
            }
        }
    }

    post {
        success {
            echo 'Pipeline uspjesno zavrsen! Aplikacija je isporucena na portu 5001.'
        }
        failure {
            echo 'Pipeline neuspjesan - provjerite greske.'
        }
    }
}
