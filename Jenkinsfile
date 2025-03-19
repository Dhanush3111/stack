pipeline {
    agent any  //Runs on any avalable Windows agent
    stages {
        stage('Checkout Code') {
            steps {
            // Clone your Github repository
                git 'https://github.com/your-repo.git'
            }
        }

        stage('Compile java code') {
            steps {
                // Navigate to the directory where the java file is located 
                bat 'javac simple.java'
            }
        }

        stage('Run java program') {
            steps {
                // Execute the java program with input (Example : adding two numbers)
                bat 'echo 10 20 | java simple'
            }
        }


    post {
        success {
            echo 'Build successful!'
        }
        failure {
            echo 'Build failed!'
        }
    }
}

