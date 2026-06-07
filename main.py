from tkinter import *
from tkinter import messagebox
from random import *

# 단어 입력 창을 띄우는 함수
def add_word_win():
    add_win = Toplevel(root)
    add_win.title("단어 입력")
    add_win.resizable(False, False)
    add_win.geometry("200x150")
    
    wordText = Label(add_win, text="단어 입력")
    wordText.pack()

    inputWord = Entry(add_win)
    inputWord.pack()

    meanText = Label(add_win, text="뜻 입력")
    meanText.pack()
    
    inputMean = Entry(add_win)
    inputMean.pack()

    checkBtn = Button(add_win, text="확인", command=lambda: add_word(inputWord, inputMean))
    checkBtn.pack()

# 입력한 단어를 자료형과 리스트박스에 추가하는 함수
def add_word(inputWord, inputMean):
    global wordDict
    global reWordDict
    global allSet
    global listbox

    word = inputWord.get()
    mean = inputMean.get()
    if word in wordDict:
        messagebox.showinfo("오류", "이미 존재하는 단어입니다.")
        return 0
    listbox.insert(END, word)
    wordDict[word] = mean
    reWordDict[mean] = word
    allSet.add(word)
    messagebox.showinfo("완료", "단어를 추가하였습니다.")
    

# 선택한 단어를 리스트박스와 자료형에서 제거하는 함수
def delete_word():
    global wordDict
    global reWordDict
    global allSet
    global incorSet
    global corSet

    selected = listbox.curselection()
    if not selected:
        messagebox.showinfo("오류", "선택된 단어가 없습니다.")
        return 0
    eng_word = listbox.get(selected[0])
    
    eng_word = eng_word.split()[0]
    
    if eng_word in wordDict:
        del reWordDict[wordDict[eng_word]]
        del wordDict[eng_word]
    if eng_word in allSet:
        allSet.remove(eng_word)

    if eng_word in incorSet:
        incorSet.remove(eng_word)
    if eng_word in corSet:
        corSet.remove(eng_word)

    listbox.delete(selected)
    messagebox.showinfo("완료", "단어를 제거하였습니다.")
    

# 단어 검색 창을 띄우는 함수
def search_word_win():
    search_win = Toplevel(root)
    search_win.title("단어 입력")
    search_win.resizable(False, False)
    search_win.geometry("200x100")

    wordText = Label(search_win, text="단어나 뜻 입력")
    wordText.pack()

    inputWord = Entry(search_win)
    inputWord.pack()

    wordResult = Label(search_win, text="이곳에 검색 결과가 표시됩니다.")
    wordResult.pack()

    checkBtn = Button(search_win, text="확인", command=lambda: search_word(inputWord, wordResult))
    checkBtn.pack()


# 단어장 안에서 단어나 뜻을 검색하는 함수
def search_word(inputWord, wordResult):
    global wordDict
    global reWordDict

    word = inputWord.get()
    if word in wordDict:
        return wordResult.configure(text=f"{word} : {wordDict[word]}")
    elif word in reWordDict:
        return wordResult.configure(text=f"{word} : {reWordDict[word]}")
    else:
        return wordResult.configure(text="해당 단어가 존재하지 않습니다.")


# 단어 맞히기 퀴즈 창을 띄우는 함수
def quiz_word_win():
    global wordDict
    
    if wordDict == {}:
        messagebox.showinfo("오류", "등록된 단어가 없습니다.")
        return 0

    wordList = list(wordDict.keys())

    count = randint(0, len(wordList) - 1)
    question = wordList[count]
    answer = wordDict[question]

    quiz_win = Toplevel(root)
    quiz_win.title("단어 맞히기")
    quiz_win.resizable(False, False)
    quiz_win.geometry("200x150")

    questionLabel = Label(quiz_win, text=f"문제 : {question}")
    questionLabel.pack()

    entryAnswer = Entry(quiz_win)
    entryAnswer.pack()

    checkBtn = Button(quiz_win, text="확인", command=lambda: quiz_word(entryAnswer, answer, question, count))
    checkBtn.pack()

# 입력한 답과 정답이 일치하는지 확인하는 함수
def quiz_word(entryAnswer, answer, question, count):
    global wordDict
    global corSet
    global incorSet

    word = entryAnswer.get()

    if word == answer:
        messagebox.showinfo("정답", "정답입니다.")
        listbox.delete(count)
        listbox.insert(count, f"{question} (V)")
        corSet.add(question)
        if question in incorSet:
            incorSet.remove(question)
    else:
        messagebox.showinfo("오답", "틀렸습니다. 정답은 %s" %(answer))
        listbox.delete(count)
        listbox.insert(count, f"{question} (X)")
        incorSet.add(question)
        if question in corSet:
            corSet.remove(question)

