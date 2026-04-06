import streamlit as st

def render():
    # Hero
    st.markdown("""
    <div class="hero-banner">
      <div class="hero-sub">⚡ A Deep Dive Into What Lurks In Your Food</div>
      <div class="hero-title">INVISIBLE<br>ENEMIES</div>
      <div style="font-family:'Space Mono',monospace; font-size:1rem; color:#00ff88; margin:.5rem 0 1rem;">Food Microbiology — Simplified.</div>
      <div class="hero-desc">
        Every meal you eat is a battlefield. Billions of microorganisms live, breed, and compete 
        in your food — some protect you, some could land you in hospital. 
        <strong style="color:#e6edf3;">This is their story.</strong>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # Stats row
    c1, c2, c3, c4 = st.columns(4)
    stats = [
        ("600M", "People sickened by unsafe food yearly"),
        ("420K", "Annual deaths from foodborne illness"),
        ("$110B", "Global economic cost per year"),
        ("40%", "Food waste from spoilage"),
    ]
    for col, (num, label) in zip([c1,c2,c3,c4], stats):
        with col:
            st.markdown(f"""
            <div class="metric-card">
              <div class="metric-num">{num}</div>
              <div class="metric-label">{label}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<div class="section-header">WHAT YOU\'LL DISCOVER</div>', unsafe_allow_html=True)

    cards = [
        ("🦠", "Microbe Gallery", "Meet the cast — heroes like Lactobacillus and villains like Salmonella. Interactive profiles of 12+ microorganisms found in everyday food."),
        ("⏰", "Spoilage Stories", "Follow milk, bread, and meat through real-time spoilage timelines. Storytelling meets science in visceral, hour-by-hour narratives."),
        ("🛡️", "Safe Practices", "Temperature danger zones, cross-contamination maps, HACCP basics — everything a home cook or food pro needs to know."),
        ("💼", "Business Impact", "From food testing kits to safety certifications — discover the $billion opportunity hiding in microbiology compliance."),
        ("🧪", "Quiz Yourself", "10 questions to test your food safety IQ. Can you score 100%? Your kitchen might depend on it."),
        ("📊", "Risk Calculator", "Input your food handling scenario and get a real-time microbial risk score with actionable advice."),
    ]

    col_pairs = [st.columns(3) for _ in range(2)]
    flat_cols = [c for row in col_pairs for c in row]
    for col, (icon, title, body) in zip(flat_cols, cards):
        with col:
            st.markdown(f"""
            <div class="info-card">
              <div class="card-icon">{icon}</div>
              <div class="card-title">{title}</div>
              <div class="card-body" style="margin-top:.6rem;">{body}</div>
            </div>
            """, unsafe_allow_html=True)

    # Teaser story
    st.markdown('<div class="section-header">TODAY\'S STORY</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="story-box">
      <div class="story-time">🥛 THE MILK INCIDENT — A 6-HOUR HORROR STORY</div>
      <div class="story-text" style="margin-top:.8rem;">
        It started innocently. A glass of cold, fresh milk left on the kitchen counter at 8 AM. 
        By 10 AM, invisible guests had arrived — <em>Lactococcus lactis</em>, 
        <em>Pseudomonas</em>, and their friends, doubling their numbers every 20 minutes. 
        By 2 PM, what looked normal to the naked eye had turned into a microbial metropolis of 
        over <strong style="color:#ff3c6e;">100 million bacteria per milliliter</strong>. 
        The milk smelled fine. It looked fine. It wasn't.
      </div>
      <div style="margin-top:1rem;">
        <span class="nav-pill">→ Full story in Spoilage Stories</span>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # Quick risk callout
    st.markdown('<div class="section-header">THE DANGER ZONE</div>', unsafe_allow_html=True)
    c1, c2 = st.columns([1, 1])
    with c1:
        st.markdown("""
        <div style="background:linear-gradient(135deg,#1a0810,#0a0c0f); border:1px solid #3a1020; 
                    border-left:4px solid #ff3c6e; border-radius:8px; padding:1.5rem;">
          <div style="font-family:'Bebas Neue',sans-serif; font-size:1.8rem; color:#ff3c6e; letter-spacing:2px;">
            🌡️ 40°F – 140°F (4°C – 60°C)
          </div>
          <div style="font-family:'Space Mono',monospace; font-size:.75rem; color:#7d8590; margin-top:.5rem; letter-spacing:1px;">
            THE TEMPERATURE DANGER ZONE
          </div>
          <div style="color:#e6edf3; margin-top:1rem; line-height:1.7;">
            Bacteria multiply most rapidly in this range. 
            <strong>Never leave perishable food in this zone for more than 2 hours.</strong>
            On a hot day above 90°F? That window shrinks to <strong style="color:#ff3c6e;">1 hour</strong>.
          </div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div style="background:var(--card); border:1px solid var(--border); border-radius:8px; padding:1.5rem;">
          <div style="font-family:'Bebas Neue',sans-serif; font-size:1.3rem; color:#00ff88; letter-spacing:2px; margin-bottom:1rem;">
            BACTERIAL GROWTH RATE
          </div>
        """, unsafe_allow_html=True)

        foods = [
            ("Raw Chicken @ 25°C", 95, "#ff3c6e"),
            ("Cooked Rice @ 20°C", 80, "#ff3c6e"),
            ("Soft Cheese @ 15°C", 65, "#ffb700"),
            ("Raw Milk @ 10°C", 45, "#ffb700"),
            ("Fresh Produce @ 4°C", 20, "#00ff88"),
        ]
        for food, pct, color in foods:
            st.markdown(f"""
            <div style="margin-bottom:.8rem;">
              <div style="font-size:.85rem; color:#e6edf3; margin-bottom:.3rem;">{food}</div>
              <div class="progress-bar-wrap">
                <div class="progress-bar-fill" style="width:{pct}%; background:{color};"></div>
              </div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
