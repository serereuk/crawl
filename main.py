from crawl import crawler
import pickle

keyword = str(input("입력해주세요\n"))
startdate = str(input("시작 날짜 형식은 2018-07-11\n"))
finishdate = str(input("끝나는 날짜 형식은 2018=07-12\n"))

result = crawler().twitter(keyword, startdate, finishdate)
with open("Result.txt", "wb") as f:
    pickle.dump(result, f)
