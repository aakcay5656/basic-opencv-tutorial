

import cv2


def main():

    camera = cv2.VideoCapture(0)


    template_path = "Your İmage"
    template = cv2.imread(template_path)

    if template is None:
        print(f"Error: Template not found at {template_path}")
        return


    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    while True:

        ret, frame = camera.read()

        if not ret:
            print("Error: Unable to capture frame")
            break


        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


        result = cv2.matchTemplate(frame_gray, template_gray, cv2.TM_CCOEFF_NORMED)


        threshold = 0.8


        loc = cv2.minMaxLoc(result)[3]
        if result[loc[1], loc[0]] > threshold:
            print("Eşleşme Bulundu!")
            cv2.putText(frame, 'Match', loc, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)


        cv2.imshow('Frame', frame)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
