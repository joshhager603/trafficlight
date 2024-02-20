import cv2

state1 = cv2.imread("./state1.png")
state2 = cv2.imread("./state2.png")
state3 = cv2.imread("./state1.png")
state4 = cv2.imread("./state2.png")

states = [state1, state2, state3, state4]

wait_times = [5000, 2000, 5000, 2000]

for _ in range(10):
    for state, wait_time in zip(states, wait_times):
        cv2.imshow('State', state)
        cv2.waitKey(wait_time)

cv2.destroyAllWindows()
