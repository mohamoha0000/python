# بيانات التدريب (AND logic)
X = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]

Y = [0, 0, 0, 1]  # نريد تعلم بوابة AND

# أوزان وانحياز عشوائي
w = [0.5, -0.5]  # يمكن أن تبدأ بأي قيمة
b = 0.0

# معدل التعلم
lr = 0.1

# عدد التكرارات
epochs = 1000

for epoch in range(epochs):
    total_loss = 0
    for i in range(len(X)):
        x1, x2 = X[i]
        target = Y[i]

        # المخرجات (بدون دالة تنشيط)
        output = x1 * w[0] + x2 * w[1] + b

        # الخطأ
        error = output - target
        total_loss += error ** 2

        # تحديث الأوزان والانحياز باستخدام التدرج
        w[0] -= lr * error * x1
        w[1] -= lr * error * x2
        b    -= lr * error

    if epoch % 10 == 0:
        print(f"Epoch {epoch}, Loss: {total_loss:.4f}")

# اختبار النيرون بعد التدريب
print("\nاختبار النيرون بعد التعلم:")
for i in range(len(X)):
    x1, x2 = X[i]
    output = x1 * w[0] + x2 * w[1] + b
    print(f"Input: {X[i]}, Raw Output: {output:.4f}, Approximated: {round(output)}")
