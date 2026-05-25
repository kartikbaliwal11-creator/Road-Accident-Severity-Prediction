pipeline {

    agent any

    stages {

        stage('Install Dependencies') {

            steps {

                bat 'pip install -r requirements.txt'

            }

        }

        stage('Run Monitoring') {

            steps {

                bat 'python monitor.py'

            }

        }

    }

}