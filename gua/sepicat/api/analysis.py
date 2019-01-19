from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework import permissions
from rest_framework.parsers import JSONParser
from rest_framework.views import exception_handler

from sepicat.data_models.year_analysis import YearAnalysis

def missing_params_error(params: []):
    return Response({
        "reason": "缺少参数",
        "detail_params": params,
    })


@api_view(['GET'])
@permission_classes((permissions.AllowAny, ))
@parser_classes((JSONParser,))
def commit_analysis(request: Request):
    if request.method == 'GET':
        params = request.query_params.dict()
        if 'login' not in params.keys():
            return missing_params_error(['login'])
        login = params['login']

        if 'year' not in params.keys():
            year = 2018
        else:
            year = params['year']

        # if 'token' not in params.keys():
        #     return missing_params_error(['token'])
        # token = params['token']

        analysis = YearAnalysis(login=login, token="", year=year)
        analysis.fetch_commits()

        return Response({
            'result': {
                'total': analysis.tot_commit,
                'repositories': analysis.repo_commits,
                'details': analysis.repo_actions_dict,
            }
        })


