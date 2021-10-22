"""install
python -m pip install opencv-python
python -m pip install pyzmq
"""
import multiprocessing
import cv2
import numpy as np
import zmq
import time
import logging
from timeit import default_timer as timer

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
log = logging.getLogger()

start = timer()
TOPIC = b"topic"

HEIGHT=480
WIDTH=640
CHANNELS=3
FPS = 10

def create_image() -> np.ndarray:
    FONT                   = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = (100,100)
    FONT_SCALE=2
    fontColor              = (0,255,0)
    lineType               = 2
    frame = np.zeros((HEIGHT, WIDTH, CHANNELS), np.uint8)
    end = timer()
    delta_sec = round(end-start, 3)
    cv2.putText(frame,str(delta_sec),
        bottomLeftCornerOfText,
        FONT,
        FONT_SCALE,
        fontColor,
        lineType)

    return frame

def pub(name="pub", show=False):
    log.info("Start publisher: %s" % name)
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    url = "tcp://*:5555"
    socket.bind(url)
    
    while True:
        frame = create_image()
        data = frame.tobytes()
        socket.send_multipart((TOPIC, data), copy=False)
        if show:
            cv2.imshow(name, frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        

        time.sleep(1/FPS)


def sub(name="sub", show=False):
    log.info("Start subscripber: %s" % name)
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    url = "tcp://127.0.0.1:5555"
    socket.connect(url)
    socket.setsockopt(zmq.SUBSCRIBE, TOPIC)
    send_counter = 0
    while True:
        topic, data = socket.recv_multipart(copy=False)
        frame = np.frombuffer(data, dtype=np.uint8)
        frame = frame.reshape((HEIGHT, WIDTH, CHANNELS))
        if send_counter%10==0:
            log.info(f"images recv  {frame.shape}")
        send_counter+=1
        if show:
            cv2.imshow(name, frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

if __name__ == "__main__":
    SUB_SHOW_IMG = False
    PUB_SHOW_IMG = False
    p_pub = multiprocessing.Process(target=pub, args=("pub", PUB_SHOW_IMG))
    p_sub = multiprocessing.Process(target=sub, args=("sub1", SUB_SHOW_IMG))
    p_sub2 = multiprocessing.Process(target=sub, args=("sub2", SUB_SHOW_IMG))
    p_sub.start()
    p_sub2.start()
    p_pub.start()

    p_pub.join()
    p_sub.join()
    p_sub2.join()
