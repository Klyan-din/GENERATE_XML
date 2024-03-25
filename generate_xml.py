#!/usr/bin/python3
import os
import csv
import subprocess
import glob
from transliterate import translit

# создание кастомного словаря
from transliterate.discover import autodiscover
autodiscover()
from transliterate.base import TranslitLanguagePack, registry


class NOSYMBOLLanguagePack(TranslitLanguagePack):
    language_code = "nosymbol"
    language_name = "nosym"
    mapping = (

       '., {}/\\()?№;:%$&\'',
       '-----------------',
    )


registry.register(NOSYMBOLLanguagePack)
from transliterate import get_available_language_codes, translit
'nosymbol' in get_available_language_codes()


# создание кастомного словаря
#from transliterate.discover import autodiscover
#autodiscover()
#from transliterate.base import TranslitLanguagePack, registry


#class XMLSYMBOLLanguagePack(TranslitLanguagePack):
#    language_code = "xmlsymbol"
#    language_name = "xmlsym"
#pre_processor_mapping = {
#	u"&amp;": u"&",
#}


#registry.register(XMLSYMBOLLanguagePack)

#from transliterate import get_available_language_codes, translit
#'xmlsymbol' in get_available_language_codes()



'''
#texts = 'Ghbd,tn rfr l/tk\.f()?:;'
#print(translit(texts, language_code='nosymbol'))
####
'''

'''
#############диалог выбора принтера или этикетки#####################################
#sxml=open('/opt/LABEL/label.xml', 'r')
#zipf="zip -j "+ tar_name + ".lbx ./label.xml /opt/LABEL/Object1.bmp /opt/LABEL/prop.xml /opt/LABEL/Object0.bmp"
'''

#интерактивное меню

def menu_1(dict_1,question):
    while True:
        print (question)
        for id_dict_1 in dict_1.keys():
            print("\t" + str(id_dict_1) + ")",dict_1[id_dict_1])
        read = input()
        if read in dict_1.keys():
            break
    val=dict_1[read]
    return(val)

def menu_2(dict_2,question_2):
    while True:
        print (question_2)
        for id_dict_2 in dict_2.keys():
            print ("\t"+str(id_dict_2)+') '+ dict_2[id_dict_2][1]) 
        read_2 = input()
        if read_2 in dict_2.keys():
            break
    val_2 = dict_2[read_2][0]
    return(val_2)

def get_id_2(dict_2_,val_2_):
    for item in dict_2_.keys():
        if dict_2_[item][0] == val_2_:
            return(item)

#проверка, где запущен скрипт
run_host = subprocess.run(['hostname'], capture_output=True, text=True)
hst = str(run_host.stdout)
print ("запущено на хосте")
print (hst)

if "RMP-DEBIAN-TECHNO-SHARA" in hst:
    d_path = './'
elif "RMP-STEND-CUBICMEDIA" in hst:
    d_path = '/mnt/vpnsh/'
elif "octopus2" in hst:
    d_path = '/mnt/vpnsh/'
else: d_path = './'

files = sorted(glob.glob(d_path + '*.csv'))
i=1
dict_files={}
for file in files:
    dict_files[str(i)]=file
    i+=1
#print(dict_files)


#Выбор файла CSV
csv_path=menu_1(dict_files,'найдены файлы csv,выберите файл:')

#выбор принтера
#словарь
dict_prnt={
            '1':['710','Q-710'],
            '2':['810','Q-810']
            } 
prnt_fold=menu_2(dict_prnt,'выберите принтер:')

#выбор типа наклейки
dict_service={
            '1':'Music',
            '2':'Vision',
            '3':'Music+Vision'
            } 
service=menu_1(dict_service,'выберите сервис:')


#Выбор наклейки

dict_label_dir_m={
            '1':['LABEL','Music Lines RPI QR'],
            '3':['LABEL_ANDROID_MUSIC','Music Lines Android QR'],
            '4':['LABEL_ANDROID_MUSIC_NO_CONTACT','Music Lines Adndroid QR no contact'],
            '6':['LABEL_ANDROID_MUSIC_TABLE','Music Table Android QR'],
            '8':['LABEL_MUSIC_CMA_TABLE','Music Table CMA QR']
            }  

dict_label_dir_v={
            '2':['LABEL_VISION','Vision Lines no QR'],
            '7':['LABEL_ANDROID_VISION_TABLE','Vision Table no QR']
            } 

dict_label_dir_mv={
            '5':['LABEL_ANDROID_MUSIC_VISION_TABLE','Music+Vision Table Android QR']
            } 

