from django.db import models


# Create your models here.
from django.forms import ModelForm


class User(models.Model):
    # 手机号 姓名 消息 熟车 积分
    tell = models.CharField(max_length=11, primary_key=True)
    myDriver = models.IntegerField()
    points = models.IntegerField()
    password = models.CharField(max_length=16)

class Msg(models.Model):
    tell = models.CharField(max_length=11, primary_key=True)
    content = models.TextField()
    msgTime = models.DateField()
    msgFrom = models.CharField(max_length=20)

class Driver(models.Model):
    # id 姓名 手机号 行驶证 车头车牌照片 身份证照 头像 积分 评价分数 车型 订单数 消息 驾驶证
    name = models.CharField(max_length=255)
    tell = models.CharField(max_length=11, primary_key=True)
    drivingLicence = models.ImageField(upload_to='driver/', blank=True, null=True)  # 添加上传路径？
    certificateOfIdentificationImage = models.ImageField(blank=True, null=True)
    headPortrait = models.ImageField(upload_to='driver/', blank=True, null=True)
    points = models.IntegerField(blank=True, null=True)
    mark = models.IntegerField(blank=True, null=True)
    vehicleType = models.CharField(max_length=30, blank=True, null=True)
    orderNum = models.IntegerField(blank=True, null=True)
    msg = models.TextField(blank=True, null=True)
    driversLicence = models.ImageField(upload_to='driver/', blank=True, null=True)
    licensePlateNumber = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=16)
    status = models.CharField(max_length=16, blank=True, null=True)


class Order(models.Model):
    # id 用车时间 起点 终点 订单状态 额外需求 备注 车型 费用 司机id 用户id 评价 打分 订单时间 接单时间 完成时间
    transportTime = models.CharField(max_length=25, blank=True, null=True)
    start = models.CharField(max_length=100)
    startDetail = models.CharField(max_length=100)
    end = models.CharField(max_length=100)
    endDetail = models.CharField(max_length=100)
    anZhuang = models.CharField(max_length=20, blank=True, null=True)
    huiDan = models.CharField(max_length=20, blank=True, null=True)
    banYun = models.CharField(max_length=20, blank=True, null=True)
    payment = models.IntegerField(blank=True, null=True)
    orderStatus = models.CharField(max_length=50, blank=True, null=True)
    additionalDemand = models.CharField(max_length=50, blank=True, null=True)
    remarks = models.CharField(max_length=300, blank=True, null=True)
    vehicleType = models.CharField(max_length=30)
    pay = models.CharField(max_length=11, blank=True)
    driverId = models.CharField(max_length=11, blank=True, null=True)
    userId = models.CharField(max_length=11)
    contactsTell = models.CharField(max_length=11, blank=True)
    contactsName = models.CharField(max_length=11, blank=True)
    evaluation = models.CharField(max_length=300, blank=True, null=True)
    mark = models.IntegerField(blank=True, null=True)
    orderTime = models.CharField(max_length=25, blank=True, null=True)
    recevingTime = models.CharField(max_length=25, blank=True, null=True)
    finishTime = models.CharField(max_length=25, blank=True, null=True)
    serviceTime = models.CharField(max_length=25, blank=True, null=True)
