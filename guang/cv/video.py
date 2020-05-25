import cv2
from pyprobar import bar
def getFrame(filename, frameNum=10, W=[0, -1], H=[0, -1], gray=False):
    """ Get a specific frame in the video
    :param W: ROI W range
    :param H: ROI H range
    """
    cap = cv2.VideoCapture(filename)
    fps = cap.get(cv2.CAP_PROP_FPS)
    size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))  # 获取视频尺寸

    cap.set(cv2.CAP_PROP_POS_FRAMES, frameNum)  # 设置要获取的帧号
    ret, frame = cap.read()
    if not gray:
        ROI = frame[H[0]:H[1], W[0]:W[1], :]
    else:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ROI = frame[H[0]:H[1], W[0]:W[1]]
    return fps, size, ROI


def embedFrameInfo(inputvideo, outputvideo):
    cap = cv2.VideoCapture(inputvideo)
    fps = cap.get(cv2.CAP_PROP_FPS)

    size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))  # 获取视频尺寸

    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 编码格式

    video = cv2.VideoWriter(outputvideo, fourcc, fps, size)

    TotolFrameNum = int(cap.get(7)) # == cv2.CV_CAP_PROP_FRAME_COUNT
    for idx in range(TotolFrameNum):
        ret, frame = cap.read()
        if not ret:
            break
        cv2.putText(frame, f'current frame: {idx}', (50, 60), cv2.FONT_HERSHEY_PLAIN, 1.0, (0, 255, 0), 2, 1)
        cv2.putText(frame, f'time: {idx/ fps:.2f} S', (50, 100), cv2.FONT_HERSHEY_PLAIN, 1.0, (0, 255, 0), 2, 1)
        video.write(frame)
        bar(idx, TotolFrameNum)
        # cv2.imshow("zd1", frame)
        # if cv2.waitKey(int(10/fps)) & 0xFF == ord('q'): # 0xFF的使用：https://blog.csdn.net/i6223671/article/details/88924481
        #     # 实际上 任何一个整数与0xff做与运算，将会取得这个数最后八位
        #     break

    cap.release()
    # if show:
    #     cv2.destroyAllWindows()
