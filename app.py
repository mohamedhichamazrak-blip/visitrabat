import streamlit as st

# ==========================================
# 1. CONFIGURATION ET DESIGN (CSS Custom)
# ==========================================
st.set_page_config(page_title="Rabat Insider", page_icon="🇲🇦", layout="centered")

# Injection de CSS pour un look "App Premium" (Coins arrondis, typographie)
st.markdown("""
    <style>
    .stImage img {
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        object-fit: cover;
    }
    .quartier-tag {
        color: #7b8a8b;
        font-size: 0.9em;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. EN-TÊTE
# ==========================================
st.title("📍 Rabat Insider")
st.markdown("*L'expérience d'une conciergerie privée dans votre poche.*")
st.divider()

# ==========================================
# 3. BASE DE DONNÉES LOCALE (Dictionnaires)
# ==========================================
# L'avantage de cette structure : tu peux rajouter des lieux en 2 secondes.

lieux_diner = [
    {
        "nom": "Dar Naji",
        "quartier": "Hassan",
        "image": "https://images.unsplash.com/photo-1585937421612-70a008356fbe?auto=format&fit=crop&w=800&q=80",
        "desc": "L'incontournable pour une pastilla ou un tajine authentique. L'ambiance est vivante, le service en tenue traditionnelle, parfait pour une immersion totale après une balade au centre-ville.",
        "budget": "Moyen 💰💰",
        "maps": "https://www.google.com/maps/search/?api=1&query=Dar+Naji+Hassan+Rabat",
        "wa": "https://wa.me/212600000000?text=Réservation%20Rabat%20Insider"
    },
    {
        "nom": "Ty Potes",
        "quartier": "Hassan",
        "image": "https://images.unsplash.com/photo-1514933651103-005eec06c04b?auto=format&fit=crop&w=800&q=80",
        "desc": "Un bistrot/crêperie à l'ambiance 'Smart Casual'. Parfait pour un dîner élégant mais décontracté dans un magnifique jardin caché. La clientèle y est très cosmopolite.",
        "budget": "Moyen-Élevé 💰💰💰",
        "maps": "https://www.google.com/maps/search/?api=1&query=Ty+Potes+Rabat",
        "wa": "https://wa.me/212600000000?text=Réservation%20Rabat%20Insider"
    },
    {
        "nom": "Le Dhow",
        "quartier": "Bouregreg / Oudayas",
        "image": "https://images.unsplash.com/photo-1544465544-1b71aee9dfa3?auto=format&fit=crop&w=800&q=80",
        "desc": "Un bateau en bois majestueux amarré sur le fleuve. Profitez d'une cuisine internationale avec la meilleure vue possible sur la Kasbah au coucher du soleil.",
        "budget": "Élevé 💰💰💰💰",
        "maps": "https://www.google.com/maps/search/?api=1&query=Le+Dhow+Rabat",
        "wa": "https://wa.me/212600000000?text=Réservation%20Rabat%20Insider"
    },
    {
        "nom": "Yamal Acham",
        "quartier": "Agdal",
        "image": "https://images.unsplash.com/photo-1528605248644-14dd04022da1?auto=format&fit=crop&w=800&q=80",
        "desc": "Une institution pour la cuisine levantine et syrienne. Les mezzés sont exceptionnels et l'endroit est toujours prisé par les fins gourmets locaux.",
        "budget": "Moyen 💰💰",
        "maps": "https://www.google.com/maps/search/?api=1&query=Yamal+Acham+Agdal+Rabat",
        "wa": "https://wa.me/212600000000?text=Réservation%20Rabat%20Insider"
    }
]

lieux_cafe = [
    {
        "nom": "Café Maure",
        "quartier": "Oudayas",
        "desc": "Un thé à la menthe et des pâtisseries avec une vue vertigineuse sur l'océan et Salé. Historique et poétique.",
        "maps": "https://www.google.com/maps/search/?api=1&query=Cafe+Maure+Oudayas+Rabat"
    },
    {
        "nom": "Le Rooftop du The View",
        "quartier": "Agdal",
        "desc": "Le point culminant de la ville. Une atmosphère premium et design pour siroter un verre en regardant Rabat s'illuminer.",
        "maps": "https://www.google.com/maps/search/?api=1&query=The+View+Hotel+Rabat"
    },
    {
        "nom": "La Tour Hassan Lounge",
        "quartier": "Hassan",
        "desc": "Un cadre feutré et luxueux. L'endroit idéal pour un rendez-vous calme, un moment de lecture ou une conversation posée.",
        "maps": "https://www.google.com/maps/search/?api=1&query=La+Tour+Hassan+Palace+Rabat"
    },
    {
        "nom": "Café 7ème Art",
        "quartier": "Hassan",
        "desc": "Le repaire des artistes et des intellectuels r'batis, niché dans une petite forêt en plein centre. Très agréable l'après-midi.",
        "maps": "https://www.google.com/maps/search/?api=1&query=Cafe+7eme+Art+Rabat"
    }
]

lieux_visite = [
    {"nom": "La Nécropole du Chellah", "maps": "https://www.google.com/maps/search/?api=1&query=Chellah+Rabat", "desc": "Notre conseil : la lumière de 16h30 y est magique pour les photos, entre ruines romaines et végétation."},
    {"nom": "Le MMVI (Musée d'Art Moderne)", "maps": "https://www.google.com/maps/search/?api=1&query=MMVI+Rabat", "desc": "Une architecture superbe et des expositions souvent de calibre international. Parfait pour une matinée culturelle."},
    {"nom": "Jardin d'Essais Botaniques", "maps": "https://www.google.com/maps/search/?api=1&query=Jardin+d+Essais+Botaniques+Rabat", "desc": "Un havre de paix secret en plein Agdal. Idéal pour une promenade digestive loin du bruit des voitures."},
    {"nom": "La Rue des Consuls", "maps": "https://www.google.com/maps/search/?api=1&query=Rue+des+Consuls+Rabat", "desc": "Pour un shopping artisanal de très haute qualité (tapis, cuir, bijoux) sans l'insistance étouffante d'autres villes."}
]

# ==========================================
# 4. NAVIGATION ET AFFICHAGE INTERACTIF
# ==========================================
categorie = st.selectbox(
    "Que souhaitez-vous découvrir ?",
    ("🍽️ Où dîner ce soir ?", "☕ Cafés & Rooftops", "📸 Visites & Culture", "💡 Pratique & Transports")
)
st.write("") # Espace visuel

if categorie == "🍽️ Où dîner ce soir ?":
    for lieu in lieux_diner:
        # Utilisation d'un container pour bien séparer chaque restaurant
        with st.container():
            st.markdown(f"### {lieu['nom']}")
            st.markdown(f"<p class='quartier-tag'>📍 Quartier : {lieu['quartier']}</p>", unsafe_allow_html=True)
            st.image(lieu['image'], use_column_width=True)
            st.write(lieu['desc'])
            st.write(f"**{lieu['budget']}**")
            
            c1, c2 = st.columns(2)
            with c1:
                st.link_button("💬 Réserver (WhatsApp)", lieu['wa'], use_container_width=True)
            with c2:
                st.link_button("🗺️ Itinéraire (Maps)", lieu['maps'], use_container_width=True)
            st.divider()

elif categorie == "☕ Cafés & Rooftops":
    st.image("https://images.unsplash.com/photo-1557006021-b85faa2bc5e2?auto=format&fit=crop&w=800&q=80", use_column_width=True)
    st.write("Rabat possède une véritable culture du café. Voici nos spots de prédilection.")
    st.write("")
    for lieu in lieux_cafe:
        with st.expander(f"✨ {lieu['nom']} ({lieu['quartier']})"):
            st.write(lieu['desc'])
            st.link_button("🗺️ S'y rendre", lieu['maps'])

elif categorie == "📸 Visites & Culture":
    st.image("https://images.unsplash.com/photo-1539020140153-e479b8c22e70?auto=format&fit=crop&w=800&q=80", caption="Architecture andalouse typique", use_column_width=True)
    for visite in lieux_visite:
        st.subheader(visite['nom'])
        st.write(visite['desc'])
        st.link_button("📍 Localiser", visite['maps'])
        st.write("---")

elif categorie == "💡 Pratique & Transports":
    st.subheader("Se déplacer à Rabat")
    st.info("🚕 **Petits Taxis (Bleus) :** Demandez le compteur. Une course en ville coûte généralement entre 15 et 25 MAD. Indispensable pour rejoindre Hassan depuis l'Agdal.")
    st.info("🚋 **Tramway :** Très propre et ponctuel (6 MAD le ticket). Idéal pour longer le centre-ville sans subir les embouteillages.")
    
    st.subheader("Urgences & Santé")
    st.error("🚓 **Police :** 19 | 🚒 **Pompiers/Ambulance :** 15")
    st.success("💊 **Pharmacies :** Les officines sont nombreuses. La nuit et les dimanches, un système de garde très efficace prend le relais.")
    st.link_button("Rechercher la pharmacie de garde du jour", "https://www.telecontact.ma/pharmacies-de-garde/rabat.php")

# ==========================================
# 5. PIED DE PAGE
# ==========================================
st.write("")
st.caption("© 2026 Rabat Insider - Conciergerie Digitale pour Hôtellerie Indépendante.")
