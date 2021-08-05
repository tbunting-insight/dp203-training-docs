import os
import modules
import os
import pyspark
from azureml.opendatasets import NycTlcYellow

variables = modules.set_environment_variables()


data = NycTlcYellow()
data_df = data.to_spark_dataframe()
display(data_df.limit(10))