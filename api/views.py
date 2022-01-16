from django.shortcuts import render
from api.pagination import StandardResultsSetPagination
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProfileSerializer
from .models import Profile

from django.db.models import Q



@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/users',
		'Create':'/users/',
		'Detail View' : '/users/<str:pk>/',
		'Update':'/users/<str:pk>/',
		'Delete':'/users/<str:pk>/',
	}
	return Response(api_urls)



@api_view(['GET', 'POST'])
def users_list(request):
	profile = Profile.objects.all()
	if request.method == 'POST':
		serializer = ProfileSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()

			return Response(serializer.data)

	#This is to load all the sample data into the database
	#Sample data gotten from https://datapeace-storage.s3-us-west-2.amazonaws.com/dummy_data/users.json
	# if request.method == 'POST':
	# 	datas = request.data
	# 	for data in datas:
	# 		serializer = ProfileSerializer(data=data)
	# 		if serializer.is_valid():
	# 			serializer.save()

		# return Response(serializer.data)

	name = request.GET.get('name')
	sort = request.GET.get('sort')
	profiles = Profile.objects.all().order_by('id')
	if name:
		profiles = Profile.objects.filter( Q(first_name__icontains=name) | Q(last_name__contains=name))
		if sort:
			profiles = profiles.order_by(f'{sort}')
	elif sort:
		profiles = profiles.order_by(f'{sort}')

	serializer = ProfileSerializer(profiles, many=True)

	if len(profiles)> 0:
		paginator = StandardResultsSetPagination()
		result_page = paginator.paginate_queryset(profiles, request)
		serializer = ProfileSerializer(result_page, many=True)
		return paginator.get_paginated_response(serializer.data)
	
	return Response({},status=status.HTTP_200_OK)




@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, id):
	profile = Profile.objects.get(id=id)
	serializer = ProfileSerializer(profile, many=False)

	if request.method == 'PUT':
		serializer = ProfileSerializer(instance=profile, data=request.data)

		if serializer.is_valid():
			serializer.save()

			return Response(serializer.data)

		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	if request.method == 'DELETE':
		profile.delete()
		return Response("User successfully Deleted")


	return Response(serializer.data)




