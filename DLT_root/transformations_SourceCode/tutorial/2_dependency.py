# import dlt
# from pyspark.sql.functions import *

# #Creating an end to end basic pipeline
# ## Staging area
# @dlt.table(
#     name ='staging_orders'
# )

# def staging_orders():
#     df= spark.readStream.table('dltminus.source.orders')
#     return df
# ##Create streaming view
# @dlt.view(
#     name = 'transformed_orders'
# )
# def transformed_orders():
#     df = spark.readStream.table('staging_orders')
#     df = df.withColumn('order_status', lower(col('order_status')))
#     return df
    
# ###Create aggregated area

# @dlt.table(
#     name = 'aggregated_orders'
# )

# def aggregated_orders():
#     df = spark.readStream.table('transformed_orders')
#     df = df.groupBy('order_status').count()
#     return df


