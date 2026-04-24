import streamlit as st
import pandas as pd

# ------------------ CONFIG ------------------
st.set_page_config(page_title="Instacart Dashboard", layout="wide")

# ------------------ STYLE ------------------
st.markdown("""
<style>

/* Sidebar padding */
section[data-testid="stSidebar"] > div {
    padding-left: 10px !important;
    padding-right: 10px !important;
}

/* Sidebar buttons */
section[data-testid="stSidebar"] button {
    width: 100% !important;
    height: 48px !important;
    border-radius: 10px !important;
    margin-bottom: 8px !important;
    border: none !important;
    text-align: left !important;
    padding-left: 14px !important;
    font-size: 14px !important;
    background-color: #1e1e1e !important;
    color: white !important;
}

/* hover */
section[data-testid="stSidebar"] button:hover {
    background-color: #333 !important;
}

/* active */
section[data-testid="stSidebar"] button[kind="primary"] {
    background-color: #4CAF50 !important;
    font-weight: bold !important;
    border-left: 4px solid #00ff99 !important;
}

/* cards */
.card {
    background-color: #1e1e1e;
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 10px;
}

</style>
""", unsafe_allow_html=True)

# ------------------ STATE ------------------
if "page" not in st.session_state:
    st.session_state.page = "Home"

if "data_loaded" not in st.session_state:
    st.session_state.data_loaded = False

if "features_ready" not in st.session_state:
    st.session_state.features_ready = False

if "clusters_ready" not in st.session_state:
    st.session_state.clusters_ready = False


# ------------------ NAVIGATION ------------------
menu_sections = {
    "📂 Data": {
        "📥 Upload Data": "Data Source",
        "⚙️ Preprocessing": "Preprocessing",
    },
    "📊 Analysis": {
        "🧩 Clustering": "Clustering (KMeans)",
        "📉 PCA": "Dimensionality Reduction (PCA)",
        "🛒 Association Rules": "Association Rules",
    },
    "📈 Results": {
        "🎯 Recommendations": "Recommendation System",
        "📊 Dashboard": "Results Dashboard",
    }
}

# ------------------ SIDEBAR ------------------
st.sidebar.markdown("## 🧭 Navigation")
st.sidebar.markdown("---")

# Home
if st.sidebar.button("🏠 Home", type="primary" if st.session_state.page == "Home" else "secondary"):
    st.session_state.page = "Home"
    st.rerun()

st.sidebar.markdown("---")

# Sections
for section, items in menu_sections.items():
    st.sidebar.markdown(f"### {section}")

    for label, value in items.items():
        is_active = (st.session_state.page == value)

        if is_active:
            st.sidebar.button(label, key=value, type="primary")
        else:
            if st.sidebar.button(label, key=value):
                st.session_state.page = value
                st.rerun()

    st.sidebar.markdown("---")

page = st.session_state.page


# ------------------ HOME ------------------
if page == "Home":

    st.markdown("""
    <h1 style='text-align:center;'>🛒 Instacart Data Mining System</h1>
    <p style='text-align:center; color:gray;'>Clustering • PCA • Market Basket • Recommendation</p>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### 📊 System Overview")

    col1, col2, col3, col4 = st.columns(4)
    col1.markdown("### 🧩\nClustering")
    col2.markdown("### 📉\nPCA")
    col3.markdown("### 🛒\nRules")
    col4.markdown("### 🎯\nRecommendation")

    st.markdown("### 🚀 What this system does")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="card">✔ Segment customers</div>', unsafe_allow_html=True)
        st.markdown('<div class="card">✔ Discover buying patterns</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">✔ Visualize with PCA</div>', unsafe_allow_html=True)
        st.markdown('<div class="card">✔ Recommend products</div>', unsafe_allow_html=True)

    if st.button("🚀 Start Analysis"):
        st.session_state.page = "Data Source"
        st.rerun()


# ------------------ DATA SOURCE ------------------
elif page == "Data Source":

    st.title("📂 Load Dataset")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.file_uploader("orders.csv")

    with col2:
        st.file_uploader("products.csv")

    with col3:
        st.file_uploader("order_products__prior.csv")

    if st.button("Simulate Load"):
        st.session_state.data_loaded = True
        st.success("Dataset loaded successfully")


# ------------------ PREPROCESSING ------------------
elif page == "Preprocessing":

    st.title("⚙️ Preprocessing")

    if not st.session_state.data_loaded:
        st.warning("Load data first")
        st.stop()

    col1, col2, col3 = st.columns(3)

    col1.info("Missing Values")
    col2.info("Encoding")
    col3.info("Scaling")

    if st.button("Generate Features"):
        st.session_state.features_ready = True
        st.success("Features ready")


# ------------------ CLUSTERING ------------------
elif page == "Clustering (KMeans)":

    st.title("🧩 Clustering")

    if not st.session_state.features_ready:
        st.warning("Run preprocessing first")
        st.stop()

    if st.button("Run Clustering"):
        st.session_state.clusters_ready = True
        st.success("Clusters generated")


# ------------------ PCA ------------------
elif page == "Dimensionality Reduction (PCA)":

    st.title("📉 PCA")

    if not st.session_state.features_ready:
        st.warning("Run preprocessing first")
        st.stop()

    st.info("PCA visualization will be shown here")


# ------------------ ASSOCIATION RULES ------------------
elif page == "Association Rules":

    st.title("🛒 Association Rules")

    if not st.session_state.data_loaded:
        st.warning("Load data first")
        st.stop()

    st.subheader("Frequent Itemsets")
    st.markdown('<div class="card">Itemsets table will appear here</div>', unsafe_allow_html=True)

    st.subheader("Rules")
    st.markdown('<div class="card">Support • Confidence • Lift</div>', unsafe_allow_html=True)


# ------------------ RECOMMENDATION ------------------
elif page == "Recommendation System":

    st.title("🎯 Recommendation System")

    if not st.session_state.clusters_ready:
        st.warning("Run clustering first")
        st.stop()

    st.markdown('<div class="card">Recommendations per segment</div>', unsafe_allow_html=True)


# ------------------ RESULTS ------------------
elif page == "Results Dashboard":

    st.title("📊 Results Dashboard")

    if not st.session_state.clusters_ready:
        st.warning("Complete analysis first")
        st.stop()

    col1, col2 = st.columns(2)

    col1.markdown('<div class="card">Cluster Plot</div>', unsafe_allow_html=True)
    col2.markdown('<div class="card">PCA Plot</div>', unsafe_allow_html=True)

    st.markdown("---")

    st.subheader("🧠 Insights")
    st.markdown('<div class="card">Cluster 1: High value customers</div>', unsafe_allow_html=True)
    st.markdown('<div class="card">Cluster 2: Low engagement customers</div>', unsafe_allow_html=True)

    st.markdown("---")

    st.subheader("🎯 Recommendations")
    st.markdown('<div class="card">Product suggestions based on segment</div>', unsafe_allow_html=True)

    st.markdown("---")

    st.subheader("📋 Tables")
    st.markdown('<div class="card">Final data tables</div>', unsafe_allow_html=True)