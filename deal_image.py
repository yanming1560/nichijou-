import cv2,pyautogui as pag

im=cv2.imread('TEST.jpg')
print(im.shape)
# suofanghou=cv2.resize(im,(1000,1000),interpolation=cv2.INTER_CUBIC)     #缩放
part = im[0:1080, 0:1920]  # 裁图
#除了截图和缩放，还应该考虑本身像素不够的问题，比如不到600*600，应该切方形放大。
# cap = cv2.VideoCapture(0)
x,y=pag.position()
num=1
while(not(x<=1 and y<=1)):  #结束判断，可以截图触发结束,也可以判断鼠标位置不截图退出。
    # cv2.imshow('suofanghou',suofanghou)
    # cv2.imshow('im',im)
    # cv2.imshow('part',part)
    # ret, frame = cap.read()
    # cv2.imshow('frame', frame)

    #加框随时显示，需要每次读图片剪裁
    im = cv2.imread('TEST.jpg')
    part = im[0:1080, 0:1920]
    x,y=pag.position()
    part2=cv2.rectangle(part,(x,y),(x+600,y+600),(255,255,255),2)
    cv2.imshow('part2', part2)
    if cv2.waitKey(1) & 0xFF == ord('p'):       #只能用一个，两个就不好使了。
        cv2.imwrite("cut_%s.jpg"%num,im[y:y+600,x:x+600])
        num+=1
        # break

    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break



cv2.destroyAllWindows()
