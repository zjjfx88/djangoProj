from django.db import models

# Create your models here.

#用户组
class UserGroup(models.Model):
	uid = models.AutoField(primary_key=True)
	caption = models.CharField(max_length=32)
	#创建时间，添加数据的时候不需要做操作，系统自动添加当前时间
	c_time = models.DateTimeField(auto_now_add=True,null=True)
	#更新时间，更新数据的时候不需要做操作，系统自动添加当前更新时间
	u_time = models.DateTimeField(auto_now=True,null=True)
	#要想让上面自动添加更新时间生效，使用models.objects.filter(id=1).update(caption='CEO'),而是用如下方式
	# obj = UserGroup.objects.filter(id=1).first()
	# obj.caption = 'CEO'
	# obj.save()

#表名app02_userinfo
class UserInfo(models.Model):
	#
	username = models.CharField(max_length=40)
	password = models.CharField(max_length=64)
	email = models.EmailField(max_length=64,null=True)
	#外键
	user_group = models.ForeignKey('UserGroup',to_field='uid',default=1,on_delete=models.CASCADE)

	user_type_choices=(
		(1,'超级用户'),
		(2, '普通用户'),
		(3, '普普通通用户'),
	)

	user_type_id = models.IntegerField(choices=user_type_choices,default=1)