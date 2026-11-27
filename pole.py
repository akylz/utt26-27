import cv2
import numpy as np 
dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
detector = cv2.aruco.ArucoDetector(dictionary)
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if not cap.isOpened():
    print("Не удалось открыть камеру")

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1920)
smooth_src = None
while True:
   ok, cadr = cap.read()

   if not ok:
      break

   corners, ids, _ = detector.detectMarkers(cadr)
   
   if ids is not None:
      cv2.aruco.drawDetectedMarkers(cadr, corners, ids)

      markers = dict(zip(ids.ravel(), corners))

      if 27 in markers and 28 in markers and 29 in markers:
         width, height = 800, 600
      
         src = np.float32([
            *markers[27][0],
            *markers[28][0],
            *markers[29][0],
         ])

         dst = np.float32([
            (739.06, 97.85), (693.00, 97.85), (693.00, 51.78), (739.06, 51.78),
            (165.86, 97.85), (119.80, 97.85), (119.80, 51.78), (165.86, 51.78),
            (94.21, 527.74), (48.15, 527.74), (48.15, 481.68), (94.21, 481.68),
         ])

         #if matrix is None:
         if smooth_src is None:
            smooth_src = src.copy()
         else:
            smooth_src = 0.85 * smooth_src + 0.15 * src

         matrix, _ = cv2.findHomography(smooth_src, dst)
         
         perspective = cv2.warpPerspective(cadr, matrix, (width, height))

         scale = (dst[4, 0] - dst[5, 0]) / 18
         x = dst[5, 0] - 5 * scale
         y = dst[5, 1] + 5 * scale

         left, top, right, bottom = map(round, (
            x, y, x + 252 * scale, y + 168 * scale
         ))

         for col in range(10):
            x = left + col * (right - left) // 9
            cv2.line(perspective, (x, top), (x, bottom), (32, 0, 128), 1)

         for row in range(7):
            y = top + row * (bottom - top) // 6
            cv2.line(perspective, (left, y), (right, y), (32, 0, 128), 1)

         cv2.imshow("perspective", perspective)

   cv2.imshow("pypynua", cadr)


   
   if cv2.waitKey(1) == 27:
      break

cap.release()
cv2.destroyAllWindows()
