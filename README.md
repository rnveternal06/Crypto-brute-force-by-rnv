
# 🚀 DOGE BY RNV - Dogecoin BIP44 Wallet Scanner

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)  
![License](https://github.com/rnveternal06/Crypto-brute-force-by-rnv/blob/afb55947f7ebae7688b8fa4972fa3b14fa3fee19/LICENSE)  
![Platform](https://img.shields.io/badge/Platform-Pydroid3%20%7C%20Linux%20%7C%20PC-green)

**DOGE BY RNV** is a Python script designed to brute-force scan Dogecoin wallets by generating BIP39 mnemonics and deriving addresses using the BIP44 standard.

> 🧠 This project is intended for educational and ethical research purposes only, to better understand how mnemonic phrases, key derivation, and Dogecoin addresses work.

---

## 🔧 Key Features

- Generate random BIP39 mnemonic phrases  
- Derive private keys using BIP44 path `m/44'/3'/0'/0/0`  
- Convert private keys to WIF format and Dogecoin address  
- Check address balances via [dogechain.info](https://dogechain.info) API  
- Multi-threaded scanning (20 threads by default)  
- Automatically save found wallets with non-zero balances  

---

## 📱 How to Run on Android (Pydroid 3)

1. Download **Pydroid 3** from Google Play Store  
2. Open the Pydroid 3 Terminal or code editor  
3. Install required libraries:

   ```
   pip install mnemonic
   pip install ecdsa
   pip install base58
   pip install requests
   pip install colorama
   ```

4. Save the script as `DOGE_BY_RNV.py` in your storage:

   ```
   /storage/emulated/0/Download/
   ```

5. Run the script:

   ```
   python /storage/emulated/0/Download/DOGE_BY_RNV.py
   ```

💡 Tip: Make sure your internet is active — the script uses a live API for balance checks.

---

## 💰 BONUS AVAILABLE

BTC and EVM versions are available and proven to generate results.

To get access:

1. Donate **100 DOGE** to this wallet address:

   ```
   DFgKicnDK8oEr2nevqoszDc8QtLT8veNeq
   ```

2. Comment **"donation complete"** and send me your **Telegram username**.  
   I’ll send you the BTC and EVM versions directly.

---

## ⚠️ Disclaimer

This tool is for **educational and ethical use only**.  
Unauthorized access to wallets is **illegal**.  
The developer is **not responsible** for any misuse.

---

## 💻 Installation on PC / Termux / Linux

```
pip install mnemonic
pip install ecdsa
pip install base58
pip install requests
pip install colorama
```

### ▶️ How to Run

```
python DOGE_BY_RNV.py
```

---

## ⭐ Give a Star

If you like this project or find it helpful, don’t forget to ⭐ star the repository!
