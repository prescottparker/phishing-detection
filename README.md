# Web Scraper for Phishing Detection

## 🚀 Project Overview
This project is a **Web Scraper for Phishing Detection** built using **React (frontend) and Python (backend)**. It scans web pages for phishing indicators and provides real-time monitoring.

## 📂 Folder Structure
```
phishing-detection/
│── backend/              # Python Flask API for phishing detection
│   ├── app.py           # Main backend server file
│   ├── scraper.py       # Web scraper logic
│   ├── models.py        # Data models for processing
│   ├── utils.py         # Helper functions
│   ├── requirements.txt # Backend dependencies
│   ├── tests/           # Unit tests for backend
│
│── frontend/             # React-based UI for displaying results
│   ├── public/          # Static files
│   │   ├── index.html   # Main HTML file
│   ├── src/             # Main React source files
│   │   ├── components/  # React components
│   │   ├── utils/       # Helper functions
│   │   ├── App.js       # Main React component
│   │   ├── index.js     # React entry point
│   ├── package.json     # Frontend dependencies
│
│── .gitignore           # Git ignored files
│── README.md            # Project documentation
```

---

## 🛠️ Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/phishing-detection.git
cd phishing-detection
```

### 2️⃣ Backend Setup (Python + Flask)
#### Install Python (Ensure Python 3 is installed)
```bash
python3 --version
```
If not installed, install it:
```bash
sudo apt update && sudo apt install python3 python3-pip -y
```

#### Create Virtual Environment & Install Dependencies
```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate     # For Windows
pip install -r requirements.txt
```

#### Run Backend Server
```bash
python app.py
```

### 3️⃣ Frontend Setup (React)
#### Install Node.js & npm
```bash
node -v
npm -v
```
If not installed, download from [Node.js Official Site](https://nodejs.org/)

#### Install Frontend Dependencies
```bash
cd ../frontend
npm install
```

#### Start React Development Server
```bash
npm start
```

---

## 🚀 Running the Full Application
After starting both the **backend** and **frontend**, open the app in your browser:
```
http://localhost:3000
```

The backend runs on: `http://localhost:5000`

---

## 📌 API Endpoints (Backend)
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/scan?url=<website_url>` | Scans a website for phishing indicators |
| POST | `/api/report` | Reports a phishing site |

---

## ✅ Testing the Project
Run backend tests:
```bash
cd backend
pytest
```

Run frontend tests:
```bash
cd frontend
npm test
```

---

## 🔥 Deployment
### Deploy Backend on Heroku
```bash
heroku create phishing-api
heroku git:remote -a phishing-api
git push heroku main
```

### Deploy Frontend on Netlify
```bash
npm run build
netlify deploy
```

---

## 📝 Author
**Prescott Parker** 🏴‍☠️🚀

Happy Coding! 🚀🔥

