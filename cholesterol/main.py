from flask import escape
import functions_framework
import json
import pandas as pd 

@functions_framework.http
def hello_http(request):

    request_args = request.args

    if request_args and "hdl" in request_args:
        hdl_value = request_args["hdl"]
    else:
        hdl_value = 60

    if request_args and "ldl" in request_args:
        ldl_value = request_args["ldl"]
    else:
        ldl_value = 100

    # Step 1 convert everything to numbers 
    hdl_num = int(hdl_value)
    ldl_num = int(ldl_value)

    # Step 2 we now some them all together 
    chol_sum = hdl_num + ldl_num 

    # Step 3 create a json object to return to the user 
    output = json.dumps(
        {
            "entered_hdl" : hdl_num, 
            "entered_ldl" : ldl_num, 
            "chol_sum" : chol_sum
        }
    )

    return output