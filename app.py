import streamlit as st

# ==========================================
# 1. CONFIGURATION ET STYLE STRICT
# ==========================================
st.set_page_config(
    page_title="Rabat Insider",
    page_icon="🇲🇦",
    layout="centered"
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Montserrat:wght@300;400&display=swap');

    /* Fond sombre uni pour un rendu luxe et pro */
    .stApp {
        background-color: #0F0F0F;
    }

    /* Titre principal Or */
    .main-title {
        font-family: 'Cinzel', serif;
        color: #D4AF37;
        text-align: center;
        font-size: 2.8rem;
        letter-spacing: 4px;
        margin-bottom: 0px;
    }

    .sub-title {
        font-family: 'Montserrat', sans-serif;
        color: #888;
        text-align: center;
        letter-spacing: 5px;
        font-size: 0.7rem;
        text-transform: uppercase;
        margin-bottom: 40px;
    }

    /* Cartes de lieux sans photos */
    .place-card {
        background-color: #1A1A1A;
        padding: 25px;
        border-radius: 0px;
        border: 1px solid #222;
        border-left: 4px solid #D4AF37;
        margin-bottom: 10px;
    }

    .place-name {
        font-family: 'Cinzel', serif;
        font-size: 1.5rem;
        color: #D4AF37;
        margin-bottom: 5px;
    }

    .place-quartier {
        font-family: 'Montserrat', sans-serif;
        font-size: 0.75rem;
        color: #666;
        text-transform: uppercase;
        letter-spacing: 2px;
    }

    /* Style des boutons Maps */
    .stButton>button {
        width: 100%;
        background-color: transparent !important;
        color: #D4AF37 !important;
        border: 1px solid #D4AF37 !important;
        border-radius: 0px !important;
        font-family: 'Montserrat', sans-serif !important;
        text-transform: uppercase;
        letter-spacing: 2px;
        height: 45px;
        transition: 0.3s;
    }

    .stButton>button:hover {
        background-color: #D4AF37 !important;
        color: #000 !important;
    }

    /* Custom Selectbox */
    .stSelectbox label { color: #888 !important; }
    
    /* Supprimer les éléments parasites */
    #MainMenu, footer, header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. LOGIQUE DE NAVIGATION (DIRECTE)
# ==========================================

# Choix de la langue en haut de page (remplace la sidebar)
lang = st.radio("", ["FRANÇAIS", "ENGLISH"], horizontal=True)

content = {
    "FRANÇAIS": {
        "title": "RABAT INSIDER",
        "tagline": "SÉLECTION PRIVÉE DE VOTRE CONCIERGE",
        "select": "EXPLORER",
        "cats": ["GASTRONOMIE", "CAFÉS STYLÉS", "CULTURE & PATRIMOINE", "INFOS PRATIQUES"],
        "btn": "VOIR L'ITINÉRAIRE",
        "taxi": "TAXIS BLEUS : Demandez toujours le compteur. Course moyenne 20 MAD.",
        "tram": "TRAMWAY : Très fiable. Lignes 1 & 2 (6 MAD le ticket)."
    },
    "ENGLISH": {
        "title": "RABAT INSIDER",
        "tagline": "PRIVATE CONCIERGE SELECTION",
        "select": "EXPLORE",
        "cats": ["GASTRONOMY", "STYLISH CAFÉS", "CULTURE & HERITAGE", "PRACTICAL INFO"],
        "btn": "GET DIRECTIONS",
        "taxi": "BLUE TAXIS: Always ask for the meter. Average ride 20 MAD.",
        "tram": "TRAMWAY: Highly reliable. Lines 1 & 2 (6 MAD per ticket)."
    }
}

t = content[lang]

# Header
st.markdown(f'<h1 class="main-title">{t["title"]}</h1>', unsafe_allow_html=True)
st.markdown(f'<p class="sub-title">{t["tagline"]}</p>', unsafe_allow_html=True)

# ==========================================
# 3. DONNÉES (SANS PHOTOS / ADRESSES CACHÉES)
# ==========================================
data = {
    "restaurants": [
        {"nom": "Mr. Brochette", "q": "Hassan", "maps": "https://www.google.com/maps/search/?api=1&query=Mr+Brochette+Rabat"},
        {"nom": "Dar Naji", "q": "Hassan", "maps": "https://www.google.com/maps/search/?api=1&query=Dar+Naji+Hassan+Rabat"},
        {"nom": "Ty Potes", "q": "Hassan", "maps": "https://www.google.com/maps/search/?api=1&query=Ty+Potes+Rabat"},
        {"nom": "Le Goethe", "q": "Centre-Ville", "maps": "https://www.google.com/maps/search/?api=1&query=Le+Goethe+Rabat"},
        {"nom": "Boqueria Fina", "q": "Hassan", "maps": "https://www.google.com/maps/search/?api=1&query=Boqueria+Fina+Rabat"},
        {"nom": "Le Limonadier", "q": "Hassan", "maps": "https://www.google.com/maps/search/?api=1&query=Le+Limonadier+Rabat"},
        {"nom": "Yamal Acham", "q": "Agdal", "maps": "https://www.google.com/maps/search/?api=1&query=Yamal+Acham+Rabat"},
        {"nom": "Les 2 Palais", "q": "Hassan", "maps": "https://www.google.com/maps/search/?api=1&query=Les+2+Palais+Rabat"}
    ],
    "cafes": [
        {"nom": "Kultur Café", "q": "Hassan", "maps": "https://www.google.com/maps/search/?api=1&query=Kultur+Cafe+Rabat"},
        {"nom": "Workstudio", "q": "Hassan", "maps": "https://www.google.com/maps/search/?api=1&query=Workstudio+Rabat"},
        {"nom": "Bloom Coffee", "q": "Agdal", "maps": "https://www.google.com/maps/search/?api=1&query=Bloom+Coffee+Rabat"},
        {"nom": "Moe Tea Room", "q": "Hassan", "maps": "https://www.google.com/maps/search/?api=1&query=Moe+Tea+Room+Rabat"},
        {"nom": "Renaissance", "q": "Centre-Ville", "maps": "https://www.google.com/maps/search/?api=1&query=Cafe+Renaissance+Rabat"}
    ],
    "culture": [
        {"nom": "Chellah", "q": "Patrimoine", "maps": "https://www.google.com/maps/search/?api=1&query=Chellah+Rabat"},
        {"nom": "Allée Mahaj", "q": "Hay Riad", "maps": "https://www.google.com/maps/search/?api=1&query=Mahaj+Riad+Rabat"},
        {"nom": "Jardins d'Essai", "q": "Agdal", "maps": "https://www.google.com/maps/search/?api=1&query=Jardin+Essais+Rabat"},
        {"nom": "Mausolée Mohammed V", "q": "Hassan", "maps": "https://www.google.com/maps/search/?api=1&query=Mausolee+Mohammed+V+Rabat"},
        {"nom": "Kasbah des Oudayas", "q": "Oudayas", "maps": "https://www.google.com/maps/search/?api=1&query=Oudayas+Rabat"},
        {"nom": "Zoo de Rabat", "q": "Loisirs", "maps": "https://www.google.com/maps/search/?api=1&query=Zoo+Rabat"}
    ]
}

# ==========================================
# 4. AFFICHAGE
# ==========================================
category = st.selectbox(t["select"], t["cats"])
st.write("")

def render_item(item):
    st.markdown(f"""
        <div class="place-card">
            <div class="place-name">{item['nom']}</div>
            <div class="place-quartier">{item['q']}</div>
        </div>
    """, unsafe_allow_html=True)
    st.link_button(t["btn"], item['maps'])
    st.write("")

if category in ["GASTRONOMIE", "GASTRONOMY"]:
    for item in data["restaurants"]:
        render_item(item)

elif category in ["CAFÉS STYLÉS", "STYLISH CAFÉS"]:
    for item in data["cafes"]:
        render_item(item)

elif category in ["CULTURE & PATRIMOINE", "CULTURE & HERITAGE"]:
    for item in data["culture"]:
        render_item(item)

elif "INFOS" in category or "INFO" in category:
    st.markdown(f"<div style='color:#FFF; padding:20px; border:1px solid #333;'>{t['taxi']}</div>", unsafe_allow_html=True)
    st.write("")
    st.markdown(f"<div style='color:#FFF; padding:20px; border:1px solid #333;'>{t['tram']}</div>", unsafe_allow_html=True)

# Pied de page
st.divider()
st.markdown("<p style='text-align:center; color:#444; font-size:0.7rem; letter-spacing:2px;'>EXCLUSIVE CONCIERGE SERVICE</p>", unsafe_allow_html=True)
