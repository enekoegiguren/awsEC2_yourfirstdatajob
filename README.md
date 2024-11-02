# yourfirstdatajob

## Streamlit Data Analysis App

![Alt text](https://github.com/enekoegiguren/awsEC2_yourfirstdatajob/blob/main/awsEC2_yourfirstdatajob.jpg)


## Overview

This project is a Streamlit application designed to analyze data related to the job market in France. The app leverages various AWS services for data extraction, transformation, and storage, providing users with insights into job categories, salary trends, and required skills.

## Features

- Interactive dashboards to visualize job market trends
- Filter options for job categories, experience levels, and salary ranges
- Real-time data updates through AWS services
- User-friendly interface for data exploration

## Architecture

The application uses the following AWS services:

- **EC2 Instances**: Hosts the Streamlit application and provides the necessary compute resources.
- **AWS Lambda**: Responsible for updating the data periodically. This serverless compute service allows for event-driven data updates.
- **Amazon S3**: Used for storing the processed data in a secure and scalable manner.
- **IAM Security Groups**: Ensures secure access to AWS resources by controlling inbound and outbound traffic.
- **CloudWatch Logs**: Monitors and logs the performance and errors of the AWS services used in the project.
- **EventBridge Scheduler**: Triggers the AWS Lambda function on a predefined schedule for automatic data updates.

## Getting Started

### Prerequisites

- AWS account with access to EC2, Lambda, S3, IAM, CloudWatch, and EventBridge
- pip install -r requirements.txt


### Data Updater

The data updater functionality is located in this [GitHub repository](https://github.com/enekoegiguren/lambda_jobdata). Follow the instructions in that repository to set up the data updating mechanism using AWS Lambda.

## Monitoring

You can monitor the AWS services and the performance of the application using AWS CloudWatch. Logs for the Lambda functions and other services can be found in the CloudWatch dashboard.


