from django.shortcuts import render
from collections import OrderedDict

from rest_framework import viewsets
from .serializers import BoardListSerializer, BoardSerializer
from .models import Board
from rest_framework.response import Response


class Board_List_API(viewsets.ViewSet):
    def list(self, request):
        queryset = Board.objects.all()
        serializer = BoardListSerializer(queryset, many=True)
        articles=serializer.data
        articles_dict={}

        for article in articles:
            article_dict=dict(article)
            articles_dict[article_dict['id']]=article_dict
        result=[ele[1] for ele in sorted(articles_dict.items(), key=(lambda x:x[1]["created_at"]), reverse=True)]

        return Response({'result':result})

class Board_API(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

