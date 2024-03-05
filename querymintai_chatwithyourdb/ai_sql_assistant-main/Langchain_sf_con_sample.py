
from langchain.document_loaders import SnowflakeLoader

QUERY = "select * from analyticsdb.public.customer limit 10"
snowflake_loader = SnowflakeLoader(
    query=QUERY,
    user="ANANYAG",
    password="Password1234!",
    account="OXJTHKI-UN86547",
    warehouse="COMPUTE_WH",
    role="ACCOUNTADMIN",
    database="analyticsdb",
    schema="PUBLIC",
)
snowflake_documents = snowflake_loader.load()
i=1
for document in snowflake_documents:
    print("row number = {} =======================".format(i))
    print(document.page_content)
    i=i+1
