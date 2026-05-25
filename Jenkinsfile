pipeline {

    agent any

    stages {

        stage('Install Dependencies') {

            steps {

                bat 'python -m pip install -r requirements.txt'

            }

        }

        stage('Run Monitoring') {

            steps {

                bat 'python monitor.py'

            }

        }

    }

}