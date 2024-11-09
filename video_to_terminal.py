import cv2
import os


def print_frame(frame):
    # Clear the terminal
    os.system('clear')
    # Print the frame
    for row in frame:
        print(''.join(row))


def resize_frame(frame, width, height):
    # Resize the frame to fit the terminal's width and height
    frame = cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)
    # Convert the frame to grayscale
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Convert the frame to ASCII characters
    ascii_frame = []
    for row in frame:
        ascii_row = []
        for pixel in row:
            ascii_row.append(chr(int(pixel / 255 * 94 + 32)))
        ascii_frame.append(ascii_row)
    return ascii_frame


def main():
    # Prompt the user for a video file
    video_file = input('Enter the path to a video file: ')
    # Open the video file
    cap = cv2.VideoCapture(video_file)
    # Get the terminal's width and height
    width, height = os.get_terminal_size()
    while True:
        # Read a frame from the video file
        ret, frame = cap.read()
        if not ret:
            break
        # Resize the frame
        ascii_frame = resize_frame(frame, width, height)
        # Print the frame
        print_frame(ascii_frame)


if __name__ == '__main__':
    main()
