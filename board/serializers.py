from rest_framework import serializers
from .models import Board

class BoardSerializer(serializers.ModelSerializer):
  class Meta:
      model = Board # 모델 설정
      fields = ('id','title','description','created_at') # 필드 설정

class BoardListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
            'created_at'
        )

        model = Board