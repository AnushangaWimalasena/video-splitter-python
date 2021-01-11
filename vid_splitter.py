import cv2


def vid_splitter(path, sec, type_of_mov, batch):

    print("\n\n========= Processing ==========\n")
    video = cv2.VideoCapture(path)
    fps = video.get(cv2.CAP_PROP_FPS)
    loop_no: int = 0
    vid_id: int = 1
    no_of_frame_req = sec * fps

    output_name = str(batch) + '_' + type_of_mov + '_' + str(vid_id) + '.avi'
    if not video.isOpened():
        print("Error reading video file")

    frame_width = int(video.get(3))
    frame_height = int(video.get(4))

    size = (frame_width, frame_height)

    result = cv2.VideoWriter(output_name, cv2.VideoWriter_fourcc(*'MJPG'), fps, size)

    while True:
        ret, frame = video.read()
        if no_of_frame_req > loop_no:
            if ret:
                result.write(frame)
                # cv2.imshow('Frame', frame)
                loop_no = loop_no + 1
                if cv2.waitKey(1) & 0xFF == ord('s'):
                    break
            else:
                break
        else:
            result.release()
            vid_id = vid_id + 1
            loop_no = 0
            output_name = str(batch) + '_' + type_of_mov + '_' + str(vid_id) + '.avi'
            result = cv2.VideoWriter(output_name, cv2.VideoWriter_fourcc(*'MJPG'), fps, size)
            if ret:
                result.write(frame)
                # cv2.imshow('Frame', frame)
                loop_no = loop_no + 1
                if cv2.waitKey(1) & 0xFF == ord('s'):
                    break
            else:
                break

    video.release()
    result.release()

    # Closes all the frames
    cv2.destroyAllWindows()

    print("The videos ware successfully saved")
