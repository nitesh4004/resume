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

# --- CSS STYLING ---
st.markdown("""
<style>
    /* Reduce padding at top */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    /* Custom fonts for headers */
    h1, h2, h3 {
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 600;
    }
    /* Style the timeline dots */
    .timeline-dot {
        height: 15px;
        width: 15px;
        background-color: #FF4B4B;
        border-radius: 50%;
        display: inline-block;
    }
    /* Profile Image styling */
    img {
        border-radius: 50%; 
        border: 3px solid #FF4B4B;
    }
    /* Button styling */
    .stButton button {
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    # Placeholder for profile image - Replace 'profile.jpg' with your actual file if available
    # st.image("profile.jpg", width=150) 
    
    st.markdown("## Nitesh Kumar")
    st.markdown("📍 *Mumbai, India*")
    st.caption("Geospatial Data Scientist | Flood Modeller | GEE Developer")
    
    # Navigation
    selected = option_menu(
        menu_title=None,
        options=["Home", "Experience", "Projects", "Skills", "Education", "Contact"],
        icons=["house", "briefcase", "rocket", "tools", "book", "envelope"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "orange", "font-size": "18px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#FF4B4B"},
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
        st.title("Hello, I'm Nitesh! 👋")
        st.subheader("Geospatial Data Scientist & Earth Observation Specialist")
        st.write("""
        I bridge the gap between **Civil Engineering** and **Earth System Science**, leveraging satellite data to solve real-world problems. 
        
        My expertise lies in:
        * 🌊 **Hydrodynamic Flood Modelling**
        * 🌾 **Crop Yield Forecasting (ML)**
        * 🛰️ **Automated Satellite Pipelines (GEE)**
        
        Currently working as a **GIS Analyst** at SWANSAT, focusing on SAR-based flood analytics.
        """)
        
        # Download Resume Button (You would need to put your actual PDF in the folder)
        with open("app.py", "rb") as file: # Placeholder: using app.py as dummy file
            st.download_button(
                label="📄 Download Resume",
                data=file,
                file_name="Nitesh_Kumar_Resume.pdf",
                mime="application/pdf",
            )

    with col2:
        # A simple interactive map showing your journey
        m = folium.Map(location=[23.5937, 78.9629], zoom_start=4, tiles="CartoDB positron")
        
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
    st.title("💼 Professional Experience")
    
    st.markdown("### 🛰️ GIS Analyst")
    st.caption("SWANSAT (OPC) Pvt Ltd. | Mumbai, India | June 2024 -- Present")
    st.markdown("""
    * **Architected flood workflows:** Used Sentinel-1 SAR & SRTM DEM in Google Earth Engine (GEE).
    * **Flood Susceptibility:** Designed models using terrain analytics and hydrodynamic interpretations.
    * **Automation:** Built pipelines for surface water extent extraction and change detection.
    """)
    st.divider()
    
    st.markdown("### 🎓 Teaching Assistant")
    st.caption("IIT Guwahati | Assam, India | Jan 2023 -- May 2024")
    st.markdown("""
    * Assisted postgraduate courses in **GIS and Hydrological Modelling**.
    * Focused on DEM hydrology, drainage extraction, and soil-vegetation-water interactions.
    """)

# --- SECTION: PROJECTS ---
if selected == "Projects":
    st.title("🚀 Key Projects")
    
    # Featured Project
    with st.container():
        st.subheader("🌟 Geospatial Ni30: Real-Time Analytics Engine")
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write("**Tech Stack:** Python, Streamlit, GEE API")
            st.write("""
            A full-stack geospatial web app to democratize access to Sentinel-1, Sentinel-2, and Landsat 8/9.
            * Implemented backend algorithms for **Land Surface Temperature (LST)** retrieval.
            * Custom dynamic band math calculator.
            * Automated GeoTIFF export pipelines.
            """)
        with col2:
            st.link_button("Launch App 🚀", "https://niteshgulzar.streamlit.app/")
            
    st.divider()
    
    # Other Projects Grid
    col1, col2 = st.columns(2)
    
    with col1:
        with st.expander("🌾 ML-Based Crop Yield Forecasting (2025)", expanded=True):
            st.write("""
            * **Goal:** Spectral signature extraction for yield estimation.
            * **Data:** Optical (Sentinel-2), Thermal (ConstellR), SAR (Sentinel-1).
            * **Method:** Classification and regression pipelines validated with ground truth.
            """)
            
        with st.expander("💧 Hydrodynamic Flood Modelling (2025)"):
            st.write("""
            * **Goal:** 1D-2D floodplain dynamics simulation.
            * **Method:** Estimated inundation depth using Sentinel-1 water extent and SRTM terrain data.
            * **Outcome:** Validated hazard maps integrated with land use layers.
            """)

    with col2:
        with st.expander("🏔️ Cloudburst Flood Analysis - Uttarakhand (2023)", expanded=True):
            st.write("""
            * **Goal:** Post-event flood extent and debris flow mapping.
            * **Data:** Sentinel-1 and ASTER DEM in GEE.
            * **Outcome:** Flood depth rasters and terrain risk zone maps.
            """)
            
        with st.expander("🛢️ MTP: Hydrocarbon Microseepage Detection (2024)"):
            st.write("""
            * **Goal:** Environmental risk assessment.
            * **Algorithms:** Random Forest and SVM on Hyperspectral (PRISMA) data.
            * **Publication:** Presented at EGU General Assembly 2024.
            """)

# --- SECTION: SKILLS ---
if selected == "Skills":
    st.title("🛠️ Technical Arsenal")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Geospatial & Remote Sensing")
        st.markdown("""
        - **Data:** Sentinel-1/2, Landsat, DEM, Thermal, Hyperspectral (PRISMA)
        - **Analysis:** Google Earth Engine (JS/Python), ArcPy, GDAL/Rasterio
        - **Software:** ArcGIS Pro, QGIS, ENVI, SNAP
        """)
        
        st.subheader("Data Science & ML")
        st.markdown("""
        - **Algorithms:** Random Forest, SVM, CNNs, Regression
        - **Libraries:** Scikit-learn, Pandas, NumPy, Matplotlib
        """)

    with col2:
        st.subheader("Programming & Web")
        st.code("""
# Languages
Python = "Advanced"
JavaScript = "Intermediate"
SQL = "Intermediate"

# Web Frameworks
Streamlit = "Advanced"
        """, language="python")
        
        st.subheader("Soft Skills")
        st.write("✅ Technical Documentation")
        st.write("✅ Executive Reporting")
        st.write("✅ Research & Validation")

# --- SECTION: EDUCATION ---
if selected == "Education":
    st.title("🎓 Education")
    
    st.subheader("M.Tech in Earth System Science and Engineering")
    st.write("**Indian Institute of Technology Guwahati** | 2022 -- 2024")
    st.write("📍 *Assam, India*")
    st.info("CGPA: **8.9/10**")
    
    st.markdown("---")
    
    st.subheader("B.Tech in Civil Engineering")
    st.write("**Rajkiya Engineering College** | 2018 -- 2022")
    st.write("📍 *Ambedkar Nagar, U.P.*")
    st.info("CGPA: **7.93/10**")

# --- SECTION: CONTACT ---
if selected == "Contact":
    st.title("📬 Get In Touch")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("Feel free to reach out for collaborations on GIS, Remote Sensing, or Machine Learning projects.")
        st.markdown("📧 **Email:** [nitesh.gulzar@gmail.com](mailto:nitesh.gulzar@gmail.com)")
        st.markdown("📱 **Phone:** +91 8795969051")
        st.markdown("💼 **LinkedIn:** [linkedin.com/in/nitesh4004](https://linkedin.com/in/nitesh4004)")
        
    with col2:
        # Simple contact form using FormSubmit (No backend required)
        contact_form = """
        <form action="https://formsubmit.co/nitesh.gulzar@gmail.com" method="POST">
             <input type="hidden" name="_captcha" value="false">
             <input type="text" name="name" placeholder="Your Name" required style="width: 100%; padding: 10px; margin-bottom: 10px; border: 1px solid #ccc; border-radius: 5px;">
             <input type="email" name="email" placeholder="Your Email" required style="width: 100%; padding: 10px; margin-bottom: 10px; border: 1px solid #ccc; border-radius: 5px;">
             <textarea name="message" placeholder="Your Message" required style="width: 100%; padding: 10px; margin-bottom: 10px; border: 1px solid #ccc; border-radius: 5px; rows: 5;"></textarea>
             <button type="submit" style="background-color: #FF4B4B; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; width: 100%;">Send Message</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)