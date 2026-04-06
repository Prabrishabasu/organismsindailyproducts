import streamlit as st
import plotly.graph_objects as go

STORIES = {
    "🥛 Milk Left Outside (6 Hours)": {
        "subtitle": "A Summer Morning Disaster",
        "intro": """
It's 8:00 AM on a warm summer day. A glass of fresh, cold milk — just taken from the refrigerator — 
is left on the kitchen counter while breakfast is prepared. The ambient temperature is 28°C (82°F). 
To the naked eye, nothing changes for hours. But inside? It's a microbial Manhattan.
        """,
        "timeline": [
            ("0 min", "Hour 0", "The milk is safe. Temperature drops from 4°C to room temp. Resident bacteria: ~10,000 per mL — well within safe limits. Lactococcus and Pseudomonas are waking up.", "#00ff88"),
            ("1 hr", "Hour 1", "Temperature reaches 20°C. Bacteria begin doubling every 30-40 minutes. Count climbs to ~80,000/mL. Still visually perfect. Still smells fine. Still tastes normal.", "#7dff88"),
            ("2 hrs", "Hour 2", "The 2-hour rule is passed. Bacterial count: ~600,000/mL. Lactic acid production begins. Slight sourness if you know to look. Most people won't notice.", "#ffb700"),
            ("3 hrs", "Hour 3", "Count hits 5 million/mL. Pseudomonas secretes proteases breaking down casein proteins. The milk's texture begins shifting. That 'off' smell is early — most miss it.", "#ff8c00"),
            ("4 hrs", "Hour 4", "15 million bacteria per mL. Lactococcus is producing so much lactic acid that the pH drops to 6.2. The milk is now souring perceptibly. Curdling begins.", "#ff5500"),
            ("5 hrs", "Hour 5", "50 million/mL. Clear souring, possible clumping. If Staphylococcus aureus is present (transferred from skin during handling), its toxin production is now underway. Toxin is heat-stable.", "#ff3c6e"),
            ("6 hrs", "Hour 6", "100+ million bacteria per mL. The milk is visually 'off'. It smells sour. But here's the terrifying part: if toxins were produced, BOILING won't destroy them. The damage is done.", "#ff0040"),
        ],
        "lesson": "The 2-hour rule isn't conservative — it's the biological minimum. After 2 hours in the danger zone, milk is a gamble. After 4 hours, throw it out.",
        "bacteria": ["Lactococcus lactis", "Pseudomonas fluorescens", "Staphylococcus aureus", "Streptococcus thermophilus"],
        "growth_data": {
            "hours": [0, 1, 2, 3, 4, 5, 6],
            "count": [10000, 80000, 600000, 5000000, 15000000, 50000000, 100000000],
        }
    },

    "🍞 Bread Left in a Humid Kitchen (5 Days)": {
        "subtitle": "The Slow Creep of Mold",
        "intro": """
A freshly baked artisan loaf. No preservatives. Stored in a plastic bag on the counter in a warm, 
humid kitchen (25°C, 70% humidity). What happens over 5 days is a masterclass in fungal biology.
        """,
        "timeline": [
            ("Day 0", "Baked & Sealed", "The bread is sterile from baking, but within minutes of cooling, mold spores from the air land on the surface. Rhizopus stolonifer and Aspergillus niger spores settle in.", "#00ff88"),
            ("Day 1", "Invisible Germination", "Spores begin germinating in the warm moisture. Hyphae (fungal threads) penetrate the bread surface invisibly. No visible change. Zero warning signs.", "#7dff88"),
            ("Day 2", "White Fuzz Appears", "Small white fuzzy patches appear, often on the cut end. This is Rhizopus stolonifer — 'black bread mold' — beginning its sporangiophore development.", "#ffb700"),
            ("Day 3", "Green Patches", "Aspergillus niger creates black-green colonies. Penicillium expansum may add blue-green patches. The bread smells musty. Mycotoxin production begins.", "#ff8c00"),
            ("Day 4", "Full Colonization", "Mold mycelium has penetrated deep into the loaf — even areas that look clean. The mold visible on the surface is the tip of the iceberg.", "#ff3c6e"),
            ("Day 5", "Total Loss", "The entire loaf is compromised. Cutting off the moldy part is NOT safe — mycotoxins have diffused throughout. The whole loaf must be discarded.", "#ff0040"),
        ],
        "lesson": "Never cut off mold from bread and eat the rest. Mold penetrates deep into porous foods. The mycotoxins it produces can survive cooking temperatures.",
        "bacteria": ["Rhizopus stolonifer", "Aspergillus niger", "Penicillium expansum", "Cladosporium herbarum"],
        "growth_data": {
            "hours": [0, 24, 48, 72, 96, 120],
            "count": [100, 10000, 500000, 2000000, 8000000, 20000000],
        }
    },

    "🍗 Raw Chicken at Room Temperature (4 Hours)": {
        "subtitle": "A Salmonella Time Bomb",
        "intro": """
A raw chicken breast, taken from the fridge at noon to 'thaw on the counter'. 
Room temperature: 22°C. By the time dinner prep begins at 4 PM, a dangerous transformation has occurred 
that cannot be undone by washing — only by thorough cooking.
        """,
        "timeline": [
            ("0 min", "Defrost Begins", "The chicken's surface temperature rises from 4°C. Pre-existing Salmonella: ~1,000 cells/cm² on the surface — below infectious dose. Campylobacter also present.", "#00ff88"),
            ("30 min", "Surface Warms", "Surface reaches 15°C. Bacterial lag phase ends. Salmonella and Campylobacter begin exponential growth. Cross-contamination risk begins if surface touched.", "#7dff88"),
            ("1 hr", "Danger Zone Entered", "Surface at 20°C. Doubling time: ~25 minutes. 10,000+ Salmonella per cm². The juice dripping onto the counter is now highly contaminated.", "#ffb700"),
            ("2 hrs", "Critical Mass", "160,000 Salmonella per cm². Infectious dose (100 cells) is far exceeded. Any cross-contamination to salad, cutting boards, or unwashed hands is dangerous.", "#ff8c00"),
            ("3 hrs", "Toxin Buildup", "1.2 million/cm². Campylobacter reaches dangerous levels — it needs only 500 cells to cause severe gastroenteritis lasting up to 10 days.", "#ff5500"),
            ("4 hrs", "CRITICAL", "4+ million Salmonella per cm². Even if cooking kills ALL bacteria, residual cross-contamination on surfaces is a serious threat to other foods and people.", "#ff0040"),
        ],
        "lesson": "NEVER thaw chicken at room temperature. Use the refrigerator (overnight), cold running water (sealed bag), or microwave (cook immediately after). Surface bacteria reach dangerous levels within 1 hour.",
        "bacteria": ["Salmonella enterica", "Campylobacter jejuni", "Staphylococcus aureus", "Clostridium perfringens"],
        "growth_data": {
            "hours": [0, 0.5, 1, 2, 3, 4],
            "count": [1000, 4000, 10000, 160000, 1200000, 4000000],
        }
    }
}


