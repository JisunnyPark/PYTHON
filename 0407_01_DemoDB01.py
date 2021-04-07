# 0407_01_DemoDB01.py
# SQLite를 사용하는 데모(로컬 데이터베이스)
import sqlite3

# 처음에는 데이터베이스 파일(또는 메모리)를 생성 ==> 연습용 그래서 파일에 저장 안함 
# ==> 끝나면 사라짐

con = sqlite3.connect(":memory:")

# SQL 구문을 실행하는 것은 대부분 커서 객체
cur = con.cursor()

# 저장소(테이블)을 만들기 : 테이블 스키마(뼈대)
cur.execute("create table PhoneBook (Name text, PhoneNum text);")

# 1건 입력
cur.execute("insert into PhoneBook values ('derick', '010-111');")

# 검색
cur.execute("select * from PhoneBook;")

for row in cur:
    print(row)