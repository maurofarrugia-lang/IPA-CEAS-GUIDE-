# 🚀 GitHub Deployment Guide

## Step-by-Step Instructions

### **Option 1: Upload via GitHub Web Interface** (Easiest)

1. **Create a new repository**
   - Go to https://github.com/new
   - Repository name: `mauros-guide` (or any name you prefer)
   - Description: "Comprehensive EU Asylum Pact Reference Tool"
   - Choose **Public** (required for free GitHub Pages)
   - ✅ Check "Add a README file" (we'll replace it)
   - Click **Create repository**

2. **Upload files**
   - Click **Add file** → **Upload files**
   - Drag all files from `mauros-guide-github` folder:
     - `index.html`
     - `complete_database.json`
     - `server.py`
     - `README.md`
     - `LICENSE`
     - `.gitignore`
     - `UPDATE_V3.md`
     - `📖_COMPLETE_GUIDE_V3.md`
     - `📖_READ_ME_FIRST.md`
     - `index-standalone.html` (optional)
   - Commit message: "Initial commit - v3.0 with 206 article items"
   - Click **Commit changes**

3. **Enable GitHub Pages**
   - Go to repository **Settings** (top right)
   - Scroll to **Pages** (left sidebar)
   - Under "Source", select:
     - Branch: `main` (or `master`)
     - Folder: `/ (root)`
   - Click **Save**
   - Wait 1-2 minutes

4. **Access your site**
   - GitHub will show: `Your site is live at https://yourusername.github.io/mauros-guide/`
   - Click the link to test
   - Share with colleagues!

---

### **Option 2: Git Command Line** (For developers)

```bash
# 1. Clone or initialize repository
git clone https://github.com/yourusername/mauros-guide.git
cd mauros-guide

# OR create new repo
mkdir mauros-guide
cd mauros-guide
git init
git branch -M main

# 2. Copy files from mauros-guide-github folder
cp /path/to/mauros-guide-github/* .

# 3. Add and commit
git add .
git commit -m "Initial commit - v3.0 with 206 article items"

# 4. Add remote (if not cloned)
git remote add origin https://github.com/yourusername/mauros-guide.git

# 5. Push to GitHub
git push -u origin main

# 6. Enable GitHub Pages via web interface (see Option 1, step 3)
```

---

### **Option 3: GitHub Desktop** (GUI alternative)

1. Download GitHub Desktop: https://desktop.github.com
2. Sign in with your GitHub account
3. Click **File** → **New Repository**
   - Name: `mauros-guide`
   - Local path: Choose location
   - Click **Create Repository**
4. Copy files from `mauros-guide-github` to the repository folder
5. In GitHub Desktop:
   - Check all files in left panel
   - Commit message: "Initial commit - v3.0"
   - Click **Commit to main**
   - Click **Publish repository** (top right)
6. Enable GitHub Pages via web interface (see Option 1, step 3)

---

## 🔧 Configuration

### **Custom Domain** (Optional)

1. In repository Settings → Pages:
2. Under "Custom domain", enter your domain (e.g., `asylum-guide.example.com`)
3. Click **Save**
4. Add DNS records at your domain registrar:
   ```
   Type: CNAME
   Name: asylum-guide (or @)
   Value: yourusername.github.io
   ```
5. Wait for DNS propagation (~10 minutes to 24 hours)

### **HTTPS Enforcement**

- ✅ Automatically enabled by GitHub Pages
- Ensure "Enforce HTTPS" is checked in Settings → Pages

---

## 📊 Repository Settings Recommendations

### **General**
- ✅ Add description: "Comprehensive EU Asylum Pact Reference Tool - 206 article-level items"
- ✅ Add website: Your GitHub Pages URL
- ✅ Add topics: `asylum`, `eu-law`, `reference-tool`, `casework`, `legal-research`

### **Social Preview**
- Upload a screenshot as social preview image (Settings → General → Social preview)

### **Issues**
- ✅ Enable Issues for user feedback and bug reports

### **Discussions** (Optional)
- Enable for Q&A and community engagement

---

## 🎯 After Deployment Checklist

- [ ] Test the live URL
- [ ] Click all 4 tabs (Regulations, Definitions, EUAA Guidelines, Caseworker Index)
- [ ] Test search function with:
  - [ ] `credibility`
  - [ ] `detention`
  - [ ] `Art 10`
  - [ ] `take charge`
- [ ] Verify EUR-Lex links open correctly
- [ ] Test on mobile device
- [ ] Add to mobile home screen
- [ ] Share URL with colleagues

---

## 🔄 Updating Content Later

### **Via Web Interface:**
1. Navigate to file (e.g., `complete_database.json`)
2. Click pencil icon (Edit)
3. Make changes
4. Commit changes (bottom of page)
5. Wait 1-2 minutes for GitHub Pages to rebuild

### **Via Git:**
```bash
# 1. Make changes to files locally
nano complete_database.json

# 2. Commit and push
git add .
git commit -m "Added new EUAA guideline on XYZ"
git push origin main

# 3. Wait 1-2 minutes for auto-deploy
```

---

## 📱 Sharing Your Deployment

### **URL Format:**
```
https://yourusername.github.io/mauros-guide/
```

### **Share on:**
- Internal wiki pages
- Email signatures
- Training materials
- Slack/Teams channels
- Professional LinkedIn

### **QR Code** (for print materials):
Generate QR code at: https://www.qr-code-generator.com

---

## 🆘 Troubleshooting

| Problem | Solution |
|---------|----------|
| **404 Page Not Found** | Wait 2-5 minutes after enabling Pages. Hard refresh (Ctrl+Shift+R). Check branch is `main` and folder is `/` |
| **Blank page** | Check browser console (F12). Verify `complete_database.json` uploaded correctly |
| **Search not working** | Hard refresh. Check file permissions (should be 644 or readable) |
| **Mobile display issues** | Ensure `index.html` viewport meta tag intact |
| **Changes not showing** | Clear cache, hard refresh, or use incognito mode |

---

## 🔐 Security Best Practices

- ✅ Never commit sensitive data (passwords, API keys)
- ✅ Repository is public (required for free GitHub Pages)
- ✅ All content is public domain or properly licensed
- ✅ No server-side processing (static site)

---

## 📈 Analytics (Optional)

Add Google Analytics to track usage:

1. Get tracking ID from https://analytics.google.com
2. Edit `index.html`, add before `</head>`:
```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```
3. Commit and push changes

---

## ⭐ Promote Your Repository

### **Add badges to README:**
```markdown
[![GitHub stars](https://img.shields.io/github/stars/yourusername/mauros-guide?style=social)](https://github.com/yourusername/mauros-guide)
[![GitHub forks](https://img.shields.io/github/forks/yourusername/mauros-guide?style=social)](https://github.com/yourusername/mauros-guide/fork)
```

### **Add to awesome lists:**
- Search for "awesome asylum" or "awesome legal-tech" lists
- Submit pull requests to include your tool

---

## 📞 Support

- **GitHub Issues:** Report bugs or request features
- **GitHub Discussions:** Q&A and community support
- **EUR-Lex:** https://eur-lex.europa.eu/contact.html
- **EUAA:** https://www.euaa.europa.eu/contact-us

---

## ✅ Deployment Complete!

**Your Reference Tool is Now Online! 🎉**

Next steps:
1. ✅ Test the live site
2. ✅ Share URL with colleagues
3. ✅ Add to bookmarks/home screen
4. ✅ Star the repository
5. ✅ Monitor for updates

---

*Need help? Open an issue on GitHub or refer to GitHub Pages documentation: https://docs.github.com/en/pages*
