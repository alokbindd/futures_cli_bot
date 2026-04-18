# 🚀 Futures CLI Bot with Streamlit UI

A modular Python application to place **Binance Futures Testnet (USDT-M)** orders with input validation, logging, and both CLI and Streamlit UI interfaces for an enhanced user experience.

---

## 📌 Features

* ✅ Place **MARKET** and **LIMIT** orders
* ✅ Supports both **BUY** and **SELL**
* ✅ CLI interface with interactive fallback input
* ✅ Streamlit web UI for easy order placement
* ✅ Input validation (type, side, quantity, price)
* ✅ Structured logging of:

  * Order requests
  * Order responses
  * Errors
* ✅ Confirmation step before placing order
* ✅ Clean and modular project structure

---

## 🧱 Project Structure

```
futures_cli_bot/
│
├── cli.py                  # CLI entrypoint
├── streamlit.py            # Streamlit UI entrypoint
├── requirements.txt        # Dependencies
├── sample_trading.log      # Sample logs (included)
├── .gitignore
│
└── bot/
    ├── __init__.py
    ├── client.py           # Binance client setup
    ├── orders.py           # Order placement logic
    ├── validators.py       # Input validation
    └── logging_config.py   # Logging setup
```

---

## ⚙️ Prerequisites

* Python **3.9+**
* Binance Futures **Testnet account**
* API credentials from Testnet

---

## 🔐 Setup

### 1. Clone the repository

```bash
git clone https://github.com/alokbindd/futures_cli_bot.git
cd futures_cli_bot
```

---

### 2. Create virtual environment

#### Windows (PowerShell)

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

#### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Create `.env` file

```
API_KEY=your_binance_testnet_api_key
API_SECRET_KEY=your_binance_testnet_secret_key
```

⚠️ Do NOT commit `.env` file.

---

## ▶️ Usage

### CLI Interface

#### 1️⃣ MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

---

#### 2️⃣ LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 65000
```

---

#### 3️⃣ Interactive Mode

```bash
python cli.py
```

👉 Prompts user for missing inputs only (partial fallback UX)

---

### Streamlit UI

Run the web interface:

```bash
streamlit run streamlit.py
```

👉 Opens a web browser with an intuitive UI for placing orders, viewing order details, and handling errors.

---

### 🔐 Confirmation Step

Before placing order (in both CLI and UI):

```
Are you sure you want to place this order? (y/n)
```

---

## ❌ Error Example

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001
```

👉 Output:

```
Price is required for LIMIT order
```

---

## 📊 Logging

* Logs are written to: `trading.log`
* Includes:

  * Order request details
  * Order response data
  * Errors and exceptions

---

## 📁 Sample Logs

A sample log file `sample_trading.log` is included demonstrating:

* ✅ MARKET order execution
* ✅ LIMIT order execution
* ❌ Error handling

> Note: Actual `trading.log` is excluded via `.gitignore`.

---

## 🎁 Bonus Features

### Enhanced CLI UX

* Interactive prompts for missing inputs
* Partial CLI + interactive hybrid mode
* Input validation with clear messages
* Confirmation before execution

### Streamlit Web UI

* User-friendly web interface
* Real-time order placement
* Detailed order response display
* Error handling with user notifications

---

## 🧠 Assumptions

* Uses Binance Futures Testnet:

  ```
  https://testnet.binancefuture.com/fapi
  ```
* Account has sufficient test balance
* Symbol format follows Binance standard (e.g., BTCUSDT)
* Quantity and price must be positive numbers
* LIMIT orders require price

---

## 📝 Notes

* No automated tests included
* Designed for clarity, modularity, and extensibility
* Logging kept clean and meaningful (no unnecessary noise)

---

## 👨‍💻 Author

**Alok Bind**

---

## 📌 Conclusion

This project demonstrates:

* API integration with Binance Futures Testnet
* Clean architecture and modular design
* Robust validation and error handling
* User-friendly CLI and web UI experiences
