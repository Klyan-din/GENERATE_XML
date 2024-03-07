import os
import csv
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
while True:
	print ('выберите принтер для генерации наклеек \n    1) Q-710\n    2) Q-810')
	sf = input()
    # print (sf)
	if sf == '1' or sf == '2':
		break



if sf == '1':
		sxmlfold = '710'
if sf == '2':
		sxmlfold = '810'


			
# print( sxmlfold )
while True:
	print ('выберите наклейку \n    1) Music\n    2) Vision\n    3) Music Android')
	uf = input()
# print (sf)
	if uf == '1' or uf == '2' or uf == '3':
		break

if uf == '1':
    lfld = 'LABEL'
if uf == '2':
    lfld = 'LABEL_VISION'
if uf == '3':
    lfld = 'LABEL_ANDROID_MUSIC'

zipff = " ./label.xml /opt/"+lfld+"/"+sxmlfold+"/*"

while True:
	print ('выберите режим \n    1) DHCP\n    2) STATIC')
	st = input()
	# print (sf)
	if st == '1' or st == '2':
		break

'''
#if st == '1' :
#      sta=''
#if st == '2' :
#      sta=" "+l[7]+" "+l[8]+" "+l[9]+" "+l[10]+" "+l[11]+" "+l[12]+" "+l[13]
#    static=" "+l[7]+" "+l[8]+" "+l[9]+" "+l[10]+" "+l[11]+" "+l[12]+" "+l[13]
#    print (static)
'''
while True:
	print ('выберите оглавление в hosts файле ansible \n    1) RASPBERRY\n    2) BUSTER')
	za = input()
	# print (sf)
	if za == '1' or za == '2':
		break

if za == '1':
    zag = 'RASPBERRY'
if za == '2':
    zag = 'BUSTER'


# открытие файла на чтение
#labcsv = open('./labels_1.csv', 'rt', encoding='utf-8-sig')
csv_path = './labels.csv'
# csv=labcsv.read()
# print(csv)

# удаление файлов и создание пустых
os.system("rm list.txt")
os.system("rm hosts")
os.system("touch list.txt")
os.system("touch hosts")

hosts_ = open('./hosts', "a")
hosts_.write('\n' + "[" + zag + "]" + '\n' + '\n')
hosts_.close()

# читаем строки csv


with open(csv_path, newline='', encoding='utf-8-sig') as csvfile:  
	reader = csv.DictReader(csvfile, delimiter=';')
	for row in reader:
		print (row['id'], row['name_1_org'], row['name_2_city'], row['name_3_street'], row['name_4_tc'])
		#, row['license'], row['time_zone'], row['address'], row['netmask_s'], row['netmask'], row['gateway'], row['dnsnameserver1'], row['dnsnameserver2'],row['ntp1'], row['ntp2'])



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
				print("!!!!!!!!!!!!!!!!!!!!!!!!!\n!!!!не указаны значения license\n!!!!!!!!!!!!!!!!!!!!!!!!!")
		if not row['time_zone']:
				print("!!!!!!!!!!!!!!!!!!!!!!!!!\n!!!!не указаны значения time_zone\n!!!!!!!!!!!!!!!!!!!!!!!!!")
		if not row['ansible_ssh_host']:
				print("!!!!!!!!!!!!!!!!!!!!!!!!!\n!!!!не указаны значения ansible_ssh_host\n!!!!!!!!!!!!!!!!!!!!!!!!!")

    
		client_name = row['name_1_org']
		point_name = row['name_2_city']
		address_name = row['name_3_street']
		tc_name = row['name_4_tc']
		license = row['license']
		timezone = row['time_zone']
		ansible_ssh_host = row['ansible_ssh_host']
		if st == '1':
			static = ''
		if st == '2':
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
				print("!!!!!!!!!!!!!!!!!!!!!!!!!\n!!!!не указаны значения netmask_s\n!!!!!!!!!!!!!!!!!!!!!!!!!")
			if not row['ntp2']:
				print("!!!!!!!!!!!!!!!!!!!!!!!!!\n!!!!не указаны значения netmask_s\n!!!!!!!!!!!!!!!!!!!!!!!!!")												
				
			static = " address=" + row['address'] + " netmask=" + row['netmask_s'] + " gateway=" + row['gateway'] + " dnsnameserver1=" + row['dnsnameserver1'] + " dnsnameserver2=" + row['dnsnameserver2'] + " ntp1=" + row['ntp1'] + " ntp2=" + row['ntp2']
#    static = sta
#    print (static)
# +"["+l[0]+"]"

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
		tar_name = client_name_n+" "+point_name_n+" "+address_name_n+" "+tc_name_n
		tar_name = translit(tar_name, language_code = 'nosymbol').replace("---", "").replace("--", "")


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
			
		print ("TARNAME, наклейка - без транслитерации:", tar_name)			
			
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
		ansibleline = vpn_txt + " ansible_ssh_host=" + ansible_ssh_host + " rmp_name=" + vpn_txt + "  rmp_licence=" + license + " timez=" + timezone

		hosts = open('./hosts', "a")
#    hosts.write(ansibleline + '\n')
		hosts.write(ansibleline + static + '\n')
		hosts.close()

#    os.system( ansibleline )
		print ('лицензия:', license)

    # print( client_name )


		sxml = open('/opt/' + lfld + "/" + sxmlfold + '/L/label.xml', 'r')

		content = sxml.read()

    ##################################
         
		contentS = content.replace(client_rename, client_name_nn).replace('&', '&amp;')
		contentX = contentS.replace(point_rename, point_name_nn).replace('&', '&amp;')
		contentY = contentX.replace(address_rename, address_name_nn).replace('&', '&amp;')
		contentZ = contentY.replace(tc_rename, tc_name_nn).replace('&', '&amp;')

		txml = open('./label.xml', "w+")

		txml.write(contentZ)
		txml.close()
    # zip ssss.lbx ./label.xml ./Object1.bmp ./prop.xml  ./Object0.bmp
    # sentence.replace(" ", "")


#    zipf="zip -j "+ tar_name + ".lbx ./label.xml /opt/LABEL/Object1.bmp /opt/LABEL/prop.xml /opt/LABEL/Object0.bmp"
		zipf = "zip -j " + tar_name + ".lbx " + zipff
		os.system(zipf)
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

