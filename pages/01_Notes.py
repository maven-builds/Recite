import streamlit as st

st.set_page_config(page_title = "Wonder Doc")

st.title("Early Research Notes")
st.write("")
st.subheader("Here, you can check out my notes from the initial phases of my project.")
st.write("")

st.subheader("Explore Literature Review & Observations")
selectNotes = st.pills("", options = ["Research (PD)", "Research (Anosmia)", "Research (RBD)", "UCI Observations", "Inquiries"])

if selectNotes == "Research (PD)":
    st.write("")

    with open("research_pd.pdf", "rb") as pdf_file:
        st.download_button(
            label = "Download Research (PD) as a PDF",
            data=pdf_file,
            file_name="research_pd.pdf",
            mime="application/pdf")

    st.write("")
    st.header("1. What is Parkinson's Disease?")
    st.write("")
    st.subheader("- My Understanding")
    st.write("")
    st.write("Parkinson’s disease is a progressive neurological disease that involves the death of dopamine-producing nerve cells. Dopamine is a powerful neurochemical that plays a major role in movement, and the death of the nerve cells that produces them results in flaws in the movement of a patient, ranging from tremors to slow reaction.")
    st.write("")
    st.subheader("- Definition")
    st.write("")
    st.write("Parkinson’s disease is a progressive, incurable movement disorder of the nervous system. Symptoms begin as barely noticeable tremors and slight stiffness, evolving into slurred speech and slowed movement (bradykinesia). ")
    st.write("")
    st.header("2. What Are The Numbers?")
    st.write("")
    st.write("According to the Government of Canada, sourcing data from the 2022-2023 fiscal year, 530 of 100,000 Canadians over the age of 40 lived with some form of Parkinsonism, a category of movement disorders, of which 3 out of 5 were men. Around 38 Canadians are diagnosed with Parkinsonism daily, with 8 out of 10 Canadians over the age of 65 being diagnosed.")
    st.write("")
    st.write("In my home province of Nova Scotia, between 2015 and 2025, nearly a decade, cases of diagnosed Parkinsonism remained steady between 2015 and 2024, in both sexes over the age of 40. However, it is important to keep in mind that wait times for a diagnosis can account for multiple unrecorded numbers.")
    st.write("")
    st.header("3. What Are The Symptoms?")
    st.write("")
    st.write("Bradykinesia: In simple terms, this is slowed movement. Bradykinesia ranges from struggling to show facial expressions to having difficulty blinking.")
    st.write("")
    st.write("Freezing of Gait: This is a sudden, involuntary inability to move the feet in the event of activities such as walking down a narrow hallway. It rarely occurs during clinical evaluations, and it normally lasts a few seconds.")
    st.write("")
    st.write("Anosmia: An olfactory dysfunction, anosmia typically occurs 10 to 20 years prior to a formal PD diagnosis.")
    st.write("")
    st.write("REM Sleep Behavior Disorder: During the Rapid Eye Movement stage of sleep, the brain temporarily paralyzes the body, a state known as muscle atonia. This prevents the body from physically acting out vivid dreams. REM Sleep Behavior Disorder is chronologically similar to anosmia in that it occurs a decade or two prior to a formal PD diagnosis. The loss of muscle atonia leads to patients engaging in a range of actions during dreams, from simple twitches to more complex actions, such as kicking and fighting.")
    st.write("")
    st.header("4. Why Dopamine?")
    st.write("")
    st.write("Dopamine is a monoamine neurotransmitter and neurohormone. As a neurotransmitter, it acts as a “reward center” for many bodily functions. These functions are based on movement, memory, and motivation. As a neurohormone, dopamine is peripherally responsible for the vasodilation and vasoconstriction of blood vessels, regulating the removal of sodium and urine from the body, reducing the amount of insulin produced by the pancreas, slowing the movement of contents in the gastrointestinal (GI) tract, and reducing lymphocyte activity in the immune system.")
    st.write("")
    st.write("As it is responsible for movement and motivation, the depletion of dopamine results in poor movement (tremors, bradykinesia) and an increase in apathy, which is why many PD patients can often “do nothing” for some time without feeling positive or negative about the inactivity. The depletion of dopamine is the cause of many neurological disorders, which is why PD will often coincide with other conditions, such as dementia. Furthermore, the depletion of dopamine leads to a loss in the quality of its functions, such as blood vessel and insulin regulation, which become immediate effects for patients.")

