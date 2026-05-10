#!/usr/bin/env python3
"""
🛡️ Onlybugs05 OTP Migration Tool
================================
A professional, offline tool to decode Google Authenticator migration URLs.
Developed by: Onlybugs05
License: MIT
"""

import base64
import urllib.parse
import sys
import os
import subprocess
import time

# --- Configuration & Styling ---
VERSION = "1.0.0"
C_BOLD = "\033[1m"
C_GREEN = "\033[92m"
C_CYAN = "\033[96m"
C_YELLOW = "\033[93m"
C_RED = "\033[91m"
C_RESET = "\033[0m"

BANNER = f"""{C_CYAN}{C_BOLD}
      ___       __    __  .______          ___      
     /   \\     |  |  |  | |   _  \\        /   \\     
    /  ^  \\    |  |  |  | |  |_)  |      /  ^  \\    
   /  /_\\  \\   |  |  |  | |      /      /  /_\\  \\   
  /  _____  \\  |  `--'  | |  |\\  \\----./  _____  \\  
 /__/     \\__\\  \\______/  | _| `.____/__/     \\__\\ 
                                                     
{C_GREEN}
         >>> AuraOTP Decoder Tool v{VERSION} <<<
           Developed by: {C_YELLOW}Onlybugs05{C_GREEN}
{C_RESET}"""


def read_varint(data, pos):
    """Reads a protobuf varint from bytes."""
    res, shift = 0, 0
    while pos < len(data):
        b = data[pos]
        res |= (b & 0x7f) << shift
        pos += 1
        if not (b & 0x80): return res, pos
        shift += 7
    return res, pos

def decode_migration(url):
    """Parses the Google Authenticator migration protobuf data."""
    try:
        parsed = urllib.parse.urlparse(url)
        qs = urllib.parse.parse_qs(parsed.query)
        data_b64 = qs.get('data', [''])[0]
        data = base64.b64decode(urllib.parse.unquote(data_b64))
    except Exception as e:
        print(f"{C_RED}[!] Error: Invalid migration URL or data format.{C_RESET}")
        return []

    pos, results = 0, []
    while pos < len(data):
        tag, pos = read_varint(data, pos)
        if (tag >> 3) == 1 and (tag & 0x07) == 2:
            length, pos = read_varint(data, pos)
            sub_data = data[pos:pos+length]
            pos += length
            sub_pos, otp = 0, {'secret': b'', 'name': '', 'issuer': ''}
            while sub_pos < len(sub_data):
                sub_tag, sub_pos = read_varint(sub_data, sub_pos)
                if (sub_tag & 0x07) == 2:
                    v_len, sub_pos = read_varint(sub_data, sub_pos)
                    val = sub_data[sub_pos:sub_pos+v_len]
                    sub_pos += v_len
                    field = sub_tag >> 3
                    if field == 1: otp['secret'] = val
                    elif field == 2: otp['name'] = val.decode('utf-8', errors='ignore')
                    elif field == 3: otp['issuer'] = val.decode('utf-8', errors='ignore')
                elif (sub_tag & 0x07) == 0: _, sub_pos = read_varint(sub_data, sub_pos)
            results.append(otp)
        elif (tag & 0x07) == 2:
            l, pos = read_varint(data, pos)
            pos += l
        elif (tag & 0x07) == 0: _, pos = read_varint(data, pos)
    return results

def clear_screen():
    """Clears the terminal screen for a clean UI."""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()
    print(BANNER)
    
    try:
        url = input(f"{C_BOLD}[?] Paste your migration URL: {C_RESET}").strip()
        if not url:
            print(f"{C_RED}[!] No URL provided. Exiting.{C_RESET}")
            return

        print(f"\n{C_CYAN}[*] Decoding and extracting accounts...{C_RESET}")
        accounts = decode_migration(url)
        
        if not accounts:
            print(f"{C_RED}[!] No accounts found. Check your URL.{C_RESET}")
            return

        print(f"{C_GREEN}[+] Success! Found {len(accounts)} 2FA accounts.{C_RESET}")
        
        want_qr = input(f"{C_BOLD}[?] Generate scannable QR codes? (y/n): {C_RESET}").lower().startswith('y')
        
        output_dir = "Decoded_QR_Codes"
        if want_qr:
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            print(f"{C_CYAN}[*] Generating QR images using qrencode...{C_RESET}")

        print(f"\n{C_BOLD}{'ISSUER:ACCOUNT':<50} | {'SECRET'}{C_RESET}")
        print(f"{C_CYAN}{'-' * 80}{C_RESET}")
        
        with open("extracted_secrets.txt", "w") as f:
            for acc in accounts:
                secret = base64.b32encode(acc['secret']).decode('utf-8').replace('=', '')
                issuer = acc['issuer'].replace("Unknown", "").strip() or "Authenticator"
                name = acc['name'].strip()
                
                if not acc['issuer'] and ":" in name:
                    p = name.split(":", 1)
                    issuer, name = p[0].strip(), p[1].strip()
                
                label = f"{issuer}:{name}"
                print(f"{C_GREEN}{label:<50}{C_RESET} | {C_YELLOW}{secret}{C_RESET}")
                f.write(f"{label} | {secret}\n")

                if want_qr:
                    encoded_label = urllib.parse.quote(label)
                    encoded_issuer = urllib.parse.quote(issuer)
                    otp_url = f"otpauth://totp/{encoded_label}?secret={secret}&issuer={encoded_issuer}"
                    safe_name = "".join([c if c.isalnum() or c in "._-" else "_" for c in label])
                    subprocess.run(["qrencode", "-o", f"{output_dir}/{safe_name}.png", otp_url])

        print(f"{C_CYAN}{'-' * 80}{C_RESET}")
        print(f"{C_BOLD}[+] All secrets have been saved to: {C_YELLOW}extracted_secrets.txt{C_RESET}")
        if want_qr:
            print(f"[*] QR images are ready in: {C_YELLOW}./{output_dir}/{C_RESET}")
        
        print(f"\n{C_BOLD}{C_GREEN}>> Stay Secure! Thank you for using Onlybugs05 Tools <<{C_RESET}\n")

    except KeyboardInterrupt:
        print(f"\n{C_RED}[!] Cancelled.{C_RESET}")
    except Exception as e:
        print(f"\n{C_RED}[!] Unexpected error: {e}{C_RESET}")

if __name__ == "__main__":
    main()
