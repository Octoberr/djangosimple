from django.shortcuts import render
# 导入数据库
from swmtt.models import UserMessage
# Create your views here.


def getform(request):
    # all_message = UserMessage.objects.all()
    # for message in all_message:
    #     print(message.name)
    usr = UserMessage()
    if request.method == "POST":
        name = request.POST.get('name', '')
        message = request.POST.get('message',  '')
        address = request.POST.get('address', '')
        email = request.POST.get('email', '')
        usr.name = name
        usr.message = message
        usr.address = address
        usr.email = email
        usr.object_id = 'c'
        usr.save()
    # 删除数据
    allmessage = UserMessage.objects.all()
    querymessage = allmessage[0]
    # allmessage.delete()
    return render(request, 'message_form.html', {"my_message":  querymessage})
    # all_message = UserMessage.objects.all()
    # print(all_message)
    # 保存数据
    # user = UserMessage()
    # user.name = "nuonuo"
    # user.message = "I would find you!"
    # user.address = "成都眉山"
    # user.email = "772827245@gmail.com"
    # user.objects = "b"
    # user.save()