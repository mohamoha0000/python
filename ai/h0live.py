import matplotlib.pyplot as plt
import time

x = 2
target = 3
w1 = 0.5
w2 = 1.0
lr = 0.1

losses = []
times = []

start_time = time.time()
plt.ion()
fig, ax = plt.subplots()

max_loss = 0.01  # بداية لتجنب المحور صفر تمامًا

for epoch in range(100):
    h = x * w1
    o = h * w2
    loss = round(((o - target)**2)**0.5,10)

    current_time = time.time() - start_time
    losses.append(loss)
    times.append(current_time)

    if loss > max_loss:
        max_loss = loss  # تحديث الحد الأقصى للخسارة

    ax.clear()
    ax.plot(times, losses, label="Loss over time", color='blue')
    ax.set_xlabel("Time (seconds)")
    ax.set_ylabel("Loss")
    ax.set_title("Live Loss Curve")

    # هنا نضبط المحور Y ليمتد دائمًا إلى أعلى loss رأيناه + هامش بسيط
    ax.set_ylim(0, max_loss + 0.1)

    ax.legend()
    plt.pause(0.5)

    print("result:", o, "loss:", loss)

    # backward (بدون أي تغيير)
    error = o - target
    delta_h = error * w2
    delta_w1 = delta_h * x * lr
    delta_w2 = error * h * lr

    w1 = w1 - delta_w1
    w2 = w2 - delta_w2

plt.ioff()
plt.show()
