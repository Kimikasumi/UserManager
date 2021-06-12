from django.http import HttpResponse
from .models import DocumentType, City, User
from django.core import serializers
import json


def getuserslist(request):
    if request.method == 'GET':
        user_list = User.objects.all().select_related()
        user_list2 = []
        for user in user_list:
            aux = {"pk": user.pk, "name": user.name, "lastName": user.last_name,
                   "documentNumber": user.document_number,
                   "city": {"pk": user.city.pk, "cityName": user.city.city_name},
                   "documentType": {"pk": user.document_type.pk,
                                    "documentTypeName": user.document_type.document_type_name}}
            user_list2.append(aux)
        print(user_list2)
        json_data = json.dumps(user_list2)
        return HttpResponse(json_data, content_type='application/json')


def createuser(request):
    if request.method == "POST":
        user_json = json.loads(request.body)
        c = City.objects.get(pk=user_json["city"])
        dT = DocumentType.objects.get(pk=user_json["documentType"])
        user = User(document_type=dT, document_number=user_json["documentNumber"], name=user_json["name"],
                    last_name=user_json["lastName"], city=c)
        user.save()
        return HttpResponse(status=204)
    return HttpResponse(request.method, content_type='application/json')


def updateuser(request, user_id):
    if request.method == "PUT":
        user_json = json.loads(request.body)
        c = City.objects.get(pk=user_json["city"])
        dT = DocumentType.objects.get(pk=user_json["documentType"])
        user = User.objects.filter(pk=user_id).update(document_type=dT, document_number=user_json["documentNumber"],
                                                      name=user_json["name"], last_name=user_json["lastName"],
                                                      city=c)
        return HttpResponse(status=204)
    return HttpResponse(request.method, content_type='application/json')


def deleteuser(request, user_id):
    if request.method == "DELETE":
        u = User.objects.filter(pk=user_id).delete()
        return HttpResponse(status=204)
    return HttpResponse(request.method, content_type='application/json')


def getdocumenttypelist(request):
    if request.method == 'GET':
        document_type_list = DocumentType.objects.all()
        data = serializers.serialize('json', document_type_list)
        return HttpResponse(data, content_type='application/json')


def getcitylist(request):
    if request.method == 'GET':
        city_list = City.objects.all()
        data = serializers.serialize('json', city_list)
        return HttpResponse(data, content_type='application/json')


def getdocumenttypebyid(request, document_type_id):
    if request.method == 'GET':
        data = serializers.serialize("json", DocumentType.objects.filter(pk=document_type_id))
        return HttpResponse(data, content_type='application/json')


def createdocumenttype(request):
    if request.method == "POST":
        dt_json = json.loads(request.body)
        dt = DocumentType(document_type_name=dt_json["document_type_name"])
        dt.save()
        # dt_json["document_type_name"]
        return HttpResponse("Document Created!", content_type='plainText')
    return HttpResponse(request.method, content_type='application/json')


def updatedocumenttype(request, document_type_id):
    if request.method == "PUT":
        dt_json = json.loads(request.body)
        dt = DocumentType.objects.filter(pk=document_type_id).update(document_type_name=dt_json["document_type_name"])
        return HttpResponse("Document Updated!", content_type='plainText')
    return HttpResponse(request.method, content_type='application/json')


def deletedocumenttype(request, document_type_id):
    if request.method == "DELETE":
        dt = DocumentType.objects.filter(pk=document_type_id).delete()
        return HttpResponse("Document Deleted!", content_type='plainText')
    return HttpResponse(request.method, content_type='application/json')
