import dlt
from pyspark.sql.functions import *


@dlt.table(
    name = 'business_sales'

)

def business_sales():
    df_fact = spark.read.table('fact_sales')
    df_dimCust = spark.read.table('dim_customers')
    df_dimProd = spark.read.table('dim_products')

    df_join = df_fact.join(df_dimCust, df_fact.customer_id == df_dimCust.customer_id, 'inner').join(df_dimProd, df_fact.product_id == df_dimProd.product_id, 'inner')

    df = df_join.select('region','category','totalAmount').groupBy('region','category').agg(sum('totalAmount').alias('total_sales'))

    return df
