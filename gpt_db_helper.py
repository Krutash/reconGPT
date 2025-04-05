import sqlite3
from utility.OpenAIClient import openai_client

def connect_to_db():
    conn = sqlite3.connect("data.db")
    return conn

#Execute SQL Query
def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    columns = [col(0) for col in cursor.description]
    results = [dict (zip(columns, row)) for row in cursor.fetchall()]
    return  results

common_prompt = """

You are an SQL expert. Generate a valid SQL query based on the user's natural language question
without including any formatting for sql, just give the raw text sql query and following are
schema info which are available with us:


"""

def generate_sql_query_for_rnf(user_query):
    rec_creation_details = """
    rec_creation_details (
    process_code VARCHAR(12),
    process_name CHAR(4),
    creation_date DATE,
    created_by VARCHAR(50)
    )
    """

    rec_stats_schema = """
    rec_stats_details (
    run_id INT,
    run_status VARCHAR(20),
    process_code VARCHAR(12),
    run_time TIME
    )
    """

    rec_errors = """
    rec_errors (
    process_code VARCHAR(12),
    run_id INT,
    error_reason VARCHAR(50)
    )
    """

    prompt = f"""

    {common_prompt}
    
    1. table Name : rec_stats with following schema
    {rec_stats_schema}
    
    2. table name : rec_creation_details with following schema
    {rec_creation_details}
    
    3. table Name : rec_errors with the following the schema
    {rec_errors}
    
    with the user query: {user_query} 
    """
    return getResponseFromGPT(prompt)

def getResponseFromGPT(prompt):
    print('sql query: ', prompt)
    response = openai_client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-4o"

    )

    print(response.choices[0].message.content)
    return response.choices[0].message.content

def generate_sql_from_query_from_gds(user_query):
    hkn_gds_data ="""
    HKTN_RECON_DATA (ACCT_ID NUMBER(38) NOT NULL,RECORD_ID NUMBER(38) NOT NULL,
    STATE NUMBER(38) NOT NULL, CS_FLAG CHAR(1) NOT NULL,PR_FLAG CHAR(1) NOT NULL,
    TRANS_DATE DATE, VALUE_DATE DATE,NARRATIVE VARCHAR2(255), INTL_REF VARCHAR2(255), 
    EXTL_REF VARCHAR2(255), AMOUNT NUMBER(23, 6) NOT NULL, TRANS_TYPE VARCHAR2(7),
    USER_THREE VARCHAR2(25), USER_SIX VARCHAR2(25), REC_GROUP NUMBER(38), ORIG_CCY CHAR(3), 
    CREATEBY NUMBER(38) NOT NULL,REC_METHOD NUMBER(38), DEPARTMENT VARCHAR2(25), 
    LASTAUDIT NUMBER(38), SUB_ACCT NUMBER(38), PASS_ID NUMBER(38), FLAG_E CHAR(1),
    QUANTITY NUMBER(38), UNITPRICE NUMBER(23, 6), USERDATE_A DATEI PERIOD VARCHAR2(25), 
    LAST_NOTE_TEXT VARCHAR2(500),LAST_NOTE_USER NUMBER(38), USER_NINE VARCHAR2(255),
    USER_THIRTEEN VARCHAR2(255), LOAD_ID NUMBER(38), DIFF_REF NUMBER(38), CREATED_DATE DATE);
    """

    prompt = f"""
    {common_prompt}
    
    1. table name : hkn_gds_data with the follwing schema:
    
    {hkn_gds_data}
    
    User query : {user_query}
    
    SQL QUERY : 
    """
    return getResponseFromGPT(prompt)