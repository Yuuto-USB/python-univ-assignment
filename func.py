from tkinter import *
from tkinter import messagebox
from random import *
import shared

# 단어 입력 창을 띄우는 함수
def add_word_win():
    add_win = Toplevel(shared.root)
    add_win.title("단어 입력")
    add_win.resizable(False, False)
    add_win.geometry("300x150")
    
    # 중앙 정렬을 위한 그리드 설정
    add_win.grid_columnconfigure(0, weight=1)
    add_win.grid_columnconfigure(1, weight=1)
    
    wordText = Label(add_win, text="단어 입력:", font=("맑은 고딕", 11))
    wordText.grid(row=0, column=0, sticky="e", padx=10, pady=(20, 10))

    inputWord = Entry(add_win, font=("맑은 고딕", 11), width=15)
    inputWord.grid(row=0, column=1, sticky="w", padx=10, pady=(20, 10))

    meanText = Label(add_win, text="뜻 입력:", font=("맑은 고딕", 11))
    meanText.grid(row=1, column=0, sticky="e", padx=10, pady=10)
    
    inputMean = Entry(add_win, font=("맑은 고딕", 11), width=15)
    inputMean.grid(row=1, column=1, sticky="w", padx=10, pady=10)

    checkBtn = Button(add_win, text="확인", font=("맑은 고딕", 10), width=8, command=lambda: add_word(inputWord, inputMean))
    checkBtn.grid(row=2, column=0, columnspan=2, pady=15)

# 입력한 단어를 자료형과 리스트박스에 추가하는 함수
def add_word(inputWord, inputMean):
    word = inputWord.get().strip()
    mean = inputMean.get().strip()
    
    if word in shared.wordDict:
        messagebox.showinfo("오류", "이미 존재하는 단어입니다.")
        return 0
    if word == "":
        messagebox.showinfo("오류", "단어를 입력해주세요.")
        return 0
            
    shared.listbox.insert(END, word)
    shared.wordDict[word] = mean
    shared.reWordDict[mean] = word
    shared.allSet.add(word)
    messagebox.showinfo("완료", "단어를 추가하였습니다.")
    
# 선택한 단어를 리스트박스와 자료형에서 제거하는 함수
def delete_word():
    selected = shared.listbox.curselection()
    if not selected:
        messagebox.showinfo("오류", "선택된 단어가 없습니다.")
        return 0
    eng_word = shared.listbox.get(selected[0])
    eng_word = eng_word.split()[0]
    
    if eng_word in shared.wordDict:
        del shared.reWordDict[shared.wordDict[eng_word]]
        del shared.wordDict[eng_word]
    if eng_word in shared.allSet:
        shared.allSet.remove(eng_word)

    if eng_word in shared.incorSet:
        shared.incorSet.remove(eng_word)
    if eng_word in shared.corSet:
        shared.corSet.remove(eng_word)

    shared.listbox.delete(selected)
    messagebox.showinfo("완료", "단어를 제거하였습니다.")
    
# 단어 검색 창을 띄우는 함수
def search_word_win():
    search_win = Toplevel(shared.root)
    search_win.title("단어 검색")
    search_win.resizable(False, False)
    search_win.geometry("320x150")

    search_win.grid_columnconfigure(0, weight=1)
    search_win.grid_columnconfigure(1, weight=1)

    wordText = Label(search_win, text="단어나 뜻 입력:", font=("맑은 고딕", 11))
    wordText.grid(row=0, column=0, sticky="e", padx=10, pady=(20, 5))

    inputWord = Entry(search_win, font=("맑은 고딕", 11), width=15)
    inputWord.grid(row=0, column=1, sticky="w", padx=10, pady=(20, 5))

    wordResult = Label(search_win, text="이곳에 검색 결과가 표시됩니다.", font=("맑은 고딕", 10), fg="blue")
    wordResult.grid(row=1, column=0, columnspan=2, pady=5)

    checkBtn = Button(search_win, text="확인", font=("맑은 고딕", 10), width=8, command=lambda: search_word(inputWord, wordResult))
    checkBtn.grid(row=2, column=0, columnspan=2, pady=10)

