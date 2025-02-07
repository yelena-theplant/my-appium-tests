#连接邮箱获取验证码

import imaplib
import email
from email.header import decode_header
import re

def get_verification_code():
    try:
        # 连接到 Gmail 邮箱
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login("yelena@theplant.jp", "bixb tqvf izre uxmp")  # 输入你的邮箱和密码

        # 选择收件箱
        mail.select("inbox")

        # 搜索邮件，获取未读邮件
        status, messages = mail.search(None, 'UNSEEN')

        if status != "OK":
            print("No new messages found.")
            return None

        # 获取邮件 ID
        for num in messages[0].split():
            status, msg_data = mail.fetch(num, "(RFC822)")
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])

                    # 解析邮件主题
                    subject = decode_subject(msg["Subject"])
                    #print("Email Subject:", subject)

                    # 根据邮件主题筛选验证码邮件
                    if "authentication code" in subject.lower():
                        # 获取邮件正文内容
                        body = get_email_body(msg)
                        if body:
                            # 打印邮件正文内容以检查
                            #print("Email Body:", body)

                            # 调用函数从邮件正文提取验证码
                            code = extract_code_from_body(body)
                            if code:
                                return code
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def decode_subject(subject):
    """
    解析邮件主题并处理可能的编码问题
    """
    if subject:
        decoded_header = decode_header(subject)
        subject_str = ""
        for part, encoding in decoded_header:
            if isinstance(part, bytes):
                try:
                    part = part.decode(encoding or "utf-8")
                except (TypeError, UnicodeDecodeError):
                    part = part.decode("utf-8", errors="ignore")
            subject_str += part
        return subject_str
    return ""


def get_email_body(msg):
    """
    提取邮件正文内容
    """
    try:
        # 如果邮件是multipart格式（通常邮件正文是多部分的）
        if msg.is_multipart():
            for part in msg.walk():
                # 查找文本部分
                content_type = part.get_content_type()
                content_disposition = str(part.get("Content-Disposition"))

                if "attachment" not in content_disposition:
                    if content_type == "text/plain":
                        # 提取文本部分
                        body = part.get_payload(decode=True).decode()
                        #print("Email Body (Plain Text):")
                        #print(body)  # 打印出正文内容
                        return body
                    # elif content_type == "text/html":
                    #     # 如果是HTML格式，提取HTML内容
                    #     body = part.get_payload(decode=True).decode()
                    #     print("Email Body (HTML):")
                    #     print(body)  # 打印出HTML格式的正文内容
                    #     return body
        else:
            body = msg.get_payload(decode=True).decode()
            #print("Email Body (Single Part):")
            #print(body)  # 打印出正文内容
            return body
    except Exception as e:
        print(f"Failed to extract body: {e}")
        return None


def extract_code_from_body(body):
    """
    使用正则表达式从邮件正文提取验证码
    """
    try:
        #print("Body of the email:", body)  # 调试输出邮件内容
        # 使用正则表达式匹配验证码（假设是6位数字）
        match = re.search(r'(\d{6})', body)  # 匹配验证码（6位数字）
        if match:
            return match.group(1)
        return None
    except Exception as e:
        print(f"Failed to extract code: {e}")
        return None


# 获取验证码
verification_code = get_verification_code()

if verification_code:
    print("The verification code is:", verification_code)
else:
    print("No verification code found.")
