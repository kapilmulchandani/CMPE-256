from pyspark import SparkContext, SparkConf, SQLContext
import pyspark.sql.functions as f

conf = (SparkConf ()
            . setMaster("local[20]")
            . setAppName("sample app for reading files")
            . set("spark.executor.memory", "2g"))

sc = SparkContext(conf=conf)

sqlContext = SQLContext (sc)
df = sqlContext.read.load ("ratings.csv",
                                format='com.databricks.spark.csv',
                                header='true',
                                inferSchema='true')

df.groupby('movieId').agg(f.avg('rating').alias('movie_rating')).orderBy('movieId', ascending=True).coalesce(1).write.format("com.databricks.spark.csv").save("WowResultsnew.csv")
