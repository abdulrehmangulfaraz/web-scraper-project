# 📚 Web Scraper Project - Books to Scrape

A complete web scraping project using **Python**, featuring both **manual scraping** with `requests` + `BeautifulSoup`, and a **framework-based scraper** using `Scrapy`.

> 🔍 Target Website: [books.toscrape.com](https://books.toscrape.com)  
> 🎯 Purpose: Learn structured web scraping, file outputs (JSON, Excel), and scraping with/without a framework.

---

## 📦 Features

- Scrapes book data from the homepage of [Books to Scrape](https://books.toscrape.com)
- Extracts:
  - ✅ Book Title
  - 💵 Price
  - ⭐ Rating
  - 🔗 Product Link
- Saves data to:
  - `data.json`
  - `data.xlsx`

---

## 🧰 Tools & Technologies

| Tool          | Purpose                          |
|---------------|----------------------------------|
| Python        | Base programming language        |
| `requests`    | To fetch HTML pages (static)     |
| `BeautifulSoup4` | To parse HTML elements        |
| `pandas`      | To convert data & save to Excel  |
| `Scrapy`      | Framework for high-speed scraping |
| Jupyter Notebook | Interactive testing & debugging |
| Git & GitHub  | Version control and collaboration |

---

## 🧪 Project Structure

```

web-scraper-project/
├── book\_scraper/                ← Scrapy project folder
│   ├── book\_scraper/
│   │   └── spiders/
│   │       └── book\_spider.py
│   └── scrapy.cfg
├── scraper.ipynb               ← BeautifulSoup scraper (Jupyter)
├── scraper.py                  ← BeautifulSoup scraper (script version)
├── convert\_scrapy\_output.py    ← Converts JSON to Excel
├── requirements.txt
├── data.json                   ← Output from BeautifulSoup
├── data.xlsx                   ← Output from BeautifulSoup
├── data\_scrapy.json            ← Output from Scrapy
├── data\_scrapy.xlsx            ← Excel version from Scrapy
└── README.md

````

---

## 🧾 Part 1: BeautifulSoup Scraper

### 📍 Location
- `scraper.ipynb` (Notebook version)
- `scraper.py` (Script version)

### ▶️ How to Run

```bash
# If using script version
python scraper.py
````

### 💾 Output Files

* `data.json`
* `data.xlsx`

---

## 🕷️ Part 2: Scrapy Version (Framework-Based)

### 📍 Location

* `book_scraper/book_scraper/spiders/book_spider.py`

### ▶️ How to Run

From inside the Scrapy project:

```bash
cd book_scraper
scrapy crawl bookspider -o ../data_scrapy.json
```

### 💾 Convert to Excel

```bash
python convert_scrapy_output.py
```

### 📂 Output Files

* `data_scrapy.json`
* `data_scrapy.xlsx`

---

## 💻 How to Set Up

1. **Clone the repository:**

```bash
git clone https://github.com/abdulrehmangulfaraz/web-scraper-project.git
cd web-scraper-project
```

2. **Create a virtual environment:**

```bash
python -m venv venv
.\venv\Scripts\Activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

---

## ✅ Skills Demonstrated

* ✅ HTML parsing & CSS selectors
* ✅ Static scraping with `requests + BeautifulSoup`
* ✅ Structured scraping with `Scrapy`
* ✅ JSON and Excel data handling with `pandas`
* ✅ CLI & Jupyter-based workflows


## 🤝 Author

**Abdulrehman Gulfaraz**
<br>
🔗 Email: [abdulrehmangulfaraz1@gmail.com](abdulrehmangulfaraz1@gmail.com)
<br>
🔗 LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/abdulrehman-gulfaraz)

---

## 📜 License

This project is for educational purposes only. Respect robots.txt of any site you scrape in real-world scenarios.
