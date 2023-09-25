import sys
import os
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_dir)

from flask import Flask, request, jsonify
from utils.analysis import *

app = Flask(__name__)


@app.route('/analysis-all-moves', methods=['POST'])
def get_analysis():
    try:
        data = request.get_json()

        analysis_result = analyze_all_chess_move(data)

        return jsonify({"analysis": analysis_result})

    except Exception as e:
        print(e)
        return jsonify({"error": str(e)})


@app.route('/analysis-one-move', methods=['POST'])
def get_analysis_one_move():
    try:
        data = request.get_json()

        analysis_result = analyze_chess_move([data])

        return jsonify({"analysis": analysis_result})

    except Exception as e:
        print(e)
        return jsonify({"error": str(e)})


if __name__ == '__main__':
    app.run(debug=True)


