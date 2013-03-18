from http import HttpResponseAjax

class XHRMiddleware(object):
    def process_response(self, request, response):
        return HttpResponseAjax(response)