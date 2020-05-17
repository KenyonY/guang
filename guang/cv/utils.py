import numpy as np
import cv2
import matplotlib.pyplot as plt

def cvtBlackWhite(fileName):
    '''
    convert image's black color to white and meanwhile convert white to black.
    '''
    img = cv2.imread(fileName, 0)
    img = 255-img
    cv2.imwrite('convert_'+fileName, img)
    
def cvt2rgb(img,channel = 'bgr'):
    '''it can convert image channel BGR,BGRA,HLS,HSV to RGB'''
    if channel=='bgr' or channel=='BGR' or channel=='BGRA':
        print('bgr',img.shape)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    elif channel=='HLS' or channel=='hls':
        img = cv2.cvtColor(img, cv2.COLOR_HLS2RGB)
    elif channel=='HSV' or channel=='hsv':
        img = cv2.cvtColor(img, cv2.COLOR_HSV2RGB)
    else:
        return 'bad channel'
    return img
    
def myplot(img,channel='bgr'):
    ''' can show image channel BGR,BGRA,HLS,HSV.
    if RGB, set channel = 0'''
    if channel:
        img = cvt2rgb(img, channel)
    plt.figure(figsize=(7,7))
    plt.imshow(img)
    plt.show()

if __name__ == "__main__":
    l = np.array([2,2,2,2,5,5,3,9,9])
    print(sort_count(l))


