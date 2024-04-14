import re

# 파일을 읽어와서 내용을 변수에 저장
with open("jft.txt", "r", encoding="utf-8") as file:
    content = file.read()

# 정규식 패턴
pattern = r"\=\?.*?\?\="

# 패턴 매칭 및 제거
cleaned_content = re.sub(pattern, "", content)

# 수정된 내용을 파일에 쓰기
with open("jft_cleaned.txt", "w", encoding="utf-8") as file:
    file.write(cleaned_content)

print("처리가 완료되었습니다.")
