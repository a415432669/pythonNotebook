import cv2
import numpy as np


cap = cv2.VideoCapture(0)
# while(1):
#     # get a frame
#     ret, frame = cap.read()
#     # show a frame
#     cv2.imshow("capture", frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

try :
    
    # show a frame
    n = 0
    while(n<10):
        n = n + 1
        ret, frame = cap.read()
        cv2.imshow("capture", frame)
        cv2.imwrite('./3.jpg',frame)
except Exception as e:
    print(e)
finally:
    cap.release()
    cv2.destroyAllWindows()