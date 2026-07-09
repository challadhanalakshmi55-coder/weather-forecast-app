# 🚀 Deployment Guide - Streamlit Cloud

Complete step-by-step guide to deploy your Weather Forecast App on Streamlit Cloud for FREE.

---

## ✅ What You Need

- GitHub account (free)
- Streamlit Cloud account (free)
- This repository pushed to GitHub
- API key ready (already in `.env`)

---

## 📋 Complete Deployment Steps

### **STEP 1: Prepare Your Repository (Local Computer)**

1. Open terminal/command prompt
2. Navigate to your project folder:
   ```bash
   cd d:\weather-forecast-app-main
   ```

3. Make sure all files are there:
   - ✅ `app.py`
   - ✅ `weather.py`
   - ✅ `requirements.txt`
   - ✅ `.env`
   - ✅ `.gitignore`
   - ✅ `README.md`
   - ✅ `.streamlit/config.toml`
   - ✅ `.streamlit/secrets.toml`

4. Test the app locally first:
   ```bash
   pip install -r requirements.txt
   streamlit run app.py
   ```
   
   - Open your browser to `http://localhost:8501`
   - Search for a city (e.g., "London", "New York")
   - Verify it shows weather info
   - Close the app (Press Ctrl+C)

---

### **STEP 2: Push to GitHub**

1. Initialize Git (if not already done):
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Weather Forecast App ready for deployment"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/weather-forecast-app.git
   git push -u origin main
   ```

   **Replace `YOUR-USERNAME` with your actual GitHub username**

2. Verify on GitHub:
   - Go to https://github.com/YOUR-USERNAME/weather-forecast-app
   - You should see all your files there

---

### **STEP 3: Create Streamlit Cloud Account**

1. Go to https://streamlit.io/cloud
2. Click **"Sign up"** (top right)
3. Sign up with your GitHub account
4. Authorize Streamlit to access your GitHub repos
5. After sign-up, you'll be on Streamlit Cloud dashboard

---

### **STEP 4: Deploy Your App**

1. On Streamlit Cloud dashboard, click **"New app"** (top left)

2. Fill in the deployment form:
   - **Repository owner:** `YOUR-USERNAME`
   - **Repository:** `weather-forecast-app`
   - **Branch:** `main`
   - **Main file path:** `app.py` ← **⚠️ IMPORTANT: NOT main.py**

3. Click **"Deploy"** button

4. Wait 2-5 minutes for deployment to complete

5. Your app URL will be: `https://weather-forecast-app.streamlit.app`

   (The exact URL depends on your repo name)

---

### **STEP 5: Add API Key to Streamlit Secrets (CRITICAL!)**

**This step is necessary for your app to work!**

1. After deployment completes, on your app page, click the **☰ (menu)** icon (top right)

2. Click **"Settings"** from the dropdown

3. In the left sidebar, click **"Secrets"** tab

4. In the text box, paste EXACTLY this:

   ```
   OPENWEATHERMAP_API_KEY = "9aac7ae37f68e3d23dbfcc5f0fa4a1ff"
   ```

5. Click **"Save"** button

6. Your app will automatically **reboot** (takes 30-60 seconds)

7. Once it's done rebooting, refresh the page

---

### **STEP 6: Test Your Deployed App**

1. Refresh the page after reboot
2. Search for a city name (e.g., "Paris", "Tokyo", "Sydney")
3. Click "Get Weather"
4. Verify you see:
   - ✅ Temperature
   - ✅ Humidity
   - ✅ Weather Condition
   - ✅ Wind Speed

**Success!** Your app is now live! 🎉

---

### **STEP 7: Share Your App Link**

Your app URL is ready to share:
```
https://weather-forecast-app.streamlit.app
```

Replace `weather-forecast-app` with your actual repo name.

Share this link with anyone and they can use your weather app!

---

## 🔧 What You Created

| File | Purpose |
|------|---------|
| `.env` | Stores API key for local testing |
| `.gitignore` | Prevents `.env` from being pushed to GitHub |
| `requirements.txt` | Lists all Python packages needed |
| `.streamlit/config.toml` | Streamlit UI configuration |
| `.streamlit/secrets.toml` | Local test secrets (not pushed) |
| `README.md` | Project documentation |
| `DEPLOYMENT.md` | This deployment guide |

---

## ⏱️ How Long It Stays Live

- **Forever!** (as long as your GitHub repo exists)
- **Auto-restarts** if there's an error
- **Updates automatically** when you push new code
- **Goes to sleep** after 7 days of no traffic (wakes up when accessed)

---

## ⚠️ Free Tier Limitations

| Limit | Details |
|-------|---------|
| **API Calls** | 1,000 per day (OpenWeatherMap) |
| **Users** | 1 at a time (others queue) |
| **Memory** | 1 GB RAM |
| **Inactivity** | Sleeps after 7 days |

---

## 🐛 Troubleshooting

### Issue: "Error running app"
**Solution:** 
- Check that secrets are added correctly
- Wait a minute after saving secrets
- Refresh the page

### Issue: "City not found"
**Solution:**
- Check spelling (e.g., "London" not "Londan")
- Try a major world city
- Try without special characters

### Issue: App shows blank page
**Solution:**
- Wait for app to fully load (can take 30-60 seconds)
- Hard refresh browser (Ctrl+Shift+R or Cmd+Shift+R)

### Issue: Can't find "Secrets" in Settings
**Solution:**
- Make sure you clicked the **☰ menu** (top right of app)
- Look for "Settings" → then "Secrets" in left sidebar

---

## 📝 Making Updates

After deployment, if you want to make changes:

1. Edit your code locally
2. Test with `streamlit run app.py`
3. Push to GitHub:
   ```bash
   git add .
   git commit -m "Update: your changes"
   git push
   ```
4. Streamlit Cloud **automatically redeploys** in 1-2 minutes

---

## ✨ You're Done!

Your Weather Forecast App is now live and shareable! 🌤️

Congratulations! 🎉
