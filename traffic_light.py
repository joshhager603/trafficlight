import cv2

state1 = cv2.imread("./state1.jpeg")
state2 = cv2.imread("./state2.jpeg")
state3 = cv2.imread("./state3.jpeg")
state4 = cv2.imread("./state4.jpeg")

states = [state1, state2, state3, state4]

wait_times = [5000, 2000, 5000, 2000]

for _ in range(10):
    for state, wait_time in zip(states, wait_times):
        cv2.imshow('Traffic Light', state)
        cv2.waitKey(wait_time)

cv2.destroyAllWindows()