import streamlit as st

# ==========================================
# 1. CONFIGURATION & DESIGN PREMIUM (CSS)
# ==========================================
st.set_page_config(page_title="Rabat Insider Pro", page_icon="🇲🇦", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@400;600&display=swap');

    /* Fond d'écran Rabat avec filtre sombre pour lisibilité */
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.65), rgba(0, 0, 0, 0.65)), 
                    url("https://images.unsplash.com/photo-1539020140153-e479b8c22e70?auto=format&fit=crop&w=1920&q=80");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    /* Style des textes et titres */
    h1 {
        font-family: 'Playfair Display', serif;
        color: #FFFFFF !important;
        text-align: center;
        margin-top: -50px;
    }
    
    .stMarkdown p, label, .stSelectbox label {
        color: #FFFFFF !important;
    }

    /* Cartes Glassmorphism */
    .place-card {
        background-color: rgba(255, 255, 255, 0.98);
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        margin-bottom: 5px;
        border-left: 6px solid #C5A059;
    }
    
    .place-name {
        font-size: 1.25em;
        font-weight: 700;
        color: #1A1A1A !important;
        margin-bottom: 2px;
    }
    
    .place-quartier {
        color: #C5A059;
        font-weight: 600;
        font-size: 0.85em;
        text-transform: uppercase;
        margin-bottom: 8px;
    }
    
    .place-address {
        font-size: 0.9em;
        color: #444 !important;
        line-height: 1.4;
    }

    /* Masquer les menus Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. TRADUCTIONS ET INTERFACE
# ==========================================
lang = st.sidebar.selectbox("🌐 Language / Langue", ["Français", "English"])

content = {
    "Français": {
        "title": "📍 Rabat Insider",
        "subtitle": "La sélection d'exception pour vivre Rabat comme un local.",
        "cat_label": "Choisissez une catégorie",
        "cats": ["🍽️ Restaurants", "☕ Cafés & Tea Rooms", "📸 Culture & Loisirs", "💡 Pratique"],
        "btn_maps": "📍 Itinéraire Google Maps",
        "footer": "© 2026 Rabat Insider - Conciergerie Privée"
    },
    "English": {
        "title": "📍 Rabat Insider",
        "subtitle": "The premium selection to experience Rabat as a local.",
        "cat_label": "Choose a category",
        "cats": ["🍽️ Restaurants", "☕ Cafés & Tea Rooms", "📸 Culture & Leisure", "💡 Practical"],
        "btn_maps": "📍 Get Directions (Maps)",
        "footer": "© 2026 Rabat Insider - Private Concierge"
    }
}

t = content[lang]

st.title(t["title"])
st.markdown(f"<p style='text-align: center; color: #EEE;'>{t['subtitle']}</p>", unsafe_allow_html=True)

# ==========================================
# 3. BASE DE DONNÉES DES LIEUX (ADRESSES EXACTES)
# ==========================================
data = {
    "restaurants": [
        {"nom": "Dar Naji", "quartier": "Hassan", "adr": "Place de Russie (Près de l'Hôtel Diwan), Rabat"},
        {"nom": "Mister Brochette", "quartier": "Agdal / Hassan", "adr": "Avenue Moulay Ismail, Rabat"},
        {"nom": "Ty Potes", "quartier": "Hassan", "adr": "11 Rue Ghafsa, Rabat"},
        {"nom": "Boqueria Fina", "quartier": "Hassan", "adr": "Avenue Moulay Hassan, Rabat"},
        {"nom": "Le Limonadier", "quartier": "Hassan", "adr": "Angle Avenue Al Alaouiyine et Rue Al Forat, Rabat"},
        {"nom": "Yamal Acham", "quartier": "Agdal", "adr": "6 Avenue Al Atlas, Rabat"},
        {"nom": "Les 2 Palais", "quartier": "Hassan", "adr": "Place Sidi Makhlouf (Face Tour Hassan), Rabat"},
        {"nom": "Muskaan", "quartier": "Agdal", "adr": "Avenue Annakhil, Rabat"},
        {"nom": "Tuscan", "quartier": "Agdal", "adr": "Avenue de France, Rabat"}
    ],
    "cafes": [
        {"nom": "Workstudio", "quartier": "Hassan", "adr": "Avenue Hassan II (Près de la gare Rabat-Ville), Rabat"},
        {"nom": "Moe Tea Room", "quartier": "Hassan", "adr": "12 Rue de Tripoli, Rabat"},
        {"nom": "Café de la Renaissance", "quartier": "Centre-Ville", "adr": "Avenue Mohammed V, Rabat"},
        {"nom": "Le Goethe", "quartier": "Centre-Ville", "adr": "Avenue de la Victoire, Rabat"}
    ],
    "culture": [
        {"nom": "Nécropole de Chellah", "adr": "Avenue Chellah, Rabat"},
        {"nom": "Allée Mahaj (Hay Riad)", "adr": "Avenue Al Mahaj, Hay Riad, Rabat"},
        {"nom": "Jardins d'Essai Botaniques", "adr": "Avenue de la Victoire, Agdal, Rabat"},
        {"nom": "Rue des Consuls (Tapis & Artisanat)", "adr": "Médina, Rabat"},
        {"nom": "Musée National de la Photographie", "adr": "Fort Rottermbourg, l'Océan, Rabat"},
        {"nom": "Jardins Andalous", "adr": "Kasbah des Oudayas, Rabat"},
        {"nom": "La Corniche de Rabat", "adr": "Avenue Mohamed VI (Côté Mer), Rabat"},
        {"nom": "Zoo de Rabat (Jardin Zoologique National)", "adr": "Annexe II, Route de Temara, Rabat"},
        {"nom": "Mausolée Mohammed V & Tour Hassan", "adr": "Boulevard Mohamed Lyazidi, Rabat"},
        {"nom": "Activités Nautiques / Surf", "adr": "Plage de Rabat / Marina du Bouregreg"}
    ]
}

# ==========================================
# 4. FONCTION D'AFFICHAGE
# ==========================================
def display_card(name, q, a):
    # Lien Google Maps précis
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

# ==========================================
# 5. LOGIQUE DE NAVIGATION
# ==========================================
choix = st.selectbox(t["cat_label"], t["cats"])
st.write("")

if "Restaurants" in choix:
    for item in data["restaurants"]:
        display_card(item["nom"], item["quartier"], item["adr"])

elif "Cafés" in choix:
    for item in data["cafes"]:
        display_card(item["nom"], item["quartier"], item["adr"])

elif "Culture" in choix:
    for item in data["culture"]:
        display_card(item["nom"], "Rabat", item["adr"])

elif "Pratique" in choix:
    if lang == "Français":
        st.success("🚕 **Petit Taxi (Bleu) :** Exigez le compteur. Course moyenne : 15-25 MAD.")
        st.success("🚋 **Tramway :** Tickets aux bornes (6 MAD). Très pratique pour Hassan <-> Agdal.")
        st.success("💊 **Pharmacie :** Pharmacies de garde disponibles 24/7 par rotation.")
    else:
        st.success("🚕 **Small Taxi (Blue):** Always ask for the meter. Average ride: 15-25 MAD.")
        st.success("🚋 **Tramway:** Tickets at kiosks (6 MAD). Best for Hassan <-> Agdal.")
        st.success("💊 **Pharmacy:** 24/7 rotating on-call pharmacies available.")

st.divider()
st.markdown(f"<p style='text-align: center; color: white; font-size: 0.8em;'>{t['footer']}</p>", unsafe_allow_html=True)
