import cv2

state1 = cv2.imread("./state1.png")
state2 = cv2.imread("./state2.png")
state3 = cv2.imread("./state3.png")
state4 = cv2.imread("./state4.png")
state5 = cv2.imread("./state5.png")
state6 = cv2.imread("./state3.png")

states = [state1, state2, state3, state4, state5, state6]
wait_times = [5000, 2000, 1000, 5000, 2000, 1000]

for _ in range(10):
    for state, wait_time in zip(states, wait_times):
        cv2.imshow('Traffic Light', state)
        key = cv2.waitKey(wait_time)
        if key == ord('q'):  #Press q to quit
            break
    else:
        continue 
    break  

cv2.destroyAllWindows()