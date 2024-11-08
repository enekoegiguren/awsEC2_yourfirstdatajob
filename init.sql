DROP TABLE IF EXISTS ft_jobdata;

CREATE TABLE IF NOT EXISTS ft_jobdata (
    id varchar(100),
    title VARCHAR(255),
    code_postal VARCHAR(10),
    latitude DECIMAL(9, 6),
    longitude DECIMAL(9, 6),
    date_creation DATE,
    date_actualization DATE,
    contract_type VARCHAR(50),
    contract_nature VARCHAR(50),
    experience_bool BOOLEAN,
    experience DECIMAL(10, 2),
    avg_salary DECIMAL(10, 2),
    min_salary DECIMAL(10,2),
    max_salary DECIMAL(10,2),
    company_field VARCHAR(255),
    job_category VARCHAR(255),
    chef VARCHAR(255),
    year INT,
    month INT,
    day INT,
    sql BOOLEAN,
    python BOOLEAN,
    pyspark BOOLEAN,
    azure BOOLEAN,
    aws BOOLEAN,
    gcp BOOLEAN,
    etl BOOLEAN,
    airflow BOOLEAN,
    kafka BOOLEAN,
    spark BOOLEAN,
    power_bi BOOLEAN,
    tableau BOOLEAN,
    snowflake BOOLEAN,
    docker BOOLEAN,
    kubernetes BOOLEAN,
    git BOOLEAN,
    data_warehouse BOOLEAN,
    hadoop BOOLEAN,
    mlops BOOLEAN,
    data_lake BOOLEAN,
    bigquery BOOLEAN,
    databricks BOOLEAN,
    dbt BOOLEAN,
    mlflow BOOLEAN,
    java BOOLEAN,
    scala BOOLEAN,
    sas BOOLEAN,
    matlab BOOLEAN,
    power_query BOOLEAN,
    looker BOOLEAN,
    apache BOOLEAN,
    hive BOOLEAN,
    terraform BOOLEAN,
    jenkins BOOLEAN,
    gitlab BOOLEAN,
    machine_learning BOOLEAN,
    deep_learning BOOLEAN,
    nlp BOOLEAN,
    api BOOLEAN,
    pipeline BOOLEAN,
    data_governance BOOLEAN,
    erp BOOLEAN,
    ssis BOOLEAN,
    ssas BOOLEAN,
    ssrs BOOLEAN,
    ssms BOOLEAN,
    postgre BOOLEAN,
    mysql BOOLEAN,
    mongodb BOOLEAN,
    cloud BOOLEAN,
    synapse BOOLEAN,
    blobstorage BOOLEAN,
    azure_devops BOOLEAN,
    fabric BOOLEAN,
    glue BOOLEAN,
    redshift BOOLEAN,
    s3 BOOLEAN,
    lambda BOOLEAN,
    emr BOOLEAN,
    athena BOOLEAN,
    kinesis BOOLEAN,
    rds BOOLEAN,
    sagemaker BOOLEAN,
    extracted_date DATE
);