if service in 'Music':
     dict_label_dir=dict_label_dir_m
elif service in 'Vision':
     dict_label_dir=dict_label_dir_v
elif service in 'Music+Vision':
     dict_label_dir=dict_label_dir_mv

#выбор наклейки
label_fold=menu_2(dict_label_dir,'выберите наклейку:')
label_id=get_id_2(dict_label_dir,label_fold)


zipff = " ./label.xml /opt/"+label_fold+"/"+prnt_fold+"/*"

#if label_id in [1,2]:

#режим
dict_rezh={
            '1':'DHCP',
            '2':'STATIC'
            } 

rezhim=menu_1(dict_rezh,'выберите режим:')

'''
#if st == '1' :
#      sta=''
#if st == '2' :
#      sta=" "+l[7]+" "+l[8]+" "+l[9]+" "+l[10]+" "+l[11]+" "+l[12]+" "+l[13]
#    static=" "+l[7]+" "+l[8]+" "+l[9]+" "+l[10]+" "+l[11]+" "+l[12]+" "+l[13]
#    print (static)
'''

#Заголовок ansible hosts
dict_zagol={
            '1':'RASPBERRY',
            '2':'BUSTER'
            }

while True:
    print ('выберите оглавление в hosts файле ansible:')
    for id_zag in dict_zagol.keys():
        print ("\t"+str(id_zag)+") "+dict_zagol[id_zag]) 
    zag_k = input()
    if zag_k in dict_zagol.keys():
        break       
zagolovok_ans = dict_zagol[zag_k]

#изменение файла labels подменой
#открытие файла на чтение
#labcsv = open('./labels_1.csv', 'rt', encoding='utf-8-sig')


#csv_path = './labels_1.csv'
# csv=labcsv.read()
# print(csv)

# удаление файлов и создание пустых
os.system("rm list.txt")
os.system("rm hosts")
os.system("touch list.txt")
os.system("touch hosts")

#добавление заголовка в hosts файл ansible
hosts_ = open('./hosts', "a")
hosts_.write('\n' + "[" + zagolovok_ans + "]" + '\n' + '\n')
hosts_.close()

# читаем строки csv
with open(csv_path, newline='', encoding='utf-8-sig') as csvfile:  
    reader = csv.DictReader(csvfile, delimiter=';')

    for row in reader:
#вывод на экран данные для наклеек
        print (row['id'], \
        row['name_1_org'], \
        row['name_2_city'], \
        row['name_3_street'], \
        row['name_4_tc'], '\n' ,\
        row['org_music'], \
        row['id_music'], \
        row['id_vision'],'\n')

        #, row['license'],\
#        row['time_zone'],\
#        row['address'],\
#        row['netmask_s'],\
#        row['netmask'],\
#        row['gateway'],\
#        row['dnsnameserver1'],\
#        row['dnsnameserver2'],\
#        row['ntp1'],\
#        row['ntp2'])

#for line in labcsv:
#    l = [line.strip() for line in line.split(';')]
#    print (l[1], l[2], l[3], l[4])

