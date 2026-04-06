# 🦠 Invisible Enemies: Food Microbiology

A stunning, full-featured Streamlit web app exploring the microbiology of everyday food — blending science education, storytelling, business insights, and interactive learning.

![Food Microbiology App](https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B?logo=streamlit)
![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🌟 Features

### 📚 Educational
- **Microbe Gallery** — 12 interactive species profiles (beneficial, harmful, spoilage organisms) with temperature ranges, pH optima, risk levels, and fun facts
- **Safe Practices** — The 4 pillars of food safety (Clean, Separate, Cook, Chill), temperature reference charts, HACCP overview, and a live risk calculator

### 📖 Storytelling
- **Spoilage Stories** — Hour-by-hour narratives following food through microbial spoilage:
  - 🥛 *Milk left outside for 6 hours* — A bacterial metropolis unfolds
  - 🍞 *Bread in a humid kitchen for 5 days* — Mold's slow takeover
  - 🍗 *Raw chicken thawed on the counter* — A Salmonella time bomb
- Each story includes: timeline visualization, interactive bacterial growth charts (Plotly), and key lessons

### 💼 Business
- **Business Impact** — Market analysis, two complete business model blueprints:
  - 🧪 **MicroCheck Home Testing Kits** — Subscription model with app integration
  - 🏅 **SafeSeal Certification Service** — B2B food safety certification for restaurants
- Market growth projection charts (2022–2030)
- ROI analysis and restaurant benefit breakdown

### 🧪 Interactive
- **Test Yourself Quiz** — 10-question food safety IQ test with instant feedback, explanations, and grading
- **Risk Calculator** — Input your food scenario and get a real-time microbial risk score

---

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/food-microbiology-app.git
cd food-microbiology-app

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

The app will open at `http://localhost:8501`

---

## 📁 Project Structure

```
food-microbiology-app/
│
├── app.py                    # Main entry point, global CSS, navigation
├── requirements.txt          # Python dependencies
├── README.md
│
└── pages/
    ├── __init__.py
    ├── home.py               # Landing page with stats, danger zone info
    ├── microbes.py           # Interactive microbe gallery (12 species)
    ├── stories.py            # Spoilage storytelling with Plotly charts
    ├── safety.py             # Safe practices, HACCP, risk calculator
    ├── business.py           # Business models, market analysis
    └── quiz.py               # Interactive 10-question quiz
```

---

## 🎨 Design Philosophy

The app uses a **dark editorial aesthetic** with:
- **Bebas Neue** for dramatic headers
- **Space Mono** for data labels and monospace accents  
- **DM Sans** for body text
- A dark base (`#0a0c0f`) with neon green (`#00ff88`), red (`#ff3c6e`), and amber (`#ffb700`) accents
- Animated hover effects, progress bars, and Plotly dark-mode charts

---

## 📊 Data Sources

- WHO Global estimates of the burden of foodborne diseases (2015)
- CDC Foodborne Diseases Active Surveillance Network
- USDA Food Safety and Inspection Service guidelines
- FDA Food Safety Modernization Act (FSMA) documentation
- Grand View Research: Food Safety Testing Market Report
- HACCP Alliance educational materials

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Streamlit | Web framework & UI components |
| Plotly | Interactive charts (growth curves, market data) |
| Pandas | Data tables |
| Python | Core logic |

---

## 📖 Learning Outcomes

After exploring this app, users will understand:
1. The difference between beneficial, spoilage, and pathogenic microorganisms
2. Why the 2-hour rule and temperature danger zone matter
3. How bacterial growth is exponential — not linear
4. HACCP principles and their business application
5. The economic opportunity in food safety technology

---

## 🤝 Contributing

Pull requests welcome. For major changes, open an issue first.

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/new-story`)
3. Commit your changes (`git commit -m 'Add: raw fish spoilage story'`)
4. Push to the branch (`git push origin feature/new-story`)
5. Open a Pull Request

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

## 🙋 About

Built as an educational platform combining food science, public health, and business strategy. Designed for students, food professionals, restaurant owners, and curious home cooks.

> *"Every meal you eat is a battlefield. Now you know the players."*
