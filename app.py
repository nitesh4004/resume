import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
from PIL import Image
import folium
from streamlit_folium import st_folium

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Nitesh Kumar | Geospatial Data Scientist",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- CSS STYLING WITH HELVETICA FONT ---
st.markdown("""
<style>
    /* Apply Font to Whole App */
    html, body, [class*="css"] {
        font-family: 'Helvetica', 'Arial', sans-serif;
    }
    
    /* Header Styling - Bolder and Spaced */
    h1, h2, h3 {
        font-family: 'Helvetica', 'Arial', sans-serif;
        font-weight: 700;
        letter-spacing: 0.5px;
        text-transform: uppercase;
    }
    
    /* Body Text Styling */
    p, div, li, .stMarkdown {
        font-family: 'Helvetica', 'Arial', sans-serif;
        font-weight: 400;
        font-size: 1.05rem; 
    }

    /* Button Styling */
    .stButton button {
        width: 100%;
        font-family: 'Helvetica', 'Arial', sans-serif;
        font-weight: 600;
        letter-spacing: 1px;
        text-transform: uppercase;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        font-family: 'Helvetica', 'Arial', sans-serif;
    }

    /* Reduce padding at top */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* Profile Image styling */
    img {
        border-radius: 50%; 
        border: 3px solid #00796B; /* Teal border */
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    # Placeholder for profile image
    # st.image("profile.jpg", width=150) 
    
    st.markdown("## Nitesh Kumar")
    st.markdown("📍 *Mumbai, India*")
    st.caption("Geospatial Data Scientist | Agri-Tech Specialist")
    
    # Navigation Menu
    selected = option_menu(
        menu_title=None,
        options=["Home", "Experience", "Projects", "Skills", "Education", "Contact"],
        icons=["house", "briefcase", "rocket", "tools", "book", "envelope"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {
                "padding": "0!important", 
                "background-color": "#262730"
            },
            "icon": {
                "color": "#4DB6AC",
                "font-size": "18px"
            }, 
            "nav-link": {
                "font-family": "Helvetica, Arial, sans-serif",
                "font-size": "16px", 
                "text-align": "left", 
                "margin":"0px", 
                "color": "white", 
            },
            "nav-link-selected": {
                "background-color": "#00796B"
            }, 
        }
    )
    
    st.markdown("---")
    st.write("### 🔗 Connect")
    st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/nitesh4004)")
    st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/nitesh4004)")
    st.markdown("[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:nitesh.gulzar@gmail.com)")

# --- SECTION: HOME ---
if selected == "Home":
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.title("HELLO, I'M NITESH! 👋")
        st.subheader("GEOSPATIAL DATA SCIENTIST")
        st.write("""
        [cite_start]As a **GIS Analyst** at **SWANSAT (OPC) Pvt Ltd**, I specialize in agricultural remote sensing and automated geospatial pipelines. My work focuses on leveraging multi-sensor data—including **Sentinel**, **ConstellR (Thermal)**, and **PlanetScope**—to monitor crop phenology and estimate biophysical parameters[cite: 16, 17].
        
        [cite_start]With an M.Tech in Earth System Science and Engineering from **IIT Guwahati** (2024), I combine technical expertise in Python, Google Earth Engine (GEE), and Machine Learning to solve complex environmental challenges[cite: 4, 5].
        
        My expertise lies in:
        * 🌾 **Crop Yield Forecasting (ML)**
        * 🌡️ **Thermal & Hyperspectral Analysis**
        * 🛠️ **Automated ETL Pipelines (GeoFormatX)**
        * 📊 **Agri-Analytics Dashboards**
        """)
        
        # Download Resume Button logic
        file_data = None
        try:
            with open("Nitesh_Kumar_Resume.pdf", "rb") as file:
                file_data = file.read()
            btn_label = "📄 DOWNLOAD RESUME"
            file_name = "Nitesh_Kumar_Resume.pdf"
            file_mime = "application/pdf"
        except FileNotFoundError:
            # Fallback
            with open("app.py", "rb") as file:
                file_data = file.read()
            btn_label = "📄 DOWNLOAD SOURCE CODE (DEMO)"
            file_name = "app.py"
            file_mime = "text/plain"

        st.download_button(
            label=btn_label,
            data=file_data,
            file_name=file_name,
            mime=file_mime,
        )

    with col2:
        # Interactive Folium Map
        m = folium.Map(location=[22.5937, 78.9629], zoom_start=4, tiles="CartoDB positron")
        
        # IIT Guwahati
        folium.Marker(
            [26.1878, 91.6916], 
            popup="IIT Guwahati (M.Tech)", 
            tooltip="Education",
            icon=folium.Icon(color="blue", icon="graduation-cap", prefix="fa")
        ).add_to(m)
        
        # REC Ambedkar Nagar
        folium.Marker(
            [26.4357, 82.6360], 
            popup="REC Ambedkar Nagar (B.Tech)", 
            tooltip="Education",
            icon=folium.Icon(color="blue", icon="graduation-cap", prefix="fa")
        ).add_to(m)
        
        # Mumbai (Current Work)
        folium.Marker(
            [19.0760, 72.8777], 
            popup="SWANSAT (GIS Analyst)", 
            tooltip="Current Work",
            icon=folium.Icon(color="red", icon="briefcase", prefix="fa")
        ).add_to(m)

        st_folium(m, height=300, width=300)

# --- SECTION: EXPERIENCE ---
if selected == "Experience":
    st.title("💼 PROFESSIONAL EXPERIENCE")
    
    st.markdown("### 🛰️ GIS ANALYST")
    st.caption("SWANSAT (OPC) Pvt Ltd. | Mumbai, India | [cite_start]June 2024 -- Present [cite: 11, 12]")
    st.markdown("""
    * [cite_start]**Crop Phenology Monitoring:** Developed automated pipelines using **Sentinel-1 SAR backscatter (VV/VH)** to track growth stages in cloud-prone regions[cite: 16].
    * [cite_start]**Biophysical Parameter Extraction:** Designed algorithms for retrieving LAI, FAPAR, and Vegetation Indices (NDVI, NDRE) using Sentinel-2/Landsat imagery[cite: 17].
    * [cite_start]**Soil Moisture Analysis:** Implemented microwave remote sensing workflows to support irrigation scheduling and drought stress detection[cite: 18].
    * [cite_start]**Yield Validation:** Collaborated with agronomy teams to validate satellite proxies against ground-truth harvest data[cite: 19].
    """)
    st.divider()
    
    st.markdown("### 🎓 TEACHING ASSISTANT")
    [cite_start]st.caption("IIT Guwahati | Assam, India | Jan 2023 -- May 2024 [cite: 20, 21]")
    st.markdown("""
    * [cite_start]Assisted postgraduate courses in **GIS and Environmental Modelling**[cite: 23].
    * [cite_start]Focused on terrain analysis for agriculture, soil spatial variability, and land-use classification workflows[cite: 23].
    """)

# --- SECTION: PROJECTS ---
if selected == "Projects":
    st.title("🚀 KEY PROJECTS")
    
    # Featured Project 1
    with st.container():
        st.subheader("🌟 GEOSPATIAL Ni30: AGRI-ANALYTICS ENGINE")
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write("**Tech Stack:** Python, Streamlit, GEE API")
            st.write("""
            [cite_start]A full-stack geospatial web app to democratize access to agricultural satellite data[cite: 28].
            * [cite_start]**Real-time Monitoring:** Backend algorithms for Vegetation Health Index (VHI) and LST retrieval[cite: 29].
            * [cite_start]**Farm ROI:** Automated KML parsing and time-series charting of crop growth cycles[cite: 30].
            * **Data Integration:** Scalable ingestion of Sentinel and PlanetScope imagery.
            """)
        with col2:
            st.link_button("LAUNCH APP 🚀", "https://niteshgulzar.streamlit.app/")

    st.divider()

    # Featured Project 2
    with st.container():
        st.subheader("🔄 geoFormatX: VECTOR INTEROPERABILITY ENGINE")
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write("**Tech Stack:** Python, Streamlit, Geopandas")
            st.write("""
            [cite_start]Serverless ETL web application for automated vector data conversion[cite: 33].
            * [cite_start]**Format Conversion:** Seamlessly converts between Shapefile, GeoJSON, and KML formats[cite: 33].
            * [cite_start]**CRS Handling:** Solves reprojection issues for precision agriculture tools[cite: 34].
            * [cite_start]**Integration:** Ensures interoperability between legacy cadastral maps and modern GIS[cite: 34].
            """)
        with col2:
            st.link_button("LAUNCH APP 🚀", "https://geoformatx.streamlit.app/")
            
    st.divider()
    
    # Other Projects Grid
    col1, col2 = st.columns(2)
    
    with col1:
        with st.expander("🌾 ML-Based Crop Yield Forecasting (2025)", expanded=True):
            st.write("""
            * [cite_start]**Data Sources:** **PlanetScope (3m)**, **ConstellR (Thermal)**, Sentinel-1/2[cite: 38].
            * [cite_start]**Objective:** Crop yield estimation using multi-sensor spectral signatures[cite: 38].
            * [cite_start]**Innovation:** Classification pipelines to differentiate Wheat vs. Barley based on phenological signatures[cite: 39].
            * [cite_start]**Result:** Achieved **85%+ accuracy** in pre-harvest yield prediction[cite: 40].
            """)
            
    with col2:
        with st.expander("🛢️ MTP: Environmental Risk Assessment (2024)", expanded=True):
            st.write("""
            * [cite_start]**Tech:** **PRISMA Hyperspectral**, Sentinel-2, SVM, Random Forest[cite: 43].
            * [cite_start]**Objective:** Detection of hydrocarbon microseepage in Northeast India[cite: 46].
            * [cite_start]**Outcome:** Utilized narrow-band spectral analysis for identifying stress markers in vegetation[cite: 44].
            * [cite_start]**Publication:** Presented at *EGU General Assembly 2024*[cite: 47].
            """)

# --- SECTION: SKILLS ---
if selected == "Skills":
    st.title("🛠️ TECHNICAL ARSENAL")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("REMOTE SENSING & GIS")
        st.markdown("""
        - **High-Res Optical:** **PlanetScope (3m)**, Sentinel-2, Landsat
        - **Thermal:** **ConstellR**, Landsat (LST)
        - [cite_start]**Hyperspectral:** **PRISMA** [cite: 43]
        - [cite_start]**Microwave/SAR:** Sentinel-1 (Backscatter VV/VH Analysis) [cite: 16]
        - [cite_start]**Tools:** Google Earth Engine, ArcGIS Pro, QGIS, SNAP [cite: 53]
        """)
        
        st.subheader("DATA SCIENCE & ML")
        st.markdown("""
        - [cite_start]**Algorithms:** Random Forest, XGBoost, SVM, Regression [cite: 38, 52]
        - [cite_start]**Techniques:** Time-Series Classification (DTW), Yield Modeling [cite: 52]
        - [cite_start]**Libraries:** Scikit-learn, Pandas, NumPy, Rasterio [cite: 51]
        """)

    with col2:
        st.subheader("PROGRAMMING")
        st.code("""
# Languages
Python = "Advanced" (Geopandas, Rasterio)
JavaScript = "Intermediate" (GEE API)

# Web Development
Streamlit = "Advanced" (Full-stack Geospatial)
        """, language="python")
        
        st.subheader("SOFT SKILLS")
        [cite_start]st.write("✅ Agronomy Collaboration [cite: 19]")
        st.write("✅ Technical Documentation")
        st.write("✅ Research & Validation")

# --- SECTION: EDUCATION ---
if selected == "Education":
    st.title("🎓 EDUCATION")
    
    st.subheader("M.TECH IN EARTH SYSTEM SCIENCE AND ENGINEERING")
    [cite_start]st.write("**Indian Institute of Technology Guwahati** | 2022 -- 2024 [cite: 4, 22]")
    st.write("📍 *Assam, India*")
    [cite_start]st.info("CGPA: **8.9/10** [cite: 6]")
    
    st.markdown("---")
    
    st.subheader("B.TECH IN CIVIL ENGINEERING")
    [cite_start]st.write("**Rajkiya Engineering College** | 2018 -- 2022 [cite: 7, 14]")
    st.write("📍 *Ambedkar Nagar, U.P.*")
    [cite_start]st.info("CGPA: **7.93/10** [cite: 9]")

# --- SECTION: CONTACT ---
if selected == "Contact":
    st.title("📬 GET IN TOUCH")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("Open for collaborations on Agri-Tech, GIS pipelines, and ML-based Remote Sensing projects.")
        st.markdown("📧 **Email:** [nitesh.gulzar@gmail.com](mailto:nitesh.gulzar@gmail.com)")
        st.markdown("💼 **LinkedIn:** [linkedin.com/in/nitesh4004](https://linkedin.com/in/nitesh4004)")
        st.markdown("🐙 **GitHub:** [github.com/nitesh4004](https://github.com/nitesh4004)")
        
    with col2:
        contact_form = """
        <form action="https://formsubmit.co/nitesh.gulzar@gmail.com" method="POST">
             <input type="hidden" name="_captcha" value="false">
             <input type="text" name="name" placeholder="YOUR NAME" required style="width: 100%; padding: 10px; margin-bottom: 10px; border: 1px solid #ccc; border-radius: 5px; font-family: 'Helvetica', 'Arial', sans-serif;">
             <input type="email" name="email" placeholder="YOUR EMAIL" required style="width: 100%; padding: 10px; margin-bottom: 10px; border: 1px solid #ccc; border-radius: 5px; font-family: 'Helvetica', 'Arial', sans-serif;">
             <textarea name="message" placeholder="YOUR MESSAGE" required style="width: 100%; padding: 10px; margin-bottom: 10px; border: 1px solid #ccc; border-radius: 5px; rows: 5; font-family: 'Helvetica', 'Arial', sans-serif;"></textarea>
             <button type="submit" style="background-color: #00796B; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; width: 100%; font-family: 'Helvetica', 'Arial', sans-serif; font-weight: 600; letter-spacing: 1px;">SEND MESSAGE</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)