# назначение переменных из csv
#    client_name = l[1]
#    point_name = l[2]
#    address_name = l[3]
#    tc_name = l[4]
#    license = l[5]
#    timezone = l[6]
        if not row['license']:
                print("!!!!!!!!!!!!!!!!!!!!!!!!!\n\
                !!!!не указаны значения license\n\
                !!!!!!!!!!!!!!!!!!!!!!!!!\n")
        if not row['time_zone']:
                print("!!!!!!!!!!!!!!!!!!!!!!!!!\n\
                !!!!не указаны значения time_zone\n\
                !!!!!!!!!!!!!!!!!!!!!!!!!\n")
        if not row['ansible_ssh_host']:
                print("!!!!!!!!!!!!!!!!!!!!!!!!!\n\
                !!!!не указаны значения ansible_ssh_host\n\
                !!!!!!!!!!!!!!!!!!!!!!!!!\n")

        pleer_id = row['id']
        client_name = row['name_1_org']
        point_name = row['name_2_city']
        address_name = row['name_3_street']
        tc_name = row['name_4_tc']
        org_music = row['org_music']
        id_music = row['id_music']
        id_vision = row['id_vision']
        license = row['license']
        date = row['date']
        timezone = row['time_zone']
        ansible_ssh_host = row['ansible_ssh_host']
        if rezhim == 'DHCP':
            static = ''
        if rezhim == 'STATIC':
            if not row['address']:
                print("!!!!!!!!!!!!!!!!!!!!!!!!!\n!!!!не указаны значения address\n!!!!!!!!!!!!!!!!!!!!!!!!!")
            if not row['netmask_s']:
                print("!!!!!!!!!!!!!!!!!!!!!!!!!\n!!!!не указаны значения netmask_s\n!!!!!!!!!!!!!!!!!!!!!!!!!")
            if not row['netmask']:
                print("!!!!!!!!!!!!!!!!!!!!!!!!!\n!!!!не указаны значения netmask\n!!!!!!!!!!!!!!!!!!!!!!!!!")
            if not row['gateway']:
                print("!!!!!!!!!!!!!!!!!!!!!!!!!\n!!!!не указаны значения gateway\n!!!!!!!!!!!!!!!!!!!!!!!!!")
            if not row['dnsnameserver1']:
                print("!!!!!!!!!!!!!!!!!!!!!!!!!\n!!!!не указаны значения dnsnameserver1\n!!!!!!!!!!!!!!!!!!!!!!!!!")
            if not row['dnsnameserver2']:
                print("!!!!!!!!!!!!!!!!!!!!!!!!!\n!!!!не указаны значения dnsnameserver2\n!!!!!!!!!!!!!!!!!!!!!!!!!")
            if not row['ntp1']:
                print("!!!!!!!!!!!!!!!!!!!!!!!!!\n!!!!не указаны значения ntp1\n!!!!!!!!!!!!!!!!!!!!!!!!!")
            if not row['ntp2']:
                print("!!!!!!!!!!!!!!!!!!!!!!!!!\n!!!!не указаны значения ntp2\n!!!!!!!!!!!!!!!!!!!!!!!!!")
    
            static = " address=" + row['address'] + \
            " netmask=" + row['netmask_s'] + \
            " gateway=" + row['gateway'] + \
            " dnsnameserver1=" + row['dnsnameserver1'] + \
            " dnsnameserver2=" + row['dnsnameserver2'] + \
            " ntp1=" + row['ntp1'] + \
            " ntp2=" + row['ntp2']
            

        '''
        string1="Test String Trailing space to be added"
        string_length=len(string1)+10    # will be adding 10 extra spaces
        string_revised=string1.ljust(string_length)
        print string_revised
        '''

# выбор того,что переименовать
        client_rename = "        SSSS       "
        point_rename = "           XXXX           "
        address_rename = "           YYYY           "
        tc_rename = "           ZZZZ           "

# вычисление длины образцов переименовываемых строк
        lss = len(client_rename)
        lxx = len(point_rename)
        lyy = len(address_rename)
        lzz = len(tc_rename)
# Получение длины переименовываемых строк 
        lssi = len(client_name)
        lxxi = len(point_name)
        lyyi = len(address_name)
        lzzi = len(tc_name)	
# Вывод сообщения о превышении длины	
        if lssi > lss:
            print ( 'название:', client_name, 'в столбце "name_1_org" обрежется в строке наклейки')
        if lxxi > lxx:
            print ( 'название:', point_name, 'в столбце "name_2_city" обрежется в строке наклейки')	
        if lyyi > lyy:
            print ( 'название:', address_name, 'в столбце "name_3_street" обрежется в строке наклейки')
        if lzzi > lzz:
            print ( 'название:', tc_name, 'в столбце "name_4_tc" обрежется в строке наклейки')
            
        
# обзезка по макс длине перименовываемой строки
        client_name_n = client_name[:lss]
        point_name_n = point_name[:lxx]
        address_name_n = address_name[:lyy]
        tc_name_n = tc_name[:lzz]
# добивка пробелами строки до длины переименовываемой строки
        client_name_nn = client_name_n.ljust(lss)
        point_name_nn = point_name_n.ljust(lxx)
        address_name_nn = address_name_n.ljust(lyy)
        tc_name_nn = tc_name_n.ljust(lzz)

# формирование имени архива и vpn строки
        tar_name = client_name_n+" "\
                   +point_name_n+" "\
                   +address_name_n+" "\
                   +tc_name_n
        tar_name = translit(tar_name, language_code = 'nosymbol').replace("---", "").replace("--", "")
        
        tar_name_id = pleer_id+" "\
                     +client_name_n+" "\
                     +point_name_n+" "\
                     +address_name_n+" "\
                     +tc_name_n
        tar_name_id = translit(tar_name_id, language_code = 'nosymbol').replace("---", "").replace("--", "")

#Нормализация длины для наклеек c id c 1 по 4
# вычисление длины всей строки
        ltn = len(tar_name)
#    print ("last",tar_name[ltn-1:ltn])
        literal = tar_name[ltn-1:ltn]
# проверка на окончание "-"
        if str(literal) == "-":
