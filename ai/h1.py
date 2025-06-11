import math

# تفعيل sigmoid
def sigmoid(z):
    return 1 / (1 + math.exp(-z))

# مشتقة sigmoid
def sigmoid_derivative(z):
    s = sigmoid(z)
    return s * (1 - s)

# المدخلات
x = 2
target = 1
learning_rate = 0.1

# الأوزان الأولية
w1 = 0.5  # x → h
w2 = 1.0  # h → o

# === الحساب الأمامي ===
z1 = x * w1
a1 = sigmoid(z1)

z2 = a1 * w2
a2 = sigmoid(z2)

# === حساب الخطأ ===
error = a2 - target

# === مشتقة نيرون الإخراج ===
delta_o = error * sigmoid_derivative(z2)

# === مشتقة نيرون h ===
delta_h = delta_o * w2 * sigmoid_derivative(z1)

# === تحديث الأوزان ===
w2 = w2 - learning_rate * delta_o * a1
w1 = w1 - learning_rate * delta_h * x

# طباعة النتائج
print("Output a2 =", a2)
print("Error =", error)
print("Delta Output =", delta_o)
print("Delta Hidden =", delta_h)
print("New w2 =", w2)
print("New w1 =", w1)