# 맞춘 정답 단어 집합을 리스트박스에 표시하는 함수
def show_correct():
    global corSet

    listbox.delete(0, END)
    for word in corSet:
        listbox.insert(END, f"{word} (V)")

# 틀린 오답 단어 집합을 리스트박스에 표시하는 함수
def show_wrong():
    global incorSet

    listbox.delete(0, END)
    for word in incorSet:
        listbox.insert(END, f"{word} (X)")

# 전체 단어와 정오답 상태를 리스트박스에 표시하는 함수
def show_all():
    global wordDict
    global incorSet
    global corSet

    listbox.delete(0, END)
    for word in wordDict.keys():
        if word in corSet:
            listbox.insert(END, f"{word} (V)")
        elif word in incorSet:
            listbox.insert(END, f"{word} (X)")
        else:
            listbox.insert(END, f"{word}")

# 퀴즈 기록을 초기화하고 원래 단어 상태로 돌리는 함수
def reset_all():
    global wordDict
    global incorSet
    global corSet

    corSet = set()
    incorSet = set()
    
    listbox.delete(0, END)
    for word in wordDict.keys():
        listbox.insert(END, f"{word}")
    messagebox.showinfo("초기화", "초기화를 완료했습니다.")


# 변수 및 자료형 선언
wordDict = {"person": "사람", "book": "책"}
reWordDict = {"사람": "person", "책": "book"}
allSet = {"person", "book"}
incorSet = set()
corSet = set()


# GUI 파트
root = Tk()
root.title("단어장 관리자")
root.geometry("500x750")
root.resizable(False, False)
root.configure(bg="#F0F0F0")  


# 그리드 열 비율 설정
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)


# 프로그램 타이틀 레이블
title_label = Label(
    root, 
    text="단어장", 
    font=("Malgun Gothic", 24), 
    bg="#F0F0F0"
)
title_label.grid(row=0, column=0, columnspan=3, pady=(30, 10))


# 중앙 이미지 레이블
img = PhotoImage(file="./학기말과제/image_file.png")
image_label = Label(root, image=img, bg="#F0F0F0")
image_label.grid(row=1, column=0, columnspan=3, pady=(0, 20))


# 단어 표시 리스트박스
listbox = Listbox(
    root, 
    width=35, 
    height=12, 
    font=("Malgun Gothic", 14), 
    bd=1, 
    relief="solid",
    selectmode="browse"
)
listbox.grid(row=2, column=0, columnspan=3, pady=(0, 30))


# 초기 데이터 삽입
listbox.insert(END, "person")
listbox.insert(END, "book")


# 버튼 공통 옵션 설정
btn_options = {"font": ("맑은 고딕", 11), "width": 10, "bd": 1, "relief": "raised"}


# 단어 제어 관련 버튼
addBtn = Button(root, text="추가", command=add_word_win, **btn_options)
delBtn = Button(root, text="삭제", command=delete_word, **btn_options)
searchBtn = Button(root, text="검색", command=search_word_win, **btn_options)

addBtn.grid(row=3, column=0, padx=15, pady=8)
delBtn.grid(row=3, column=1, padx=15, pady=8)
searchBtn.grid(row=3, column=2, padx=15, pady=8)


# 퀴즈 및 정오답 관련 버튼
quizBtn = Button(root, text="단어 맞히기", command=quiz_word_win, **btn_options)
ansBtn = Button(root, text="정답 보기", command=show_correct, **btn_options)
wrongBtn = Button(root, text="오답 보기", command=show_wrong, **btn_options)

quizBtn.grid(row=4, column=0, padx=15, pady=8)
ansBtn.grid(row=4, column=1, padx=15, pady=8)
wrongBtn.grid(row=4, column=2, padx=15, pady=8)


# 화면 보기 설정 및 초기화 버튼
allBtn = Button(root, text="전체 보기", command=show_all, **btn_options)
resetBtn = Button(root, text="초기화", command=reset_all, **btn_options)

allBtn.grid(row=5, column=0, sticky="e", padx=(0, 20), pady=8)
resetBtn.grid(row=5, column=2, sticky="w", padx=(20, 0), pady=8)


root.mainloop()