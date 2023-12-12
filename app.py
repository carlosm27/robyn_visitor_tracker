from robyn import Robyn, status_codes, ALLOW_CORS

from robyn.robyn import Response, Headers, Request
from controllers import all_logs, new_log
from robyn import logger
from middleware import Tracker

import json
app = Robyn(__file__)

ALLOW_CORS(app,["*"])

@app.before_request()
async def log_request(request: Request):
    
    tracker = Tracker.visitor_tracker(request=request)
    new_log(tracker["ip_address"], tracker["request_url"], tracker["request_path"], tracker["request_method"], tracker["request_time"])
    logger.info(f"Received request: %s", tracker)

    return request

@app.get("/")
async def hello():
    return Response(status_code=status_codes.HTTP_200_OK,headers=Headers({}), description="Hello, World!")

@app.get("/visitors")
async def hello():
    logs = all_logs()
    
    return Response(status_code = status_codes.HTTP_200_OK, headers=Headers({}), description = json.dumps(logs))


app.start(port=8000, host="0.0.0.0")