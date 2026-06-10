from tkinter import *
from random import *
import shared
import func

# GUI 파트
root = Tk()
root.title("단어장 관리자")
root.geometry("500x750")
root.resizable(False, False)
root.configure(bg="#F0F0F0")  

# 변수 설정
shared.root = root

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
img = PhotoImage(file="../학기말과제/image_file.png")
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

# 리스트박스 변수 설정
shared.listbox = listbox

# 초기 데이터 삽입
shared.listbox.insert(END, "person")
shared.listbox.insert(END, "book")

# 버튼 공통 옵션 설정
btn_options = {"font": ("맑은 고딕", 11), "width": 10, "bd": 1, "relief": "raised"}

# 단어 제어 관련 버튼
addBtn = Button(root, text="추가", command=func.add_word_win, **btn_options)
delBtn = Button(root, text="삭제", command=func.delete_word, **btn_options)
searchBtn = Button(root, text="검색", command=func.search_word_win, **btn_options)

addBtn.grid(row=3, column=0, padx=15, pady=8)
delBtn.grid(row=3, column=1, padx=15, pady=8)
searchBtn.grid(row=3, column=2, padx=15, pady=8)

# 퀴즈 및 정오답 관련 버튼
quizBtn = Button(root, text="단어 맞히기", command=func.quiz_word_win, **btn_options)
ansBtn = Button(root, text="정답 보기", command=func.show_correct, **btn_options)
wrongBtn = Button(root, text="오답 보기", command=func.show_wrong, **btn_options)

quizBtn.grid(row=4, column=0, padx=15, pady=8)
ansBtn.grid(row=4, column=1, padx=15, pady=8)
wrongBtn.grid(row=4, column=2, padx=15, pady=8)

# 화면 보기 설정 및 초기화 버튼
allBtn = Button(root, text="전체 보기", command=func.show_all, **btn_options)
resetBtn = Button(root, text="초기화", command=func.reset_all, **btn_options)

allBtn.grid(row=5, column=0, sticky="e", padx=(0, 20), pady=8)
resetBtn.grid(row=5, column=2, sticky="w", padx=(20, 0), pady=8)

root.mainloop()