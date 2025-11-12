# Auracle-1
> Seal it, sign it, sell it: hardware-rooted acoustic oracle for ads, royalties & compliance.

Turn any speaker into a trustless cash-register—pay only for seconds that actually hit the air.

---

## 📋 Table of Contents
- [Quick Start](#quick-start)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## ⚡ Quick Start (phone only)
1. Record 5 s WAV → `demo.wav`
2. Upload to Replit → terminal:
   ```bash
   pip install pydub eth-account
   python sign_audio.py demo.wav

   ---

## 🎯 Features
• 1-second acoustic slicing & hashing
 
• Inaudible watermark detection (15–18 kHz)
 
• On-device ECDSA signing (Ethereum)
 
• On-chain receipt minting (ERC-20 compatible)
 
• Zero-trust, sealed hardware option

---

## 🧰 Tech Stack
• Python 3.10+ (pydub, eth-account)
 
• Solidity ^0.8 (IAudioOracle.sol)
 
• Ethereum / Base testnet
 
• GitHub Actions (auto-stats)

---

## 🛠️ Usage
from sign_audio import slice_hash
data = slice_hash("ad.wav")  # returns signed JSON
## Output:
[{"chunk":0,"hash":"0x7f2a...","sig":"0x8b3c...","addr":"0xabc..."}]

---

## 🗺️ Roadmap
• Live Android mic stream
 
• Sealed Pi sensor + tamper case
 
• 100-venue pilot (JHB + PTA)
 
• Patent filing (SA provisional)
 
• Installer bounty program

---

## 🤝 Contributing
1. Open an issue → get assigned
2. Fork → branch  feat/your-name 
3. PR → merge → earn contributor NFT key
4. MIT licence — do what you want, leave my name.

---

📄 License
MIT © 2025 BioShepard
