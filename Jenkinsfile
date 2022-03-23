pipeline {
    agent any
    environment {
        Main_Branch = "Welcome in the main branch!"
    }
    stages {
        stage('CheckBranch') {
            steps {
                when {
                        branch 'main'
                    }
                    steps{
                        echo " check ${Main_Branch}"
                    }
            }
        }
        stage('TestCode') {
            steps {
                
            }
        }
        stage('RunCode') {
            steps {
                
            }
        }
        stage('BuildImage') {
            steps {
               
            }
        }
        stage('PushImage') {
            steps {
                
            }
        }
    }
}