import streamlit as st

st.set_page_config(
    page_title="Invisible Enemies: Food Microbiology",
    page_icon="🦠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Global CSS ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Space+Mono:ital,wght@0,400;0,700;1,400&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,500;0,9..40,700;1,9..40,300&display=swap');

/* --- HIDE DEFAULT NAV --- */
[data-testid="stSidebarNav"] { display: none !important; }

:root {
  --bg:         #0a0c0f;
  --surface:    #111418;
  --card:       #161b22;
  --border:     #21262d;
  --accent:     #00ff88;
  --accent2:    #ff3c6e;
  --accent3:    #ffb700;
  --text:       #e6edf3;
  --muted:      #7d8590;
  --glow:       rgba(0,255,136,0.15);
}

html, body, [data-testid="stAppViewContainer"] {
  background: var(--bg) !important;
  color: var(--text) !important;
  font-family: 'DM Sans', sans-serif !important;
}

[data-testid="stSidebar"] {
  background: var(--surface) !important;
  border-right: 1px solid var(--border) !important;
}

[data-testid="stSidebar"] * { color: var(--text) !important; }

h1, h2, h3 { font-family: 'Bebas Neue', sans-serif !important; letter-spacing: 2px !important; }

.stButton > button {
  background: var(--accent) !important;
  color: #000 !important;
  font-family: 'Space Mono', monospace !important;
  font-weight: 700 !important;
  border: none !important;
  border-radius: 4px !important;
  padding: 0.5rem 1.5rem !important;
  transition: all .2s !important;
}
.stButton > button:hover {
  box-shadow: 0 0 20px var(--glow) !important;
  transform: translateY(-2px) !important;
}

.hero-banner {
  background: linear-gradient(135deg, #0a0c0f 0%, #0d1f14 50%, #0a0c0f 100%);
  border: 1px solid var(--border);
  border-top: 3px solid var(--accent);
  border-radius: 8px;
  padding: 3rem 2.5rem;
  margin-bottom: 2rem;
  position: relative;
  overflow: hidden;
}
.hero-banner::before {
  content: '';
  position: absolute; inset: 0;
  background: radial-gradient(ellipse 60% 80% at 80% 50%, rgba(0,255,136,.06), transparent);
}
.hero-title {
  font-family: 'Bebas Neue', sans-serif;
  font-size: clamp(2.5rem, 5vw, 4.5rem);
  letter-spacing: 4px;
  line-height: 1;
  color: var(--text);
  margin: 0 0 .5rem;
}
.hero-sub {
  font-family: 'Space Mono', monospace;
  font-size: .85rem;
  color: var(--accent);
  letter-spacing: 3px;
  text-transform: uppercase;
  margin-bottom: 1.2rem;
}
.hero-desc {
  font-size: 1.1rem;
  color: var(--muted);
  max-width: 600px;
  line-height: 1.7;
}

.metric-card {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 1.4rem 1.2rem;
  text-align: center;
  transition: border-color .3s, box-shadow .3s;
}
.metric-card:hover {
  border-color: var(--accent);
  box-shadow: 0 0 20px var(--glow);
}
.metric-num {
  font-family: 'Bebas Neue', sans-serif;
  font-size: 2.8rem;
  color: var(--accent);
  line-height: 1;
}
.metric-label {
  font-family: 'Space Mono', monospace;
  font-size: .7rem;
  color: var(--muted);
  text-transform: uppercase;
  letter-spacing: 1.5px;
  margin-top: .4rem;
}

.section-header {
  font-family: 'Bebas Neue', sans-serif;
  font-size: 2rem;
  letter-spacing: 3px;
  border-left: 4px solid var(--accent);
  padding-left: 1rem;
  margin: 2rem 0 1.2rem;
}

.info-card {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 1.5rem;
  height: 100%;
  transition: transform .2s, border-color .2s;
}
.info-card:hover { transform: translateY(-3px); border-color: var(--accent); }
.card-icon { font-size: 2.5rem; margin-bottom: .8rem; }
.card-title {
  font-family: 'Bebas Neue', sans-serif;
  font-size: 1.4rem;
  letter-spacing: 2px;
  color: var(--accent);
}
.card-body { color: var(--muted); font-size: .9rem; line-height: 1.6; }

.story-box {
  background: linear-gradient(135deg, var(--card), #1a1008);
  border: 1px solid #3a2a0a;
  border-left: 4px solid var(--accent3);
  border-radius: 8px;
  padding: 1.8rem;
  margin: 1.5rem 0;
}
.story-time {
  font-family: 'Bebas Neue', sans-serif;
  font-size: 1.6rem;
  color: var(--accent3);
  letter-spacing: 2px;
}
.story-text { color: var(--text); line-height: 1.8; font-size: .95rem; }

.danger-badge {
  display: inline-block;
  background: rgba(255,60,110,.15);
  border: 1px solid var(--accent2);
  border-radius: 4px;
  padding: .2rem .7rem;
  font-family: 'Space Mono', monospace;
  font-size: .7rem;
  color: var(--accent2);
  letter-spacing: 1px;
  margin-right: .5rem;
}
.safe-badge {
  display: inline-block;
  background: rgba(0,255,136,.1);
  border: 1px solid var(--accent);
  border-radius: 4px;
  padding: .2rem .7rem;
  font-family: 'Space Mono', monospace;
  font-size: .7rem;
  color: var(--accent);
  letter-spacing: 1px;
  margin-right: .5rem;
}

.progress-bar-wrap {
  background: var(--border);
  border-radius: 4px;
  height: 8px;
  margin: .4rem 0 1rem;
  overflow: hidden;
}
.progress-bar-fill {
  height: 100%;
  border-radius: 4px;
  transition: width .8s ease;
}

.biz-card {
  background: var(--card);
  border: 1px solid var(--border);
  border-top: 3px solid var(--accent3);
  border-radius: 8px;
  padding: 1.5rem;
  text-align: center;
}
.biz-price {
  font-family: 'Bebas Neue', sans-serif;
  font-size: 2.5rem;
  color: var(--accent3);
}

.mono { font-family: 'Space Mono', monospace; }
.accent-text { color: var(--accent); }
.danger-text { color: var(--accent2); }
.warn-text { color: var(--accent3); }

[data-testid="stSelectbox"] > div { background: var(--card) !important; border-color: var(--border) !important; }
[data-testid="stSlider"] > div > div > div { background: var(--accent) !important; }

.nav-pill {
  display: inline-block;
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 20px;
  padding: .3rem .9rem;
  font-family: 'Space Mono', monospace;
  font-size: .72rem;
  color: var(--muted);
  margin: .2rem;
}

/* --- MOBILE NAVIGATION FIX --- */
footer { visibility: hidden; }
#MainMenu { visibility: hidden; }

/* Do NOT use visibility:hidden on header; it kills the mobile sidebar button */
header { 
    background-color: rgba(0,0,0,0) !important; 
    color: var(--text) !important;
}

/* Ensure the sidebar trigger button is visible on mobile */
[data-testid="stHeader"] {
    background: transparent !important;
}
</style>
""", unsafe_allow_html=True)

# ── Sidebar Navigation ───────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='text-align:center; padding: 1rem 0 1.5rem;'>
      <div style='font-family:Bebas Neue,sans-serif; font-size:1.6rem; letter-spacing:3px; color:#00ff88;'>🦠 INVISIBLE</div>
      <div style='font-family:Bebas Neue,sans-serif; font-size:1.6rem; letter-spacing:3px;'>ENEMIES</div>
      <div style='font-family:Space Mono,monospace; font-size:.65rem; color:#7d8590; letter-spacing:2px;'>FOOD MICROBIOLOGY</div>
    </div>
    """, unsafe_allow_html=True)

    page = st.radio(
        "Navigate",
        ["🏠 Home", "🔬 Microbe Gallery", "⏰ Spoilage Stories", "🛡️ Safe Practices", "💼 Business Impact", "🧪 Test Yourself"],
        label_visibility="collapsed"
    )

    st.markdown("---")
    st.markdown("""
    <div style='font-family:Space Mono,monospace; font-size:.7rem; color:#7d8590; text-align:center; padding:1rem 0;'>
      Built for food safety education<br>& business insights
    </div>
    """, unsafe_allow_html=True)

# ── Page Router ──────────────────────────────────────────────────────────────
# Ensure the "pages" folder exists with these files and render() functions
try:
    if page == "🏠 Home":
        from pages import home
        home.render()
    elif page == "🔬 Microbe Gallery":
        from pages import microbes
        microbes.render()
    elif page == "⏰ Spoilage Stories":
        from pages import stories
        stories.render()
    elif page == "🛡️ Safe Practices":
        from pages import safety
        safety.render()
    elif page == "💼 Business Impact":
        from pages import business
        business.render()
    elif page == "🧪 Test Yourself":
        from pages import quiz
        quiz.render()
except ImportError:
    st.error("Page modules not found. Ensure the 'pages' directory contains the required files.")