if selectNotes == "Research (Anosmia)":
    st.write("")

    with open("research_anosmia.pdf", "rb") as pdf_file:
            st.download_button(
                label = "Download Research (Anosmia) as a PDF",
                data=pdf_file,
                file_name="research_anosmia.pdf",
                mime="application/pdf")

    st.write("")        
    st.header("What is Anosmia?")
    st.write("")
    st.write("Anosmia is the complete inability to correctly identify odors. It can arise from certain genetics, such as the presence of polymorphisms (rare DNA sequence variations) in the OR7D4 gene, an olfactory receptor responsible for detecting steroid-based odors, such as androstenone. ")
    st.write("")
    st.write("Olfactory testing is not a staple of general health screening, and as such, diagnoses of a disorder like anosmia depend on self-reporting, which, in turn, depends on the individual in question’s ability to correctly identify their specific situation and their standard of “normal”. In most cases, the consensus appears to be that self-reporting individuals have clarity on what is “normal” for them, but they often have difficulty identifying what exactly is causing the issue.")
    st.write("")
    st.write("Anosmia as an isolated/idiopathic condition is quite rare, affecting around 3% of Americans over the age of 40, and only a minority of that demographic will go on to develop Parkinson’s disease. This is because any disruption to olfactory functioning can be attributed to a wide variety of factors, from viral infections to aging.")

if selectNotes == "Research (RBD)":
     st.write("")
     with open("research_rbd.pdf", "rb") as pdf_file:
                 st.download_button(
                     label = "Download Research (RBD) as a PDF",
                     data=pdf_file,
                     file_name="research_rbd.pdf",
                     mime="application/pdf")
     st.write("")            
     st.header("1. What is Rapid Eye Movement?")
     st.write("")
     st.write("Rapid Eye Movement (REM) is the phase of sleep during which vivid dreams occur, denoted by the rapid movement of the eyes under closed lids. During REM, eyes have been proposed to move in a manner as if tracking and observing the environment around them, as if the sleeping individual were awake. Dreams give individuals visuals to process during sleep, and as such, the eyes respond by moving as if those visuals were real, at least in some theories. ")
     st.write("")
     st.header("2. Understanding Muscle Atonia")
     st.write("")
     st.write("During REM, the brain temporarily paralyzes the body to prevent you from acting out physically in response to this stage’s active dreams. During atonia, the skeletal muscles are severely relaxed with decreased tone. This hypotonic state is the main element of paralysis. Beyond the muscles associated with full-body movement, atonia also requires cooperation between numerous neurotransmitters to occur.")
     st.write("")
     st.write("Despite its fascinating nature, the direct or dominant cause(s) of atonia remain a mystery. Glycinergic inhibition has once been floated around as a popular theory, but recent studies have labeled the belief incomplete, concluding that glycine plays a minimal role during atonia, with the lack of impact on masseter muscles being a point of evidence.")
     st.write("")
     st.header("3. Understanding REM Sleep Behavior Disorder")
     st.write("")
     st.write("REM Sleep Behavior Disorder (RBD) is a form of parasomnia defined by the loss of muscle atonia during the Rapid Eye Movement stage of sleep. It is highly indicative of the acquisition of neurodegenerative disorders, such as Parkinson’s disease among other synucleinopathic conditions, in the future. RBD can be idiopathic, drug-induced, or secondary to another medical condition. When idiopathic, it is most suggestive of future neurodegenerative disorders as it theoretically involves abnormal links between the brainstem’s control of atonia and the cortex.")
     st.write("")
     st.header("4. What are the Demographics?")
     st.write("")
     st.write("Overall, confirmed RBD cases account for around 1% of a surveyed ~30,000 respondents within Canada, with the majority of diagnoses being of men over the age of 50. This implies that RBD becomes more likely with the degenerative effects of aging, often accelerated by the use of drugs. The figure of 1% accounts for all forms of RBD, and as such, we can infer that the total number of recorded cases of idiopathic RBD represents a super-minority of the total population. ")
     st.write("")
     st.write("Cases of possible RBD are more equal when comparing both sexes. However, in isolation, RBD can be thought of as a familiar non-motor marker of future synucleinopathies, occurring decades before the formal diagnosis of a neurodegenerative disorder.")
     st.write("")
     st.header("5. Understanding the Pathophysiology of RBD")
     st.write("")
     st.write("As mentioned before, the primary marker of RBD is the loss of muscle atonia during sleep. Atonia takes place when the inhibitory interneurons of the spinal cord are activated by the release of glutamate, an excitatory neurotransmitter. The axons of glutamatergic neurons latch onto the inhibitory neurons of the spinal cord, specifically the ventral horn running from the base of the brain and through the neck and back.")
     st.write("")
     st.write("Once this synapse occurs, glutamate binds to the AMPA (alpha-amino-3-hydroxy-5-methyl-4-isooxazole-propionic acid) and NMDA (N-methyl-D-aspartate) receptors of these interneurons, leading to the influx of positive sodium and calcium ions. This influx then leads to the release of the inhibitory neurotransmitters glycine and gamma-aminobutyric acid (GABA).")
     st.write("")
     st.write("Muscle atonia is an intricate mechanism dependent on several known and unseen factors that primarily involve the brainstem. As such, the loss of this hypotonic state, leading to the physical enactment of dreams, is a failure of one of the required processes needed to achieve that state.")