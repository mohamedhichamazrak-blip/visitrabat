import streamlit as st

# ==========================================
# 1. CONFIGURATION & DESIGN RAHAL STYLE
# ==========================================
st.set_page_config(page_title="Rabat Insider | Premium", page_icon="🇲🇦", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Inter:wght@300;400;600&display=swap');

    /* Fond noir profond avec texture légère */
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.85), rgba(0, 0, 0, 0.95)), 
                    url("https://images.unsplash.com/photo-1539020140153-e479b8c22e70?auto=format&fit=crop&w=1920&q=80");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    /* Titre style Cinzel (Luxueux) */
    h1 {
        font-family: 'Cinzel', serif;
        color: #D4AF37 !important; /* Or pur */
        text-align: center;
        letter-spacing: 3px;
        margin-top: -40px;
        font-size: 2.5em;
    }
    
    .stMarkdown p, label, .stSelectbox label {
        color: #FFFFFF !important;
        font-family: 'Inter', sans-serif;
    }

    /* Cartes Noir & Or */
    .place-card {
        background-color: #1A1A1A;
        padding: 25px;
        border-radius: 5px; /* Moins arrondi pour un look plus institutionnel */
        border: 1px solid #333;
        border-top: 4px solid #D4AF37; /* Liseré Or */
        box-shadow: 0 15px 35px rgba(0,0,0,0.5);
        margin-bottom: 5px;
        transition: transform 0.3s ease;
    }
    
    .place-name {
        font-family: 'Cinzel', serif;
        font-size: 1.4em;
        font-weight: 700;
        color: #D4AF37 !important;
        margin-bottom: 5px;
    }
    
    .place-quartier {
        color: #888;
        font-weight: 400;
        font-size: 0.8em;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 12px;
    }
    
    .place-address {
        font-size: 0.95em;
        color: #CCC !important;
        line-height: 1.6;
        border-top: 1px solid #333;
        padding-top: 10px;
    }

    /* Style du bouton Maps */
    .stButton>button {
        background-color: transparent !important;
        color: #D4AF37 !important;
        border: 1px solid #D4AF37 !important;
        border-radius: 0px !important;
        font-family: 'Cinzel', serif !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: all 0.4s;
    }
    .stButton>button:hover {
        background-color: #D4AF37 !important;
        color: black !important;
    }

    #MainMenu, footer, header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. LOGIQUE DE LANGUE
# ==========================================
lang = st.sidebar.selectbox("🌐 LANGUAGE", ["Français", "English"])

content = {
    "Français": {
        "title": "Rabat Insider",
        "subtitle": "CONCIERGERIE PRIVÉE & SÉLECTION D'EXCEPTION",
        "cat_label": "EXPLORER L'ART DE VIVRE",
        "cats": ["🍽️ Gastronomie", "☕ Salons de Thé & Cafés", "📸 Culture & Patrimoine", "💡 Informations"],
        "btn_maps": "Découvrir l'itinéraire",
        "footer": "RABAT INSIDER — SERVICE DE CONCIERGERIE PREMIUM"
    },
    "English": {
        "title": "Rabat Insider",
        "subtitle": "PRIVATE CONCIERGE & EXCLUSIVE SELECTION",
        "cat_label": "EXPLORE LIFESTYLE",
        "cats": ["🍽️ Gastronomy", "☕ Tea Rooms & Cafés", "📸 Culture & Heritage", "💡 Information"],
        "btn_maps": "View Directions",
        "footer": "RABAT INSIDER — PREMIUM CONCIERGE SERVICE"
    }
}

t = content[lang]

st.title(t["title"])
st.markdown(f"<p style='text-align: center; color: #D4AF37; letter-spacing: 2px; font-size: 0.8em;'>{t['subtitle']}</p>", unsafe_allow_html=True)
st.write("")

