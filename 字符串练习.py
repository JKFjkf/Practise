phone_number = '1386-666-0006'
hiding_number = phone_number.replace(phone_number[:9],'*'*9)
print(hiding_number)


#寻找含168的字段
serch = '168'
num_a = '1386-168-0006'
num_b = '1681-222-0006'
print(serch+' is at '+str(num_a.find(serch))+' to '+str(num_a.find(serch)+len(serch))+' of nmu_a')


city = input("请输入你的城市：")
url = "http://apistore.baidu.com/microservice/weather?citypinyin={}".format(city)
print(url)