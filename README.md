# 🛡️ AuraOTP Decoder

![Version](https://img.shields.io/badge/version-1.0.0-blue?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)
![Python](https://img.shields.io/badge/python-3.6+-blue?style=for-the-badge)

**AuraOTP Decoder** is a premium, high-performance, and 100% offline tool designed to decode Google Authenticator migration URLs. It extracts raw Base32 secrets and generates scannable QR codes, allowing you to seamlessly migrate your 2FA accounts to open-standard authenticators like Bitwarden, KeePassXC, or Ente Auth.

Developed with ❤️ by **Onlybugs05**.

---

## 🚀 Why AuraOTP?

Google Authenticator's "Export" feature uses a proprietary, encoded format that is difficult to use with other applications. **AuraOTP** breaks this barrier by providing a transparent, secure, and user-friendly way to reclaim your 2FA secrets.

### Key Features:
- **🔒 100% Offline & Private**: No network requests. Your secrets never leave your local environment.
- **⚡ One-Command Recovery**: Automatically parses complex Protobuf data into readable text and images.
- **📱 Universal Compatibility**: Generates standard `otpauth://` QR codes compatible with EVERY modern 2FA app.
- **✨ Premium UI**: Branded interactive CLI with color-coded status updates and ASCII art.

---

## 🛠️ Tech Stack

- **Language**: Python 3
- **Encoding**: Base64, Base32, Protobuf (Manual Parser)
- **Dependencies**: `qrencode` (Optional for image generation)

---

## 📥 Installation & Setup

### 1. Install System Dependencies
Ensure you have Python 3 and `qrencode` installed on your machine:
```bash
# Debian / Ubuntu / Kali / Parrot
sudo apt update && sudo apt install -y qrencode
```

### 2. Clone the Tool
```bash
git clone https://github.com/onlybugs05/AuraOTP-Decoder.git
cd AuraOTP-Decoder
chmod +x AuraOTP_Decoder.py
```

---

## 📖 How to Use

Simply run the tool and follow the interactive prompts:
```bash
./AuraOTP_Decoder.py
```

1. **Export from Google**: Open Google Authenticator -> Settings -> Transfer accounts -> Export accounts.
2. **Get the URL**: Scan the QR code with any standard scanner to get the `otpauth-migration://` URL.
3. **Run AuraOTP**: Paste the URL into the tool and choose if you want to generate QR code images.

---

## 🛡️ Security Best Practices

> [!IMPORTANT]
> - **Wipe Data**: Once you have imported your accounts, delete the `extracted_secrets.txt` and the `Decoded_QR_Codes` folder.
> - **Secure Deletion**: Use `shred` or a similar tool for permanent file removal.
> - **Trust**: Only run this script on a machine you fully control.

---

## 🤝 Contributing

We welcome contributions! 
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## ⚖️ License

Distributed under the **MIT License**. See `LICENSE` for more information.

---

<p align="center">
  <b>Built by Onlybugs05</b><br>
  <i>"Securing the web, one bug at a time."</i>
</p>

