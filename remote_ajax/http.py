from conf import access_control_allow_origin

def HttpResponseAjax(response):
    response["Access-Control-Allow-Origin"] = access_control_allow_origin
    response["Access-Control-Allow-Credentials"] = "true"
    return response