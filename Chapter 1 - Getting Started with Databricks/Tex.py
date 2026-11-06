# Databricks notebook source
# MAGIC %md
# MAGIC #Getting Started
# MAGIC
# MAGIC Using Databricks Certification Guide from O'reilly

# COMMAND ----------

# MAGIC %md
# MAGIC ##Magic Commands

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT "Hello world from SQL!"

# COMMAND ----------

print("Hello World!")

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'

# COMMAND ----------

dbutils.help()


# COMMAND ----------

files = dbutils.fs.ls("file:/Workspace/Users/talbuja@thoughtworks.com/oreilly-databricks-dea")
display(files)

# COMMAND ----------

