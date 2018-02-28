from django.db import models

# Create your models here.

class Business(models.Model):
	#id 自动创建
	caption = models.CharField(max_length=32)

class Host(models.Model):
	nid = models.AutoField(primary_key=True)
	hostname = models.CharField(max_length=32,db_index=True)
	ip = models.GenericIPAddressField(db_index=True)
	port = models.IntegerField()
	#创建外键，和Business进行关联，约束host当中主机的业务线
	b = models.ForeignKey(to="Business",to_field='id',on_delete=models.CASCADE)