# ==========================================
# 3. DONNÉES (ADRESSES VÉRIFIÉES)
# ==========================================
data = {
    "restaurants": [
        {"nom": "Mr. Brochette", "quartier": "Hassan", "adr": "Avenue Moulay Ismail, Rabat"},
        {"nom": "Dar Naji", "quartier": "Hassan", "adr": "Place de Russie (Hassan), Rabat"},
        {"nom": "Ty Potes", "quartier": "Hassan", "adr": "11 Rue Ghafsa, Rabat"},
        {"nom": "Boqueria Fina", "quartier": "Hassan", "adr": "Avenue Moulay Hassan, Rabat"},
        {"nom": "Le Limonadier", "quartier": "Hassan", "adr": "Angle Avenue Al Alaouiyine et Rue Al Forat, Rabat"},
        {"nom": "Yamal Acham", "quartier": "Agdal", "adr": "6 Avenue Al Atlas, Rabat"},
        {"nom": "Les 2 Palais", "quartier": "Hassan", "adr": "Place Sidi Makhlouf, Rabat"},
        {"nom": "Muskaan", "quartier": "Agdal", "adr": "Avenue Annakhil, Rabat"},
        {"nom": "Tuscan", "quartier": "Agdal", "adr": "Avenue de France, Rabat"}
    ],
    "cafes": [
        {"nom": "Workstudio", "quartier": "Hassan", "adr": "Avenue Hassan II, Rabat"},
        {"nom": "Moe Tea Room", "quartier": "Hassan", "adr": "12 Rue de Tripoli, Rabat"},
        {"nom": "Café de la Renaissance", "quartier": "Centre-Ville", "adr": "Avenue Mohammed V, Rabat"},
        {"nom": "Le Goethe", "quartier": "Centre-Ville", "adr": "Avenue de la Victoire, Rabat"}
    ],
    "culture": [
        {"nom": "Nécropole de Chellah", "adr": "Avenue Chellah, Rabat"},
        {"nom": "Allée Mahaj", "adr": "Hay Riad, Rabat"},
        {"nom": "Jardins d'Essai Botaniques", "adr": "Avenue de la Victoire, Rabat"},
        {"nom": "Rue des Consuls", "adr": "Médina, Rabat"},
        {"nom": "Musée de la Photographie", "adr": "Fort Rottermbourg, Rabat"},
        {"nom": "Jardins Andalous", "adr": "Kasbah des Oudayas, Rabat"},
        {"nom": "Corniche de Rabat", "adr": "Avenue Mohamed VI, Rabat"},
        {"nom": "Zoo de Rabat", "adr": "Route de Temara, Rabat"},
        {"nom": "Mausolée Mohammed V", "adr": "Boulevard Mohamed Lyazidi, Rabat"},
        {"nom": "Surf & Nautisme", "adr": "Plage de Rabat, Rabat"}
    ]
}

# ==========================================
# 4. AFFICHAGE
# ==========================================
choix = st.selectbox(t["cat_label"], t["cats"])

def render_card(name, q, a):
    search_query = f"{name} {a} Rabat".replace(" ", "+")
    maps_url = f"https://www.google.com/maps/search/?api=1&query={search_query}"
    
    st.markdown(f"""
        <div class="place-card">
            <div class="place-name">{name}</div>
            <div class="place-quartier">{q}</div>
            <div class="place-address">{a}</div>
        </div>
    """, unsafe_allow_html=True)
    st.link_button(t["btn_maps"], maps_url, use_container_width=True)
    st.write("")

if "Gastronomie" in choix or "Gastronomy" in choix:
    for item in data["restaurants"]:
        render_card(item["nom"], item["quartier"], item["adr"])
elif "Salons" in choix or "Tea Rooms" in choix:
    for item in data["cafes"]:
        render_card(item["nom"], item["quartier"], item["adr"])
elif "Patrimoine" in choix or "Heritage" in choix:
    for item in data["culture"]:
        render_card(item["nom"], "PATRIMOINE DE RABAT", item["adr"])
elif "Informations" in choix or "Information" in choix:
    st.info("🚕 **PETITS TAXIS :** Couleur Bleue. Tarif minimum 7.50 MAD. Compteur obligatoire.")
    st.info("🚋 **TRAMWAY :** Propre et rapide. Ticket 6 MAD aux automates.")

st.divider()
st.markdown(f"<p style='text-align: center; color: #888; font-size: 0.7em; letter-spacing: 2px;'>{t['footer']}</p>", unsafe_allow_html=True)
