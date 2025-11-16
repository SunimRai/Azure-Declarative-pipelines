# import dlt

# # Create Stream Table
# @dlt.table(
#     name = 'first_stream_table'
# )

# def first_stream_table():
#     df = spark.readStream.table('dltminus.source.orders')
#     return df

# ###For Batch processing create materialized view

# @dlt.table(
#     name = 'first_mat_view'
# )

# def first_mat_view():
#     df = spark.read.table('dltminus.source.orders')
#     return df

# ##Create view (Batch view and stream view)
# @dlt.view(
#     name = 'first_batch_view'
# )

# def first_batch_view():
#     df = spark.read.table('dltminus.source.orders')
#     return df

# ##Streaming view
# @dlt.view(
#     name = 'first_stream_view'
# )

# def first_stream_view():
#     df= spark.readStream.table('dltminus.source.orders')
#     return df


