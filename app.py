import streamlit as st

# ==========================================
# 1. CONFIGURATION DE LA PAGE
# ==========================================
st.set_page_config(
    page_title="Rabat Insider | Private Concierge",
    page_icon="🇲🇦",
    layout="centered"
)

# ==========================================
# 2. LOGIQUE D'ARRIÈRE-PLAN ET STYLE AVANCÉ
# ==========================================
bg_images = {
    "ACCUEIL": "https://images.unsplash.com/photo-1539020140153-e479b8c22e70?auto=format&fit=crop&w=1920&q=80",
    "RESTAURANTS": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?auto=format&fit=crop&w=1920&q=80",
    "CAFÉS": "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?auto=format&fit=crop&w=1920&q=80",
    "CULTURE": "https://images.unsplash.com/photo-1548013146-72479768bbaa?auto=format&fit=crop&w=1920&q=80",
    "INFOS": "https://images.unsplash.com/photo-1506012733851-46297839fa01?auto=format&fit=crop&w=1920&q=80"
}

def apply_ultra_luxe_css(category_key):
    img_url = bg_images.get(category_key, bg_images["ACCUEIL"])
    st.markdown(f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Montserrat:wght@300;400;600&display=swap');

        .stApp {{
            background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.85)), 
                        url("{img_url}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}

        /* Barre de Langue Ultra-Visible */
        .lang-container {{
            background: rgba(0, 0, 0, 0.6);
            border: 1px solid #D4AF37;
            padding: 15px;
            text-align: center;
            margin-bottom: 25px;
            border-radius: 4px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.5);
        }}

        .main-title {{
            font-family: 'Cinzel', serif;
            color: #D4AF37;
            text-align: center;
            font-size: 3rem;
            letter-spacing: 7px;
            margin-bottom: 0px;
            text-shadow: 2px 2px 10px rgba(0,0,0,0.8);
        }}

        .sub-title {{
            font-family: 'Montserrat', sans-serif;
            color: #FFFFFF;
            text-align: center;
            letter-spacing: 5px;
            font-size: 0.8rem;
            text-transform: uppercase;
            margin-bottom: 40px;
            opacity: 0.9;
        }}

        /* Cartes Premium */
        .premium-card {{
            background-color: rgba(15, 15, 15, 0.92);
            padding: 25px;
            border-left: 4px solid #D4AF37;
            margin-bottom: 5px;
            border-radius: 0px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.6);
        }}

        .item-name {{
            font-family: 'Cinzel', serif;
            font-size: 1.4rem;
            color: #D4AF37;
            letter-spacing: 1px;
        }}

        .item-tag {{
            font-family: 'Montserrat', sans-serif;
            font-size: 0.7rem;
            color: #AAA;
            letter-spacing: 2px;
            text-transform: uppercase;
            margin-bottom: 10px;
        }}

        /* Boutons de navigation et Maps */
        .stButton>button {{
            width: 100%;
            background-color: transparent !important;
            color: #D4AF37 !important;
            border: 1px solid #D4AF37 !important;
            border-radius: 0px !important;
            text-transform: uppercase;
            letter-spacing: 2px;
            font-family: 'Montserrat', sans-serif;
            font-weight: 600;
            transition: 0.4s;
        }}
        .stButton>button:hover {{
            background-color: #D4AF37 !important;
            color: #000 !important;
        }}

        .stRadio label, .stSelectbox label {{
            color: #D4AF37 !important;
            font-family: 'Montserrat', sans-serif;
            font-weight: 600;
            font-size: 0.9rem;
        }}

        #MainMenu, footer, header {{visibility: hidden;}}
        </style>
    """, unsafe_allow_html=True)

# ==========================================
# 3. BASE DE DONNÉES MISE À JOUR
# ==========================================
data = {
    "REST_MAROC": [
        {"nom": "Mr. Brochette", "q": "Hassan", "maps": "https://www.google.com/maps/search/?api=1&query=Mr+Brochette+Rabat"},
        {"nom": "Dar Naji", "q": "Hassan", "maps": "https://www.google.com/maps/search/?api=1&query=Dar+Naji+Hassan+Rabat"},
        {"nom": "Les 2 Palais", "q": "Hassan", "maps": "https://www.google.com/maps/search/?api=1&query=Les+2+Palais+Rabat"}
    ],
    "REST_INT": [
        {"nom": "La Mamma", "q": "Hassan", "maps": "https://www.google.com/maps/search/?api=1&query=La+Mamma+Rabat"},
        {"nom": "Le Goethe", "q": "Centre-Ville", "maps": "https://www.google.com/maps/search/?api=1&query=Le+Goethe+Rabat"},
        {"nom": "Ty Potes", "q": "Hassan", "maps": "https://www.google.com/maps/search/?api=1&query=Ty+Potes+Rabat"},
        {"nom": "Yamal Acham", "q": "Agdal", "maps": "https://www.google.com/maps/search/?api=1&query=Yamal+Acham+Rabat"}
    ],
    "REST_GASTRO": [
        {"nom": "Le Goeland", "q": "Centre-Ville", "maps": "https://www.google.com/maps/search/?api=1&query=Le+Goeland+Rabat"},
        {"nom": "Restaurant de la Marina", "q": "Bouregreg", "maps": "https://www.google.com/maps/search/?api=1&query=Restaurant+Marina+Rabat"},
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
        {"nom": "Nécropole de Chellah", "q": "Patrimoine", "maps": "https://www.google.com/maps/search/?api=1&query=Chellah+Rabat"},
        {"nom": "Mausolée Mohammed V & Tour Hassan", "q": "Hassan", "maps": "https://www.google.com/maps/search/?api=1&query=Mausolee+Mohammed+V+Rabat"},
        {"nom": "Kasbah des Oudayas", "q": "Oudayas", "maps": "https://www.google.com/maps/search/?api=1&query=Oudayas+Rabat"},
        {"nom": "Jardins d'Essai Botaniques", "q": "Agdal", "maps": "https://www.google.com/maps/search/?api=1&query=Jardin+Essais+Rabat"},
        {"nom": "Musée National de la Photographie", "q": "Fort Rottermbourg", "maps": "https://www.google.com/maps/search/?api=1&query=Musee+Photographie+Rabat"},
        {"nom": "Allée Mahaj", "q": "Hay Riad", "maps": "https://www.google.com/maps/search/?api=1&query=Mahaj+Riad+Rabat"},
        {"nom": "La Corniche de Rabat", "q": "L'Océan", "maps": "https://www.google.com/maps/search/?api=1&query=Corniche+Rabat"},
        {"nom": "Zoo National de Rabat", "q": "Loisirs", "maps": "https://www.google.com/maps/search/?api=1&query=Zoo+Rabat"},
        {"nom": "Activités Nautiques / Surf", "q": "Plage de Rabat", "maps": "https://www.google.com/maps/search/?api=1&query=Surf+Rabat"}
    ]
}

# ==========================================
# 4. LOGIQUE D'AFFICHAGE
# ==========================================

# Barre de Langue stylisée pour une visibilité maximale
st.markdown('<div class="lang-container">', unsafe_allow_html=True)
lang = st.radio("SÉLECTIONNEZ VOTRE LANGUE / SELECT YOUR LANGUAGE", ["FRANÇAIS", "ENGLISH"], horizontal=True)
st.markdown('</div>', unsafe_allow_html=True)

# Titre
st.markdown('<h1 class="main-title">RABAT INSIDER</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Selection Privée de votre Concierge</p>', unsafe_allow_html=True)

# Menu principal
cats = {
    "FRANÇAIS": ["ACCUEIL", "RESTAURANTS", "CAFÉS", "CULTURE & LOISIRS", "INFOS"],
    "ENGLISH": ["HOME", "RESTAURANTS", "CAFÉS", "CULTURE & LEISURE", "INFO"]
}
choice = st.selectbox("", cats[lang])

# Application du CSS et du Background dynamique
bg_key = choice.split(" ")[0]
apply_ultra_luxe_css(bg_key)

def render_list(items):
    btn_txt = "VOIR L'ITINÉRAIRE" if lang == "FRANÇAIS" else "GET DIRECTIONS"
    for item in items:
        st.markdown(f"""
            <div class="premium-card">
                <div class="item-name">{item['nom']}</div>
                <div class="item-tag">{item['q']}</div>
            </div>
        """, unsafe_allow_html=True)
        st.link_button(btn_txt, item['maps'])
        st.write("")

# Navigation de contenu
if bg_key in ["ACCUEIL", "HOME"]:
    st.write("")
    msg = "Bienvenue. Découvrez l'exceptionnel à travers notre sélection exclusive pour nos invités." if lang == "FRANÇAIS" else "Welcome. Discover the exceptional through our exclusive selection for our guests."
    st.markdown(f"<p style='text-align:center; color:white; font-size:1.2rem; font-style:italic; padding: 20px;'>{msg}</p>", unsafe_allow_html=True)

elif bg_key == "RESTAURANTS":
    options = ["Marocain", "International", "Gastronomique"] if lang == "FRANÇAIS" else ["Moroccan", "International", "Fine Dining"]
    sub_cat = st.radio("CATÉGORIE :", options, horizontal=True)
    
    if "Maroc" in sub_cat or "Moroccan" in sub_cat:
        render_list(data["REST_MAROC"])
    elif "Internat" in sub_cat:
        render_list(data["REST_INT"])
    else:
        render_list(data["REST_GASTRO"])

elif bg_key == "CAFÉS":
    render_list(data["CAFES"])

elif bg_key == "CULTURE":
    render_list(data["CULTURE"])

elif bg_key == "INFOS":
    st.info("🚕 **TAXIS :** Les petits taxis bleus sont très pratiques. Demandez le compteur. Course moyenne : 20-30 MAD.")
    st.info("🚋 **TRAMWAY :** Le réseau est moderne et propre. Lignes 1 & 2. Ticket : 6 MAD.")

# Pied de page
st.divider()
st.markdown("<p style='text-align:center; color:#666; font-size:0.7rem; letter-spacing:2px;'>EXCLUSIVE CONCIERGE SERVICE • RABAT 2026</p>", unsafe_allow_html=True)
