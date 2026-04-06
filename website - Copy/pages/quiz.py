import streamlit as st

QUESTIONS = [
    {
        "q": "What is the 'Temperature Danger Zone' for bacterial growth?",
        "options": ["0°C – 20°C", "4°C – 60°C (40°F – 140°F)", "20°C – 80°C", "10°C – 100°C"],
        "answer": 1,
        "explanation": "The danger zone is 4°C–60°C. In this range, bacteria can double every 20 minutes. Always keep cold food cold and hot food hot.",
    },
    {
        "q": "A glass of milk has been left at room temperature (22°C) for 3 hours. What should you do?",
        "options": [
            "Smell it — if it smells fine, it's safe",
            "Boil it before drinking to kill bacteria",
            "Discard it — the 2-hour rule has been exceeded",
            "Refrigerate it immediately — it'll be safe again",
        ],
        "answer": 2,
        "explanation": "The 2-hour rule: discard perishables left in the danger zone for more than 2 hours. Boiling may kill bacteria but won't destroy toxins already produced. Refrigerating does NOT reset the clock.",
    },
    {
        "q": "Which microorganism is primarily responsible for 'fried rice syndrome'?",
        "options": ["Salmonella enterica", "Listeria monocytogenes", "Bacillus cereus", "E. coli O157:H7"],
        "answer": 2,
        "explanation": "Bacillus cereus forms heat-resistant spores in cooked rice. When rice is left at room temperature, spores germinate and produce toxins. Even reheating won't destroy these toxins.",
    },
    {
        "q": "You notice mold on one corner of a loaf of bread. What is the safest action?",
        "options": [
            "Cut off the moldy section (1 inch margin) and eat the rest",
            "Toast the bread to kill the mold",
            "Discard the entire loaf",
            "Scrape off the mold and refrigerate the rest",
        ],
        "answer": 2,
        "explanation": "Mold penetrates deep into porous foods like bread. Mycotoxins can diffuse throughout the loaf even in areas that appear clean. The USDA recommends discarding moldy bread entirely.",
    },
    {
        "q": "What is the minimum safe internal temperature for cooking whole poultry?",
        "options": ["63°C (145°F)", "71°C (160°F)", "74°C (165°F)", "82°C (180°F)"],
        "answer": 2,
        "explanation": "Poultry (whole birds, ground poultry, stuffing) must reach 74°C (165°F) measured at the thickest part. This kills Salmonella, Campylobacter, and other poultry-borne pathogens.",
    },
    {
        "q": "Which bacterium can grow in refrigerator temperatures (4°C) and is especially dangerous for pregnant women?",
        "options": ["Salmonella enterica", "Staphylococcus aureus", "Listeria monocytogenes", "Bacillus cereus"],
        "answer": 2,
        "explanation": "Listeria monocytogenes is unique — it's psychrotrophic, meaning it grows even in the fridge. It causes listeriosis, which can lead to miscarriage, stillbirth, or meningitis in high-risk groups.",
    },
    {
        "q": "How many E. coli O157:H7 cells are needed to cause infection?",
        "options": ["~10,000 cells", "~1,000 cells", "~100 cells", "As few as 10 cells"],
        "answer": 3,
        "explanation": "E. coli O157:H7 has one of the lowest infectious doses of any foodborne pathogen — as few as 10 cells can cause infection. This makes cross-contamination prevention extremely critical.",
    },
    {
        "q": "What is the correct way to thaw raw chicken safely?",
        "options": [
            "Leave it on the kitchen counter overnight",
            "In the refrigerator, cold running water (sealed), or microwave",
            "In warm water to speed up the process",
            "In the sun for 1–2 hours",
        ],
        "answer": 1,
        "explanation": "Safe thawing methods: (1) In the fridge overnight, (2) sealed bag under cold running water, (3) microwave — cook immediately. NEVER thaw at room temperature or in warm water.",
    },
    {
        "q": "Staphylococcus aureus produces toxins in food. If you cook the contaminated food thoroughly, are the toxins destroyed?",
        "options": [
            "Yes — cooking above 74°C destroys all toxins",
            "Partially — some toxins survive",
            "No — Staph aureus toxins are heat-stable and survive cooking",
            "It depends on how long the food was contaminated",
        ],
        "answer": 2,
        "explanation": "Staph aureus toxins are heat-stable. Even if the bacteria are killed by cooking, the pre-formed toxins survive and cause rapid-onset vomiting (within 1–6 hours). Prevention is the only solution.",
    },
    {
        "q": "Which of these is a probiotic beneficial bacterium used in yogurt production?",
        "options": ["Salmonella typhimurium", "Lactobacillus acidophilus", "Clostridium botulinum", "Campylobacter jejuni"],
        "answer": 1,
        "explanation": "Lactobacillus acidophilus is a probiotic bacterium that ferments lactose to produce lactic acid, giving yogurt its characteristic tang and texture. It also supports gut health.",
    },
]

