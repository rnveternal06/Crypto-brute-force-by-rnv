import os, hmac, hashlib, struct, base58, requests, threading
from mnemonic import Mnemonic
from ecdsa import SigningKey, SECP256k1
from hashlib import sha256
from colorama import Fore, Style, init

init(autoreset=True)

# Konstanta Dogecoin
DOGE_COIN_TYPE = 3
ADDRESS_PREFIX = b'\x1e'
WIF_PREFIX = b'\x9e'

counter = 0
lock = threading.Lock()

print("="*60)
print(f"{Fore.GREEN}🚀 DOGE BIP44 Wallet Scanner")
print(f"{Fore.CYAN}🔧 Created by RNVEternal")
print("="*60)

# Fungsi generate seed dari mnemonic
def mnemonic_to_seed(mnemonic, passphrase=""):
    mnemonic = mnemonic.encode("utf-8")
    salt = b"mnemonic" + passphrase.encode("utf-8")
    return hashlib.pbkdf2_hmac("sha512", mnemonic, salt, 2048)

# Fungsi derivasi BIP32
def derive_child_key(parent_key, parent_chain_code, index):
    hardened = index >= 0x80000000
    if hardened:
        data = b'\x00' + parent_key + struct.pack('>L', index)
    else:
        sk = SigningKey.from_string(parent_key, curve=SECP256k1)
        vk = sk.verifying_key
        pubkey = b'\x02' + vk.to_string()[:32] if vk.pubkey.point.y() % 2 == 0 else b'\x03' + vk.to_string()[:32]
        data = pubkey + struct.pack('>L', index)

    I = hmac.new(parent_chain_code, data, hashlib.sha512).digest()
    Il, Ir = I[:32], I[32:]
    return Il, Ir

# Derivasi path BIP44
def derive_path(seed, path):
    I = hmac.new(b"Bitcoin seed", seed, hashlib.sha512).digest()
    key, chain_code = I[:32], I[32:]
    for level in path.split("/")[1:]:
        hardened = "'" in level
        index = int(level.replace("'", ""))
        if hardened:
            index += 0x80000000
        key, chain_code = derive_child_key(key, chain_code, index)
    return key

# Private Key ke WIF Dogecoin
def private_to_wif(private_key_bytes):
    payload = WIF_PREFIX + private_key_bytes + b'\x01'  # compressed
    checksum = sha256(sha256(payload).digest()).digest()[:4]
    return base58.b58encode(payload + checksum).decode()

# Private Key ke Dogecoin Address
def private_to_doge_address(private_key_bytes):
    sk = SigningKey.from_string(private_key_bytes, curve=SECP256k1)
    vk = sk.verifying_key
    pubkey = b'\x02' + vk.to_string()[:32] if vk.pubkey.point.y() % 2 == 0 else b'\x03' + vk.to_string()[:32]
    sha = hashlib.sha256(pubkey).digest()
    rip = hashlib.new("ripemd160", sha).digest()
    payload = ADDRESS_PREFIX + rip
    checksum = hashlib.sha256(hashlib.sha256(payload).digest()).digest()[:4]
    address = base58.b58encode(payload + checksum).decode()
    return address

# Cek saldo address DOGE
def check_balance_doge(address):
    try:
        url = f"https://dogechain.info/api/v1/address/balance/{address}"
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            return float(r.json().get("balance", 0.0))
    except:
        return 0.0
    return 0.0

# Worker Thread
def worker():
    global counter
    mnemo = Mnemonic("english")
    while True:
        mnemonic_phrase = mnemo.generate(strength=128)
        seed = mnemonic_to_seed(mnemonic_phrase)
        priv_key = derive_path(seed, "m/44'/3'/0'/0/0")
        address = private_to_doge_address(priv_key)
        wif = private_to_wif(priv_key)
        balance = check_balance_doge(address)

        with lock:
            counter += 1
            color = Fore.YELLOW
            if balance > 0:
                color = Fore.RED
                print(f"{color}[{counter}] 🎯 FOUND! {address} | Balance: {balance} DOGE")

                with open("found_doge.txt", "a") as f:
                    f.write(f"Mnemonic: {mnemonic_phrase}\n")
                    f.write(f"Address : {address}\n")
                    f.write(f"WIF     : {wif}\n")
                    f.write(f"Balance : {balance} DOGE\n")
                    f.write("="*60 + "\n")
            else:
                print(f"{color}[{counter}] {mnemonic_phrase} | {address} | Balance: {balance} DOGE")

# Jalankan Multi Thread
THREAD_COUNT = 20
for _ in range(THREAD_COUNT):
    t = threading.Thread(target=worker)
    t.daemon = True
    t.start()

# Loop utama
try:
    while True:
        pass
except KeyboardInterrupt:
    print(f"\n{Fore.RED}❌ Stopped by user.")