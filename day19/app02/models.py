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

#表名app02_userinfo，查带外键的数据如下，直接取id或者取用户组对象，然后逐一取对象内部的字段
# user_list = UserInfo.objects.all()
# for row in user_list:
# 	print(row.user_group_id)
# 	print(row.user_group.uid)
# 	print(row.user_group.caption)
class UserInfo(models.Model):
	#
	username = models.CharField(max_length=40)
	password = models.CharField(max_length=64)
	email = models.EmailField(max_length=64,null=True)
	#外键,default创建数据时字段默认值,生成数据库表的时候自动加了个一个id，即user_group_id,而查询user_group的时候则user_group是一个
	#对象，这个对象是一个用户组表对象，即UserGroup，里面包含UserGroup里面的各个字段
	user_group = models.ForeignKey('UserGroup',to_field='uid',default=1,on_delete=models.CASCADE)#(uid,caption,c_time,u_time)`

	user_type_choices=(
		(1, '超级用户'),
		(2, '普通用户'),
		(3, '普普通通用户'),
	)

	user_type_id = models.IntegerField(choices=user_type_choices,default=1)
