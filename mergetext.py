import os

def merge_text_files(folder_path, output_file):
    # 폴더 안의 모든 파일 목록을 가져옴
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    # 파일 확장자가 .txt 인 파일만 필터링
    txt_files = [f for f in files if f.endswith('.txt')]
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for txt_file in txt_files:
            file_path = os.path.join(folder_path, txt_file)
            with open(file_path, 'r', encoding='utf-8') as infile:
                # 각 파일의 내용을 출력 파일에 쓰기
                outfile.write(infile.read())
                outfile.write('\n')  # 각 파일 사이에 개행 추가

# 사용법 예시
folder_path = 'C:/JFT/text'  # 텍스트 파일들이 있는 폴더 경로
output_file = 'C:/JFT/merged_text.txt'  # 병합된 텍스트 파일의 경로
merge_text_files(folder_path, output_file)
