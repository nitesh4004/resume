import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_folium import st_folium
import folium

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Nitesh Kumar | Geospatial Data Scientist",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- COLOR PALETTE VARIABLES ---
primary_color = "#003366"  # Navy Blue
secondary_color = "#D9534F" # Terra Cotta Red
text_color = "#333333"      # Dark Grey
bg_color = "#F0F2F6"        # Light Blue-Grey

# --- CSS STYLING WITH OSWALD FONT & COLOR THEME ---
st.markdown(f"""
<style>
    /* Import Oswald Font */
    @import url('https://fonts.googleapis.com/css2?family=Oswald:wght@300;400;500;700&display=swap');

    /* GLOBAL FONT & COLOR SETTINGS */
    html, body, [class*="css"] {{
        font-family: 'Oswald', sans-serif;
        color: {text_color};
    }}

    /* HEADERS */
    h1, h2, h3 {{
        font-family: 'Oswald', sans-serif;
        font-weight: 700;
        letter-spacing: 1.2px;
        text-transform: uppercase;
        color: {primary_color};
    }}
    
    h1 {{ font-size: 3rem !important; }}
    h2 {{ font-size: 2rem !important; }}
    h3 {{ font-size: 1.5rem !important; }}

    /* BODY TEXT */
    p, div, li, .stMarkdown {{
        font-family: 'Oswald', sans-serif;
        font-weight: 400;
        font-size: 1.15rem;
        line-height: 1.6;
        color: {text_color};
    }}
    
    /* CAPTIONS (Job Titles, Dates) */
    .stCaption {{
        font-family: 'Oswald', sans-serif;
        color: #666666;
        font-size: 1rem;
    }}

    /* BUTTON STYLING */
    .stButton button {{
        width: 100%;
        background-color: {secondary_color};
        color: white;
        border: none;
        border-radius: 5px;
        padding: 0.5rem 1rem;
        font-weight: 500;
        letter-spacing: 1px;
        text-transform: uppercase;
        transition: all 0.3s ease;
    }}
    
    .stButton button:hover {{
        background-color: {primary_color};
        color: white;
        border: 1px solid {secondary_color};
    }}
    
    /* LINK BUTTONS */
    a {{
        text-decoration: none;
    }}

    /* SIDEBAR STYLING */
    [data-testid="stSidebar"] {{
        background-color: #ffffff;
        border-right: 1px solid #e6e6e6;
    }}

    /* PROFILE IMAGE STYLING */
    img {{
        border-radius: 10px; 
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }}

    /* BLOCK CONTAINER PADDING */
    .block-container {{
        padding-top: 2rem;
        padding-bottom: 4rem;
    }}
    
    /* EXPANDER STYLING */
    .streamlit-expanderHeader {{
        font-weight: 500;
        color: {primary_color};
        background-color: white;
        border-radius: 5px;
    }}
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    # Placeholder for profile image
    # st.image("profile.jpg", width=150) 
    
    st.markdown(f"<h2 style='color: {primary_color}; text-align: left; margin-bottom: 0;'>Nitesh Kumar</h2>", unsafe_allow_html=True)
    st.markdown("📍 *Mumbai, India*")
    st.caption("Geospatial Data Scientist | Flood Modeller | GEE Developer")
    
    st.write("") # Spacer

    # Navigation Menu
    selected = option_menu(
        menu_title=None,
        options=["Home", "Experience", "Projects", "Skills", "Education", "Contact"],
        icons=["house", "briefcase", "rocket", "tools", "book", "envelope"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": secondary_color, "font-size": "18px"}, 
            "nav-link": {
                "font-family": "Oswald, sans-serif", 
                "font-size": "16px", 
                "text-align": "left", 
                "margin":"5px", 
                "color": text_color,
                "--hover-color": "#f0f2f6"
            },
            "nav-link-selected": {"background-color": primary_color, "color": "white"},
        }
    )
    
    st.markdown("---")
    st.write("### 🔗 Connect")
    # Using columns for icons to make them tighter
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown("[![LinkedIn](https://img.shields.io/badge/in-0077B5?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/nitesh4004)")
    with c2: st.markdown("[![GitHub](https://img.shields.io/badge/git-100000?style=flat&logo=github&logoColor=white)](https://github.com/nitesh4004)")
    with c3: st.markdown("[![Email](https://img.shields.io/badge/mail-D14836?style=flat&logo=gmail&logoColor=white)](mailto:nitesh.gulzar@gmail.com)")

# --- SECTION: HOME ---
if selected == "Home":
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.title("HELLO, I'M NITESH! 👋")
        st.markdown(f"<h3 style='color: {secondary_color};'>GEOSPATIAL DATA SCIENTIST & EARTH OBSERVATION SPECIALIST</h3>", unsafe_allow_html=True)
        
        st.write("""
        I bridge the gap between **Civil Engineering** and **Earth System Science**, leveraging satellite data to solve real-world problems. 
        
        My expertise lies in:
        * 🌊 **Hydrodynamic Flood Modelling**
        * 🌾 **Crop Yield Forecasting (ML)**
        * 🛰️ **Automated Satellite Pipelines (GEE)**
        
        Currently working as a **GIS Analyst** at SWANSAT, focusing on SAR-based flood analytics.
        """)
        
        st.write("") # Spacer

        # Download Resume Button
        try:
            with open("Nitesh_Kumar_Resume.pdf", "rb") as file:
                btn_label = "📄 DOWNLOAD RESUME"
                file_data = file
                file_mime = "application/pdf"
        except FileNotFoundError:
            with open(__file__, "rb") as file:
                btn_label = "📄 DOWNLOAD SOURCE CODE (DEMO)"
                file_data = file
                file_mime = "text/plain"

        st.download_button(
            label=btn_label,
            data=file_data,
            file_name="Nitesh_Kumar_Resume.pdf",
            mime=file_mime,
        )

    with col2:
        # Interactive Folium Map
        m = folium.Map(location=[22.0, 79.0], zoom_start=4, tiles="CartoDB positron")
        
        # Markers
        locations = [
            {"coords": [26.1878, 91.6916], "label": "IIT Guwahati", "icon": "graduation-cap", "color": "blue"},
            {"coords": [26.4357, 82.6360], "label": "REC Ambedkar Nagar", "icon": "graduation-cap", "color": "blue"},
            {"coords": [19.0760, 72.8777], "label": "SWANSAT (Mumbai)", "icon": "briefcase", "color": "red"}
        ]
        
        for loc in locations:
            folium.Marker(
                loc["coords"], 
                popup=loc["label"], 
                tooltip=loc["label"],
                icon=folium.Icon(color=loc["color"], icon=loc["icon"], prefix="fa")
            ).add_to(m)

        st_folium(m, height=350, width=350)

# --- SECTION: EXPERIENCE ---
if selected == "Experience":
    st.title("💼 PROFESSIONAL EXPERIENCE")
    
    with st.container():
        st.markdown(f"### 🛰️ GIS ANALYST")
        st.caption("SWANSAT (OPC) Pvt Ltd. | Mumbai, India | June 2024 -- Present")
        st.markdown("""
        * **Architected flood workflows:** Used Sentinel-1 SAR & SRTM DEM in Google Earth Engine (GEE).
        * **Flood Susceptibility:** Designed models using terrain analytics and hydrodynamic interpretations.
        * **Automation:** Built pipelines for surface water extent extraction and change detection.
        """)
        
    st.divider()
    
    with st.container():
        st.markdown(f"### 🎓 TEACHING ASSISTANT")
        st.caption("IIT Guwahati | Assam, India | Jan 2023 -- May 2024")
        st.markdown("""
        * Assisted postgraduate courses in **GIS and Hydrological Modelling**.
        * Focused on DEM hydrology, drainage extraction, and soil-vegetation-water interactions.
        """)

# --- SECTION: PROJECTS ---
if selected == "Projects":
    st.title("🚀 KEY PROJECTS")
    
    # Featured Project Box
    st.info("🌟 **FEATURED:** GEOSPATIAL Ni30 - REAL-TIME ANALYTICS ENGINE")
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write("**Tech Stack:** Python, Streamlit, GEE API")
        st.write("A full-stack geospatial web app to democratize access to Sentinel-1, Sentinel-2, and Landsat data.")
    with col2:
        st.link_button("LAUNCH APP 🚀", "https://niteshgulzar.streamlit.app/")
            
    st.write("")

    # Other Projects Grid
    col1, col2 = st.columns(2)
    
    with col1:
        with st.expander("🌾 ML-Based Crop Yield Forecasting (2025)", expanded=True):
            st.markdown("""
            * **Goal:** Spectral signature extraction for yield estimation.
            * **Data:** Optical (Sentinel-2), Thermal (ConstellR), SAR (Sentinel-1).
            * **Method:** Classification and regression pipelines validated with ground truth.
            """)
            
        with st.expander("💧 Hydrodynamic Flood Modelling (2025)"):
            st.markdown("""
            * **Goal:** 1D-2D floodplain dynamics simulation.
            * **Method:** Estimated inundation depth using Sentinel-1 water extent and SRTM terrain data.
            """)

    with col2:
        with st.expander("🏔️ Cloudburst Flood Analysis (2023)", expanded=True):
            st.markdown("""
            * **Goal:** Post-event flood extent and debris flow mapping in Uttarakhand.
            * **Data:** Sentinel-1 and ASTER DEM in GEE.
            """)
            
        with st.expander("🛢️ Hydrocarbon Microseepage Detection (2024)"):
            st.markdown("""
            * **Goal:** Environmental risk assessment.
            * **Algorithms:** Random Forest and SVM on Hyperspectral (PRISMA) data.
            """)

# --- SECTION: SKILLS ---
if selected == "Skills":
    st.title("🛠️ TECHNICAL ARSENAL")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("GEOSPATIAL & REMOTE SENSING")
        st.markdown(f"""
        <div style="background-color: white; padding: 20px; border-radius: 10px; border-left: 5px solid {primary_color};">
        <b>Data:</b> Sentinel-1/2, Landsat, DEM, Thermal, Hyperspectral (PRISMA)<br>
        <b>Analysis:</b> Google Earth Engine (JS/Python), ArcPy, GDAL/Rasterio<br>
        <b>Software:</b> ArcGIS Pro, QGIS, ENVI, SNAP
        </div>
        """, unsafe_allow_html=True)
        
        st.write("")
        st.subheader("DATA SCIENCE & ML")
        st.markdown(f"""
        <div style="background-color: white; padding: 20px; border-radius: 10px; border-left: 5px solid {secondary_color};">
        <b>Algorithms:</b> Random Forest, SVM, CNNs, Regression<br>
        <b>Libraries:</b> Scikit-learn, Pandas, NumPy, Matplotlib
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.subheader("PROGRAMMING")
        # Customizing the code block to look cleaner
        st.code("""
# Languages
Python      = "Advanced"
JavaScript  = "Intermediate"
SQL         = "Intermediate"

# Frameworks
Streamlit   = "Advanced"
GEE API     = "Advanced"
        """, language="python")
        
        st.subheader("SOFT SKILLS")
        st.success("✅ Technical Documentation")
        st.success("✅ Executive Reporting")
        st.success("✅ Research & Validation")

# --- SECTION: EDUCATION ---
if selected == "Education":
    st.title("🎓 EDUCATION")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div style="background-color: white; padding: 20px; border-radius: 10px; border-top: 5px solid {primary_color}; text-align: center;">
            <h3>M.TECH</h3>
            <p><b>Earth System Science</b><br>IIT Guwahati (2022-2024)</p>
            <p style="font-size: 2rem; font-weight: 700; color: {secondary_color};">8.9/10</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown(f"""
        <div style="background-color: white; padding: 20px; border-radius: 10px; border-top: 5px solid {primary_color}; text-align: center;">
            <h3>B.TECH</h3>
            <p><b>Civil Engineering</b><br>REC Ambedkar Nagar (2018-2022)</p>
            <p style="font-size: 2rem; font-weight: 700; color: {secondary_color};">7.93/10</p>
        </div>
        """, unsafe_allow_html=True)

# --- SECTION: CONTACT ---
if selected == "Contact":
    st.title("📬 GET IN TOUCH")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("Feel free to reach out for collaborations on GIS, Remote Sensing, or Machine Learning projects.")
        st.info("**Email:** nitesh.gulzar@gmail.com")
        st.info("**Phone:** +91 8795969051")
        st.markdown("[LinkedIn Profile >](https://linkedin.com/in/nitesh4004)")
        
    with col2:
        # Added specific styling to input fields to ensure text is visible (black on white)
        contact_form = f"""
        <form action="https://formsubmit.co/nitesh.gulzar@gmail.com" method="POST">
             <input type="hidden" name="_captcha" value="false">
             <input type="text" name="name" placeholder="YOUR NAME" required style="width: 100%; padding: 10px; margin-bottom: 10px; border: 1px solid #ccc; border-radius: 5px; font-family: 'Oswald', sans-serif; color: #333; background-color: white;">
             <input type="email" name="email" placeholder="YOUR EMAIL" required style="width: 100%; padding: 10px; margin-bottom: 10px; border: 1px solid #ccc; border-radius: 5px; font-family: 'Oswald', sans-serif; color: #333; background-color: white;">
             <textarea name="message" placeholder="YOUR MESSAGE" required style="width: 100%; padding: 10px; margin-bottom: 10px; border: 1px solid #ccc; border-radius: 5px; rows: 5; font-family: 'Oswald', sans-serif; color: #333; background-color: white;"></textarea>
             <button type="submit" style="background-color: {secondary_color}; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; width: 100%; font-family: 'Oswald', sans-serif; font-weight: 500; letter-spacing: 1px;">SEND MESSAGE</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)
