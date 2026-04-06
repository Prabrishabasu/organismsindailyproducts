import streamlit as st
import pandas as pd

# The data remains the same
MICROBES = [
    {
        "name": "Lactobacillus acidophilus",
        "type": "BENEFICIAL",
        "emoji": "😊",
        "found_in": "Yogurt, kefir, fermented vegetables",
        "role": "Produces lactic acid, preserves food, supports gut health. Used in probiotics worldwide.",
        "temp_optimum": "37°C",
        "ph_range": "4.0 – 5.5",
        "fun_fact": "Lactobacillus has been fermenting food for over 10,000 years.",
        "risk": 0,
    },
    {
        "name": "Salmonella enterica",
        "type": "HARMFUL",
        "emoji": "⚠️",
        "found_in": "Raw poultry, eggs, unpasteurized milk, raw produce",
        "role": "Causes salmonellosis: fever, diarrhea, cramps. 1.35 million infections/year in the US.",
        "temp_optimum": "37°C",
        "ph_range": "6.5 – 7.5",
        "fun_fact": "Salmonella can survive on dry surfaces for weeks.",
        "risk": 95,
    },
    {
        "name": "Listeria monocytogenes",
        "type": "HARMFUL",
        "emoji": "🚨",
        "found_in": "Deli meats, soft cheeses, smoked fish, raw sprouts",
        "role": "Causes listeriosis — dangerous for pregnant women. Can grow at fridge temperatures.",
        "temp_optimum": "30-37°C",
        "ph_range": "5.0 – 9.6",
        "fun_fact": "Listeria thrives at 4°C — the fridge is NOT a safe zone.",
        "risk": 90,
    },
    {
        "name": "E. coli O157:H7",
        "type": "HARMFUL",
        "emoji": "☠️",
        "found_in": "Undercooked beef, raw milk, contaminated produce",
        "role": "Produces Shiga toxin causing bloody diarrhea and potentially fatal HUS.",
        "temp_optimum": "37°C",
        "ph_range": "4.4 – 8.5",
        "fun_fact": "Just 10 cells of E. coli O157:H7 can cause infection.",
        "risk": 98,
    },
    {
        "name": "Clostridium botulinum",
        "type": "HARMFUL",
        "emoji": "💀",
        "found_in": "Improperly canned foods, fermented fish, honey (infant risk)",
        "role": "Produces the most lethal toxin known. Causes botulism and paralysis.",
        "temp_optimum": "35°C",
        "ph_range": "4.8 – 7.0",
        "fun_fact": "1 gram of pure botulinum toxin could theoretically kill 1 million people.",
        "risk": 100,
    },
    {
        "name": "Aspergillus flavus",
        "type": "SPOILAGE",
        "emoji": "🍄",
        "found_in": "Peanuts, corn, wheat, stored grains",
        "role": "Produces aflatoxin — a potent carcinogen and liver toxin.",
        "temp_optimum": "25-35°C",
        "ph_range": "3.0 – 8.0",
        "fun_fact": "Aflatoxin B1 is invisible, odorless, and tasteless on contaminated peanuts.",
        "risk": 85,
    },
    {
        "name": "Pseudomonas fluorescens",
        "type": "SPOILAGE",
        "emoji": "🦠",
        "found_in": "Refrigerated meat, fish, dairy, vegetables",
        "role": "Primary spoilage organism in refrigerated foods. Produces slime and off-odors.",
        "temp_optimum": "20-25°C",
        "ph_range": "5.5 – 8.0",
        "fun_fact": "Pseudomonas is why refrigerated fish starts smelling within days.",
        "risk": 30,
    },
    {
        "name": "Staphylococcus aureus",
        "type": "HARMFUL",
        "emoji": "🤢",
        "found_in": "Ready-to-eat foods, egg salads, cream pastries, sandwiches",
        "role": "Produces heat-stable toxins causing rapid-onset vomiting and nausea.",
        "temp_optimum": "37°C",
        "ph_range": "4.5 – 9.3",
        "fun_fact": "~25% of healthy humans carry Staph aureus in their nose.",
        "risk": 80,
    },
    {
        "name": "Penicillium roqueforti",
        "type": "BENEFICIAL",
        "emoji": "🧀",
        "found_in": "Blue cheese (Roquefort, Gorgonzola, Stilton)",
        "role": "Creates the blue-green veins and creamy texture in blue cheeses.",
        "temp_optimum": "20-25°C",
        "ph_range": "3.0 – 7.5",
        "fun_fact": "The same mold genus gave us both blue cheese and penicillin.",
        "risk": 0,
    },
    {
        "name": "Bacillus cereus",
        "type": "HARMFUL",
        "emoji": "🍚",
        "found_in": "Cooked rice, pasta, starchy foods",
        "role": "Causes 'fried rice syndrome'. Forms heat-resistant spores.",
        "temp_optimum": "28-35°C",
        "ph_range": "4.9 – 9.3",
        "fun_fact": "Leaving cooked rice at room temperature overnight is a common risk.",
        "risk": 70,
    },
]

def render():
    st.title("🔬 Microbe Gallery")
    st.write("Explore the microorganisms found in our food systems.")

    # 1. Standard Filters
    filter_type = st.selectbox("Filter by Category", ["ALL", "BENEFICIAL", "HARMFUL", "SPOILAGE"])
    
    filtered = MICROBES if filter_type == "ALL" else [m for m in MICROBES if m["type"] == filter_type]

    # 2. Native Grid Layout
    for i in range(0, len(filtered), 2):
        batch = filtered[i:i+2]
        cols = st.columns(2)
        
        for idx, m in enumerate(batch):
            with cols[idx]:
                # Use st.container(border=True) for the card look without CSS
                with st.container(border=True):
                    st.subheader(f"{m['emoji']} {m['name']}")
                    
                    # Native status tags
                    if m['type'] == "BENEFICIAL":
                        st.success(m['type'])
                    elif m['type'] == "HARMFUL":
                        st.error(m['type'])
                    else:
                        st.warning(m['type'])

                    st.write(f"**Found in:** {m['found_in']}")
                    st.write(m['role'])
                    st.caption(f"Temp: {m['temp_optimum']} | pH: {m['ph_range']}")

                    # Native Progress Bar for Risk
                    if m['risk'] > 0:
                        st.write(f"Danger Level: {m['risk']}%")
                        st.progress(m['risk'] / 100)

                    # Native Info Box for Fun Fact
                    st.info(f"💡 {m['fun_fact']}")

    # 3. Reference Table
    st.divider()
    st.subheader("Quick Reference Data")
    st.dataframe(pd.DataFrame(MICROBES), use_container_width=True, hide_index=True)