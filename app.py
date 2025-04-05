from http.client import responses

from flask import Flask, request, render_template, jsonify
import os

from gpt_db_helper import connect_to_db, execute_query, generate_sql_from_query_from_gds, generate_sql_query_for_rnf
from gpt_doc_helper import summarize_document, analyze_document

from gpt_git_helper import getGitRequests
from flask_cors import cross_origin, CORS

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads'

FILE_PATH_USER_GUIDE = "sample/File/Path"

CORS(app, resources={r"/*":{"origins": "https://localhost.world.socgen:3000"}})

@app.route("/user_query", methods=["GET"])
@cross_origin()
def index():
    print(request.args)
    user_selection = request.args.get('user_selection')
    user_prompt = request.args.get('user_prompt')

    print(user_selection, user_prompt)
    response = "return result"
    if(user_selection=="1"):
        sql_query  = generate_sql_query_for_rnf(user_prompt)
        response = execute_query(connect_to_db(), sql_query)

    if(user_selection=="2"):
        sql_query = generate_sql_from_query_from_gds(user_prompt)
        response = execute_query(connect_to_db(), sql_query)

    if(user_selection == "3"):
        response = summarize_document(user_prompt, FILE_PATH_USER_GUIDE)

    if(user_selection == "4"):
        response = getGitRequests(user_prompt)


    return jsonify({"response": response})
