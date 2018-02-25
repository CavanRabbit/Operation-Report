from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify
import json
import report
app = Flask(__name__)


@app.route('/getMetricByDate', methods=['POST'])
def get_metric_by_date():
    req_data = request.get_data()
    req_data = json.loads(req_data)
    metric_id = req_data['metricId']
    start_date = req_data['startDate']
    end_date = req_data['endDate']
    value_type = req_data['valueType']
    return 'hahah'


@app.route('/getMetricByTimestamp', methods=['POST'])
def get_metric_by_timestamp():
    req_data = request.get_data()
    req_data = json.loads(req_data)
    metric_id = req_data['metricId']
    start_timestamp = req_data['startTimestamp']
    end_timestamp = req_data['endTimestamp']
    value_type = req_data['valueType']
    return 'heiheihei'


if __name__ == '__main__':
    app.run(port=8081, debug=True)