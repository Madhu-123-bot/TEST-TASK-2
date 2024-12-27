pipeline {
    agent any
    environment {
        VIRTUAL_ENV_DIR = "${WORKSPACE}/myenv"  // Virtual environment directory
        REQUIREMENTS_FILE = "${WORKSPACE}/requirements.txt"  // Path to requirements file
        REPORT_DIR = "${WORKSPACE}/test-reports"  // Directory for test reports
    }
    stages {
        stage('Cleanup') {
            steps {
                script {
                    sh "rm -rf ${WORKSPACE}/*"
                }
            }
        }
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Madhu-123-bot/TEST-TASK-2.git'
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                script {
                    sh """
                        python3 -m venv ${VIRTUAL_ENV_DIR}
                    """
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    sh """
                        bash -c 'source ${VIRTUAL_ENV_DIR}/bin/activate && pip install -r ${REQUIREMENTS_FILE}'
                    """
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh "mkdir -p ${REPORT_DIR}"
                    sh """
                        bash -c 'source ${VIRTUAL_ENV_DIR}/bin/activate && pytest --html=${REPORT_DIR}/report.html --self-contained-html'
                    """
                }
            }
        }
    }
    post {
        always {
            script {
                archiveArtifacts artifacts: '**/test-reports/report.html', allowEmptyArchive: true
            }
        }
        failure {
            echo 'Build failed. Check the test report for more details.'
        }
    }
}

