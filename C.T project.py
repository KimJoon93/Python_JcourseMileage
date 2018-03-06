from tkinter import *
from tkinter import ttk
from tkinter import messagebox
 

 

win=Tk()    #tk창으로 우선 만들고

win.title("C.T project")  #메인창 제목을 '어플'로!

win.geometry('500x700+100+100')   #실행시키면 위치랑 크기 정해보자!
 

win.resizable(0, 0)                 #윈도우 크기를 고정시키자!
 
win.configure(background='light blue')     #색깔을 입히자


 

#콤보박스로 과목명 선택하면 그걸로 이름이 바뀌도록 합니다.

 

def clickMe():
 
    label1.configure(text = str1.get())
    subjectlist = openfile(str1.get()+'.txt')
    label5.configure(text = subjectlist[0])
    label8.configure(text = subjectlist[1])
    label12.configure(text = subjectlist[2])
    label10.configure(text = subjectlist[3])
    if subjectlist[0] == subjectlist[1]:
         messagebox.showinfo("알림", "이 과목은 미달된 과목입니다")
#label5=수강신청한 수
#label8=실제수강생 수
#label10= 추천점수 값
#label2= 최소점수 값


      

            

str1 = StringVar()

label1= Label(win, text = '과목을 선택하세요 ', bg='light blue',font='Helvetica -20 bold')
label1.place(x = 150, y = 200)


#검색버튼 
action=ttk.Button(win,text="검색",command=clickMe)
action.place(x=380, y=100)     
 

#영역 리스트입니다(1~10영역)

ListM = ['문학과예술','인간과역사','언어와표현','가치와윤리','국가와사회공동체','지역사회와세계','논리와수리','자연과우주','생명과환경','소프트웨어']

#과목 리스트(A부터 순서대로)
ListA=['서양음악의이해','대중문학의이해1','대중문학의이해2','연극의이해','영화의이해1','영화의이해2','문학기행','미술사','미학']
ListB=['현대사회와심리학','인간행동의심리적이해','우리교육의어제와오늘','서양문화의유산1','서양문화의유산2','한국근현대사1','한국근현대사2','한국전통문화의유산','동양문화의유산','동양철학사1','동양철학사2','서양철학사']
ListC=['비즈니스영어1','비즈니스영어2','일본어','중국어','한문','러시아어','독일어','불어']
ListD=['성평등리더쉽의이해와실천','철학과윤리','동양의가치와철학','환경오염과인간']
ListE=['경제학입문','축제문화의이해1','축제문화의이해2','문화인류학','국제개발학의기초1','국제개발학의기초2','STARTUPBUSINESS']
ListF=['컴퓨터프로그래밍','공업수학(2)','행정정보분석','컴퓨터활용1','컴퓨터활용2','수학적사고의아름다움','논리와분석적판단','웹멀티미디어','인터넷활용1','인터넷활용2','창의성과아이템탐색']
ListG=['물리학의현대적이해','우주의이해']
ListH=['일반생물학및실험(2)','인간의생물학적이해','현대생명론']
ListI=['정치학입문','현대사회의법과권리1','현대사회의법과권리2','법학개론','기업가정신과리더십','민법총칙','계약의체결과이행','생활과행정','생활과헌법','상법의이해']
ListJ=['C.T']

def comboselect(event):
      print(str.get())
      if str.get()=="문학과예술":
           comboB['values'] = ListA
           comboB.current(0)
      elif str.get()=="인간과역사":
            comboB['values'] = ListB
            comboB.current(0)
      elif str.get()=="언어와표현":
            comboB['values'] = ListC
            comboB.current(0)
      elif str.get()=="가치와윤리":
            comboB['values'] = ListD
            comboB.current(0)
      elif str.get()=="지역사회와세계":
            comboB['values'] = ListE
            comboB.current(0)
      elif str.get()=="논리와수리":
            comboB['values'] = ListF
            comboB.current(0)
      elif str.get()=="자연과우주":
            comboB['values'] = ListG
            comboB.current(0)
      elif str.get()=="생명과환경":
            comboB['values'] = ListH
            comboB.current(0)
      elif str.get()=="국가와사회공동체":
            comboB['values'] = ListI
            comboB.current(0)
      elif str.get()=="소프트웨어":
            comboB['values'] = ListJ
            comboB.current(0)
            
      else:
           print("오류입니다")

           
#1번째 콤보박스    
str = StringVar()
comboA = ttk.Combobox(win, width=10, textvariable= str)
comboA.place(x = 30 , y = 100)
comboA['values'] = ListM
comboA.bind('<<ComboboxSelected>>', comboselect);


#2번째 콤보박스

str1 = StringVar()
comboB = ttk.Combobox(win, width=25, textvariable= str1)
comboB.place(x = 150 , y = 100)



 

 
 
 
#제목 
label2=Label(win,text='수강신청 마일리치 합격예측',font='Helvetica -18 bold', bg = 'light blue')
 
label2.pack()
 
label2.place(x=120,y=10)
 
 
 
#제목2
label3=Label(win,text='for 필수교양',bg = 'light blue')
 
label3.pack()
 
label3.place(x=200,y=40)
 

 
#제목3 
label4=Label(win,text='2018년 1학기  필수 교양과목',bg = 'light blue')
 
label4.pack()
 
label4.place(x=150,y=70)
 
 

 #수강신청수 값
label5=Label(win,text='',bg = 'light blue',font='Helvetica -20 bold')
 
label5.pack()
 
label5.place(x=200,y=500)


 
#수강신청수 텍스트 
label6=Label(win,text='수강신청 수: ',bg = 'light blue',font='Helvetica -20 bold')
 
label6.pack()
 
label6.place(x=10,y=500)
 


# 합격한 수강생 텍스트
label7=Label(win,text='합격한 수강생: ',bg = 'light blue',font='Helvetica -20 bold')
 
label7.pack()
 
label7.place(x=10,y=600)
 


# 합격한 수강생 값
label8=Label(win,text='',bg = 'light blue',font='Helvetica -20 bold')
 
label8.pack()
 
label8.place(x=200,y=600)
 


#추천점수 텍스트 
label9=Label(win,text='추천 점수: ',bg = 'light blue',font='Helvetica -20 bold')
 
label9.pack()
 
label9.place(x=10,y=400)

 

#추천점수 값 
label10=Label(win,text='',bg = 'light blue',font='Helvetica -20 bold')
 
label10.pack()
 
label10.place(x=200,y=380)
 
 

#최소점수 텍스트 
label11=Label(win,text='최소 점수:',bg = 'light blue',font='Helvetica -20 bold')
 
label11.pack()
 
label11.place(x=10,y=300)
 



#최소점수 값 
label12=Label(win,text='',bg = 'light blue',font='Helvetica -20 bold')
 
label12.pack()
 
label12.place(x=200,y=300)


####파일을 불러옵니다. 이름은 openfile

def openfile(filename):
    tLine = 0
    oCount = 0
    file = open(filename,'r')
    lines = file.readlines()
    for i in lines:
        tLine = tLine + 1
        splitlist = i.split()
        if splitlist[10]=='O':
            oCount = oCount + 1
    medianMileList = lines[int((oCount+1)/2)].split()
    leastMileList = lines[oCount-1].split()
    #[전체수강생, 실제수강생, 성공최저마일리지, 성공중앙값마일리지]
    returnlist = [tLine, oCount, leastMileList[1],medianMileList[1]]
    return returnlist
    file.close
