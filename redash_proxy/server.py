from flask import Flask, abort, request
from flask_cors import CORS
from redash_client.client import RedashClient
import os
import sys

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-type'


@app.route("/")
def hello_world():
    return "Hello, world!"


@app.route("/<data_source_name>", methods=["POST"])
def run_query(data_source_name):
    data_source = app.data_sources.get(data_source_name)
    if data_source is None:
        abort(404)
    data_source_id = data_source["id"]
    query_str = str(request.form["query"])
    return str(app.redash_client.get_query_results(query_str, data_source_id))


def get_data_sources(redash_client):
    sources_list = redash_client.get_data_sources()
    data_sources = {}
    for source in sources_list:
        data_sources[source["name"]] = source
    return data_sources


def main():
    api_key = os.environ.get("REDASH_API_KEY")
    if not api_key:
        app.logger.error("No REDASH_API_KEY environment variable is set!")
        sys.exit(1)
    app.redash_client = RedashClient(api_key)
    app.data_sources = get_data_sources(app.redash_client)
    app.run()
