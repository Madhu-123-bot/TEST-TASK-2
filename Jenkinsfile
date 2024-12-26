pipeline {
    agent any
    environment {
        VIRTUAL_ENV_DIR = "${WORKSPACE}/myenv"  // Use Jenkins workspace for virtual environment
        REQUIREMENTS_FILE = "${WORKSPACE}/requirements.txt"  // Path to requirements.txt
    }
    stages {
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
                    // Run tests using pytest
                    sh """
                        bash -c 'source ${VIRTUAL_ENV_DIR}/bin/activate && pytest ${WORKSPACE}'
                    """
                }
            }
        }
    }
}