def render():
    st.markdown("""
    <div class="hero-banner" style="padding:2rem 2.5rem;">
      <div class="hero-sub">⏰ Hour-by-Hour Narratives</div>
      <div class="hero-title" style="font-size:3rem;">SPOILAGE STORIES</div>
      <div class="hero-desc">Follow real food through real microbial timelines. This is what science looks like when it gets personal.</div>
    </div>
    """, unsafe_allow_html=True)

    story_choice = st.selectbox("Choose a story", list(STORIES.keys()), label_visibility="collapsed")
    story = STORIES[story_choice]

    # Intro
    st.markdown(f"""
    <div style="background:var(--card); border:1px solid var(--border); border-radius:8px; padding:1.8rem; margin:1rem 0;">
      <div style="font-family:'Bebas Neue',sans-serif; font-size:1.8rem; letter-spacing:2px; color:#ffb700;">
        {story_choice}
      </div>
      <div style="font-family:Space Mono,monospace; font-size:.75rem; color:#7d8590; margin:.3rem 0 1rem; letter-spacing:1px;">
        {story['subtitle']}
      </div>
      <div style="color:#e6edf3; line-height:1.8; font-size:.95rem;">{story['intro'].strip()}</div>
    </div>
    """, unsafe_allow_html=True)

    # Timeline
    st.markdown('<div class="section-header">THE TIMELINE</div>', unsafe_allow_html=True)

    for ts, title, body, color in story["timeline"]:
        st.markdown(f"""
        <div style="display:flex; gap:1rem; margin-bottom:1rem;">
          <div style="min-width:80px; text-align:center;">
            <div style="background:{color}22; border:1px solid {color}; border-radius:6px; padding:.5rem; 
                        font-family:Bebas Neue,sans-serif; font-size:1.1rem; color:{color}; letter-spacing:1px;">
              {ts}
            </div>
          </div>
          <div style="background:var(--card); border:1px solid var(--border); border-left:3px solid {color};
                      border-radius:0 8px 8px 0; padding:1rem 1.2rem; flex:1;">
            <div style="font-family:'Bebas Neue',sans-serif; font-size:1.2rem; letter-spacing:1.5px; 
                        color:{color}; margin-bottom:.5rem;">{title}</div>
            <div style="color:#e6edf3; font-size:.88rem; line-height:1.65;">{body.strip()}</div>
          </div>
        </div>
        """, unsafe_allow_html=True)

    # Growth chart
    st.markdown('<div class="section-header">BACTERIAL GROWTH CHART</div>', unsafe_allow_html=True)

    gd = story["growth_data"]
    x_label = "Hours" if max(gd["hours"]) <= 24 else "Hours"

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=gd["hours"],
        y=gd["count"],
        mode="lines+markers",
        line=dict(color="#ff3c6e", width=3),
        marker=dict(size=10, color="#ff3c6e", symbol="circle"),
        fill="tozeroy",
        fillcolor="rgba(255,60,110,0.08)",
        name="Bacterial Count"
    ))

    # Danger zone annotation
    fig.add_hline(y=1000000, line_dash="dash", line_color="#ffb700", 
                  annotation_text="⚠️ DANGER THRESHOLD (1M/mL)", 
                  annotation_position="bottom right",
                  annotation_font_color="#ffb700")

    fig.update_layout(
        paper_bgcolor="#161b22",
        plot_bgcolor="#0a0c0f",
        font=dict(color="#e6edf3", family="Space Mono"),
        xaxis=dict(
            title=x_label,
            gridcolor="#21262d",
            showgrid=True,
            color="#7d8590",
        ),
        yaxis=dict(
            title="Bacteria per mL/cm²",
            type="log",
            gridcolor="#21262d",
            showgrid=True,
            color="#7d8590",
        ),
        margin=dict(l=60, r=20, t=20, b=60),
        height=350,
    )
    st.plotly_chart(fig, use_container_width=True)

    # Bacteria involved
    st.markdown('<div class="section-header">MICROBES INVOLVED</div>', unsafe_allow_html=True)
    cols = st.columns(len(story["bacteria"]))
    for col, b in zip(cols, story["bacteria"]):
        with col:
            st.markdown(f"""
            <div style="background:rgba(255,60,110,.07); border:1px solid #3d0d1a; border-radius:6px; 
                        padding:.8rem; text-align:center; font-family:Space Mono,monospace; 
                        font-size:.75rem; color:#ff3c6e;">
              🦠 {b}
            </div>
            """, unsafe_allow_html=True)

    # Key lesson
    st.markdown(f"""
    <div style="background:linear-gradient(135deg,#0d3d22,#0a0c0f); border:1px solid #0d3d22; 
                border-left:4px solid #00ff88; border-radius:8px; padding:1.5rem; margin-top:1.5rem;">
      <div style="font-family:'Bebas Neue',sans-serif; font-size:1.3rem; color:#00ff88; 
                  letter-spacing:2px; margin-bottom:.8rem;">✓ KEY LESSON</div>
      <div style="color:#e6edf3; line-height:1.8; font-size:.95rem;">{story['lesson']}</div>
    </div>
    """, unsafe_allow_html=True)
