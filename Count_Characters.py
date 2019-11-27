import json
import os
import io
import sys
import ast
import keyboard
import pygame

from PIL import Image
#from io import StringIO
#chinese_dir = 'chinese'
#if not os.path.exists(chinese_dir):
#    os.mkdir(chinese_dir)

def Output_One_Font(word,i):

    count = 0 
    path_count = os.path.join('Count_Result_Font',"Font"+str(i).zfill(3)+".png")
    path_count2 = os.path.join('Count_Result_Font',"Font"+str(i).zfill(3)+".bmp")

    pygame.init()
    #start,end = (0x4E00, 0x4E02)#汉字编码范围
    #for codepoint in range(int(start),int(end)):
    ir = Image.new("RGB", (16, 16), (255, 255, 255))

    #    word = chr(codepoint)
    #word = '我'
    #text = word.encode('utf-8')
    #text = str(word).encode('utf-8')
    text = word
    if os.path.exists('Count_Source_Font.ttf'):
        font = pygame.font.Font("Count_Source_Font.ttf", 12)#当前目录下要有字体文件
    elif os.path.exists('Count_Source_Font.ttc'):
        font = pygame.font.Font("Count_Source_Font.ttc", 12)#当前目录下要有字体文件
    rtext = font.render(text, True, (0, 0, 0), (255, 255, 255))
    pygame.image.save(rtext, path_count)
    im = Image.open(path_count)
    
    move = 8 - int(im.size[0]/2)
    ir.paste(im,(move,0))
    #ip = im.resize((16,16),Image.LANCZOS)
    ir.save(path_count2,'bmp')
    



        





def Func_Count_Txt():
    import json
    import time
    import csv
    import codecs
    import sys
    import io
    import os

    from PIL import Image
    from io import StringIO

 
    if not os.path.exists('Count_Result_Font'):
        os.mkdir('Count_Result_Font')

    Source_File = open(str(Source_File_Path_Txt),'r',encoding='utf-8')
    Source_Content = Source_File.read()
    Source_File.close()
    Source_Dict={}
    for Character in Source_Content:
        Source_Dict[Character]=Source_Content.count(Character)
    #del Source_Dict['\t']
    #del Source_Dict['\n']

    json=json.dumps(Source_Dict,ensure_ascii=False)


    Work_File = os.path.join(str(Work_Path),'Count_Result.txt')
    Result_File = open(str(Work_File),'w+',encoding='utf-8')
    Result_File.write("\n统计执行时间： {}\n\n".format(time.strftime('%Y.%m.%d %H:%M:%S',time.localtime(time.time()))))

    Result_File.write("编码表已输出至： Count_Result.csv \n\n")

    Result_File.write("统计结果如下：\n\n")
    Result_File.write("**************************************************\n")
    Result_File.write("共有字符类型：\n{}\n\n".format(len(Source_Dict)))
    Result_File.write("**************************************************\n")
    Result_File.write("所有字符如下： \n")

    for Key in Source_Dict.keys():
        Result_File.write(str(Key))
    Result_File.write('\n\n')
    Result_File.write("**************************************************\n")
    Result_File.write("各字符详细统计如下： \n")
    Result_File.write(json)
    Result_File.close()

    Work_File_Csv = os.path.join(str(Work_Path),'Count_Result.csv')
    
    R_Count = 16
    C_Count = int(len(Source_Dict)/16)+1

    Num_Line = [[0 for i in range(R_Count)] for i in range(C_Count)]
    k = 0
    for i in range(C_Count):
        for j in range (R_Count):
            if k>=len(Source_Dict):
                Num_Line[i][j]=""
            else:
                Num_Line[i][j] = str(k)
            k = k+1
    print(Num_Line) 

    Key_Line = [[0 for i in range(R_Count)] for i in range(C_Count)]
    Key_Line_Dict = list(Source_Dict.keys())
    #Key_Line_Dict = Source_Dict.items()
    print(Key_Line_Dict)

    k = 0
    for i in range(C_Count):
        for j in range (R_Count):
            if k>=len(Source_Dict):
                Key_Line[i][j]=""
            else:
                Key_Line[i][j] = Key_Line_Dict[k]
                Output_One_Font(Key_Line_Dict[k],k)
            k = k+1

    with open(str(Work_File_Csv),'w+',encoding='utf-8-sig') as f:
        csv_write = csv.writer(f)
        csv_head = ["统计执行时间",time.strftime('%Y.%m.%d %H:%M:%S',time.localtime(time.time()))]
        csv_write.writerow(csv_head)
        for i in range(C_Count):
            csv_write.writerow(Num_Line[i])
            csv_write.writerow(Key_Line[i])


        f.close()




