pipeline {
    agent any
    stages{
        stage('deploy to S3'){
            steps{
                sh 'aws s3 cp a.html s3://dungpham-test-glue'
                sh 'aws s3api put-object-acl --bucket dungpham-test-glue --key a.html --acl public-read'
                sh 'aws s3 cp a.html s3://dungpham-test-glue'
                sh 'aws s3api put-object-acl --bucket dungpham-test-glue --key a.html --acl public-read'
            }
        }
    }
}