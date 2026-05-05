import streamlit as st

# ==========================================
# 1. CONFIGURATION & STYLE PREMIUM (CSS)
# ==========================================
st.set_page_config(page_title="Rabat Insider Pro", page_icon="🇲🇦", layout="centered")

st.markdown("""
    <style>
    /* Importation d'une police élégante */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@400;600&display=swap');

    /* Background global */
    .stApp {
        background-color: #F8F9FA;
    }

    /* Style des titres */
    h1 {
        font-family: 'Playfair Display', serif;
        color: #1A1A1A;
        text-align: center;
        padding-bottom: 20px;
    }
    
    /* Cartes de lieux */
    .place-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        border-left: 5px solid #C5A059; /* Couleur Or/Sable Rabat */
    }
    
    .place-name {
        font-size: 1.2em;
        font-weight: 600;
        color: #1A1A1A;
        margin-bottom: 5px;
    }
    
    .place-address {
        font-size: 0.9em;
        color: #666;
        font-style: italic;
        margin-bottom: 10px;
    }

    /* Masquer le menu Streamlit pour faire plus "App" */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. GESTION DES LANGUES
# ==========================================
col_lang1, col_lang2 = st.columns([8, 2])
with col_lang2:
    lang = st.selectbox("🌐", ["FR", "EN"])

content = {
    "FR": {
        "title": "📍 Rabat Insider",
        "subtitle": "La sélection exclusive pour nos invités.",
        "cat_label": "Que cherchez-vous ?",
        "cats": ["🍽️ Restaurants", "☕ Cafés & Tea Rooms", "📸 Culture & Loisirs", "💡 Pratique"],
        "btn_maps": "📍 Voir sur Google Maps",
        "footer": "© 2026 Rabat Insider - Service Premium"
    },
    "EN": {
        "title": "📍 Rabat Insider",
        "subtitle": "The exclusive selection for our guests.",
        "cat_label": "What are you looking for?",
        "cats": ["🍽️ Restaurants", "☕ Cafés & Tea Rooms", "📸 Culture & Leisure", "💡 Practical"],
        "btn_maps": "📍 View on Google Maps",
        "footer": "© 2026 Rabat Insider - Premium Service"
    }
}

t = content[lang]

st.title(t["title"])
st.markdown(f"<p style='text-align: center; color: #666;'>{t['subtitle']}</p>", unsafe_allow_html=True)

# ==========================================
# 3. BASE DE DONNÉES (Tes adresses)
# ==========================================

data = {
    "restaurants": [
        {"nom": "Dar Naji", "quartier": "Hassan / Medina", "adr": "Place de Russie, Rabat"},
        {"nom": "Mister Brochette", "quartier": "Agdal / Hassan", "adr": "Avenue Moulay Ismail, Rabat"},
        {"nom": "Ty Potes", "quartier": "Hassan", "adr": "11 Rue Ghafsa, Rabat"},
        {"nom": "Boqueria Fina", "quartier": "Hassan", "adr": "Avenue Moulay Hassan, Rabat"},
        {"nom": "Le Limonadier", "quartier": "Hassan", "adr": "Avenue Al Alaouiyine, Rabat"},
        {"nom": "Yamal Acham", "quartier": "Agdal", "adr": "Avenue Al Atlas, Rabat"},
        {"nom": "Les 2 Palais", "quartier": "Hassan", "adr": "Près du Mausolée, Rabat"},
        {"nom": "Muskaan", "quartier": "Agdal", "adr": "Avenue Annakhil, Rabat"},
        {"nom": "Tuscan", "quartier": "Agdal", "adr": "Avenue de France, Rabat"}
    ],
    "cafes": [
        {"nom": "Workstudio", "quartier": "Hassan", "adr": "Avenue Hassan II, Rabat"},
        {"nom": "Moe Tea Room", "quartier": "Hassan", "adr": "Quartier Hassan, Rabat"},
        {"nom": "Café de la Renaissance", "quartier": "Centre Ville", "adr": "Avenue Mohammed V, Rabat"},
        {"nom": "Le Goethe", "quartier": "Centre Ville", "adr": "Avenue Victoire, Rabat"}
    ],
    "culture": [
        {"nom": "Nécropole de Chellah", "adr": "Quartier Chellah, Rabat"},
        {"nom": "Allée Mahaj", "adr": "Hay Riad, Rabat"},
        {"nom": "Jardins d'Essai Botaniques", "adr": "Avenue de la Victoire, Rabat"},
        {"nom": "Rue des Consuls (Artisanat)", "adr": "Médina, Rabat"},
        {"nom": "Musée de la Photographie", "adr": "Fort Rottermbourg, Rabat"},
        {"nom": "Jardins Andalous", "adr": "Kasbah des Oudayas, Rabat"},
        {"nom": "La Corniche de Rabat", "adr": "Quartier l'Océan / Bouregreg"},
        {"nom": "Zoo de Rabat", "adr": "Route de Temara, Rabat"},
        {"nom": "Mausolée Mohammed V & Tour Hassan", "adr": "Boulevard Mohamed Lyazidi, Rabat"},
        {"nom": "Activités Nautiques / Surf", "adr": "Plage de Rabat / Marina"}
    ]
}

# ==========================================
# 4. AFFICHAGE
# ==========================================

choix = st.selectbox(t["cat_label"], t["cats"])
st.write("")

def display_item(name, quartier, address):
    maps_url = f"https://www.google.com/maps/search/?api=1&query={name.replace(' ', '+')}+Rabat"
    st.markdown(f"""
        <div class="place-card">
            <div class="place-name">{name}</div>
            <div style="color: #C5A059; font-weight: bold; font-size: 0.8em;">{quartier}</div>
            <div class="place-address">{address}</div>
        </div>
    """, unsafe_allow_html=True)
    st.link_button(t["btn_maps"], maps_url)
    st.write("")

if "Restaurants" in choix:
    for item in data["restaurants"]:
        display_item(item["nom"], item["quartier"], item["adr"])

elif "Cafés" in choix:
    for item in data["cafes"]:
        display_item(item["nom"], item["quartier"], item["adr"])

elif "Culture" in choix:
    for item in data["culture"]:
        display_item(item["nom"], "Rabat", item["adr"])

elif "Pratique" in choix:
    if lang == "FR":
        st.info("🚕 **Taxis :** Les petits taxis bleus utilisent le compteur. Prix moyen 20 MAD.")
        st.info("🚋 **Tramway :** Ligne 1 et 2. Ticket : 6 MAD.")
    else:
        st.info("🚕 **Taxis :** Small blue taxis use meters. Average price 20 MAD.")
        st.info("🚋 **Tramway :** Line 1 & 2. Ticket: 6 MAD.")

st.divider()
st.caption(t["footer"])
