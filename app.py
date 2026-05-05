import streamlit as st

# ==========================================
# 1. CONFIGURATION DE LA PAGE
# ==========================================
st.set_page_config(
    page_title="Rabat Insider | Premium Concierge",
    page_icon="🇲🇦",
    layout="centered"
)

# ==========================================
# 2. LOGIQUE D'ARRIÈRE-PLAN DYNAMIQUE
# ==========================================
# On définit les images selon le choix de l'utilisateur
bg_images = {
    "ACCUEIL": "https://images.unsplash.com/photo-1539020140153-e479b8c22e70?auto=format&fit=crop&w=1920&q=80",
    "RESTAURANTS": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?auto=format&fit=crop&w=1920&q=80",
    "CAFÉS": "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?auto=format&fit=crop&w=1920&q=80",
    "CULTURE": "https://images.unsplash.com/photo-1548013146-72479768bbaa?auto=format&fit=crop&w=1920&q=80",
    "INFOS": "https://images.unsplash.com/photo-1506012733851-46297839fa01?auto=format&fit=crop&w=1920&q=80"
}

def set_bg(category_key):
    img_url = bg_images.get(category_key, bg_images["ACCUEIL"])
    st.markdown(f"""
        <style>
        .stApp {{
            background: linear-gradient(rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0.85)), 
                        url("{img_url}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        
        @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Montserrat:wght@300;400&display=swap');

        /* Style global */
        .main-title {{
            font-family: 'Cinzel', serif;
            color: #D4AF37;
            text-align: center;
            font-size: 2.5rem;
            letter-spacing: 5px;
            margin-bottom: 0px;
            text-transform: uppercase;
        }}

        .sub-title {{
            font-family: 'Montserrat', sans-serif;
            color: #FFFFFF;
            text-align: center;
            letter-spacing: 4px;
            font-size: 0.7rem;
            text-transform: uppercase;
            margin-bottom: 30px;
            opacity: 0.8;
        }}

        /* Cartes Minimalistes */
        .premium-card {{
            background-color: rgba(20, 20, 20, 0.8);
            padding: 20px;
            border-left: 3px solid #D4AF37;
            margin-bottom: 8px;
            border-radius: 2px;
        }}

        .item-name {{
            font-family: 'Cinzel', serif;
            font-size: 1.3rem;
            color: #D4AF37;
        }}

        .item-tag {{
            font-family: 'Montserrat', sans-serif;
            font-size: 0.65rem;
            color: #888;
            letter-spacing: 2px;
            text-transform: uppercase;
        }}

        /* Boutons */
        .stButton>button {{
            width: 100%;
            background-color: transparent !important;
            color: #D4AF37 !important;
            border: 1px solid #D4AF37 !important;
            border-radius: 0px !important;
            text-transform: uppercase;
            letter-spacing: 2px;
            transition: 0.4s;
        }}
        .stButton>button:hover {{
            background-color: #D4AF37 !important;
            color: #000 !important;
        }}

        #MainMenu, footer, header {{visibility: hidden;}}
        </style>
    """, unsafe_allow_html=True)

