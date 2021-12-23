from decimal import Decimal

from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse, HttpResponseRedirect
from django.core import serializers
from qxs.models import *
import json
from django.db.models import Q

# Create your views here.
#登录
def Login(request):
    reso = request.body
    res = json.loads(reso.decode('utf-8'))
    name = res.get('username')
    pwd = res.get('password')
    user = QxsUsers.objects.filter(username=name)
    status = 'failed'
    role = -1
    if user and user[0] and user[0].password == pwd:
        request.session['user'] = name
        role = user[0].role
        status = 'success'
    msg = {
        'status':status,
        'username':name,
        'role':role
    }
    return JsonResponse(msg)
#登出
def Logout(request):
    request.session.flush()
    return HttpResponseRedirect('')

# 改密码
def resetPw(request):
    reso = request.body
    res = json.loads(reso)
    oldpw = res.get('oldpw')
    newpw = res.get('newpw')
    username = res.get('username')
    user = QxsUsers.objects.filter(username=username)
    status = 'failed'
    if user and user[0] and user[0].password == oldpw:
        user[0].password = newpw
        print(username,newpw)
        user[0].save()
        status = 'success'
    msg = {
        'status':status
    }
    return JsonResponse(msg)



#查询学生信息
def StuInfo(request):
    res = request.GET
    st_id = res.get('st_id')
    stus = QianxuesenQianxuesenQianxuesenst.objects.filter(st_id = st_id)
    status = 'failed'
    st_name = None
    if stus and stus[0]:
        status = 'success'
        st_name = stus[0].st_name
    msg = {
        'status':status,
        'st_name':st_name,
        'st_id':st_id
    }
    return JsonResponse(msg)

#2021培养方案------学生选课详情------查看选课情况
def qianxuesen_Getxuanke(request):
    res=request.GET
    st_id=res.get('st_id')
    clist=[]
    datas=QianxuesenQianxuesenQianxuesen.objects.filter(st_id=st_id)
    list=QxsTeaRate.objects.filter(st_id=st_id)
    if datas:
        for data in datas:
            ispj = False
            for item in list:
                if item.cl_cid==data.cl_cid:
                    ispj = True
                    break
            if data.cl_name == "毕业实习":
                ispj = True
            clist.append(
                {"cl_name": data.cl_name, "cl_cid": data.cl_cid, "cl_id": data.cl_id, "cl_credit": data.cl_credit, "teacher":data.teacher,"ispj":ispj})
    status = 'success'
    msg = {
        'status': status,
        'clist':clist
    }
    return JsonResponse(msg)

#评教
'''
注意：1.   此处接收数据为JSON
      2.  由于精度问题，评教的分数存在误差
'''
def Pingjiao(request):
    reso = request.body
    res = json.loads(reso)
    cl_cid = res.get('cl_cid')
    cl_name = res.get('cl_name')
    teacher = res.get('teacher')
    point = res.get('point')
    adv = res.get('advice')
    st_id = res.get('st_id')
    cl_id = res.get('cl_id')

    status = 'failed'
     # 评教信息就结束
    if QxsTeaRate.objects.filter(st_id=st_id).filter(cl_cid=cl_cid):
        msg = {
            'status': status
        }
        return JsonResponse(msg)
    # 插入评教信息
    t_rate = QxsTeaRate(cl_cid=cl_cid, cl_name=cl_name, teacher=teacher, point=point, adv=adv, st_id=st_id,cl_id=cl_id)
    t_rate.save()

    # 设置教师信息
    cl_school = ''
    teacher_id = ''
    teainfo = QianxuesenQianxuesenKebiao.objects.filter(cl_cid=cl_cid,teacher=teacher)
    if len(teainfo)>0:
        cl_school = teainfo[0].cl_school
        teacher_id = teainfo[0].teacher_id

    # 插入教师信息（不可重复）
    rate_details = QxsRatedetils.objects.filter(teacher_id=teacher_id,cl_id=cl_id)
    if len(rate_details)==0:
        newdetails = QxsRatedetils(cl_school=cl_school,cl_cid=cl_cid,cl_id=cl_id,teacher_id=teacher_id,teacher=teacher,cl_name=cl_name,num=0)
        newdetails.save()
    status = 'success'
    msg = {
        'status':status
    }
    return JsonResponse(msg)

