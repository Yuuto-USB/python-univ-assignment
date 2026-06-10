# 메인 윈도우 및 위젯 객체 참조 변수
root = None
listbox = None

# 단어장 데이터 관리를 위한 딕셔너리 선언
wordDict = {"person": "사람", "book": "책"}
reWordDict = {"사람": "person", "책": "book"}

# 정오답 필터링 및 퀴즈 제어를 위한 집합 선언
allSet = {"person", "book"}
incorSet = set()
corSet = set()