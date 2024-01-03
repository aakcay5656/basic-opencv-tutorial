
# Template Matching with OpenCV

This Python application checks whether a given template matches the live video stream from the computer camera. If a match is found, it displays "Match" on the screen.

### Usage

1. Install Python and OpenCV:

    ```bash
    pip install opencv-python
    ```

2. Ensure the camera is working:

    - Connect the camera to your computer.
    - Change the value of `cv2.VideoCapture(0)` in the code to the opening number of your camera (usually 0 or 1).

3. Specify the Template:

    - Replace `Your İmage` with the file name of the template you want to use.

4. Run the Code:

    ```bash
    python your_script_name.py
    ```

5. Press 'q' to exit.

### Notes

- You can adjust the match threshold (`threshold`) according to your needs.

- Make sure to install the [OpenCV](https://pypi.org/project/opencv-python/) library before using the code.


----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# OpenCV ile Eşleşen Şablon Bulma

Bu Python uygulaması, bilgisayar kamerasından canlı video akışını alarak verilen bir şablonun eşleşip eşleşmediğini kontrol eder ve eşleşme durumunda ekrana "Match" yazısı çizer.

### Kullanım

1. Python ve OpenCV'yi yükleyin:

    ```bash
    pip install opencv-python
    ```

2. Kameranın çalıştığından emin olun:

    - Kamerayı bilgisayarınıza bağlayın.
    - Kodun içindeki `cv2.VideoCapture(0)` satırındaki `0` değerini, kameranın açılış numarasına göre değiştirin (genellikle 0 veya 1).

3. Şablonu Belirtin:

    - `Your İmage` kısmını, kullanmak istediğiniz şablonun dosya adıyla değiştirin.

4. Kodu Çalıştırın:

    ```bash
    python your_script_name.py
    ```

5. Çıkış için 'q' tuşuna basın.

### Notlar

- Eşleşme eşiği (`threshold`) değerini ihtiyaca göre ayarlayabilirsiniz.

- Kodu kullanmadan önce [OpenCV](https://pypi.org/project/opencv-python/) kütüphanesini yüklediğinizden emin olun.
