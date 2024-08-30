import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Page configuration
st.set_page_config(page_title="Jason C. Smith - Professional Resume", layout="wide")

# Custom CSS to improve the layout
st.markdown("""
    <style>
    .big-font {
        font-size:30px !important;
        font-weight: bold;
    }
    .medium-font {
        font-size:24px !important;
        font-weight: bold;
    }
    .small-font {
        font-size:18px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Header
st.markdown('<p class="big-font">Jason C. Smith</p>', unsafe_allow_html=True)

# Professional Summary
st.markdown('<p class="medium-font">Professional Summary</p>', unsafe_allow_html=True)
st.write("""
Innovative entrepreneur and versatile professional with a diverse background spanning technology, finance, music industry, and military service. Proven track record in developing cutting-edge solutions for e-commerce and cryptocurrency management. Skilled in software development, business leadership, and creating user-centric platforms. Demonstrates adaptability, technical expertise, and strong problem-solving skills across various industries.
""")

# Core Competencies
st.markdown('<p class="medium-font">Core Competencies</p>', unsafe_allow_html=True)
competencies = [
    "Entrepreneurship & Start-up Management",
    "E-commerce Solutions Development",
    "Cryptocurrency & Digital Asset Management",
    "Software Development (Python, VSCode, Plotly, Matplotlib, NPM)",
    "Music Production & Royalty Management",
    "Mechanical Repair & Diagnostics",
    "Customer Service & Relationship Management",
    "Project Management & Team Leadership"
]
for comp in competencies:
    st.markdown(f"- {comp}")

# Professional Experience
st.markdown('<p class="medium-font">Professional Experience</p>', unsafe_allow_html=True)

# Function to create expandable sections for each job
def job_section(title, company, period, responsibilities):
    with st.expander(f"{title} | {company} | {period}"):
        for resp in responsibilities:
            st.markdown(f"- {resp}")

# SH X Coin
job_section(
    "Founder and CEO",
    "SH X Coin",
    "2021-Present",
    [
        "Developed an innovative cryptocurrency management platform, emphasizing security and user experience",
        'Created the tagline "Everything Music Coined: Where Financial Security Meets Musical Harmony"',
        "Integrated financial security measures to protect users' digital assets",
        "Implemented a feature-rich interface combining cryptocurrency management with musical elements",
        "Focused on creating a movement encompassing financial stability, philanthropy, and musical enlightenment",
        "Led the company's vision to redefine digital finance management"
    ]
)

# Storqese LLC
job_section(
    "Founder and CEO",
    "Storqese LLC",
    "2016-2021",
    [
        "Developed and launched an all-in-one e-commerce solution to simplify online selling for businesses",
        "Created a user-friendly platform streamlining product listing, inventory management, and order processing",
        "Implemented tools to help businesses focus on growth rather than technical complexities",
        "Integrated multiple sales channels to maximize reach and revenue potential for clients",
        "Managed all aspects of the start-up, including product development, marketing, and financial operations"
    ]
)

# Freightliner
job_section(
    "Truck Mechanic",
    "Freightliner (Mercedes & Daimler)",
    "2014-2016",
    [
        "Diagnosed and repaired issues in diesel engine trucks",
        "Conducted safety inspections and maintained detailed repair records",
        "Handled deliveries for Fortune 500 companies across 48 states and Canada"
    ]
)

# Earlier Career Highlights
st.markdown('<p class="small-font">Earlier Career Highlights</p>', unsafe_allow_html=True)
earlier_career = [
    "Hydraulic Performance Technician, Halliburton (2014-2016)",
    "Professional Truck Driver (2009-2014)",
    "Legal Assistant, Law Offices of Iris Bright (2000-2007)",
    "Customer Service Representative, Home Federal Savings Bank (1998-1999)",
    "Software Developer, Entune Multimedia Group (1996-1998)",
    "Production/Marketing Specialist, Ruthless Records (1994-1995)",
    "Production Executive, Death Row Records (1993-1994)",
    "Loan Officer, Capital Home Loans (1991-1995)",
    "U.S. Navy, Active Duty and Reserves (1987-1995)"
]
for career in earlier_career:
    st.markdown(f"- {career}")

# Technical Skills
st.markdown('<p class="medium-font">Technical Skills</p>', unsafe_allow_html=True)
technical_skills = [
    "Programming Languages: Python",
    "Development Tools: VSCode, NPM",
    "Data Visualization: Plotly, Matplotlib",
    "Version Control: Git",
    "Blockchain Technology",
    "E-commerce Platforms",
    "Cryptocurrency Management Systems"
]

# Create a radar chart for technical skills using Matplotlib
categories = [skill.split(":")[0] for skill in technical_skills]
values = [len(skill.split(":")[1].strip().split(",")) if ":" in skill else 1 for skill in technical_skills]
values += values[:1]  # Closing the radar chart

angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
angles += angles[:1]  # Closing the radar chart

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.fill(angles, values, color='teal', alpha=0.25)
ax.plot(angles, values, color='teal', linewidth=2) 
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories)

st.pyplot(fig)

for skill in technical_skills:
    st.markdown(f"- {skill}")

# Footer
st.markdown("---")
st.markdown("Created with Streamlit by Jason C. Smith")
