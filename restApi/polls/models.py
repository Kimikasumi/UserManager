from django.db import models


class DocumentType(models.Model):
    document_type_name = models.CharField(max_length=200)

    def __str__(self):
        return self.document_type_name


class City(models.Model):
    city_name = models.CharField(max_length=200)

    def __str__(self):
        return self.city_name


class User(models.Model):
    document_type = models.ForeignKey(DocumentType, on_delete=models.CASCADE, related_name='dT')
    document_number = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='c')

    def __str__(self):
        return "Tipo de documento: " +self.document_type.document_type_name + " Documento: " +\
               self.document_number + " Nombre: " +self.name + " Apellido: " + self.last_name + " Ciudad: " +\
               self.city.city_name
