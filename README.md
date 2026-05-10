# 🛡️ Onlybugs05 OTP Migration Tool

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.6+-blue)

A high-performance, offline interactive tool to decode Google Authenticator migration URLs and generate scannable QR codes for easy account recovery and backup.

---

## 🌟 Features

- **🚀 100% Offline**: No data ever leaves your machine. Your 2FA secrets stay private.
- **🛠️ All-in-One**: Extracts Base32 secrets and generates QR codes in a single run.
- **🎨 Interactive CLI**: Premium user interface with branding and color-coded feedback.
- **📦 Zero Dependencies**: Runs using standard Python libraries (optional `qrencode` for QR generation).
- **🛡️ Security First**: Designed to help you move away from proprietary export formats to open standards like Bitwarden or KeePassXC.

---

## 🚀 Installation

### Prerequisites
- **Python 3.6+**
- **qrencode** (Optional, for generating QR code images)
  ```bash
  # Debian/Ubuntu/Kali/Parrot
  sudo apt install qrencode
  ```

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/otp-migration-tool.git
   cd otp-migration-tool
   ```
2. Make the script executable:
   ```bash
   chmod +x otp_tool.py
   ```

---

## 📖 Usage

Run the tool interactively:
```bash
./otp_tool.py
```

1. **Paste your URL**: When prompted, paste your `otpauth-migration://offline?data=...` URL.
2. **Choose QR Generation**: Type `y` if you want to generate `.png` QR codes for your accounts.
3. **View Results**: Your secrets will be printed on screen and saved to `extracted_secrets.txt`.

---

## 🛡️ Security Warning

**This tool handles highly sensitive 2FA secrets.** 
- Never share your migration URL with anyone.
- Run this tool only on a trusted, secure machine.
- Delete the generated `extracted_secrets.txt` and QR codes once you have imported them into your new authenticator.

---

## ⚖️ License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements or bug fixes, feel free to open an issue or submit a pull request.

**Crafted with ❤️ by Onlybugs05**
