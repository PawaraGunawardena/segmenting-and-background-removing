from os.path import join
import cv2

def write_frame_output(output_path, img_name, img):
    file_path = join(output_path+"/",img_name )
    # img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.imwrite(file_path, img)

def background_substractor(video_name, background_removed_frames_path):
    cap = cv2.VideoCapture(video_name)
    bgSubThreshold = 10
    fgbg = cv2.createBackgroundSubtractorMOG2(0, bgSubThreshold)
    ret = True
    frame_no = 1

    while(ret):
        ret, frame = cap.read()
        fgmask = fgbg.apply(frame)
        write_frame_output(background_removed_frames_path, str(frame_no) + ".jpg", fgmask)
        cv2.imshow('frame',fgmask)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
        frame_no+=1
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    video_name = 'Statue of Liberty.mp4'

    frame_path = "background_removed_frames"
    background_substractor(video_name, frame_path)
