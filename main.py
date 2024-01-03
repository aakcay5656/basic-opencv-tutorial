

import cv2


def main():
    # Kamera açılımını belirtin (genellikle 0 veya 1 olabilir)
    camera = cv2.VideoCapture(0)

    # Karşılaştırılacak şablon fotoğrafı
    template_path = "im2.jpeg"
    template = cv2.imread(template_path)

    if template is None:
        print(f"Error: Template not found at {template_path}")
        return

    # Şablonun gri tonlamalı hali
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    while True:
        # Kamera görüntüsünü alın
        ret, frame = camera.read()

        if not ret:
            print("Error: Unable to capture frame")
            break

        # Görüntüyü gri tonlamaya çevirin
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Şablon eşleştirmesi yapın
        result = cv2.matchTemplate(frame_gray, template_gray, cv2.TM_CCOEFF_NORMED)

        # Eşleşme eşiği
        threshold = 0.8

        # Eşleşme bulundu mu kontrol edin
        loc = cv2.minMaxLoc(result)[3]
        if result[loc[1], loc[0]] > threshold:
            print("Eşleşme Bulundu!")
            cv2.putText(frame, 'Match', loc, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        # Görüntüyü gösterin
        cv2.imshow('Frame', frame)

        # Çıkış için 'q' tuşuna basılıp basılmadığını kontrol edin
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Kamera ve pencereyi serbest bırakın
    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
