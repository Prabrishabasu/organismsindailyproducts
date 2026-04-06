import streamlit as st
import plotly.graph_objects as go

def render():
    st.markdown("""
    <div class="hero-banner" style="padding:2rem 2.5rem;">
      <div class="hero-sub">🛡️ Evidence-Based Food Safety</div>
      <div class="hero-title" style="font-size:3rem;">SAFE PRACTICES</div>
      <div class="hero-desc">Science-backed guidelines to keep your kitchen, restaurant, or food operation safe.</div>
    </div>
    """, unsafe_allow_html=True)

    # The 4 core principles
    st.markdown('<div class="section-header">THE 4 PILLARS OF FOOD SAFETY</div>', unsafe_allow_html=True)

    pillars = [
        ("🧼", "CLEAN", "#00ff88", "Wash hands for 20+ seconds. Sanitize surfaces. Use separate cutting boards for raw meat vs produce.", [
            "Wash hands before and after handling raw meat",
            "Clean AND sanitize cutting boards (clean removes dirt; sanitize kills bacteria)",
            "Wash produce under running water — even if you'll peel it",
            "Change dish towels daily — they're bacterial hotspots",
        ]),
        ("🔀", "SEPARATE", "#00ccff", "Prevent cross-contamination between raw and ready-to-eat foods at every step.", [
            "Use color-coded cutting boards (red=meat, green=veg, yellow=poultry)",
            "Store raw meat on the bottom shelf of the fridge",
            "Never reuse marinade that touched raw meat",
            "Bag raw meats separately in the grocery store",
        ]),
        ("🌡️", "COOK", "#ffb700", "Heat to safe internal temperatures. Use a food thermometer — color is not reliable.", [
            "Poultry: 165°F (74°C) minimum",
            "Ground beef/pork: 160°F (71°C)",
            "Whole cuts beef/pork/lamb: 145°F (63°C) + 3 min rest",
            "Fish: 145°F (63°C) or flesh is opaque/flakes easily",
        ]),
        ("❄️", "CHILL", "#ff3c6e", "Refrigerate within 2 hours. Keep fridge at 40°F (4°C) or below. Never thaw on the counter.", [
            "Fridge temp: ≤40°F (4°C) | Freezer: 0°F (-18°C)",
            "Thaw in the fridge, cold water, or microwave — NEVER countertop",
            "Divide large leftovers into small containers for faster chilling",
            "Never over-pack the fridge — air needs to circulate",
        ]),
    ]

    cols = st.columns(2)
    for i, (icon, title, color, summary, points) in enumerate(pillars):
        with cols[i % 2]:
            points_html = "".join([f"<li style='margin-bottom:.4rem;'>{p}</li>" for p in points])
            st.markdown(f"""
            <div style="background:var(--card); border:1px solid {color}33; border-top:3px solid {color};
                        border-radius:8px; padding:1.5rem; margin-bottom:1rem; min-height:280px;">
              <div style="font-size:2rem; margin-bottom:.5rem;">{icon}</div>
              <div style="font-family:'Bebas Neue',sans-serif; font-size:1.8rem; letter-spacing:3px; color:{color};">
                {title}
              </div>
              <div style="color:#e6edf3; font-size:.88rem; margin:.6rem 0 1rem; line-height:1.6;">{summary}</div>
              <ul style="color:#7d8590; font-size:.84rem; line-height:1.7; padding-left:1.2rem;">
                {points_html}
              </ul>
            </div>
            """, unsafe_allow_html=True)

    # Temperature guide
    st.markdown('<div class="section-header">TEMPERATURE REFERENCE GUIDE</div>', unsafe_allow_html=True)

    fig = go.Figure()

    # Temperature zones
    zones = [
        (0, 4, "rgba(0,200,255,0.15)", "❄️ Safe Refrigeration"),
        (4, 60, "rgba(255,60,110,0.15)", "⚠️ DANGER ZONE (Bacteria multiply rapidly)"),
        (60, 74, "rgba(255,183,0,0.15)", "🔥 Killing Zone (Bacteria die, slow)"),
        (74, 100, "rgba(0,255,136,0.15)", "✅ Safe Cooking Temperatures"),
    ]

    for y0, y1, color, label in zones:
        fig.add_hrect(y0=y0, y1=y1, fillcolor=color, line_width=0, annotation_text=label,
                      annotation_position="right", annotation_font_color="#e6edf3",
                      annotation_font_size=11)

    # Key temp points
    temps = [
        (4, "Fridge max (4°C)", "#00ccff"),
        (20, "Room temp (20°C)", "#ff8c00"),
        (60, "Minimum hot hold (60°C)", "#ffb700"),
        (63, "Safe whole cuts (63°C)", "#00ff88"),
        (71, "Safe ground meat (71°C)", "#00ff88"),
        (74, "Safe poultry (74°C)", "#00ff88"),
    ]

    for y, label, color in temps:
        fig.add_hline(y=y, line_color=color, line_dash="dot", line_width=1.5,
                      annotation_text=f" {label}", annotation_position="left",
                      annotation_font_color=color, annotation_font_size=10)

    fig.update_layout(
        paper_bgcolor="#161b22",
        plot_bgcolor="#0a0c0f",
        font=dict(color="#e6edf3", family="Space Mono"),
        xaxis=dict(visible=False),
        yaxis=dict(
            title="Temperature (°C)",
            gridcolor="#21262d",
            color="#7d8590",
            range=[-5, 110],
        ),
        margin=dict(l=60, r=200, t=20, b=20),
        height=400,
        showlegend=False,
    )
    st.plotly_chart(fig, use_container_width=True)

    # HACCP overview
    st.markdown('<div class="section-header">HACCP — THE GOLD STANDARD</div>', unsafe_allow_html=True)

    st.markdown("""
    <div style="background:var(--card); border:1px solid var(--border); border-radius:8px; padding:1.5rem; margin-bottom:1.5rem;">
      <div style="color:#7d8590; font-size:.9rem; line-height:1.7; margin-bottom:1rem;">
        <strong style="color:#e6edf3;">Hazard Analysis Critical Control Points (HACCP)</strong> is the systematic 
        approach to food safety used by all major food businesses worldwide. Here are its 7 principles:
      </div>
    </div>
    """, unsafe_allow_html=True)

    haccp = [
        ("1", "Conduct Hazard Analysis", "Identify all potential biological, chemical, and physical hazards in your process."),
        ("2", "Identify Critical Control Points (CCPs)", "Find the steps where controls can be applied to prevent, eliminate, or reduce hazards."),
        ("3", "Establish Critical Limits", "Set measurable limits (e.g., min cooking temp = 74°C) for each CCP."),
        ("4", "Establish Monitoring Procedures", "Define how and how often you'll monitor each CCP."),
        ("5", "Establish Corrective Actions", "Plan what to do if a CCP falls outside its critical limit."),
        ("6", "Establish Verification Procedures", "Confirm the HACCP system is working through testing, audits, and review."),
        ("7", "Establish Record-Keeping", "Document everything. Records prove compliance and enable traceability."),
    ]

    for num, title, desc in haccp:
        st.markdown(f"""
        <div style="display:flex; gap:1rem; margin-bottom:.8rem;">
          <div style="min-width:40px; height:40px; background:rgba(0,255,136,.15); border:1px solid #00ff88;
                      border-radius:50%; display:flex; align-items:center; justify-content:center;
                      font-family:Bebas Neue,sans-serif; font-size:1.2rem; color:#00ff88; flex-shrink:0;">
            {num}
          </div>
          <div style="background:var(--card); border:1px solid var(--border); border-radius:8px; 
                      padding:.8rem 1.2rem; flex:1;">
            <div style="font-family:'Space Mono',monospace; font-size:.8rem; color:#00ff88; margin-bottom:.3rem;">
              {title}
            </div>
            <div style="color:#7d8590; font-size:.84rem; line-height:1.6;">{desc}</div>
          </div>
        </div>
        """, unsafe_allow_html=True)

    # Quick risk calculator
    st.markdown('<div class="section-header">🧮 QUICK RISK CALCULATOR</div>', unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        food_type = st.selectbox("Food type", ["Raw poultry", "Raw beef/pork", "Cooked rice/pasta", "Dairy", "Fresh produce", "Deli meats"])
        temp = st.slider("Storage temperature (°C)", -20, 50, 20)
        hours = st.slider("Hours left out", 0, 12, 2)

    with c2:
        # Simple risk scoring
        base_risk = {"Raw poultry": 90, "Raw beef/pork": 75, "Cooked rice/pasta": 65, 
                     "Dairy": 60, "Fresh produce": 35, "Deli meats": 70}
        risk = base_risk[food_type]

        if temp < 4:
            risk = max(5, risk - 60)
        elif temp < 8:
            risk = max(10, risk - 40)
        elif temp < 15:
            risk = max(20, risk - 20)
        elif temp < 20:
            pass
        else:
            risk = min(100, risk + 10 * (temp - 20) // 5)

        risk = min(100, risk + hours * 5)

        if risk < 30:
            verdict = "✅ LOW RISK"
            v_color = "#00ff88"
            advice = "Food appears safe. Continue monitoring temperature."
        elif risk < 60:
            verdict = "⚠️ MODERATE RISK"
            v_color = "#ffb700"
            advice = "Use or cook soon. Do not leave out further."
        elif risk < 80:
            verdict = "🚨 HIGH RISK"
            v_color = "#ff8c00"
            advice = "Significant risk. Cook thoroughly if possible, or discard."
        else:
            verdict = "☠️ CRITICAL RISK"
            v_color = "#ff3c6e"
            advice = "Discard immediately. Do not consume."

        st.markdown(f"""
        <div style="background:var(--card); border:1px solid {v_color}44; border-top:3px solid {v_color};
                    border-radius:8px; padding:1.5rem; text-align:center; margin-top:.5rem;">
          <div style="font-family:'Bebas Neue',sans-serif; font-size:2.5rem; color:{v_color}; letter-spacing:2px;">
            {risk}%
          </div>
          <div style="font-family:Space Mono,monospace; font-size:.8rem; color:{v_color}; margin:.5rem 0; letter-spacing:1px;">
            {verdict}
          </div>
          <div style="color:#e6edf3; font-size:.88rem; line-height:1.6; margin-top:.8rem;">{advice}</div>
        </div>
        """, unsafe_allow_html=True)
