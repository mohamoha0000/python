# repeat_whatsapp.py
from mitmproxy import http
import asyncio
import copy

# عدد التكرارات (بجانب الأصلية)
REPEAT_COUNT = 4

async def repeat_request(flow, count):
    for i in range(count):
        # إنشاء نسخة من الطلب
        new_flow = copy.deepcopy(flow)
        new_flow.request.timestamp_start = None
        new_flow.request.timestamp_end = None
        new_flow.response = None

        # إرسال الطلب من جديد
        await asyncio.sleep(0.3)  # تأخير بسيط لتفادي الحظر
        flow.reply.send(new_flow.request)
        print(f"[✅] Replayed request #{i+1} to: {new_flow.request.pretty_url}")

def request(flow: http.HTTPFlow):
    # فحص إن كان الطلب موجه إلى واتساب
    if "c.whatsapp.net" in flow.request.pretty_host and flow.request.method == "POST":
        print(f"[📩] Intercepted WhatsApp message: {flow.request.pretty_url}")
