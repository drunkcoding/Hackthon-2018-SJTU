import cv2 
import time
import screeninfo

if __name__ == '__main__':
    cv2.namedWindow("camera",1)
    
    video="http://192.168.1.101:8080/video"
    capture =cv2.VideoCapture(video)

    num = 0;
    while True:
        success, img = capture.read()

        # print (success)
        # window_name = 'projector'
        # cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
        # cv2.moveWindow(window_name, screen.x - 1, screen.y - 1)
        # cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN,
        #                       cv2.WINDOW_FULLSCREEN)
        cv2.imshow("camera",img)
        key = cv2.waitKey(10) 
        if key == 27:
            print("esc break...")
            break
        if key == ord(' '):
            num = num+1
            filename = "frames_%s.jpg" % num
            print (num)

    capture.release()
    cv2.destroyWindow("camera")