from django.contrib.auth import get_user_model
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from link.models import News

from rest_framework.views import APIView
from rest_framework.response import Response


User = get_user_model()


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        items = (
            News.objects.all()
            .values("pub_date__year", "pub_date__month")
            .annotate(total=Count("id"))
        )
        labels = []
        default_items = []
        for item in items:
            print(item)
            labels.append(
                f"{str(item['pub_date__year'])}-{str(item['pub_date__month'])}"
            )
            default_items.append(item["total"])
        data = {
            "labels": labels,
            "default": default_items,
        }
        return Response(data)
