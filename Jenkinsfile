// Deklarativni Jenkins pipeline (Windows okruzenje)
// Definira faze CI/CD procesa: dohvat koda, instalacija ovisnosti,
// izvodenje testova te osnovni proces isporuke.

pipeline {
    agent any

    environment {
        // Putanja do Python interpretera na sustavu
        PYTHON = 'C:\\Users\\Fran\\AppData\\Local\\Programs\\Python\\Python313\\python.exe'
    }

    stages {
        stage('Checkout') {
            steps {
                // Dohvat izvornog koda iz repozitorija
                checkout scm
            }
        }

        stage('Install') {
            steps {
                // Kreiranje virtualnog okruzenja i instalacija ovisnosti
                bat '"%PYTHON%" -m venv venv'
                bat 'venv\\Scripts\\python.exe -m pip install --upgrade pip'
                bat 'venv\\Scripts\\pip.exe install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                // Izvodenje automatiziranih testova uz generiranje izvjestaja
                bat 'venv\\Scripts\\pytest.exe --junitxml=rezultati.xml'
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
                // Osnovni proces isporuke (prosirit cemo u Fazi D)
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
