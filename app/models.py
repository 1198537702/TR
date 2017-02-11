from django.db import models


# Create your models here.
class User(models.Model):
    # 手机号 姓名 消息 熟车 积分
    tell = models.CharField(max_length=11, primary_key=True)
    name = models.CharField(max_length=255)
    myDriver = models.IntegerField()
    points = models.IntegerField()


class Msg(models.Model):
    tell = models.CharField(max_length=11, primary_key=True)
    content = models.TextField()
    msgTime = models.DateField()
    msgFrom = models.CharField(max_length=20)

class Driver(models.Model):
    # id 姓名 手机号 行驶证 车头车牌照片 身份证照 头像 积分 评价分数 车型 订单数 消息 驾驶证
    id = models.IntegerField
    name = models.CharField(max_length=255)
    tell = models.CharField(max_length=11)
    drivingLicence = models.ImageField()  # 添加上传路径？
    carImage = models.ImageField()
    certificateOfIdentificationImage = models.ImageField()
    headPortrait = models.ImageField()
    points = models.IntegerField()
    mark = models.IntegerField()
    vehicleType = models.CharField(max_length=30)
    orderNum = models.IntegerField()
    msg = models.TextField()
    driversLicence = models.ImageField()


class Order(models.Model):
    # id 用车时间 起点 终点 订单状态 额外需求 备注 车型 费用 司机id 用户id 评价 打分 订单时间 接单时间 完成时间
    id = models.IntegerField
    transportTime = models.TimeField()
    startingPoint = models.CharField(max_length=100)
    end = models.CharField(max_length=100)
    orderStatus = models.CharField(max_length=50)
    additionalDemand = models.CharField(max_length=50)
    remarks = models.CharField(max_length=300)
    vehicleType = models.CharField(max_length=30)
    pay = models.IntegerField()
    driverId = models.IntegerField()
    userId = models.IntegerField()
    evaluation = models.CharField(max_length=300)
    mark = models.IntegerField()
    orderTime = models.TimeField()
    recevingTime = models.TimeField()
    finishTime = models.TimeField()