# 단어장 안에서 단어나 뜻을 검색하는 함수
def search_word(inputWord, wordResult):
    word = inputWord.get().strip()
    if word in shared.wordDict:
        return wordResult.configure(text=f"{word} : {shared.wordDict[word]}", fg="black")
    elif word in shared.reWordDict:
        return wordResult.configure(text=f"{word} : {shared.reWordDict[word]}", fg="black")
    else:
        return wordResult.configure(text="해당 단어가 존재하지 않습니다.", fg="red")

# 단어 맞히기 퀴즈 창을 띄우는 함수
def quiz_word_win():
    if shared.wordDict == {}:
        messagebox.showinfo("오류", "등록된 단어가 없습니다.")
        return 0

    wordList = list(shared.wordDict.keys())
    count = randint(0, len(wordList) - 1)
    question = wordList[count]
    answer = shared.wordDict[question]

    quiz_win = Toplevel(shared.root)
    quiz_win.title("단어 맞히기")
    quiz_win.resizable(False, False)
    quiz_win.geometry("300x140")

    quiz_win.grid_columnconfigure(0, weight=1)
    quiz_win.grid_columnconfigure(1, weight=1)

    questionLabel = Label(quiz_win, text=f"{question} 뜻은?", font=("맑은 고딕", 11))
    questionLabel.grid(row=0, column=0, sticky="e", padx=10, pady=(25, 15))

    entryAnswer = Entry(quiz_win, font=("맑은 고딕", 11), width=15)
    entryAnswer.grid(row=0, column=1, sticky="w", padx=10, pady=(25, 15))

    checkBtn = Button(quiz_win, text="확인", font=("맑은 고딕", 10), width=8, command=lambda: quiz_word(entryAnswer, answer, question, count, quiz_win))
    checkBtn.grid(row=1, column=0, columnspan=2, pady=10)

# 입력한 답과 정답이 일치하는지 확인하는 함수
def quiz_word(entryAnswer, answer, question, count, quiz_win):
    word = entryAnswer.get().strip()

    if word == answer:
        messagebox.showinfo("정답", "정답입니다.")
        shared.listbox.delete(count)
        shared.listbox.insert(count, f"{question} (V)")
        shared.corSet.add(question)
        if question in shared.incorSet:
            shared.incorSet.remove(question)
    else:
        messagebox.showinfo("오답", f"틀렸습니다. 정답은 {answer}")
        shared.listbox.delete(count)
        shared.listbox.insert(count, f"{question} (X)")
        shared.incorSet.add(question)
        if question in shared.corSet:
            shared.corSet.remove(question)
    return quiz_win.destroy()

# 맞춘 정답 단어 집합을 리스트박스에 표시하는 함수
def show_correct():
    shared.listbox.delete(0, END)
    for word in shared.allSet.intersection(shared.corSet):
        shared.listbox.insert(END, f"{word} (V)")

# 틀린 오답 단어 집합을 리스트박스에 표시하는 함수
def show_wrong():
    shared.listbox.delete(0, END)
    for word in shared.allSet.intersection(shared.incorSet):
        shared.listbox.insert(END, f"{word} (X)")

# 전체 단어와 정오답 상태를 리스트박스에 표시하는 함수
def show_all():
    shared.listbox.delete(0, END)
    for word in shared.wordDict.keys():
        if word in shared.corSet:
            shared.listbox.insert(END, f"{word} (V)")
        elif word in shared.incorSet:
            shared.listbox.insert(END, f"{word} (X)")
        else:
            shared.listbox.insert(END, f"{word}")

# 퀴즈 기록을 초기화하고 원래 단어 상태로 돌리는 함수
def reset_all():
    shared.corSet = set()
    shared.incorSet = set()
    
    shared.listbox.delete(0, END)
    for word in shared.wordDict.keys():
        shared.listbox.insert(END, f"{word}")
    messagebox.showinfo("초기화", "초기화를 완료했습니다.")