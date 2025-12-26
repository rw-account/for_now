import requests
import json

# ============================
# إعداد مفاتيح Mailjet
# ============================
MJ_APIKEY_PUBLIC = 'dd321cd6b24fe16fdf7afa6f8513d534'
MJ_APIKEY_PRIVATE = "b846ed65ef4fbe3d60bd4f6f8be260bd"
import html
from datetime import datetime, timezone

current_year = datetime.now(timezone.utc).year

def send_reset_password_email(email, username, reset_password_link):
  safe_link = html.escape(reset_password_link)
  # ============================
  # إعداد المستلمين
  # ============================
  TO_EMAIL = email
  TO_NAME = username

  # ============================
  # محتوى الرسالة
  # ============================
  SUBJECT = "طلب إعادة تعيين كلمة المرور"
  HTML_BODY = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>إعادة تعيين كلمة المرور - نظام إدارة المخازن</title>
</head>
<body style="font-family:'Segoe UI', Tahoma, Geneva, Verdana, Arial, sans-serif; line-height:1.6; color:#333; margin:0; padding:0; background-color:#f5f5f5; direction:rtl; text-align:right;">
    <div style="max-width:600px; margin:0 auto; background-color:#ffffff; border-radius:8px; overflow:hidden; box-shadow:0 4px 12px rgba(0,0,0,0.1); direction:rtl; text-align:right;">
        <div style="background-color:#2c5aa0; color:white; padding:25px 30px; text-align:center; direction:rtl;">
            <h1 style="margin:0; font-size:24px; direction:rtl;">نظام إدارة المخازن</h1>
            <p style="direction:rtl;">إعادة تعيين كلمة المرور</p>
        </div>
        <div style="padding:30px; direction:rtl; text-align:right;">
            <div style="font-size:18px; margin-bottom:20px; color:#2c5aa0; direction:rtl;">مرحباً {username}</div>
            <div style="margin-bottom:25px; font-size:16px; color:#444; direction:rtl;">
                <p style="direction:rtl;">تحية طيبة وبعد،</p>
                <p style="direction:rtl;">لقد تلقينا طلباً لإعادة تعيين كلمة المرور الخاصة بحسابك في <strong>نظام إدارة المخازن</strong>.</p>
                <p style="direction:rtl;">إذا كنت أنت من طلب ذلك، يرجى الضغط على الزر أدناه لإنشاء كلمة مرور جديدة. هذا الرابط آمن وفريد ويُستخدم لمرة واحدة فقط.</p>
            </div>
            <div style="text-align:center; margin:30px 0; direction:rtl;">
                <a href="{safe_link}" style="display:inline-block !important; background-color:#2c5aa0; color:white !important; text-decoration:none !important; padding:14px 30px; border-radius:5px; font-weight:bold; font-size:16px; margin:20px 0; text-align:center; direction:rtl;">إعادة تعيين كلمة المرور الآن</a>
            </div>
            <div style="background-color:#f8f9fa; border-right:4px solid #2c5aa0; padding:15px; margin:25px 0; border-radius:4px; direction:rtl; text-align:right;">
                <div style="font-weight:bold; color:#2c5aa0; margin-bottom:8px; direction:rtl;">يرجى الملاحظة:</div>
                <ul style="margin:10px 0; padding-right:20px; direction:rtl; text-align:right;">
                    <li style="direction:rtl;">هذا الرابط ساري المفعول <strong>لمدة ساعة فقط</strong>.</li>
                    <li style="direction:rtl;">لأسباب أمنية، <strong>لا تشارك هذا الرابط مع أي شخص</strong>.</li>
                </ul>
            </div>
            <div style="color:#d32f2f; font-weight:bold; background-color:#ffebee; padding:10px; border-radius:4px; margin:20px 0; text-align:center; border-right:3px solid #d32f2f; direction:rtl;">
                <p style="direction:rtl;">إذا لم تقم أنت بهذا الطلب،</p>
                <p style="direction:rtl;">يمكنك تجاهل هذه الرسالة بأمان. لن يتم إجراء أي تغييرات على حسابك.</p>
            </div>
            <div style="margin-top:30px; padding-top:20px; border-top:1px solid #eee; font-weight:bold; color:#2c5aa0; direction:rtl; text-align:right;">
                مع فائق الاحترام والتقدير،<br>
                <strong>إدارة الموقع</strong><br>
            </div>
        </div>
        <div style="background-color:#f1f1f1; padding:20px 30px; text-align:center; font-size:14px; color:#666; border-top:1px solid #ddd; direction:rtl;">
            <p style="direction:rtl;">هذه رسالة آلية، يرجى عدم الرد على هذا البريد الإلكتروني.</p>
            <p style="font-size:12px; color:#999; margin-top:10px; direction:rtl;">  نظام إدارة المخازن. جميع الحقوق محفوظة © { current_year }.</p>
        </div>
    </div>
