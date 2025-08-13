import pandas as pd
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas

# Load data
df = pd.read_csv("data/sample_data.csv")
print("Data preview:")
print(df)

# Snowflake credentials
conn = snowflake.connector.connect(
    user='YOUR_USERNAME',
    password='YOUR_PASSWORD',
    account='YOUR_ACCOUNT_ID',
    warehouse='YOUR_WAREHOUSE',
    database='YOUR_DATABASE',
    schema='YOUR_SCHEMA'
)

# Insert data into Snowflake
success, nchunks, nrows, _ = write_pandas(conn, df, 'LOGS_TABLE')
print(f"Success: {success}, Rows inserted: {nrows}")
