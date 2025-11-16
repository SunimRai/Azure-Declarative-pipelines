# Databricks notebook source
df = spark.read.table('dltminus.source.orders')
df.display()



# COMMAND ----------


