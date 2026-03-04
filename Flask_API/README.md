# 🚀 Flask + Playwright API Project

This project demonstrates how to integrate **Flask** with **Playwright** to run browser automation through an API endpoint.

The API launches a headless browser, navigates to a website, extracts the page title, and returns the result as JSON.

---

## 📌 Features

* Flask REST API
* Playwright headless browser automation
* Async function execution
* JSON API response
* Simple and clean structure

---

## 🛠 Technologies Used

* Python 3.x
* Flask
* Playwright
* AsyncIO

---

## 📂 Project Structure

```
project-folder/
│
├── app.py
├── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```
git clone <your-repo-url>
cd project-folder
```

### 2️⃣ Create Virtual Environment (Recommended)

```
python -m venv venv
```

Activate it:

**Windows (PowerShell):**

```
.\venv\Scripts\Activate.ps1
```

**Windows (CMD):**

```
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```
pip install flask playwright
```

Install Playwright browsers:

```
playwright install
```

---

## ▶️ Running the Application

Start the Flask server:

```
python app.py
```

Server will start at:

```
http://127.0.0.1:5000
```

---

## 🌐 API Endpoints

### 🔹 Home Route

```
GET /
```

Response:

```
Flask + Playwright is running!
```

---

### 🔹 Run Playwright Automation

```
GET /run-test
```

This endpoint:

* Launches a headless Chromium browser
* Navigates to https://example.com
* Extracts the page title
* Returns JSON response

Example Response:

```json
{
  "message": "Playwright executed successfully",
  "page_title": "Example Domain"
}
```

---

## 🧠 How It Works

1. Flask receives request on `/run-test`
2. `asyncio.run()` executes the async Playwright function
3. Playwright launches browser in headless mode
4. Navigates to target URL
5. Extracts page title
6. Returns JSON response

---

## ⚠️ Notes

* This setup is suitable for development/testing.
* For production, consider:

  * Running with Gunicorn
  * Using background task queue (Celery)
  * Switching to async framework like Quart

---


## 👨‍💻 Author

Muthukumar K

---

## 📜 License

This project is for educational purposes.
