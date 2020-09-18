import cv2
import numpy as np


def main():
     # 读取名称为 IMG_3067.png的图片
     img = cv2.imread("IMG_3067.png",1)
      
     # 将图片转换为格式 hsv
     hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
      
     # 定义蓝色的上下限 
     #lower_blue =  np.array([100,50,50])
     #higher_blue = np.array([140,255,255])


     # 定义蓝色的上下限  139,140,145  90,91,99
     lower = np.array([90,10,60])
     higher =  np.array([120,43,156])
      
     #在图片中提取指定颜色的部分
     mask = cv2.inRange(hsv,lower,higher)
      
     #和原图像求“与”操作，只保留
     left = cv2.bitwise_and(img,img,mask=mask)

     # 显示Blue
     cv2.imshow("P3",left)
     cv2.waitKey(0);
     cv2.destroyAllWindows();
 
 


if __name__ == "__main__":
    main()