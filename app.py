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
# 2. CSS AVANCÉ POUR LA VISIBILITÉ ET LES BOUTONS
# ==========================================
def apply_premium_ui(category_key, bg_url):
    st.markdown(f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Montserrat:wght@400;600&display=swap');

        /* Fond avec overlay plus sombre pour protéger la lecture */
        .stApp {{
            background: linear-gradient(rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0.85)), 
                        url("{bg_url}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}

        /* Bandeau Header pour protéger le titre et la langue */
        .header-box {{
            background: rgba(0, 0, 0, 0.6);
            padding: 30px;
            border-radius: 15px;
            border: 1px solid rgba(212, 175, 55, 0.3);
            text-align: center;
            margin-bottom: 30px;
            backdrop-filter: blur(10px);
        }}

        .main-title {{
            font-family: 'Cinzel', serif;
            color: #D4AF37 !important;
            font-size: 3.2rem !important;
            letter-spacing: 5px;
            margin: 0;
            text-shadow: 0px 4px 10px rgba(0,0,0,1);
        }}

        /* Style des "Cases" de sélection (Boutons Streamlit détournés) */
        div.stButton > button {{
            background-color: rgba(20, 20, 20, 0.9) !important;
            color: #D4AF37 !important;
            border: 1px solid #D4AF37 !important;
            border-radius: 0px !important;
            height: 60px !important;
            font-family: 'Montserrat', sans-serif !important;
            font-weight: 600 !important;
            text-transform: uppercase !important;
            letter-spacing: 2px !important;
            transition: all 0.3s ease !important;
            margin-bottom: 10px !important;
        }}

        div.stButton > button:hover {{
            background-color: #D4AF37 !important;
            color: #000 !important;
            border: 1px solid #D4AF37 !important;
        }}

        /* Cartes de lieux encore plus lisibles */
        .place-card {{
            background-color: rgba(255, 255, 255, 0.05);
            padding: 25px;
            border-left: 5px solid #D4AF37;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            margin-bottom: 5px;
            backdrop-filter: blur(5px);
        }}

        .item-name {{
            font-family: 'Cinzel', serif;
            font-size: 1.6rem;
            color: #D4AF37;
            margin-bottom: 5px;
        }}

        .item-tag {{
            font-family: 'Montserrat', sans-serif;
            font-size: 0.8rem;
            color: #FFF;
            opacity: 0.8;
            letter-spacing: 2px;
            text-transform: uppercase;
        }}

        /* Customization des widgets standards */
        .stSelectbox label, .stRadio label {{
            color: #FFF !important;
            font-weight: 600 !important;
            background: rgba(0,0,0,0.4);
            padding: 5px 15px;
            border-radius: 5px;
        }}

        #MainMenu, footer, header {{visibility: hidden;}}
        </style>
    """, unsafe_allow_html=True)

# ==========================================
# 3. GESTION DES IMAGES ET TRADUCTIONS
# ==========================================
bg_images = {
    "ACCUEIL": "https://images.unsplash.com/photo-1539020140153-e479b8c22e70?auto=format&fit=crop&w=1920&q=80",
    "RESTAURANTS": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?auto=format&fit=crop&w=1920&q=80",
    "CAFÉS": "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?auto=format&fit=crop&w=1920&q=80",
    "CULTURE": "https://images.unsplash.com/photo-1548013146-72479768bbaa?auto=format&fit=crop&w=1920&q=80",
    "INFOS": "https://images.unsplash.com/photo-1506012733851-46297839fa01?auto=format&fit=crop&w=1920&q=80"
}

# Base de données complète
db = {
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
        {"nom": "Mausolée Mohammed V", "q": "Hassan", "maps": "https://www.google.com/maps/search/?api=1&query=Mausolee+Mohammed+V+Rabat"},
        {"nom": "Kasbah des Oudayas", "q": "Oudayas", "maps": "https://www.google.com/maps/search/?api=1&query=Oudayas+Rabat"},
        {"nom": "Jardins d'Essai Botaniques", "q": "Agdal", "maps": "https://www.google.com/maps/search/?api=1&query=Jardin+Essais+Rabat"},
        {"nom": "Musée de la Photographie", "q": "Fort Rottermbourg", "maps": "https://www.google.com/maps/search/?api=1&query=Musee+Photographie+Rabat"},
        {"nom": "Allée Mahaj", "q": "Hay Riad", "maps": "https://www.google.com/maps/search/?api=1&query=Mahaj+Riad+Rabat"},
        {"nom": "La Corniche de Rabat", "q": "L'Océan", "maps": "https://www.google.com/maps/search/?api=1&query=Corniche+Rabat"},
        {"nom": "Zoo National de Rabat", "q": "Loisirs", "maps": "https://www.google.com/maps/search/?api=1&query=Zoo+Rabat"},
        {"nom": "Activités Nautiques / Surf", "q": "Plage de Rabat", "maps": "https://www.google.com/maps/search/?api=1&query=Surf+Rabat"}
    ]
}

# ==========================================
# 4. EXÉCUTION DE L'INTERFACE
# ==========================================

# HEADER FIXE POUR VISIBILITÉ
st.markdown('<div class="header-box">', unsafe_allow_html=True)
st.markdown('<h1 class="main-title">RABAT INSIDER</h1>', unsafe_allow_html=True)

# SELECTION DE LANGUE (Boutons rectangulaires visibles)
lang_col1, lang_col2 = st.columns(2)
with lang_col1:
    if st.button("FRANÇAIS 🇫🇷"): st.session_state.lang = "FR"
with lang_col2:
    if st.button("ENGLISH 🇬🇧"): st.session_state.lang = "EN"

if 'lang' not in st.session_state: st.session_state.lang = "FR"
lang = st.session_state.lang
st.markdown('</div>', unsafe_allow_html=True)

# MENU PRINCIPAL (Catégories)
cats = {
    "FR": ["ACCUEIL", "RESTAURANTS", "CAFÉS", "CULTURE & LOISIRS", "INFOS"],
    "EN": ["HOME", "RESTAURANTS", "CAFÉS", "CULTURE & LEISURE", "INFO"]
}
choice = st.selectbox("", cats[lang])

# Background dynamique
bg_key = choice.split(" ")[0]
apply_premium_ui(bg_key, bg_images.get(bg_key, bg_images["ACCUEIL"]))

# FONCTION D'AFFICHAGE DES LISTES
def render_list(items):
    btn_txt = "VOIR L'ITINÉRAIRE" if lang == "FR" else "GET DIRECTIONS"
    for item in items:
        st.markdown(f"""
            <div class="place-card">
                <div class="item-name">{item['nom']}</div>
                <div class="item-tag">{item['q']}</div>
            </div>
        """, unsafe_allow_html=True)
        st.link_button(btn_txt, item['maps'])
        st.write("")

# LOGIQUE DE CONTENU
if bg_key in ["ACCUEIL", "HOME"]:
    st.write("")
    msg = "Bienvenue. Découvrez l'exceptionnel à Rabat." if lang == "FR" else "Welcome. Discover the exceptional in Rabat."
    st.markdown(f"<p style='text-align:center; color:white; font-size:1.5rem; font-style:italic;'>{msg}</p>", unsafe_allow_html=True)

elif bg_key == "RESTAURANTS":
    st.markdown("### " + ("TYPE DE CUISINE :" if lang == "FR" else "CUISINE TYPE :"))
    # CASES POUR GASTRONOMIE
    c1, c2, c3 = st.columns(3)
    with c1: 
        if st.button("MAROCAIN" if lang == "FR" else "MOROCCAN"): st.session_state.sub = "MAROC"
    with c2: 
        if st.button("INTERNATIONAL"): st.session_state.sub = "INT"
    with c3: 
        if st.button("GASTRONOMIQUE" if lang == "FR" else "FINE DINING"): st.session_state.sub = "GASTRO"

    if 'sub' not in st.session_state: st.session_state.sub = "MAROC"
    render_list(db[f"REST_{st.session_state.sub}"])

elif bg_key == "CAFÉS":
    render_list(db["CAFES"])

elif bg_key == "CULTURE":
    render_list(db["CULTURE"])

elif bg_key == "INFOS":
    st.info("🚕 **TAXIS :** Bleus. Compteur obligatoire.")
    st.info("🚋 **TRAMWAY :** Lignes 1 & 2. 6 MAD.")

st.divider()
st.caption("EXCLUSIVE CONCIERGE SERVICE • RABAT 2026")
