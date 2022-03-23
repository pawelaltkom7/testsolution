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
                        echo "${Main_Branch}"
                    }
            }
        }
        stage('TestCode') {
            steps {
                echo ""
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