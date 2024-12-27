pipeline {
    agent any
    environment {
        VIRTUAL_ENV_DIR = "${WORKSPACE}/myenv"  // Virtual environment directory
        REQUIREMENTS_FILE = "${WORKSPACE}/requirements.txt"  // Path to requirements.txt
        TEST_REPORT_DIR = "${WORKSPACE}/test-reports"  // Directory for test reports
    }
    options {
        timestamps() // Adds timestamps to console log
    }
    stages {
        stage('Cleanup') {
            steps {
                script {
                    // Clean up the workspace before starting
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
                    // Ensure Python virtual environment is set up
                    sh """
                        python3 -m venv ${VIRTUAL_ENV_DIR}
                    """
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Install dependencies from requirements.txt
                    sh """
                        bash -c 'source ${VIRTUAL_ENV_DIR}/bin/activate && pip install -r ${REQUIREMENTS_FILE}'
                    """
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Create a directory for test reports
                    sh "mkdir -p ${TEST_REPORT_DIR}"
                    
                    // Run tests using pytest and generate an HTML report
                    sh """
                        bash -c 'source ${VIRTUAL_ENV_DIR}/bin/activate && pytest --html=${TEST_REPORT_DIR}/report.html --self-contained-html ${WORKSPACE}'
                    """
                }
            }
        }
    }
    post {
        always {
            script {
                // Archive test reports
                archiveArtifacts artifacts: 'test-reports/*.html', allowEmptyArchive: true
            }
        }
        success {
            echo "Build succeeded and test report generated!"
        }
        failure {
            echo "Build failed. Check the test report for more details."
        }
    }
}

