#!/usr/bin/env groovy

pipeline {
  // Agent Initialization
  agent {
    dockerfile true
  }

  // Parameters
  parameters {
    booleanParam(name: 'RUN_STATIC_CODE_ANALYSIS', defaultValue: true, description: 'Would you like to perform static code analysis?')
    booleanParam(name: 'RUN_TESTS', defaultValue: true, description: 'Would you like to run unit tests?')
    choice(name: 'DEPLOY', choices: ['NO', 'DEV', 'QA', 'PROD'], description: 'Which environment would you like to deploy to?')
  }

  stages {
    // Static Code Analysis
    stage('Static Code Analysis') {
      steps {
        script {
          if (params.RUN_STATIC_CODE_ANALYSIS) {
            sh 'echo "Static Code Analysis"'
            sh 'python manage.py jenkins'

            def flake8 = scanForIssues tool: flake8(pattern: '**/reports/flake8.report')
            publishIssues issues:[flake8]

            def pep8 = scanForIssues tool: pep8(pattern: '**/reports/pep8.report')
            publishIssues issues:[pep8]

            sh 'pylint --disable=W1202 --output-format=parseable --reports=no module > pylint.log || echo "pylint exited with $?")'
            sh 'cat render/pylint.log'

            step([$class: 'WarningsPublisher', parserConfigurations: [[parserName: 'PYLint', pattern   : 'pylint.log']],unstableTotalAll : '0',usePreviousBuildAsReference: true])
          } else {
            sh 'echo "Skipped Static Code Analysis"'
          }
        }
      }
    }

    // Tests
    stage('Tests') {
      steps {
        script {
          if (params.RUN_TESTS) {
            sh 'echo "Tests"'
            sh 'python manage.py test'

            junit '**/reports/junit.xml'
          } else {
            sh 'echo "Skipped Tests"'
          }
        }
      }
    }

    // Deployment
    stage('Deployment') {
      steps {
        script {
          if (params.DEPLOY == 'NO') {
            sh 'echo "skipping deployment"'
          } else if (params.DEPLOY == 'DEV'){
            sh 'echo "deploying to dev..."'
          } else if (params.DEPLOY == 'QA') {
            sh 'echo "deploying to qa..."'
          } else if (params.DEPLOY == 'PROD') {
            sh 'echo "deploying to prod..."'
          }
        }
      }
    }
  }
}