def list(request):
    res = request.GET
    pagenum = int(res.get('pagenum'))
    pagesize = int(res.get('pagesize'))
    updatedetails()
    datas = QxsRatedetils.objects.all().order_by('-cl_school')
    print(datas)
    list = []
    total = len(datas)

    if datas:
        if pagenum*pagesize in range(total):
            for index in range((pagenum-1)*pagesize,pagenum*pagesize):
                list.append(
                    {'cl_school':datas[index].cl_school,'cl_cid':datas[index].cl_cid,
                     'cl_name':datas[index].cl_name,'teacher':datas[index].teacher,
                     'num':datas[index].num,'point':datas[index].point,'id':datas[index].id
                     }
                )
        elif (pagenum-1)*pagesize in range(total):
            for index in range((pagenum - 1) * pagesize, total):
                list.append(
                    {'cl_school': datas[index].cl_school, 'cl_cid': datas[index].cl_cid,
                     'cl_name': datas[index].cl_name, 'teacher': datas[index].teacher,
                     'num': datas[index].num, 'point': datas[index].point,'id':datas[index].id
                     }
                )

    status = 'success'
    msg = {
        'list':list,
        'total':total,
        'status':status
    }
    return JsonResponse(msg)

#更新教师评价数据
def updatedetails():
    datas = QxsRatedetils.objects.all()
    for data in datas:
        teacher = data.teacher
        cl_cid = data.cl_cid
        rates = QxsTeaRate.objects.filter(cl_cid=cl_cid,teacher=teacher)
        if len(rates)==data.num:
            break;
        # 各分段统计
        excellent = 0  # 评分>=90
        good = 0  # >=80,<90
        common = 0  # >=70,<80
        passed = 0  # >=60,<70
        nopass = 0  # <60
        # 平均分
        average = 0
        for rate in rates:
            average += rate.point
            if rate.point >= 90:
                excellent += 1
            elif rate.point >= 80 and rate.point < 90:
                good += 1
            elif rate.point >= 70 and rate.point < 80:
                common += 1
            elif rate.point >= 60 and rate.point < 70:
                passed += 1
            else:
                nopass += 1

        average = average/len(rates)

        data.num = len(rates)
        data.point = average
        data.excellent = excellent
        data.good = good
        data.common = common
        data.passed = passed
        data.nopass = nopass
        data.save()

#查看评教详情
def details(request):
    status = 'failed'
    res = request.GET
    id = res.get('id')
    data = QxsRatedetils.objects.filter(id=id)
    teacher = ''
    cl_name = ''
    cl_school = ''
    num = 0
    advnum = 0
    list = []
    if data:
        teacher=data[0].teacher
        cl_name=data[0].cl_name
        cl_school=data[0].cl_school
        num=data[0].num
        advs=QxsTeaRate.objects.filter(teacher=teacher,cl_name=cl_name)
        if advs:
            advnum=len(advs)
            for adv in advs:
                list.append(
                    {'adv':adv.adv}
                )
        status='success'
    msg ={
        'status':status,
        'teacher':teacher,
        'cl_name':cl_name,
        'cl_school':cl_school,
        'num':num,
        'advnum':advnum,
        'list':list,
    }
    return JsonResponse(msg)

def Charts(request):
    status = 'failed'
    res = request.GET
    id = res.get('id')
    data = QxsRatedetils.objects.filter(id=id)
    bar = []
    if data:
        bar = [data[0].nopass, data[0].passed, data[0].common,
               data[0].good, data[0].excellent]
        status = 'success'
    msg = {
        'status':status,
        'bar':bar
    }
    return JsonResponse(msg)
#index
def index(request):
    return HttpResponse('')