// Deklarativni Jenkins pipeline
// Definira faze CI/CD procesa: dohvat koda, instalacija, testiranje i isporuka.

pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Dohvat izvornog koda iz repozitorija
                checkout scm
            }
        }

        stage('Install') {
            steps {
                // Instalacija ovisnosti aplikacije
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                // Izvodenje automatiziranih testova
                sh 'pytest --junitxml=rezultati.xml'
            }
            post {
                always {
                    // Objava rezultata testova u Jenkinsu
                    junit 'rezultati.xml'
                }
            }
        }

        stage('Deploy') {
            steps {
                // Osnovni proces isporuke (placeholder - prosirit cemo u Fazi D)
                echo 'Isporuka aplikacije...'
            }
        }
    }

    post {
        success {
            echo 'Pipeline uspjesno zavrsen!'
        }
        failure {
            echo 'Pipeline neuspjesan - provjerite greske.'
        }
    }
}
