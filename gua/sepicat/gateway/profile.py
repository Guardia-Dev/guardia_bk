from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework import permissions
from rest_framework.parsers import JSONParser
from rest_framework.views import exception_handler

from sepicat.data_models.user.profile import fetch_state

def missing_params_error(params: []):
    return Response({
        "reason": "缺少参数",
        "detail_params": params,
    })

def crawl_params_error(params: []):
    return Response({
        "reason": "参数错误",
        "detail_params": params,
    })


@api_view(['GET'])
@permission_classes((permissions.AllowAny, ))
@parser_classes((JSONParser,))
def user_profile_state(request: Request):
    if request.method == 'GET':
        params = request.query_params.dict()
        if 'login' not in params.keys():
            return missing_params_error(['login'])
        login = params['login']
        res = fetch_state(login=login)
        if res is not None and type(res) is dict:
            return Response({
                "result": res
            })
        return crawl_params_error(['login'])

