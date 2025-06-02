# بيانات التدريب (AND logic)
X = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]

Y = [0, 0, 0, 1]  # المخرجات المتوقعة

# أوزان الطبقة المخفية (2 نيرون مخفي × 2 مدخل)
w1 = [0.1, 0.2]  # نيرون h1
w2 = [0.3, 0.4]  # نيرون h2

# أوزان من الطبقة المخفية إلى المخرج
w3 = [0.5, 0.6]  # من h1 و h2 إلى المخرج

# الانحيازات
b1 = 0.1  # انحياز h1
b2 = 0.2  # انحياز h2
b3 = 0.3  # انحياز نيرون المخرج

# معدل التعلم
lr = 0.01

# عدد مرات التكرار
epochs = 1000

for epoch in range(epochs):
    total_loss = 0
    for i in range(4):
        x1, x2 = X[i]
        target = Y[i]

        # === Forward pass بدون أي دالة تفعيل ===
        h1 = x1 * w1[0] + x2 * w1[1] + b1
        h2 = x1 * w2[0] + x2 * w2[1] + b2

        y = h1 * w3[0] + h2 * w3[1] + b3

        # === الخطأ (error) ===
        error = y - target
        total_loss += error ** 2
        # === Backpropagation (يدوي بدون مشتقات تفعيل) ===
        # نحسب deltas مباشرة من الخطأ
        dy = error  # لا مشتقة، لأن لا تفعيل

        # التدرجات للأوزان بين h → y
        dw3_0 = dy * h1
        dw3_1 = dy * h2
        db3   = dy

        # التدرجات للأوزان بين x → h
        dh1 = dy * w3[0]  # تأثير y على h1
        dh2 = dy * w3[1]  # تأثير y على h2

        dw1_0 = dh1 * x1
        dw1_1 = dh1 * x2
        db1   = dh1

        dw2_0 = dh2 * x1
        dw2_1 = dh2 * x2
        db2   = dh2

        # === تحديث الأوزان والانحيازات ===
        w3[0] -= lr * dw3_0
        w3[1] -= lr * dw3_1
        b3    -= lr * db3

        w1[0] -= lr * dw1_0
        w1[1] -= lr * dw1_1
        b1    -= lr * db1

        w2[0] -= lr * dw2_0
        w2[1] -= lr * dw2_1
        b2    -= lr * db2

    if epoch % 100 == 0:
        print(f"Epoch {epoch}, Loss: {total_loss:.4f}")

# === اختبار النموذج بعد التدريب ===
print("\nنتائج التعلم بعد التدريب:")
for i in range(4):
    x1, x2 = X[i]
    h1 = x1 * w1[0] + x2 * w1[1] + b1
    h2 = x1 * w2[0] + x2 * w2[1] + b2
    y = h1 * w3[0] + h2 * w3[1] + b3
    print(f"Input: {[x1, x2]}, Output: {y:.4f}, Rounded: {round(y)}")
