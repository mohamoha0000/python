x = 2
target = 3
w1 = 0.5
w2 = 1.0
lr = 0.1
for i in range(10):
    h = x * w1
    o = h * w2
    loss = ((o - target)**2)**0.5
    print("ruslt:"+str(o)+" loss:"+str(loss))
    # backward
    error = o - target
    delta_h = error * w2
    delta_w1 = delta_h * x * lr
    delta_w2 = error * h * lr

    # update
    w1 = w1 - delta_w1
    w2 = w2 - delta_w2
#https://chatgpt.com/share/68434c4c-f06c-8004-a997-7c6dfb0eff3d