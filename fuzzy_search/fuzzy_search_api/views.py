from rest_framework.response import Response
from rest_framework.views import APIView


class FuzzySearch(APIView):

    def get(self, request, *args, **kwargs):
        try:
            word = request.GET.get('word')
            return Response(
                data='Partial word'+word
            )

        except Exception as exception:
            print(str(exception))
