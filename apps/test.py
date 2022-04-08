from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["get"])
def test_view(request, *args, **kwargs):
    return Response({"data":1})