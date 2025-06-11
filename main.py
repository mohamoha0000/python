import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# إعدادات Brevo SMTP
smtp_server = "smtp-relay.brevo.com"
smtp_port = 587
smtp_login = "8f5763001@smtp-brevo.com"
smtp_password = "xsmtpsib-5a1c7cf8daaa95e8809c5e3bcc62f2e9cd54244a14fbac10de9c10cd5166758a-A19KHYtEDfhrbSxd"

# إعداد البريد
sender_email = "moham3iof@gmail.com"  # يجب أن يكون بريد فعّال في حساب Brevo
receiver_email = "mohamedelmaeyouf@gmail.com"
subject = "رسالة تجريبية من Python عبر Brevo"
body = "مرحبًا! هذه رسالة تجريبية أُرسلت عبر SMTP باستخدام Python و Brevo."

# بناء الرسالة
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = subject
msg.attach(MIMEText(body, "plain"))

# إرسال الرسالة
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_login, smtp_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    print("✅ تم إرسال البريد الإلكتروني بنجاح.")
except Exception as e:
    print("❌ حدث خطأ أثناء الإرسال:", e)
finally:
    server.quit()
