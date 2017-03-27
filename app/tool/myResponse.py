from django.http import JsonResponse


class MyResponse(JsonResponse):
    @staticmethod
    def CrossDomainResponse(response):
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
