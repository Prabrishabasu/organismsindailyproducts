import streamlit as st
import plotly.graph_objects as go

def render():
    st.markdown("""
    <div class="hero-banner" style="padding:2rem 2.5rem;">
      <div class="hero-sub">💼 Market Opportunity & Revenue Models</div>
      <div class="hero-title" style="font-size:3rem;">BUSINESS IMPACT</div>
      <div class="hero-desc">Food safety isn't just a health issue — it's a multi-billion dollar business opportunity with growing demand.</div>
    </div>
    """, unsafe_allow_html=True)

    # Market metrics
    c1, c2, c3, c4 = st.columns(4)
    for col, (num, label) in zip([c1,c2,c3,c4], [
        ("$25B", "Global food testing market by 2030"),
        ("8.3%", "Annual market growth (CAGR)"),
        ("$110B", "Economic cost of foodborne illness"),
        ("3×", "ROI on food safety investment"),
    ]):
        with col:
            st.markdown(f"""
            <div class="metric-card">
              <div class="metric-num" style="color:#ffb700;">{num}</div>
              <div class="metric-label">{label}</div>
            </div>
            """, unsafe_allow_html=True)

    # Business Ideas Section
    st.markdown('<div class="section-header">TWO FLAGSHIP BUSINESS MODELS</div>', unsafe_allow_html=True)

    biz_tab1, biz_tab2 = st.tabs(["🧪 Home Food Testing Kits", "🏅 Safety Certification Service"])

    with biz_tab1:
        c1, c2 = st.columns([3, 2])
        with c1:
            st.markdown("""
            <div style="background:var(--card); border:1px solid var(--border); border-radius:8px; padding:1.5rem;">
              <div style="font-family:'Bebas Neue',sans-serif; font-size:2rem; letter-spacing:2px; color:#00ff88; margin-bottom:1rem;">
                🧪 MICROCHECK HOME KIT
              </div>
              <div style="color:#e6edf3; font-size:.95rem; line-height:1.8; margin-bottom:1.2rem;">
                A subscription-based home food testing kit that lets consumers test their food, 
                water, and kitchen surfaces for dangerous pathogens in under 30 minutes.
                No lab required. Results via smartphone app.
              </div>
              <div style="font-family:'Bebas Neue',sans-serif; font-size:1.2rem; color:#ffb700; letter-spacing:2px; margin-bottom:.8rem;">
                WHAT'S INCLUDED
              </div>
            """, unsafe_allow_html=True)
            
            features = [
                ("🥩", "Salmonella/E. coli strips for raw meat"),
                ("🥛", "Coliform test for dairy & water"),
                ("🧽", "ATP surface swabs for kitchen hygiene"),
                ("📱", "App-connected results & alerts"),
                ("📊", "Monthly household food safety report"),
            ]
            for icon, feat in features:
                st.markdown(f"""
                <div style="display:flex; align-items:center; gap:.8rem; padding:.6rem 0; 
                            border-bottom:1px solid var(--border);">
                  <div style="font-size:1.2rem;">{icon}</div>
                  <div style="color:#e6edf3; font-size:.88rem;">{feat}</div>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)

        with c2:
            st.markdown("""
            <div style="background:var(--card); border:1px solid var(--border); border-top:3px solid #ffb700;
                        border-radius:8px; padding:1.5rem; margin-bottom:1rem;">
              <div style="font-family:'Bebas Neue',sans-serif; font-size:1.2rem; color:#ffb700; letter-spacing:2px; margin-bottom:1rem;">
                PRICING TIERS
              </div>
            """, unsafe_allow_html=True)
            
            plans = [
                ("STARTER", "$12/mo", "10 tests/month, basic app"),
                ("FAMILY", "$24/mo", "30 tests, full app, reports"),
                ("PRO", "$49/mo", "Unlimited, lab backup, priority"),
            ]
            for name, price, desc in plans:
                st.markdown(f"""
                <div style="background:#111418; border:1px solid var(--border); border-radius:6px; 
                            padding:1rem; margin-bottom:.8rem; text-align:center;">
                  <div style="font-family:Space Mono,monospace; font-size:.7rem; color:#7d8590; letter-spacing:1px;">{name}</div>
                  <div style="font-family:'Bebas Neue',sans-serif; font-size:2rem; color:#ffb700;">{price}</div>
                  <div style="font-size:.8rem; color:#7d8590;">{desc}</div>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)

            st.markdown("""
            <div style="background:rgba(0,255,136,.07); border:1px solid #0d3d22; border-radius:8px; padding:1.2rem;">
              <div style="font-family:Space Mono,monospace; font-size:.72rem; color:#00ff88; letter-spacing:1px; margin-bottom:.5rem;">
                TARGET MARKET
              </div>
              <div style="color:#7d8590; font-size:.82rem; line-height:1.7;">
                • Families with young children<br>
                • Elderly/immunocompromised households<br>
                • Home chefs & food enthusiasts<br>
                • Rural areas with water quality concerns
              </div>
            </div>
            """, unsafe_allow_html=True)

    with biz_tab2:
        c1, c2 = st.columns([3, 2])
        with c1:
            st.markdown("""
            <div style="background:var(--card); border:1px solid var(--border); border-radius:8px; padding:1.5rem;">
              <div style="font-family:'Bebas Neue',sans-serif; font-size:2rem; letter-spacing:2px; color:#00ccff; margin-bottom:1rem;">
                🏅 SAFESEAL CERTIFICATION
              </div>
              <div style="color:#e6edf3; font-size:.95rem; line-height:1.8; margin-bottom:1.2rem;">
                A tiered food safety certification service for restaurants, cloud kitchens, 
                food trucks, and food delivery platforms. Visible certification drives customer 
                trust and reduces liability.
              </div>
              <div style="font-family:'Bebas Neue',sans-serif; font-size:1.2rem; color:#ffb700; letter-spacing:2px; margin-bottom:.8rem;">
                CERTIFICATION PROCESS
              </div>
            """, unsafe_allow_html=True)
            
            steps = [
                ("Step 1", "Application & Baseline Audit", "Review of current food safety practices, equipment, and staff training."),
                ("Step 2", "Microbial Testing", "Swab testing of surfaces, equipment, and food samples in certified lab."),
                ("Step 3", "HACCP Plan Development", "Custom food safety plan creation with critical control points."),
                ("Step 4", "Staff Training", "Food safety training for all kitchen staff. Digital certification."),
                ("Step 5", "Certification Award", "SafeSeal badge, digital certificate, and listing in public directory."),
                ("Step 6", "Annual Renewal", "Quarterly check-ins + annual full audit to maintain certification."),
            ]
            for step, title, desc in steps:
                st.markdown(f"""
                <div style="display:flex; gap:.8rem; margin-bottom:.8rem;">
                  <div style="font-family:Space Mono,monospace; font-size:.65rem; color:#00ccff; min-width:55px; 
                              padding:.3rem; text-align:center; border:1px solid #00ccff33; border-radius:4px; height:fit-content;">
                    {step}
                  </div>
                  <div>
                    <div style="font-family:Space Mono,monospace; font-size:.78rem; color:#e6edf3; margin-bottom:.2rem;">{title}</div>
                    <div style="color:#7d8590; font-size:.82rem; line-height:1.6;">{desc}</div>
                  </div>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)

        with c2:
            st.markdown("""
            <div style="background:var(--card); border:1px solid var(--border); border-top:3px solid #00ccff;
                        border-radius:8px; padding:1.5rem; margin-bottom:1rem;">
              <div style="font-family:'Bebas Neue',sans-serif; font-size:1.2rem; color:#00ccff; letter-spacing:2px; margin-bottom:1rem;">
                REVENUE PRICING
              </div>
            """, unsafe_allow_html=True)
            
            cert_plans = [
                ("FOOD TRUCK", "$499", "Initial + $199/yr renewal"),
                ("RESTAURANT", "$1,299", "Initial + $499/yr renewal"),
                ("CHAIN (5+)", "$3,999", "Custom contract, volume discount"),
            ]
            for name, price, sub in cert_plans:
                st.markdown(f"""
                <div style="background:#111418; border:1px solid var(--border); border-radius:6px; 
                            padding:1rem; margin-bottom:.8rem; text-align:center;">
                  <div style="font-family:Space Mono,monospace; font-size:.65rem; color:#7d8590; letter-spacing:1px;">{name}</div>
                  <div style="font-family:'Bebas Neue',sans-serif; font-size:2rem; color:#00ccff;">{price}</div>
                  <div style="font-size:.75rem; color:#7d8590;">{sub}</div>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)

    # Restaurant ROI Section
    st.markdown('<div class="section-header">HOW RESTAURANTS BENEFIT</div>', unsafe_allow_html=True)

    benefits = [
        ("📉", "Reduced Liability", "A single foodborne illness outbreak can cost a restaurant $75,000–$2M in legal fees, settlements, and remediation. Certification provides documented due diligence."),
        ("⭐", "Consumer Trust", "Studies show 78% of diners would choose a certified 'food safe' restaurant over an uncertified competitor when price and quality are equal."),
        ("🏛️", "Regulatory Compliance", "Certification aligns with FDA Food Safety Modernization Act (FSMA) requirements, simplifying health inspections and reducing violations."),
        ("📱", "Marketing Advantage", "SafeSeal badge on delivery apps, Google Maps, and restaurant websites functions as a trust signal — measurably increasing conversion rates."),
        ("👨‍🍳", "Staff Retention", "Structured food safety training and certification improves kitchen culture, reduces accidents, and improves staff retention by 15–20%."),
        ("🔄", "Supply Chain", "Certified restaurants can qualify for preferred supplier status with major food distributors, potentially reducing ingredient costs by 5–12%."),
    ]

    cols = st.columns(3)
    for i, (icon, title, desc) in enumerate(benefits):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="info-card" style="margin-bottom:1rem;">
              <div class="card-icon">{icon}</div>
              <div class="card-title" style="color:#ffb700;">{title}</div>
              <div class="card-body" style="margin-top:.6rem;">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    # Market growth chart
    st.markdown('<div class="section-header">MARKET GROWTH PROJECTION</div>', unsafe_allow_html=True)

    years = [2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030]
    market_size = [14.5, 15.7, 17.0, 18.4, 19.9, 21.6, 23.4, 24.3, 25.8]

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=years[:5], y=market_size[:5],
        marker_color="#00ff88",
        name="Historical",
        opacity=0.9,
    ))
    fig.add_trace(go.Bar(
        x=years[4:], y=market_size[4:],
        marker_color="#ffb700",
        name="Projected",
        opacity=0.7,
    ))
    fig.add_trace(go.Scatter(
        x=years, y=market_size,
        mode="lines+markers",
        line=dict(color="#ffffff", width=2, dash="dot"),
        marker=dict(size=8, color="#ffffff"),
        name="Trend",
    ))

    fig.update_layout(
        paper_bgcolor="#161b22",
        plot_bgcolor="#0a0c0f",
        font=dict(color="#e6edf3", family="Space Mono"),
        xaxis=dict(gridcolor="#21262d", color="#7d8590"),
        yaxis=dict(title="Market Size ($B)", gridcolor="#21262d", color="#7d8590"),
        legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(color="#e6edf3")),
        margin=dict(l=60, r=20, t=20, b=60),
        height=320,
        barmode="overlay",
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
    <div style="font-family:Space Mono,monospace; font-size:.72rem; color:#7d8590; text-align:center; margin-top:.5rem;">
      Source: Grand View Research, MarketsandMarkets | CAGR: 8.3%
    </div>
    """, unsafe_allow_html=True)
