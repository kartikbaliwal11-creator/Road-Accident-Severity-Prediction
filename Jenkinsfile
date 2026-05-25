pipeline {

    agent any

    stages {

        stage('Clone Repository') {

            steps {

                git 'https://github.com/kartikbaliwal11-creator/Road-Accident-Severity-Prediction.git'

            }

        }

        stage('Install Dependencies') {

            steps {

                bat 'pip install -r requirements.txt'

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