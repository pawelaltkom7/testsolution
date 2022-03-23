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
                bat "${python} main.py"
            }
        }
        stage('BuildImage') {
            steps {
               bat "docker build -t \"jenkinspf:latest\" ."
               bat "docker run jenkinspf:latest"
            }
        }
        stage('PushImage') {
            steps {
                bat "docker tag jenkinspf:latest pawelaltkom7/demo:fromjenkinspipeline"
                bat "docker push pawelaltkom7/demo:fromjenkinspipeline"
            }
        }
    }
}