# ==========================================
# 3. BASE DE DONNÉES
# ==========================================
data = {
    "REST_MAROC": [
        {"nom": "Dar Naji", "q": "Hassan", "maps": "https://www.google.com/maps/search/?api=1&query=Dar+Naji+Hassan+Rabat"},
        {"nom": "Les 2 Palais", "q": "Hassan", "maps": "https://www.google.com/maps/search/?api=1&query=Les+2+Palais+Rabat"}
    ],
    "REST_INT": [
        {"nom": "La Mamma", "q": "Hassan", "maps": "https://www.google.com/maps/search/?api=1&query=La+Mamma+Rabat"},
        {"nom": "Le Goeland", "q": "Centre-Ville", "maps": "https://www.google.com/maps/search/?api=1&query=Le+Goeland+Rabat"},
        {"nom": "Ty Potes", "q": "Hassan", "maps": "https://www.google.com/maps/search/?api=1&query=Ty+Potes+Rabat"},
        {"nom": "Yamal Acham", "q": "Agdal", "maps": "https://www.google.com/maps/search/?api=1&query=Yamal+Acham+Rabat"},
        {"nom": "Restaurant de la Marina", "q": "Bouregreg", "maps": "https://www.google.com/maps/search/?api=1&query=Restaurant+Marina+Rabat"}
    ],
    "REST_GASTRO": [
        {"nom": "Mr. Brochette", "q": "Hassan", "maps": "https://www.google.com/maps/search/?api=1&query=Mr+Brochette+Rabat"},
        {"nom": "Le Goethe", "q": "Agdal", "maps": "https://www.google.com/maps/search/?api=1&query=Le+Goethe+Rabat"},
        {"nom": "Boqueria Fina", "q": "Hassan", "maps": "https://www.google.com/maps/search/?api=1&query=Boqueria+Fina+Rabat"},
        {"nom": "Le Limonadier", "q": "Hassan", "maps": "https://www.google.com/maps/search/?api=1&query=Le+Limonadier+Rabat"}
    ],
    "CAFES": [
        {"nom": "Boho Café", "q": "Hassan", "maps": "https://www.google.com/maps/search/?api=1&query=Boho+Cafe+Rabat"},
        {"nom": "Workstudio", "q": "Hassan", "maps": "https://www.google.com/maps/search/?api=1&query=Workstudio+Rabat"},
        {"nom": "Moe Tea Room", "q": "Hassan", "maps": "https://www.google.com/maps/search/?api=1&query=Moe+Tea+Room+Rabat"},
        {"nom": "Renaissance", "q": "Centre-Ville", "maps": "https://www.google.com/maps/search/?api=1&query=Cafe+Renaissance+Rabat"}
    ],
    "CULTURE": [
        {"nom": "Chellah", "q": "Patrimoine", "maps": "https://www.google.com/maps/search/?api=1&query=Chellah+Rabat"},
        {"nom": "Mausolée Mohammed V", "q": "Hassan", "maps": "https://www.google.com/maps/search/?api=1&query=Mausolee+Mohammed+V+Rabat"},
        {"nom": "Kasbah des Oudayas", "q": "Oudayas", "maps": "https://www.google.com/maps/search/?api=1&query=Oudayas+Rabat"},
        {"nom": "Zoo de Rabat", "q": "Loisirs", "maps": "https://www.google.com/maps/search/?api=1&query=Zoo+Rabat"}
    ]
}

# ==========================================
# 4. INTERFACE PRINCIPALE
# ==========================================

# Langue
lang = st.radio("", ["FRANÇAIS", "ENGLISH"], horizontal=True)

# Titre
st.markdown('<h1 class="main-title">RABAT INSIDER</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Selection Privée de votre Concierge</p>', unsafe_allow_html=True)

# Catégories principales
cats = {
    "FRANÇAIS": ["ACCUEIL", "RESTAURANTS", "CAFÉS", "CULTURE & LOISIRS", "INFOS"],
    "ENGLISH": ["HOME", "RESTAURANTS", "CAFÉS", "CULTURE & LEISURE", "INFO"]
}
choice = st.selectbox("", cats[lang])

# Définition de l'arrière-plan selon le choix
bg_key = choice.split(" ")[0] # Prend le premier mot pour la clé image
set_bg(bg_key)

def render_list(items):
    for item in items:
        st.markdown(f"""
            <div class="premium-card">
                <div class="item-name">{item['nom']}</div>
                <div class="item-tag">{item['q']}</div>
            </div>
        """, unsafe_allow_html=True)
        st.link_button("ITINÉRAIRE / DIRECTIONS", item['maps'])
        st.write("")

# Logique d'affichage
if bg_key in ["ACCUEIL", "HOME"]:
    st.write("")
    st.markdown("<p style='text-align:center; color:white;'>Bienvenue à Rabat. Utilisez le menu ci-dessus pour explorer nos sélections exclusives.</p>", unsafe_allow_html=True)

elif bg_key == "RESTAURANTS":
    sub_cat = st.radio("Sélection :", ["Marocain", "International", "Gastronomique"], horizontal=True)
    if sub_cat == "Marocain":
        render_list(data["REST_MAROC"])
    elif sub_cat == "International":
        render_list(data["REST_INT"])
    else:
        render_list(data["REST_GASTRO"])

elif bg_key == "CAFÉS":
    render_list(data["CAFES"])

elif bg_key == "CULTURE":
    render_list(data["CULTURE"])

elif bg_key == "INFOS":
    st.info("🚕 **TAXIS :** Taxis bleus. Compteur obligatoire. Course : ~20-30 MAD.")
    st.info("🚋 **TRAMWAY :** Ligne 1 & 2. 6 MAD.")

# Footer
st.divider()
st.markdown("<p style='text-align:center; color:#555; font-size:0.7rem; letter-spacing:2px;'>EXCLUSIVE CONCIERGE SERVICE</p>", unsafe_allow_html=True)
