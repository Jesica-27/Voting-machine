# 🗳️ Digital VVPAT Counting System using QR Code Detection

## 📌 Overview

The **Digital VVPAT Counting System** is a Python-based project designed to digitize the counting of VVPAT (Voter Verifiable Paper Audit Trail) slips.

This system introduces an innovative approach by using **unique QR codes for each political party**, which are scanned using a webcam to automatically count votes. This reduces manual effort and increases accuracy and speed in the counting process.

---

## 🎯 Project Objective

* To digitize VVPAT slip counting
* To eliminate manual counting errors
* To automate vote counting using QR codes
* To improve transparency and efficiency in elections

---

## 🧠 Problem Statement

In traditional systems:

* VVPAT slips are counted manually
* Counting is time-consuming
* Human errors may occur
* Verification process is slow

---

## 💡 Proposed Solution

This project uses:

* 📷 A webcam to capture VVPAT slips
* 🔳 Unique QR codes assigned to each party
* 🧠 A Python-based system to detect and decode QR codes
* 📊 Automatic vote counting and dashboard display

---

## ⚙️ Working Principle

1. Each party is assigned a **unique QR code**
2. The QR code is printed on the VVPAT slip
3. A webcam captures the QR code image
4. The system decodes the QR code
5. The corresponding party’s vote count is incremented
6. Results are updated in real-time on the dashboard

---

## 🚀 Features

* 🔳 QR code-based vote identification
* 📷 Real-time webcam scanning
* 📊 Automatic vote counting
* ⚡ Fast and accurate processing
* 📈 Live result display dashboard

---

## 🧱 Project Structure

```id="q1z7mf"
Voting-machine/
│
├── voting.py        # QR scanning and vote processing
├── dashboard.py     # Displays live results
├── README.md        # Documentation
```

---

## ⚙️ Technologies Used

* **Programming Language:** Python
* **Libraries (suggested/used):**

  * OpenCV (for webcam capture)
  * QR code detection libraries (like pyzbar)
* **Concepts:**

  * Image Processing
  * Real-time Data Processing
  * Automation Systems

---

## ▶️ How to Run

### Clone Repository

```bash id="d9k3pa"
git clone https://github.com/Jesica-27/Voting-machine.git
```

### Navigate to Folder

```bash id="c7v2qx"
cd Voting-machine
```

### Run QR Voting System

```bash id="s4n8yt"
python voting.py
```

### View Dashboard

```bash id="z6m1hr"
python dashboard.py
```

---

## 📊 Example Workflow

```id="k2p9dw"
Scan QR Code → Detect Party → Increment Vote → Update Dashboard
```

---

## 🔒 Advantages

* ✔ Eliminates manual counting
* ✔ Reduces human error
* ✔ Faster result processing
* ✔ Scalable for large elections
* ✔ Improves transparency

---

## 🔒 Limitations

* Requires good lighting for QR detection
* Webcam quality affects accuracy
* Currently a prototype (not deployed in real elections)

---

## 🌱 Future Enhancements

* 🤖 AI-based image validation
* 📡 Raspberry Pi integration (edge device)
* 📷 High-speed camera for large-scale counting
* ☁️ Cloud database for centralized results
* 🔐 Secure encryption for QR codes
* 📊 Advanced analytics dashboard

---

## 🔗 Real-World Application

* Election Commission vote verification
* Automated audit systems
* Smart polling/counting centers

---

## ⚡ Innovation Highlight

👉 This project introduces **QR code-based automated VVPAT counting**, replacing manual verification with a fast, reliable, and scalable digital solution.

---

## 👩‍💻 Author

**Jesica**
GitHub: https://github.com/Jesica-27

---