#a-4/b-5/c-6/d-7/e-8/f-9/g-10/h-11/i-12/j-13
#k-14/l-15/m-16/n-17/o-18/p-19/q-20/r-21
def Func_Get_Csv_Key(key):
    import keyboard
    r = keyboard.KeyboardEvent('down',21,'r')#row行
    c = keyboard.KeyboardEvent('down',6,'c')#row列
    if key.event_type == 'down' and key.name == r.name:
        print("r press")
    if key.event_type == 'down' and key.name == c.name:
        print("c press")

Count_Csv_Type = 0

def Func_Count_Csv_Type(type):
    if type==0:
        Count_Csv_Type = 0
        print("将 按行统计 ，",end='')
        print("请按 Enter 键启动 ...")
#        keyboard.unhook_all_hotkeys()
    if type==1:
        Count_Csv_Type = 1
        print("将 按列统计 ，",end='')
        print("请按 Enter 键启动 ...")
#        keyboard.unhook_all_hotkeys()
#    keyboard.write('esc')
#    keyboard.press_and_release('esc')


def Func_Count_Csv():
    import json
    import time
    import csv
    with open(str(Source_File_Path_Csv),'r',encoding='utf-8') as Source_File:
        Line_Count =  len(Source_File.readlines())








print("\n\n*** Program is begin to run ***\n")
print("Program Text Encoding is: ",end='')
print(sys.getdefaultencoding())
print("System Text Encoding is: ",end='')
print(sys.stdout.encoding)
print("Please Make Sure same here.")
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')



print("\n*** 本程序用于统计字符类型及数量 ***\n")

print("当前工作目录为：",end='')  
Work_Path = os.path.dirname(__file__)
print(Work_Path)

print("请将文件名为：Count_Source.txt 或/和 Count_Source.csv 的文件放入工作目录。")  
print("请将文件名为：Count_Source_Font.ttf 或 Count_Source_Font.ttc 的文件放入工作目录。")  
print("输出结果将存放于工作目录下 Count_Result.txt 或/和 Count_Result.csv 文件中。")


#Source_Type=input("Enter: ")




Source_File_Path_Txt = os.path.join(str(Work_Path),'Count_Source.txt')
Source_File_Path_Csv = os.path.join(str(Work_Path),'Count_Source.csv')

Source_File_Txt_Flag = 0
Source_File_Csv_Flag = 0

print("\n准备查找源文件 Count_Source.txt ...")
print("\n* 注意： 回车 及 空格 将被忽略， 同时可能有特殊空格因无法识别而被保留！！！ \n")
print("\n准备好后按 Enter 继续 ...\n")
keyboard.wait('enter')

if os.path.exists(Source_File_Path_Txt):
    print("源文件 Count_Source.txt 存在，开始统计 ...")


    Func_Count_Txt()
    Source_File_Txt_Flag = 1
    print("\n源文件 Count_Source.txt 统计结果已输出至 Count_Result.txt ...")
    print("源文件 Count_Source.txt 编码表已输出至 Count_Result.csv ...")
else:
    print("源文件 Count_Source.txt 不存在，跳过 ...")

#print("\n准备查找源文件 Count_Source.csv ...")
#if os.path.exists(Source_File_Path_Csv):
#    print("源文件 Count_Source.csv 存在，准备开始统计 ...")
#    print("按 r 选择按行统计，按 c 选择按列统计，请按键 ...")
#    print("* 注意： 若检查到连续两行或两列为空，将视为文件结尾 ！！！")
#    Source_File_Csv_Flag = 1
#    keyboard.hook(Func_Get_Csv_Key)
#    keyboard.wait()we
#    keyboard.add_hotkey('r',Func_Count_Csv_Type,args=(0,))
#    keyboard.add_hotkey('c',Func_Count_Csv_Type,args=(1,))
#    keyboard.wait('enter')
#    keyboard.clear_all_hotkeys()
#    Func_Count_Csv()
#    print("源文件 Count_Source.csv 统计结果已输出 ...")
#else:
#
#    print("源文件 Count_Source.csv 不存在，跳过 ...")


if Source_File_Txt_Flag==0 and Source_File_Csv_Flag==0:
    print("\n没有找到任何源文件 ...")
else:
    print("\n源文件 ",end='')
    if Source_File_Txt_Flag==1:
        print("Count_Source.txt ",end='')
    if Source_File_Csv_Flag==1:
        print("Count_Source.csv ",end='')
    print("已处理 ...")    


print("按 Enter 键结束，或直接关闭程序 ...")
keyboard.wait('enter')




