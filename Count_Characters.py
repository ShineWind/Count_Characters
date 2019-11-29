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

def Output_One_Font(output_path,word,i):
    from PIL import Image

    work_path = os.path.join(output_path+'/Font_Img_Output')

    if not os.path.exists(work_path):
        os.mkdir(work_path)

    Folder_PNG = os.path.join(work_path+'/Font_Img_PNG')
    if not os.path.exists(Folder_PNG):
        os.mkdir(Folder_PNG)

    Folder_RGB888 = os.path.join(work_path+'/Font_Img_RGB888')
    if not os.path.exists(Folder_RGB888):
        os.mkdir(Folder_RGB888)

    Folder_BIT256P = os.path.join(work_path+'/Font_Img_BIT256P')
    if not os.path.exists(Folder_BIT256P):
        os.mkdir(Folder_BIT256P)

    Folder_BIT256L = os.path.join(work_path+'/Font_Img_BIT256L')
    if not os.path.exists(Folder_BIT256L):
        os.mkdir(Folder_BIT256L)

    count = 0 
    Path_PNG = os.path.join(Folder_PNG,"Font"+str(i).zfill(3)+".png")
    Path_RGB888 = os.path.join(Folder_RGB888,"Font"+str(i).zfill(3)+".bmp")
    Path_BIT256P = os.path.join(Folder_BIT256P,"Font"+str(i).zfill(3)+".bmp")
    Path_BIT256L = os.path.join(Folder_BIT256L,"Font"+str(i).zfill(3)+".bmp")

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
    pygame.image.save(rtext, Path_PNG)
    im = Image.open(Path_PNG)
    
    move = 8 - int(im.size[0]/2)
    ir.paste(im,(move,0))
    #ip = im.resize((16,16),Image.LANCZOS)
    #ir = ir.convert("I;16L")
    ir.save(Path_RGB888,'bmp')
    iz = ir.convert("P")
    iz.save(Path_BIT256P,'bmp')
    iy = ir.convert("L")
    iz.save(Path_BIT256L,'bmp')
    



        





def Func_Count_Txt(file_path,work_path,output_path):
    import json
    import time
    import csv
    import codecs
    import sys
    import io
    import os

    from PIL import Image
    from io import StringIO

 
    #if not os.path.exists('Count_Result_Font'):
    #    os.mkdir('Count_Result_Font')

    #Source_File = open(str(Source_File_Path_Txt),'r',encoding='utf-8')
    Source_File = open(file_path,'r',encoding='utf-8')
    Source_Content = Source_File.read()
    Source_File.close()
    Source_Dict={}
    for Character in Source_Content:
        Source_Dict[Character]=Source_Content.count(Character)
    #del Source_Dict['\t']
    #del Source_Dict['\n']

    json=json.dumps(Source_Dict,ensure_ascii=False)


    Work_File = os.path.join(output_path,'Count_Result.txt')
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

    Work_File_Csv = os.path.join(output_path,'Count_Result.csv')
    
    R_Count = 16
    C_Count = int(len(Source_Dict)/16)+1

    Num_Line = [[0 for i in range(R_Count+1)] for i in range(C_Count)]
    k = 0
    for i in range(C_Count):
        for j in range (R_Count+1):
            if k>=len(Source_Dict):
                Num_Line[i][j]=""
            else:
                if(j !=0):
                    Num_Line[i][j] = str(k)
                    k = k+1
                else:
                    Num_Line[i][j] = "编号："
    #print(Num_Line) 

    Key_Line = [[0 for i in range(R_Count+1)] for i in range(C_Count)]
    Key_Line_Dict = list(Source_Dict.keys())
    #Key_Line_Dict = Source_Dict.items()
    print(Key_Line_Dict)

    k = 0
    for i in range(C_Count):
        for j in range (R_Count+1):
            if k>=len(Source_Dict):
                Key_Line[i][j]=""
            else:
                if(j !=0):
                    Key_Line[i][j] = Key_Line_Dict[k]
                    Output_One_Font(output_path,Key_Line_Dict[k],k)
                    k = k+1
                else:
                    Key_Line[i][j] = "字符："

    Cnt_Line = [[0 for i in range(R_Count+1)] for i in range(C_Count)]
    Cnt_Line_Dict = list(Source_Dict.values())
    #Key_Line_Dict = Source_Dict.items()
    print(Cnt_Line_Dict)

    k = 0
    for i in range(C_Count):
        for j in range (R_Count+1):
            if k>=len(Source_Dict):
                Cnt_Line[i][j]=""
            else:
                if(j !=0):
                    Cnt_Line[i][j] = Cnt_Line_Dict[k]
                    k = k+1
                else:
                    Cnt_Line[i][j] = "数量："


    with open(str(Work_File_Csv),'w+',encoding='utf-8-sig') as f:

        csv_write = csv.writer(f, lineterminator='\n')
        csv_head = ["统计执行时间：",time.strftime('%Y.%m.%d %H:%M:%S',time.localtime(time.time()))]
        csv_write.writerow(csv_head)
        csv_write.writerow("")
        Row = ["字符总数：",str(len(Source_Dict))]
        csv_write.writerow(Row)
        csv_write.writerow("")
        for i in range(C_Count):
            csv_write.writerow(Num_Line[i])
            csv_write.writerow(Key_Line[i])
            csv_write.writerow(Cnt_Line[i])
            csv_write.writerow("")

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





def Main_Function():


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

    Output_Path = os.path.join(str(Work_Path),'Count_Characters_Output')

    if not os.path.exists(str(Output_Path)):
        os.mkdir(str(Output_Path))


    Source_File_Path_Txt = os.path.join(str(Work_Path),'Count_Source.txt')
    Source_File_Path_Csv = os.path.join(str(Work_Path),'Count_Source.csv')

    Source_File_Txt_Flag = 0
    Source_File_Csv_Flag = 0

    print("\n准备查找源文件 Count_Source.txt ...")
    print("\n* 注意： 回车 及 空格 将被忽略， 同时可能有特殊空格因无法识别而被保留！！！ \n")
    print("\n准备好后按 Enter 继续 ...\n")
    #keyboard.wait('enter')

    if os.path.exists(Source_File_Path_Txt):
        print("源文件 Count_Source.txt 存在，开始统计 ...")


        Func_Count_Txt(Source_File_Path_Txt,Work_Path,Output_Path)
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
    #keyboard.wait('enter')





Show_Text="""请将文件名为：Count_Source.txt 或/和 Count_Source.csv 的文件放入工作目录。\n
请将文件名为：Count_Source_Font.ttf 或 Count_Source_Font.ttc 的文件放入工作目录。\n
输出结果将存放于工作目录下 Count_Result.txt 或/和 Count_Result.csv 文件中。"""



#Main_Function()
Cmd_Text = "点击运行"

from tkinter import *    #注意模块导入方式，否则代码会有差别
import tkinter.messagebox

 
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self,text=Show_Text,height=15,  width=80)
        self.helloLabel.pack()
        self.quitButton = Button(self, text=Cmd_Text, command=self.action,height=2,width=15)
        self.quitButton.pack()
        self.hello2Label = Label(self,height=2,  width=80)
        self.hello2Label.pack()

    def hello(self):
        tkinter.messagebox.showinfo("提示", "执行完毕，可关闭程序\n或再次 点击运行")

    def action(self):
        Main_Function()
        self.hello()
        #name = self.nameInput.get() or 'world'
        #tkMessageBox.showinfo('Message', 'Hello, %s' % name)


 
        
app = Application()
# 设置窗口标题:
app.master.title('Count_Characters')
# 主消息循环:
app.mainloop()

