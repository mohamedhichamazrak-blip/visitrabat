import streamlit as st
import base64

# ==========================================
# 1. CONFIGURATION DE LA PAGE
# ==========================================
st.set_page_config(
    page_title="Rabat Insider | Private Concierge",
    page_icon="🇲🇦",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ==========================================
# 2. SYSTÈME DE STYLE CSS AVANCÉ (RAHAL & LUXE)
# ==========================================
def local_css():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,wght@0,400;0,700;1,400&family=Montserrat:wght@300;400;600&display=swap');

        /* Background et Overlay */
        .stApp {
            background: linear-gradient(rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0.9)), 
                        url("https://images.unsplash.com/photo-1539020140153-e479b8c22e70?auto=format&fit=crop&w=1920&q=80");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }

        /* Sidebar personnalisée */
        [data-testid="stSidebar"] {
            background-color: rgba(10, 10, 10, 0.95) !important;
            border-right: 1px solid #D4AF37;
        }

        /* Typographie */
        h1, h2, h3 {
            font-family: 'Bodoni Moda', serif !important;
            color: #D4AF37 !important;
            text-align: center;
        }

        .main-title {
            font-size: 3.5rem !important;
            letter-spacing: 5px;
            margin-bottom: 0px;
            text-transform: uppercase;
        }

        .sub-title {
            font-family: 'Montserrat', sans-serif;
            color: #D4AF37;
            text-align: center;
            letter-spacing: 4px;
            font-size: 0.7rem;
            text-transform: uppercase;
            margin-bottom: 50px;
        }

        /* Cartes Premium */
        .premium-card {
            background: rgba(26, 26, 26, 0.8);
            border: 1px solid #333;
            border-top: 3px solid #D4AF37;
            border-radius: 0px;
            padding: 0px;
            margin-bottom: 30px;
            overflow: hidden;
            transition: all 0.4s ease;
        }

        .premium-card:hover {
            border-top: 3px solid #FFFFFF;
            transform: translateY(-5px);
            box-shadow: 0 20px 40px rgba(0,0,0,0.6);
        }

        .card-content {
            padding: 20px;
        }

        .item-name {
            font-family: 'Bodoni Moda', serif;
            font-size: 1.6rem;
            color: #D4AF37;
            margin-bottom: 5px;
        }

        .item-quartier {
            font-family: 'Montserrat', sans-serif;
            font-size: 0.75rem;
            color: #888;
            letter-spacing: 2px;
            text-transform: uppercase;
            margin-bottom: 15px;
        }

        /* Images avec effet */
        .card-img {
            width: 100%;
            height: 250px;
            object-fit: cover;
            filter: grayscale(30%);
            transition: 0.5s;
        }
        .card-img:hover {
            filter: grayscale(0%);
        }

        /* Boutons personnalisés */
        .stButton>button {
            width: 100%;
            background-color: transparent !important;
            color: #D4AF37 !important;
            border: 1px solid #D4AF37 !important;
            border-radius: 0px !important;
            font-family: 'Montserrat', sans-serif !important;
            font-weight: 400 !important;
            letter-spacing: 2px;
            padding: 10px 0px !important;
            text-transform: uppercase;
            transition: 0.4s;
        }

        .stButton>button:hover {
            background-color: #D4AF37 !important;
            color: #000 !important;
            border: 1px solid #D4AF37 !important;
        }

        /* Masquage UI Streamlit */
        #MainMenu, footer, header {visibility: hidden;}
        .stSelectbox label { color: #D4AF37 !important; font-family: 'Montserrat'; letter-spacing: 1px;}
        </style>
    """, unsafe_allow_html=True)

local_css()

# ==========================================
# 3. DONNÉES ET CONTENU (BILINGUE)
# ==========================================

def get_data():
    return {
        "restaurants": [
            {
                "nom": "Mr. Brochette",
                "quartier": "Hassan",
                "img": "https://images.unsplash.com/photo-1544124499-58912cbddaad?auto=format&fit=crop&w=800&q=80",
                "maps": "https://www.google.com/maps/search/?api=1&query=Mr+Brochette+Rabat"
            },
            {
                "nom": "Dar Naji",
                "quartier": "Hassan",
                "img": "https://images.unsplash.com/photo-1541518763669-27fef04b14ea?auto=format&fit=crop&w=800&q=80",
                "maps": "https://www.google.com/maps/search/?api=1&query=Dar+Naji+Hassan+Rabat"
            },
            {
                "nom": "Ty Potes",
                "quartier": "Hassan",
                "img": "https://images.unsplash.com/photo-1550966841-3ee3ad15f0d5?auto=format&fit=crop&w=800&q=80",
                "maps": "https://www.google.com/maps/search/?api=1&query=Ty+Potes+Rabat"
            },
            {
                "nom": "Le Goethe",
                "quartier": "Centre-Ville",
                "img": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&w=800&q=80",
                "maps": "https://www.google.com/maps/search/?api=1&query=Le+Goethe+Rabat"
            },
            {
                "nom": "Boqueria Fina",
                "quartier": "Hassan",
                "img": "https://images.unsplash.com/photo-1515446134809-993c501ca304?auto=format&fit=crop&w=800&q=80",
                "maps": "https://www.google.com/maps/search/?api=1&query=Boqueria+Fina+Rabat"
            },
            {
                "nom": "Le Limonadier",
                "quartier": "Hassan",
                "img": "https://images.unsplash.com/photo-1559339352-11d035aa65de?auto=format&fit=crop&w=800&q=80",
                "maps": "https://www.google.com/maps/search/?api=1&query=Le+Limonadier+Rabat"
            },
            {
                "nom": "Yamal Acham",
                "quartier": "Agdal",
                "img": "https://images.unsplash.com/photo-1561651823-34feb02250e4?auto=format&fit=crop&w=800&q=80",
                "maps": "https://www.google.com/maps/search/?api=1&query=Yamal+Acham+Rabat"
            },
            {
                "nom": "Les 2 Palais",
                "quartier": "Hassan",
                "img": "https://images.unsplash.com/photo-1590577976322-3d2d6e213005?auto=format&fit=crop&w=800&q=80",
                "maps": "https://www.google.com/maps/search/?api=1&query=Les+2+Palais+Rabat"
            }
        ],
        "cafes": [
            {
                "nom": "Kultur Café",
                "quartier": "Hassan",
                "img": "https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?auto=format&fit=crop&w=800&q=80",
                "maps": "https://www.google.com/maps/search/?api=1&query=Kultur+Cafe+Rabat"
            },
            {
                "nom": "Workstudio",
                "quartier": "Hassan",
                "img": "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=800&q=80",
                "maps": "https://www.google.com/maps/search/?api=1&query=Workstudio+Rabat"
            },
            {
                "nom": "Bloom Coffee",
                "quartier": "Agdal",
                "img": "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?auto=format&fit=crop&w=800&q=80",
                "maps": "https://www.google.com/maps/search/?api=1&query=Bloom+Coffee+Rabat"
            },
            {
                "nom": "Moe Tea Room",
                "quartier": "Hassan",
                "img": "https://images.unsplash.com/photo-1544787210-2213d24276f7?auto=format&fit=crop&w=800&q=80",
                "maps": "https://www.google.com/maps/search/?api=1&query=Moe+Tea+Room+Rabat"
            },
            {
                "nom": "Renaissance",
                "quartier": "Centre-Ville",
                "img": "https://images.unsplash.com/photo-1554118811-1e0d58224f24?auto=format&fit=crop&w=800&q=80",
                "maps": "https://www.google.com/maps/search/?api=1&query=Cafe+Renaissance+Rabat"
            }
        ],
        "culture": [
            {"nom": "Nécropole de Chellah", "adr": "Patrimoine Mondial UNESCO", "maps": "https://www.google.com/maps/search/?api=1&query=Chellah+Rabat"},
            {"nom": "Jardins d'Essai", "adr": "Espace Botanique Royal", "maps": "https://www.google.com/maps/search/?api=1&query=Jardin+Essais+Rabat"},
            {"nom": "Rue des Consuls", "adr": "Artisanat d'Exception", "maps": "https://www.google.com/maps/search/?api=1&query=Rue+des+Consuls+Rabat"},
            {"nom": "Mausolée Mohammed V", "adr": "Chef-d'œuvre Architectural", "maps": "https://www.google.com/maps/search/?api=1&query=Mausolee+Mohammed+V+Rabat"},
            {"nom": "Musée Photographie", "adr": "Fort Rottermbourg", "maps": "https://www.google.com/maps/search/?api=1&query=Musee+Photographie+Rabat"},
            {"nom": "Corniche Rabat", "adr": "Loisirs & Océan", "maps": "https://www.google.com/maps/search/?api=1&query=Corniche+Rabat"}
        ]
    }

# ==========================================
# 4. FONCTIONS DE RENDU
# ==========================================

def render_header(lang_dict):
    st.markdown(f'<h1 class="main-title">{lang_dict["title"]}</h1>', unsafe_allow_html=True)
    st.markdown(f'<p class="sub-title">{lang_dict["tagline"]}</p>', unsafe_allow_html=True)

def render_place_card(name, quartier, image_url, maps_url, btn_text):
    st.markdown(f"""
        <div class="premium-card">
            <img src="{image_url}" class="card-img">
            <div class="card-content">
                <div class="item-name">{name}</div>
                <div class="item-quartier">{quartier}</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.link_button(btn_text, maps_url)
    st.write("")

# ==========================================
# 5. LOGIQUE PRINCIPALE
# ==========================================

def main():
    # Sidebar Setup
    with st.sidebar:
        st.markdown("<h2 style='text-align:left; font-size:1.5rem;'>CONCIERGE</h2>", unsafe_allow_html=True)
        language = st.radio("Language / Langue", ["FR", "EN"])
        st.divider()
        
        if language == "FR":
            nav_options = ["Gastronomie", "Cafés Stylés", "Culture & Patrimoine", "Informations"]
            t = {
                "title": "Rabat Insider",
                "tagline": "Private Concierge Selection",
                "select": "Veuillez choisir un univers",
                "btn": "Découvrir l'Itinéraire",
                "info_t": "Notes de Voyage",
                "taxi": "Taxis bleus : Demandez le compteur systématiquement.",
                "tram": "Tramway : Fréquence toutes les 10 min. Ticket 6 MAD."
            }
        else:
            nav_options = ["Gastronomy", "Stylish Cafés", "Culture & Heritage", "Information"]
            t = {
                "title": "Rabat Insider",
                "tagline": "Private Concierge Selection",
                "select": "Please select a category",
                "btn": "View Directions",
                "info_t": "Traveler Notes",
                "taxi": "Blue Taxis: Always request the meter to be turned on.",
                "tram": "Tramway: Runs every 10 min. Ticket is 6 MAD."
            }

    # Main Content
    render_header(t)
    category = st.selectbox(t["select"], nav_options)
    st.write("")
    
    data = get_data()

    if category in ["Gastronomie", "Gastronomy"]:
        for item in data["restaurants"]:
            render_place_card(item["nom"], item["quartier"], item["img"], item["maps"], t["btn"])

    elif category in ["Cafés Stylés", "Stylish Cafés"]:
        for item in data["cafes"]:
            render_place_card(item["nom"], item["quartier"], item["img"], item["maps"], t["btn"])

    elif category in ["Culture & Patrimoine", "Culture & Heritage"]:
        for item in data["culture"]:
            render_place_card(item["nom"], item["adr"], "https://images.unsplash.com/photo-1548013146-72479768bbaa?auto=format&fit=crop&w=800&q=80", item["maps"], t["btn"])

    elif category in ["Informations", "Information"]:
        st.markdown(f"### {t['info_t']}")
        st.success(t["taxi"])
        st.info(t["tram"])
        
    # Footer Premium
    st.write("")
    st.write("")
    st.markdown("<p style='text-align:center; color:#555; font-size:0.6rem; letter-spacing:3px;'>EXCLUSIVE SERVICE BY RABAT INSIDER © 2026</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
