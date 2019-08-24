from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Bank
from .serializers import BankSerializer
from rest_framework.views import APIView
from api.settings import BASE_DIR
import os
import csv
import json
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination


@csrf_exempt
def feed_data(request):
	file_path = os.path.join(BASE_DIR, 'app/bank_branches.csv')

	for bank in Bank.objects.all():
		if Bank.objects.filter(ifsc=bank.ifsc).count() > 1:
			bank.delete()


	with open(file_path) as f:
		reader = csv.reader(f)
		counter = 0

		for read in reader:
			if counter == 0:
				counter = 1
				continue
			if counter == 1000:
				break

			temp, created = Bank.objects.get_or_create(
				ifsc=read[0], 
				bank_id=read[1], 
				branch=read[2], 
				address=read[3], 
				city=read[4], 
				district=read[5], 
				state=read[6], 
				bank_name=read[7]
			)
			counter += 1

	return HttpResponse('done')


class bank_list(APIView):
	permission_classes = (IsAuthenticated,)
	
	def get(self, request, ifsc):
		# body_unicode = request.body.decode("utf-8")
		# body = json.loads(body_unicode)
		# ifsc = body['ifsc']
		obj = Bank.objects.get(ifsc=ifsc)
		serializer = BankSerializer(obj)
		pagination_class = LimitOffsetPagination
		return JsonResponse(serializer.data)


class branch_list(APIView):
	permission_classes = (IsAuthenticated,)

	def get(self, request, bank_name, city):
		# body_unicode = request.body.decode("utf-8")
		# body = json.loads(body_unicode)
		# bank_name = body['bank_name']
		# city = body['city']

		bank_name = bank_name.replace("%20", " ")
		# pagination_class = api_settings.DEFAULT_PAGINATION_CLASS
		obj = Bank.objects.filter(
			bank_name=bank_name,
			city=city
		)
	    page = self.paginate_queryset(obj)
	    if page in not None:
	    	serializer = BankSerializer(page, many=True)
	    	return self.get_paginated_response(serializer.data)

	    serializer = BankSerializer(obj, many=True)
	    return JsonResponse(serializer.data, safe=False)

	    # serializer = BankSerializer(page, many=True)

	    # return paginator.get_paginated_response(serializer.data)


		serializer = BankSerializer(obj, many=True)
		pagination_class = LimitOffsetPagination
		# pagination_class = DEFAULT_PAGINATION_CLASS
		return JsonResponse(serializer.data, safe=False)
