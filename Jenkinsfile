pipeline {
    agent any
    environment {
        Main_Branch = "Welcome in the main branch!"
    }
    stages {
        stage('ScriptTest') {
            steps {
                script{
                    def a = "ala ma kota"
                    println a
                }
            }
        }
        stage('TestCode') {
            steps {
                bat "python -m pytest"
            }
        }
        stage('RunCode') {
            steps {
                echo ""
            }
        }
        stage('BuildImage') {
            steps {
               echo ""
            }
        }
        stage('PushImage') {
            steps {
                echo ""
            }
        }
    }
}