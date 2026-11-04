from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Project
from .serializers import ProjectSerializer


@api_view(['GET', 'POST'])
def project_list(request):

    if request.method == 'GET':
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)

        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ProjectSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)
    

  # Project detail operations by project ID

@api_view(['GET', 'PUT', 'DELETE'])
def project_detail(request, pk):

    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return Response(
            {'error': 'Project not found'},
            status=404
        )

    if request.method == 'GET':
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = ProjectSerializer(
            project,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    if request.method == 'DELETE':
        project.delete()
        return Response(
            {'message': 'Project deleted successfully'},
            status=200
        )