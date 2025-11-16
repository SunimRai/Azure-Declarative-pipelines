import dlt
from pyspark.sql.functions import *
###Transforming sales data creating a view in middle to capture only new data

@dlt.view(
    name = 'sales_enriched_view'
)

def sales_enriched_view():
    df = spark.readStream.table('sales_stg')
##Transfomrations
    df = df.withColumn('totalAmount', col('quantity') * col('amount'))
    return df

##Creating Destination silver table

dlt.create_streaming_table(
    name = 'sales_enriched'
)

dlt.create_auto_cdc_flow(
  target = "sales_enriched",
  source = "sales_enriched_view",
  keys = ["sales_id"],
  sequence_by = "sale_timestamp",
  ignore_null_updates = False,
  apply_as_deletes = None,
  apply_as_truncates = None,
  column_list = None,
  except_column_list = None,
  stored_as_scd_type = 1,
  track_history_column_list = None,
  track_history_except_column_list = None,
  name = None,
  once = False
)