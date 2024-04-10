import os
import re
import email
import email.header

def decode_mime_words(s):
    return ' '.join(word if isinstance(word, str) else word.decode(encoding or 'utf-8') for word, encoding in email.header.decode_header(s))

def extract_attachment(part, folder_path):
    filename = part.get_filename()
    if filename:
        decoded_filename = decode_mime_words(filename)
        filepath = os.path.join(folder_path, decoded_filename)
        with open(filepath, 'wb') as f:
            f.write(part.get_payload(decode=True))
        return decoded_filename
    else:
        return None

def parse_eml_file(eml_file, attachment_folder):
    with open(eml_file, 'rb') as f:
        msg = email.message_from_bytes(f.read())
    
    sender = msg.get('From', '')
    
    body = ''
    attachments = []

    for part in msg.walk():
        if part.get_content_type() == 'text/plain':
            body += part.get_payload(decode=True).decode('utf-8', 'ignore')
        elif part.get_content_type().startswith('multipart'):
            continue
        elif part.get('Content-Disposition') is not None:
            attachments.append(extract_attachment(part, attachment_folder))
    
    sender_email = re.search(r'<([^>]+)>', sender)
    if sender_email:
        sender = sender_email.group(1)

    return sender, body, attachments

def parse_eml_folder(folder_path, attachment_folder):
    for filename in os.listdir(folder_path):
        if filename.endswith('.eml'):
            eml_file = os.path.join(folder_path, filename)
            txt_filename = os.path.splitext(filename)[0] + '.txt'
            txt_filepath = os.path.join(attachment_folder, txt_filename)
            sender, body, _ = parse_eml_file(eml_file, attachment_folder)
            with open(txt_filepath, 'w', encoding='utf-8') as txt_file:
                txt_file.write(body)
            print(f"Processed {filename} and saved to {txt_filepath}")

# Usage example
if __name__ == "__main__":
    eml_folder = r'D:\test\messages'  # EML 파일이 있는 폴더 경로
    attachment_folder = r'D:\test\results'  # 첨부 파일을 저장할 폴더 경로

    # EML 파일들을 파싱하고 텍스트 파일로 저장
    parse_eml_folder(eml_folder, attachment_folder)
