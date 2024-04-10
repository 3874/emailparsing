import email
import os
import re
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

def parse_eml(eml_path, attachment_folder):
    with open(eml_path, 'rb') as f:
        msg = email.message_from_bytes(f.read())
    
    subject = msg.get('Subject', '')
    sender = msg.get('From', '')
    recipient = msg.get('To', '')
    
    body = ''
    attachments = []

    for part in msg.walk():
        if part.get_content_type() == 'text/plain':
            body += part.get_payload(decode=True).decode('utf-8', 'ignore')
        elif part.get_content_type() == 'text/html':
            # You can handle HTML content similarly if needed
            pass
        elif part.get_content_type().startswith('multipart'):
            # Skip multipart content
            continue
        elif part.get('Content-Disposition') is not None:
            attachments.append(extract_attachment(part, attachment_folder))
    
    # Extracting sender's email from sender string
    sender_email = re.search(r'<([^>]+)>', sender)
    if sender_email:
        sender = sender_email.group(1)

    return {
        'subject': subject,
        'sender': sender,
        'recipient': recipient,
        'body': body,
        'attachments': attachments
    }

# Usage example
if __name__ == "__main__":
    eml_path = r'D:\test\messages\00000.eml'  # eml 파일 경로
    attachment_folder = r'D:\test\results'  # 첨부 파일을 저장할 폴더 경로

    # eml 파일 파싱
    parsed_data = parse_eml(eml_path, attachment_folder)
    
    # 결과 출력
    print("Subject:", parsed_data['subject'])
    print("Sender:", parsed_data['sender'])
    print("Recipient:", parsed_data['recipient'])
    print("Body:", parsed_data['body'])
    print("Attachments:", parsed_data['attachments'])
