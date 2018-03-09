from django.db import models

# Create your models here.

class Business(models.Model):
	#id 自动创建
	caption = models.CharField(max_length=32)
	#新增一列code用来存储英文名字，如果执行makemigrations会报错，一种是根据报错提示输入一个默认是完成增加列
	#另一种是在增加列名的时候增加null=True（不加的话默认不允许为空）
	code = models.CharField(max_length=32,null=True)

class Host(models.Model):
	nid = models.AutoField(primary_key=True)
	hostname = models.CharField(max_length=32,db_index=True)
	ip = models.GenericIPAddressField(db_index=True)
	port = models.IntegerField()
	#创建外键，和Business进行关联，约束host当中主机的业务线
	b = models.ForeignKey(to="Business",to_field='id',on_delete=models.CASCADE)

class Application(models.Model):
	name = models.CharField(max_length=32)
	#自动创建关系表，创建多对多的第二种方式
	r = models.ManyToManyField("Host")

#自定义关系表，创建多对多的一种方式
# class HostToApp(models.Model):
# 	hobj = models.ForeignKey(to='Host',to_field='nid',on_delete=models.CASCADE)
# 	aobj = models.ForeignKey(to='Application',to_field='id',on_delete=models.CASCADE)