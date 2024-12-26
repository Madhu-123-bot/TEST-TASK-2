pipeline {
    agent any
    environment {
        VIRTUAL_ENV_DIR = "/home/ubuntu/myenv"  // Virtual environment path
        REQUIREMENTS_FILE = "/home/ubuntu/proj_lts_2/requirements.txt"  // Path to requirements.txt
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
                        source ${VIRTUAL_ENV_DIR}/bin/activate
                    """
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Install dependencies from requirements.txt
                    sh """
                        source ${VIRTUAL_ENV_DIR}/bin/activate
                        pip install -r ${REQUIREMENTS_FILE}
                    """
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run tests using pytest
                    sh """
                        source ${VIRTUAL_ENV_DIR}/bin/activate
                        pytest /home/ubuntu/proj_lts_2
                    """
                }
            }
        }
    }
}