#       print ("trim")
            tar_name = tar_name[:ltn-1]
        else:
            tar_name = tar_name
            
        print ('\n',\
        'TARNAME, наклейка - без транслитерации:', \
        tar_name, \
        tar_name_id)
            
 #     print ("notrim")

    # tar_name=tar_name.replace(" ", "")

    # texts = 'Ghbd,tn rfr l/tk\.f()?:;'
    # print(translit(texts, language_code='nosymbol'))

#    print ("tar_name",client_name_n,point_name_n,address_name_n,tc_name_n)
#    print (tar_name)

# заполнение строки list.txt, транслитерация замена апострофа
        vpn_txt = translit(tar_name, language_code='ru', reversed=True).upper().replace("'", "").replace("TS", "C")

        print ('hostname,vpn :', vpn_txt)

        list = open('./list.txt', "a")
        list.write(vpn_txt + '\n')
        list.close()

#    vpnline="echo "+vpn_txt+" >> list.txt"
#    os.system( vpnline )

# заполнение строки ansible
# ansibleline="echo "+vpn_txt+" ansible_ssh_host=192.168.88.ххх rmp_name="+vpn_txt+"  rmp_licence="+license+" timez="+timezone+" >> hosts"
        ansibleline = vpn_txt + \
        " ansible_ssh_host=" + ansible_ssh_host + \
        " rmp_name=" + vpn_txt + \
        " rmp_licence=" + license + \
        " timez=" + timezone

#запись в hosts файл
#hosts.write(ansibleline + '\n')
        hosts = open('./hosts', "a")
        hosts.write(ansibleline + static + '\n')
        hosts.close()

#    os.system( ansibleline )
        print ('лицензия:', license, '\n')

# чтение XML
        sxml = open('/opt/' + label_fold + "/" + prnt_fold + '/L/label.xml', 'r')

        content = sxml.read()

##################################
#ДЛЯ НАКЛЕЕК 1-4
        if label_id in ['1','2','3','4']:
# выбор того,что переименовать
            client_rename = "        SSSS       "
            point_rename = "           XXXX           "
            address_rename = "           YYYY           "
            tc_rename = "           ZZZZ           "
            date_rename = "**********"

            contentZ = content.replace(client_rename, client_name_nn)\
            .replace(point_rename, point_name_nn)\
            .replace(address_rename, address_name_nn)\
            .replace(tc_rename, tc_name_nn)\
            .replace(date_rename, date)\
            .replace('&', '&amp;')

            txml = open('./label.xml', "w+")

            txml.write(contentZ)
            txml.close()
            
#Наклейки - таблички
        if label_id in ['5','6','7','8']:
            
            client_rename = "SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS"
            point_rename = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
            address_rename = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY"
            tc_rename = "ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ"
            music_org_rename = "OOOOOO"
            music_id_rename = "IIIIII"
            vision_id_rename = "VVVVVVVVVV"
            date_rename = "**********"
            
            contentVT = content.replace(client_rename, client_name)\
            .replace(point_rename, point_name)\
            .replace(address_rename, address_name)\
            .replace(tc_rename, tc_name)\
            .replace(music_org_rename, org_music)\
            .replace(music_id_rename, id_music)\
            .replace(vision_id_rename, id_vision)\
            .replace(date_rename, date)\
            .replace('&', '&amp;')

            txmlt = open('./label.xml', "w+")
            txmlt.write(contentVT)
            txmlt.close()
        
 #создание архива (файла .lbx)       
    # zip ssss.lbx ./label.xml ./Object1.bmp ./prop.xml  ./Object0.bmp
    # sentence.replace(" ", "")


#    zipf="zip -j "+ tar_name + ".lbx ./label.xml /opt/LABEL/Object1.bmp /opt/LABEL/prop.xml /opt/LABEL/Object0.bmp"

        os.system("zip -j " + tar_name_id + ".lbx " + zipff)
        print("\n")

# хук-замена в последней строке файла list.txt символа перевода строки в конце файла
# читаем и удаляем последний символ в памяти
list = open('./list.txt', 'r')
lists = list.read()
listss = lists[:-1]
list.close()
# записываем без перевода строки
listn = open('./list.txt', "w+")
listn.write(listss)
listn.close()

    # s=[s for s in l]
    # print (s)

# with open(filename) as file:    lines = file.readlines()    lines = [line.rstrip() for line in lines]
# lines = labcsv.readlines()
# print (lines)

# !echo {tar_name}
#labcsv.close()
csvfile.close()
# удаляем модифицированный lanbel.xml
os.system('rm ./label.xml')
# f.close()