def render():
    st.markdown("""
    <div class="hero-banner" style="padding:2rem 2.5rem;">
      <div class="hero-sub">🧪 Food Safety IQ Test</div>
      <div class="hero-title" style="font-size:3rem;">TEST YOURSELF</div>
      <div class="hero-desc">10 questions. How safe is your kitchen, really? Most people fail at least 3.</div>
    </div>
    """, unsafe_allow_html=True)

    if "quiz_answers" not in st.session_state:
        st.session_state.quiz_answers = {}
    if "quiz_submitted" not in st.session_state:
        st.session_state.quiz_submitted = False
    if "quiz_started" not in st.session_state:
        st.session_state.quiz_started = False

    if not st.session_state.quiz_started:
        c1, c2, c3 = st.columns([1,2,1])
        with c2:
            st.markdown("""
            <div style="background:var(--card); border:1px solid var(--border); border-radius:8px; 
                        padding:2rem; text-align:center; margin-top:1rem;">
              <div style="font-size:4rem; margin-bottom:1rem;">🧠</div>
              <div style="font-family:'Bebas Neue',sans-serif; font-size:1.8rem; letter-spacing:3px; margin-bottom:1rem;">
                10 QUESTIONS
              </div>
              <div style="color:#7d8590; font-size:.9rem; line-height:1.7; margin-bottom:1.5rem;">
                Topics covered: danger zones, pathogens, safe handling,<br>
                microbiology basics, and food safety regulations.
              </div>
              <div style="font-family:Space Mono,monospace; font-size:.75rem; color:#ffb700; margin-bottom:1.5rem;">
                Average score: 6.2 / 10
              </div>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("🚀 Start Quiz", use_container_width=True):
                st.session_state.quiz_started = True
                st.session_state.quiz_answers = {}
                st.session_state.quiz_submitted = False
                st.rerun()
        return

    if not st.session_state.quiz_submitted:
        st.markdown(f"""
        <div style="font-family:Space Mono,monospace; font-size:.75rem; color:#7d8590; margin-bottom:1.5rem; letter-spacing:1px;">
          ANSWERED: {len(st.session_state.quiz_answers)} / {len(QUESTIONS)}
        </div>
        """, unsafe_allow_html=True)

        for i, q in enumerate(QUESTIONS):
            st.markdown(f"""
            <div style="background:var(--card); border:1px solid var(--border); border-left:3px solid {'#00ff88' if i in st.session_state.quiz_answers else '#21262d'};
                        border-radius:8px; padding:1.5rem; margin-bottom:1rem;">
              <div style="font-family:Space Mono,monospace; font-size:.7rem; color:#7d8590; margin-bottom:.5rem; letter-spacing:1px;">
                QUESTION {i+1} OF {len(QUESTIONS)}
              </div>
              <div style="color:#e6edf3; font-size:1rem; font-weight:500; margin-bottom:1rem; line-height:1.5;">
                {q['q']}
              </div>
            </div>
            """, unsafe_allow_html=True)

            selected = st.radio(
                f"Q{i+1}",
                q["options"],
                key=f"q_{i}",
                index=st.session_state.quiz_answers.get(i, None),
                label_visibility="collapsed",
            )
            if selected:
                st.session_state.quiz_answers[i] = q["options"].index(selected)

        st.markdown("<br>", unsafe_allow_html=True)
        
        if len(st.session_state.quiz_answers) == len(QUESTIONS):
            if st.button("✅ Submit Answers", use_container_width=True):
                st.session_state.quiz_submitted = True
                st.rerun()
        else:
            remaining = len(QUESTIONS) - len(st.session_state.quiz_answers)
            st.info(f"Answer {remaining} more question{'s' if remaining > 1 else ''} to submit.")

    else:
        # Results
        score = sum(1 for i, q in enumerate(QUESTIONS) 
                    if st.session_state.quiz_answers.get(i) == q["answer"])
        pct = score / len(QUESTIONS) * 100

        if pct >= 90:
            grade, color, msg = "EXPERT", "#00ff88", "Outstanding! Your food safety knowledge is at professional level."
        elif pct >= 70:
            grade, color, msg = "PROFICIENT", "#7dff88", "Good work! A few gaps to address, but you're safer than most."
        elif pct >= 50:
            grade, color, msg = "AVERAGE", "#ffb700", "You know the basics, but some dangerous knowledge gaps exist."
        else:
            grade, color, msg = "AT RISK", "#ff3c6e", "Your kitchen may be at risk. Review all sections of this site."

        st.markdown(f"""
        <div style="background:var(--card); border:1px solid {color}44; border-top:4px solid {color};
                    border-radius:8px; padding:2rem; text-align:center; margin-bottom:2rem;">
          <div style="font-family:'Bebas Neue',sans-serif; font-size:5rem; color:{color}; line-height:1;">
            {score}/{len(QUESTIONS)}
          </div>
          <div style="font-family:Space Mono,monospace; font-size:1rem; color:{color}; letter-spacing:3px; margin:.5rem 0;">
            {grade}
          </div>
          <div style="color:#e6edf3; font-size:.95rem; margin-top:.8rem;">{msg}</div>
        </div>
        """, unsafe_allow_html=True)

        # Answer review
        st.markdown('<div class="section-header">ANSWER REVIEW</div>', unsafe_allow_html=True)

        for i, q in enumerate(QUESTIONS):
            user_ans = st.session_state.quiz_answers.get(i)
            is_correct = user_ans == q["answer"]
            icon = "✅" if is_correct else "❌"
            border = "#00ff88" if is_correct else "#ff3c6e"

            st.markdown(f"""
            <div style="background:var(--card); border:1px solid {border}33; border-left:3px solid {border};
                        border-radius:8px; padding:1.2rem; margin-bottom:1rem;">
              <div style="display:flex; justify-content:space-between; align-items:flex-start;">
                <div style="font-size:.9rem; color:#e6edf3; font-weight:500; flex:1; margin-right:1rem;">
                  Q{i+1}: {q['q']}
                </div>
                <div style="font-size:1.3rem;">{icon}</div>
              </div>
              <div style="margin-top:.8rem; font-size:.84rem; color:#7d8590;">
                Your answer: <span style="color:{'#00ff88' if is_correct else '#ff3c6e'};">
                  {q['options'][user_ans] if user_ans is not None else 'Not answered'}
                </span>
              </div>
              {'<div style="font-size:.84rem; color:#7d8590; margin-top:.3rem;">Correct answer: <span style="color:#00ff88;">' + q["options"][q["answer"]] + '</span></div>' if not is_correct else ''}
              <div style="background:rgba(255,183,0,.06); border:1px solid #3d2800; border-radius:6px; 
                          padding:.8rem; margin-top:.8rem; font-size:.82rem; color:#ffb700; line-height:1.6;">
                💡 {q['explanation']}
              </div>
            </div>
            """, unsafe_allow_html=True)

        if st.button("🔄 Retake Quiz", use_container_width=True):
            st.session_state.quiz_started = False
            st.session_state.quiz_submitted = False
            st.session_state.quiz_answers = {}
            st.rerun()
