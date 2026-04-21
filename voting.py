from luma.core.interface.serial import i2c
from luma.oled.device import sh1106
from PIL import Image
from gpiozero import Button, LED
from pyzbar.pyzbar import decode
import cv2
import time
import os
import json

# ---------------- OLED ----------------
serial = i2c(port=1, address=0x3C)
device = sh1106(serial)

# ---------------- BUTTONS ----------------
buttons = [
    Button(17, pull_up=True),
    Button(27, pull_up=True),
    Button(5, pull_up=True),
    Button(6, pull_up=True),
    Button(16, pull_up=True)
]

# ---------------- LEDS ----------------
leds = [
    LED(22),
    LED(23),
    LED(24),
    LED(25),
    LED(20)
]

# ---------------- DATA ----------------
image_folder = "/home/pi/Desktop/images"

party_images = [
    "Congress.png",
    "ADMK.png",
    "DMK.png",
    "TVK.png",
    "BJP.png"
]

# ---------------- DISPLAY ----------------
def display_image_with_qr(img_file):
    try:
        img = Image.open(os.path.join(image_folder, img_file)).resize((64,64)).convert("1")
        qr  = Image.open(os.path.join(image_folder, img_file.replace(".png","_qr.png"))).resize((64,64)).convert("1")

        combined = Image.new("1", (128,64))
        combined.paste(img, (0,0))
        combined.paste(qr, (64,0))

        device.display(combined)

    except Exception as e:
        print("Display Error:", e)

# ---------------- QR SCAN (NO GUI) ----------------
def scan_qr_once():
    cap = cv2.VideoCapture(0, cv2.CAP_V4L2)

    print("Scanning QR (10 sec)...")
    start_time = time.time()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        barcodes = decode(gray)

        if not barcodes:
            barcodes = decode(frame)

        for barcode in barcodes:
            data = barcode.data.decode("utf-8")
            print("Scanned:", data)

            cap.release()
            return data

        if time.time() - start_time > 10:
            print("Timeout")
            break

    cap.release()
    return None

# ---------------- MAIN LOOP ----------------
print("System Ready...")

try:
    while True:
        for i, button in enumerate(buttons):

            if button.is_pressed:

                leds[i].on()
                img_file = party_images[i]

                # Show symbol + QR
                display_image_with_qr(img_file)
                time.sleep(1)

                # Scan QR
                qr_data = scan_qr_once()

                if qr_data == img_file:

                    # ?? Load current votes
                    with open("votes.json", "r") as f:
                        counts = json.load(f)

                    # ?? Increase count
                    counts[img_file] += 1

                    # ?? Save back
                    with open("votes.json", "w") as f:
                        json.dump(counts, f)

                    print(f"? Vote counted for {img_file}")
                    print("Total:", counts[img_file])

                elif qr_data is None:
                    print("No QR detected")

                else:
                    print("? Invalid QR")

                device.clear()
                leds[i].off()

                # Prevent multiple presses
                while button.is_pressed:
                    time.sleep(0.1)

                time.sleep(0.5)

        time.sleep(0.1)

except KeyboardInterrupt:
    print("Stopped")
    device.clear()