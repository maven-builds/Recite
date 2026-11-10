import streamlit as st

st.set_page_config(page_title="Logbook")

st.title("My Logbook")
st.write("")
st.write("*Working Title:")
st.header("Studying Non-Motor Dysfunction for the Prodromal Screening of Parkinson’s Disease and Similar Synucleinopathies")
st.write("")
st.subheader("Explore")

selectMonth = st.selectbox("", options = ["","August 2026", "September 2026", "October 2026", "November 2026"])

if selectMonth == "":
    st.write("")

if selectMonth == "August 2026":
    st.write("")
    with open("august_logs.pdf", "rb") as pdf_file:
            st.download_button(
                label = "Download Full August Logs (PDF)",
                data=pdf_file,
                file_name="august_logs.pdf",
                mime="application/pdf")
    st.write("")
    st.subheader("2026-08-01 | 07:00 PM – 10:00 PM:")
    st.subheader("OBJECTIVE: Expanding my understanding of Parkinson’s disease")
    st.subheader("NEXT STEP: Find a direction for my research and look into each symptom")
    st.write("Studied the symptoms of Parkinson’s disease, particularly bradykinesia, freezing of gait, paradoxical kinesia, anosmia, and RBD. The role of dopamine as both a neurotransmitter and a neurohormone with peripheral function was researched much more in depth, with my notes covering its nature beyond acting as the primary neurochemical in motivation.")
    st.write("")
    st.subheader("2026-08-02 | 01:00 PM – 03:00 PM:")
    st.subheader("OBJECTIVE: Researching anosmia and finding a thesis")
    st.subheader("NEXT STEP: Narrow down my thesis")
    st.write("After writing a short note on anosmia in my research tab for Parkinson’s disease, I expanded those notes in a new tab on my research doc. I covered its definition, statistics in the American population, and its difficult detection, caused by a reliance on self-reporting and several possible factors that come with cases of olfactory dysfunction. Furthermore, I found a general direction for my research. A big picture inquiry; “How can the occurence of non-motor conditions, primarily anosmia and REM sleep behavior disorder (RBD) be studied and used for the screening and early detection of Parkinson’s disease before the onset of motor dysfunction?” Alongside a comparative inquiry; “How can non-motor biomarkers shared by synucleinopathic disorders such as Alzheimer’s and Dementia with Lewy Bodies, be studied for early detection before the later stages of these conditions?” ")
    st.write("")


st.write("")
st.header("Ebuka Akobundu")
st.write("")
st.write("July 15th, 2026 – March 31st, 2027")
st.write("Sourcing UCI Biomarkers Dataset")
st.write("")
st.header("Table of Contents")
st.write("")
st.subheader("July 15th, 2026")
st.write("Writing Basic Notes to Understand Parkinson’s Disease")
st.write("")
st.subheader("August 2026")
st.write("Parsing Data Through Python (Pandas, Matplotlib) and Recording Research & Observations")
st.write("")
st.subheader("September 2026")
st.write("Recording Speech Metrics and Running The First Statistical Tests")
st.write("")
st.subheader("October 2026")
st.write("Running Comparisons and Corrections")
st.write("")
st.subheader("November 2026")
st.write("Running Corrections and Effect Sizes")
st.write("")
st.write("... more months coming soon ...")