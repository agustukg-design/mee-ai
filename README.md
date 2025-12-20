# 🧠 Mee AI: Sovereign Cognitive Layer (OS-Native)

> **"Intelligence without Surveillance."**
> A next-generation offline cognitive layer designed to run locally on Linux/Windows, bringing Large Language Model (LLM) capabilities to the operating system level without a single byte leaving the device.

---

## 🏗️ The Problem & The Vision
In the current era, AI utility comes at the cost of **Data Sovereignty**. Users must upload their private documents to cloud providers to get analysis.
* **The Risk:** Data leakage, dependency on internet connectivity, and lack of cultural context.
* **Our Solution:** **Mee AI** acts as a cognitive bridge between the User and the OS. It lives in the RAM, processes data locally, and understands local context (Mee Culture focus).

## 🛡️ Core Architecture
1.  **100% Air-Gapped:** Designed to run with zero internet connection. No telemetry, no API calls to external servers.
2.  **OS-Native Service:** Runs as a `systemd` service (Linux) or Background Service (Windows), managed directly by the kernel.
3.  **Fundamental Solidity:** Dependency-locked environment ensures stability across machines.

## 🚀 Installation

### Prerequisites
* Python 3.10+
* RAM: 8GB (Recommended) / 4GB (Minimum)

### Quick Start
```bash
# 1. Clone the repository
git clone https://github.com/agustukg-design/mee-ai.git
cd mee_os

# 2. Create Virtual Environment
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# 3. Install Dependencies (Locked Version)
pip install -r requirements.txt

# 4. Run the Cognitive Core
python3 app.py
```

## 📂 Project Structure
* `app.py`: The central cognitive cortex (Flask/FastAPI based).
* `latih_otak.py`: Training module for local contextual adaptation.
* `requirements.txt`: Immutable dependency lockfile.
* `install_hardened_mee.sh`: Security-focused deployment script.

---
*Built with ❤️ in Papua Tengah | "Mee AI" - Local Spirit, Global Standard.*
