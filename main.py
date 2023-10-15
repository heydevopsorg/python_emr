from pyspark.sql import SparkSession
from pyspark.sql.functions import col

S3_DATA_SOURCE='s3://bucket-emr123456/data-source/survey_results_public.csv'

S3_OUTPUT='s3://bucket-emr123456/data-output'


def main():
    spark = SparkSession.builder.appName('test').getOrCreate()
    all_data = spark.read.csv(S3_DATA_SOURCE,header=true)
    selected_data = all_data.where((col('country') == 'United States') & (col('WorkWeekHrs')>45 ))
    print('The total engineers are: %s' % selected_data.count())



if __name__ == '__main__':
    main()




