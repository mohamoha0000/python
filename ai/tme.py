x = 2
target = 2
w1 = 0.5
lr = 0.1
for i in range(150):
    o = x * w1
    loss = ((o - target)**2)**0.5
    print("ruslt:"+str(o)+" loss:"+str(loss))
    # backward
    error = o - target
    delta_w1 = error * x * lr

    # update
    w1 = w1 - delta_w1
#https://chatgpt.com/share/68434c4c-f06c-8004-a997-7c6dfb0eff3d