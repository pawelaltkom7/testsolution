pipeline {
    agent any
    environment {
        python = "C:\\\\Users\\Student\\AppData\\Local\\Programs\\Python\\Python310\\python.exe"
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
                bat "${python} -m pytest"
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