</body>
</html>


  """
  TEXT_BODY = f"""
مرحباً {username}

وصلنا طلب لإعادة تعيين كلمة المرور الخاصة بحسابك على موقع نظام إدارة المخازن.

لإنشاء كلمة مرور جديدة، استخدم الرابط التالي:
{safe_link}

تنبيه: هذا الرابط صالح لفترة محدودة فقط.

إذا لم تطلب إعادة تعيين كلمة المرور، يمكنك تجاهل هذه الرسالة بأمان ولن يتم إجراء أي تغيير على حسابك.

مع تحياتنا،
إدارة الموقع
"""

  # ============================
  # تحضير بيانات JSON للإرسال
  # ============================
  data = {
      "Messages": [
          {
              "From": {"Email": "ramyformyproject@gmail.com", "Name": "نظام ادارة المخازن"},
              "To": [{"Email": TO_EMAIL, "Name": TO_NAME}],
              "Subject": SUBJECT,
              "HTMLPart": HTML_BODY,
              "TextPart": TEXT_BODY,
          }
      ]
  }

  # ============================
  # إرسال الرسالة
  # ============================
  response = requests.post(
      "https://api.mailjet.com/v3.1/send",
      auth=(MJ_APIKEY_PUBLIC, MJ_APIKEY_PRIVATE),
      headers={"Content-Type": "application/json"},
      data=json.dumps(data)
  )

  # ============================
  # طباعة نتيجة الإرسال
  # ============================
  #print("Status Code:", response.status_code)
  #print("Response Body:", response.json())





def send_register_email(email, username, register_link):
  safe_link = html.escape(register_link)
  # ============================
  # إعداد المستلمين
  # ============================
  TO_EMAIL = email
  TO_NAME = username

  # ============================
  # محتوى الرسالة
  # ============================
  SUBJECT = "طلب إنشاء حساب جديد"
  HTML_BODY = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">  
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>إنشاء حساب جديد - نظام إدارة المخازن</title>
</head>
<body style="font-family:'Segoe UI', Tahoma, Geneva, Verdana, Arial, sans-serif; line-height:1.6; color:#333; margin:0; padding:0; background-color:#f5f5f5; direction:rtl; text-align:right;">
    <div style="max-width:600px; margin:0 auto; background-color:#ffffff; border-radius:8px; overflow:hidden; box-shadow:0 4px 12px rgba(0,0,0,0.1); direction:rtl; text-align:right;">
        <div style="background-color:#2c5aa0; color:white; padding:25px 30px; text-align:center; direction:rtl;">
            <h1 style="margin:0; font-size:24px; direction:rtl;">نظام إدارة المخازن</h1>
            <p style="direction:rtl;">إنشاء حساب جديد</p>
        </div>
        <div style="padding:30px; direction:rtl; text-align:right;">
            <div style="font-size:18px; margin-bottom:20px; color:#2c5aa0; direction:rtl;">مرحباً {username}</div>
            <div style="margin-bottom:25px; font-size:16px; color:#444; direction:rtl;">
                <p style="direction:rtl;">تحية طيبة وبعد،</p>
                <p style="direction:rtl;">لقد تلقينا طلباً لإنشاء حساب جديد في <strong>نظام إدارة المخازن</strong>.</p>
                <p style="direction:rtl;">إذا كنت أنت من طلب ذلك، يرجى الضغط على الزر أدناه لإكمال عملية التسجيل وإنشاء حسابك.</p>
            </div>
            <div style="text-align:center; margin:30px 0; direction:rtl;">
                <a href="{safe_link}" style="display:inline-block !important; background-color:#2c5aa0; color:white !important; text-decoration:none !important; padding:14px 30px; border-radius:5px; font-weight:bold; font-size:16px; margin:20px 0; text-align:center; direction:rtl;">إنشاء الحساب الآن</a>
            </div>
            <div style="background-color:#f8f9fa; border-right:4px solid #2c5aa0; padding:15px; margin:25px 0; border-radius:4px; direction:rtl; text-align:right;">
                <div style="font-weight:bold; color:#2c5aa0; margin-bottom:8px; direction:rtl;">يرجى الملاحظة:</div>
                <ul style="margin:10px 0; padding-right:20px; direction:rtl; text-align:right;">
                    <li style="direction:rtl;">هذا الرابط ساري المفعول <strong>لمدة ساعة واحدة فقط</strong>.</li>
                    <li style="direction:rtl;">لأسباب أمنية، <strong>لا تشارك هذا الرابط مع أي شخص</strong>.</li>
                </ul>
            </div>
            <div style="margin-top:30px; padding-top:20px; border-top:1px solid #eee; font-weight:bold; color:#2c5aa0; direction:rtl; text-align:right;">
                مع فائق الاحترام والتقدير،<br>
                <strong>إدارة الموقع</strong><br>
            </div>
        </div>
        <div style="background-color:#f1f1f1; padding:20px 30px; text-align:center; font-size:14px; color:#666; border-top:1px solid #ddd; direction:rtl;">
            <p style="direction:rtl;">هذه رسالة آلية، يرجى عدم الرد على هذا البريد الإلكتروني.</p>
            <p style="font-size:12px; color:#999; margin-top:10px; direction:rtl;">  نظام إدارة المخازن. جميع الحقوق محفوظة © { current_year }.</p>
        </div>
    </div>
</body>
</html>

"""

  TEXT_BODY = f"""
مرحباً {username}

وصلنا طلب لإنشاء حساب جديد على موقع نظام إدارة المخازن.

لإكمال عملية التسجيل وإنشاء حسابك، استخدم الرابط التالي:
{safe_link}

تنبيه: هذا الرابط صالح لفترة محدودة فقط.

اذا لم تطلب إنشاء حساب، يمكنك تجاهل هذه الرسالة بأمان ولن يتم إجراء أي تغيير على حسابك.

مع تحياتنا،
إدارة الموقع
"""
  






  # ============================
  # تحضير بيانات JSON للإرسال
  # ============================
  data = {
      "Messages": [
          {
              "From": {"Email": "ramyformyproject@gmail.com", "Name": "نظام ادارة المخازن"},
              "To": [{"Email": TO_EMAIL, "Name": TO_NAME}],
              "Subject": SUBJECT,
              "HTMLPart": HTML_BODY,
              "TextPart": TEXT_BODY,
          }
      ]
  }

  # ============================
  # إرسال الرسالة
  # ============================
  response = requests.post(
      "https://api.mailjet.com/v3.1/send",
      auth=(MJ_APIKEY_PUBLIC, MJ_APIKEY_PRIVATE),
      headers={"Content-Type": "application/json"},
      data=json.dumps(data)
  )

  # ============================
  # طباعة نتيجة الإرسال
  # ============================
  #print("Status Code:", response.status_code)
  #print("Response Body:", response.json())

