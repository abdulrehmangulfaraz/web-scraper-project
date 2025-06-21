# 📘 Book Scraper with BeautifulSoup

This project is a real-world web scraping tool built using Python, `requests`, `BeautifulSoup`, and `pandas`.

It scrapes books from [Books to Scrape](https://books.toscrape.com/), a perfect static site for learning web scraping.

---

## 🚀 Features

- Extracts:
  - ✅ Book Title
  - 💰 Price
  - ⭐ Rating
  - 🔗 Link
- Stores output in:
  - `data.json`
  - `data.xlsx`
- Clean, structured code inside Jupyter Notebook

---

## 📂 Project Structure

```

web-scraper-project/
├── data.json            ← Scraped book data in JSON format
├── data.xlsx            ← Same data in Excel format
├── scraper.ipynb        ← Jupyter notebook with all scraping logic
├── requirements.txt     ← Dependencies
├── .gitignore

````

---

## 📦 Requirements

- Python 3.x
- Libraries:
  - `requests`
  - `beautifulsoup4`
  - `pandas`

Install them with:

```bash
pip install -r requirements.txt
````

---

## 🧪 How to Run

1. Clone the repo:

   ```bash
   git clone https://github.com/abdulrehmangulfaraz/web-scraper-project.git
   cd web-scraper-project
   ```

2. Activate your virtual environment *(if used)*

3. Run the notebook:

   ```bash
   jupyter notebook
   ```

---

## 🌐 Source

Scraping target: [https://books.toscrape.com](https://books.toscrape.com)
(Open-source site designed for scraping practice)

---

## 👑 Author

**Abdulrehman Gulfaraz**
[GitHub](https://github.com/abdulrehmangulfaraz) • [LinkedIn](https://www.linkedin.com/in/abdulrehman-gulfaraz)

---

## ⚠️ Disclaimer

This project is for educational purposes only. Please respect `robots.txt` and terms of any website you scrape.
