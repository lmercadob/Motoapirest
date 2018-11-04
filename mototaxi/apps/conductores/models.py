from django.db import models

"""
class Moto(models.Model):
	placa=models.CharField(max_length=17, blank=True, default='')
	modelo=models.IntegerField()

	class Meta:
		ordering=('placa',)
"""
class Conductor(models.Model):
	nombre=models.CharField(max_length=110, blank=True)
	identificacion= models.IntegerField()
	correo= models.EmailField()
	celular= models.IntegerField()
	#moto= models.ForeignKey(Moto, on_delete=models.CASCADE)
	placaMoto=models.CharField(max_length=17, blank=True, null=True, default='')
	#foto=models.ImageField(blank=True, null=True)

	class Meta:
		ordering=('identificacion',)