def send_message_from_contact_form(name, email, subject, message):
    # ============================
    # إعداد المستلمين
    # ============================
    TO_EMAIL = "ramyformyproject@gmail.com" 
    FROM_EMAIL = "ramyformyproject@gmail.com"
    # ============================
    # محتوى الرسالة
    # ============================
    SUBJECT = subject
    safe_name = html.escape(name)
    safe_email = html.escape(email)
    safe_subject = html.escape(subject)
    safe_message = html.escape(message).replace('\n', '<br>')

    HTML_BODY = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>رسالة من نموذج التواصل - نظام إدارة المخازن</title>
</head>
<body style="font-family:'Segoe UI', Tahoma, Geneva, Verdana, Arial, sans-serif; line-height:1.6; color:#333; margin:0; padding:0; background-color:#f5f5f5; direction:rtl; text-align:right;">
    <div style="max-width:600px; margin:0 auto; background-color:#ffffff; border-radius:8px; overflow:hidden; box-shadow:0 4px 12px rgba(0,0,0,0.1); direction:rtl; text-align:right;">
        <div style="background-color:#2c5aa0; color:white; padding:20px 25px; text-align:center;">
            <h1 style="margin:0; font-size:22px;">نظام إدارة المخازن</h1>
            <p style="margin:5px 0 0;">رسالة جديدة من نموذج التواصل</p>
        </div>
        <div style="padding:25px;">
            <div style="font-size:18px; margin-bottom:15px; color:#2c5aa0;">بيانات المرسِل</div>
            <div style="margin-bottom:12px; font-size:15px; color:#444;">
                <p><strong>الاسم:</strong> {safe_name}</p>
                <p><strong>البريد الإلكتروني:</strong> {safe_email}</p>
                <p><strong>الموضوع:</strong> {safe_subject}</p>
            </div>
            <div style="background-color:#f8f9fa; border-right:4px solid #2c5aa0; padding:15px; margin:15px 0; border-radius:4px;">
                <div style="font-weight:bold; color:#2c5aa0; margin-bottom:8px;">نص الرسالة:</div>
                <div style="color:#444; font-size:15px; line-height:1.6;">{safe_message}</div>
            </div>
        </div>
        <div style="background-color:#f1f1f1; padding:15px 20px; text-align:center; font-size:13px; color:#666; border-top:1px solid #ddd;">
            <p style="font-size:12px; color:#999; margin-top:8px;">نظام إدارة المخازن. جميع الحقوق محفوظة © {current_year}.</p>
        </div>
    </div>
</body>
</html>
"""
    TEXT_BODY = f"""
    رسالة جديدة من نموذج التواصل
    الاسم: {name}
    البريد الإلكتروني: {email}
    الموضوع: {subject}
    الرسالة:
    {message}
    """
    # ============================
    # تحضير بيانات JSON للإرسال
    # ============================
    # تحضير بيانات JSON للإرسال
    data = {
        "Messages": [
            {
                "From": {"Email": FROM_EMAIL, "Name": "رسالة من نموذج التواصل"},
                "To": [{"Email": TO_EMAIL, "Name": "مدير نظام ادارة المخازن"}],
                "Subject": SUBJECT,
                "HTMLPart": HTML_BODY,
                "TextPart": TEXT_BODY,
            }
        ]
    }

    # ============================
    # إرسال الرسالة
    response = requests.post(
        "https://api.mailjet.com/v3.1/send",
        auth=(MJ_APIKEY_PUBLIC, MJ_APIKEY_PRIVATE),
        headers={"Content-Type": "application/json"},
        data=json.dumps(data),
    )

    # ============================
    # طباعة نتيجة الإرسال (اختياري)
    # print("Status Code:", response.status_code)
    # print("Response Body:", response.json())
