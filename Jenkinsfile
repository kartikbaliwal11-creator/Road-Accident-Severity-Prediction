pipeline {

    agent any

    stages {

        stage('Install Dependencies') {

            steps {

                bat 'python -m pip install -r requirements.txt'

            }

        }

        stage('Run Monitoring Script') {

            steps {

                bat 'python monitor.py'

            }

        }

        stage('Build Docker Image') {

            steps {

                bat 'docker build -t accident-prediction .'

            }

        }

    }

}