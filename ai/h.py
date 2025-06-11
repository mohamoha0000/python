# البيانات
x = 2              # المدخل
target = 2         # الهدف (القيمة الصحيحة)
learning_rate = 0.1

# الأوزان الأولية
w1 = 0.5           # الوزن بين x و h
w2 = 1.0           # الوزن بين h و o

# === الحساب الأمامي (Forward) ===
h = x * w1
o = h * w2

# === حساب الخطأ ===
error = o - target
print(f"o = {o}, erro= {error}")

# === التحديث للخلف (Backpropagation) ===

# تحديث الوزن w2 (من h إلى o)
delta_w2 = error * h * learning_rate
w2 = w2 - delta_w2


# تحديث الوزن w1 (من x إلى h)
delta_w1 = error * w2 * x * learning_rate  # استخدم w2 القديم هنا
w1 = w1 - delta_w1


h = x * w1
o = h * w2

# === حساب الخطأ ===
error = o - target
print(f"o = {o}, erro= {error}")