from rest_framework import viewsets
import boto.dynamodb
from boto.dynamodb2.table import Table, Item
from rest_framework.response import Response
from ApiDataLab.serializers import AutorSerializer
from django.shortcuts import get_object_or_404

class dynamo_viewset(viewsets.ModelViewSet):

    conn=boto.connect_dynamodb()
    table=conn.get_table("Thread")
    result = table.query(hash_key='forum-87')

    serializer_class = AutorSerializer
    queryset = result.response['Items']

    def create(self, request, *args, **kwargs):
        """
        Función POST para agregar una nueva entrada en la base de datos
        """
        tabla= Table('Thread')
        author = Item(tabla, data={'forum_name': self.request.data['forum_name'],'subject': self.request.data['subject'],'views': self.request.data['views'], 'replies': self.request.data['replies']})
        author.save()

        result = self.table.query(hash_key=self.request.data['forum_name'])
        data = result.response['Items']
        print(data)
        return  Response(data)


    def retrieve(self, request, *args, **kwargs):
        """
        Retornar un elemento
        """
        print("Retrieve")
        data = self.table.get_item(hash_key="forum-87")
        return Response(data)

    def destroy(self, request, *args, **kwargs):
        """
        Eliminar un elemento de base de datos
        """

    def update(self, request, *args, **kwargs):
        """
        Actualizar un elemento en base de datos
        """