import streamlit as st

st.set_page_config(
    page_title="GP Memory Coach",
    page_icon="🎓",
    layout="wide"
)

ESSAY = {
    1: {
        "title": "Introduction",
        "text": """
Main Thesis:
Technology is deeply integrated into modern life and creates both benefits and risks.
While society depends heavily on technology, humans are not completely at its mercy
because people can regulate, adapt, and shape technological development.

INTRODUCTION:
The Times feature was premised on Manjoo's realisation that the companies are impossible
to live without in the modern day. Technology has become an undeniable force in our lives,
transforming communication, commerce, entertainment and education. This pervasive influence
begs the question: to what extent are we at the mercy of technology?
""",
        "ideas": [
            "technology",
            "communication",
            "commerce",
            "education"
        ]
    },

    2: {
        "title": "Technology Empowers",
        "text": """
The relationship between humans and technology is complex, empowering us while also creating
new dependencies. The internet has revolutionised access to information, allowing individuals
worldwide to connect with vast knowledge resources. Educational materials are readily available
online, democratising access to learning.
""",
        "ideas": [
            "internet",
            "information",
            "worldwide",
            "knowledge",
            "learning"
        ]
    },

    3: {
        "title": "Communication Benefits",
        "text": """
Communication tools like video conferencing and instant messaging have shrunk geographical
distances, fostering collaboration and personal connections across borders.
""",
        "ideas": [
            "video conferencing",
            "instant messaging",
            "collaboration",
            "communication"
        ]
    },

    4: {
        "title": "Quality of Life",
        "text": """
Technological advancements have improved quality of life. Artificial intelligence and
automation reduce repetitive tasks. Medical technology has produced breakthroughs in
diagnosis and treatment, while electric vehicles support sustainability.
""",
        "ideas": [
            "artificial intelligence",
            "automation",
            "medical technology",
            "electric vehicles"
        ]
    },

    5: {
        "title": "Vulnerabilities",
        "text": """
Dependence on technology creates vulnerabilities. Cybersecurity threats include data breaches,
hacking and identity theft. Critical infrastructure can also be disrupted.
""",
        "ideas": [
            "cybersecurity",
            "data breaches",
            "hacking",
            "identity theft"
        ]
    },

    6: {
        "title": "Psychological Effects",
        "text": """
Technology can contribute to isolation, anxiety, depression and information overload.
Social media also enables the spread of misinformation and disinformation.
""",
        "ideas": [
            "social media",
            "anxiety",
            "isolation",
            "disinformation"
        ]
    },

    7: {
        "title": "Human Control",
        "text": """
Humans cannot predict every consequence of technology. Nevertheless, society is not
completely at technology's mercy because we can continually evaluate and adapt the way
technology is used.
""",
        "ideas": [
            "evaluate",
            "adapt",
            "society",
            "control"
        ]
    },

    8: {
        "title": "Conclusion",
        "text": """
Engineers, policymakers and business leaders can implement policies and improvements that
maximise benefits while minimising harm. Ultimately, humanity remains in control of how
technology shapes society.
""",
        "ideas": [
            "policymakers",
            "engineers",
            "regulation",
            "society"
        ]
    }
}

TRANSFER_QUESTIONS = [
    "Has technology improved our quality of life?",
    "Are humans too dependent on technology?",
    "Does technology connect or isolate people?",
    "Should governments regulate technology?",
    "Does social media do more harm than good?",
    "Is AI a threat or an opportunity?"
]


st.title("🎓 GP 4-Day Memory Coach")

paragraph_no = st.selectbox(
    "Select Paragraph",
    options=list(ESSAY.keys()),
    format_func=lambda x: f"Paragraph {x} - {ESSAY[x]['title']}"
)

current = ESSAY[paragraph_no]

st.subheader(f"Paragraph {paragraph_no}: {current['title']}")

st.info(current["text"])

st.subheader("Day 2 - Recall")

answer = st.text_area(
    "Write the paragraph from memory here:",
    height=300
)

if st.button("Check My Answer"):

    answer_lower = answer.lower()

    found = []
    missing = []

    for idea in current["ideas"]:
        first_word = idea.split()[0].lower()

        if first_word in answer_lower:
            found.append(idea)
        else:
            missing.append(idea)

    coverage = int(
        len(found) / len(current["ideas"]) * 100
    )

    if coverage >= 80:
        content = 8
    elif coverage >= 60:
        content = 6
    else:
        content = 4

    word_count = len(answer.split())

    if word_count >= 60:
        analysis = 8
    elif word_count >= 30:
        analysis = 6
    else:
        analysis = 4

    language = min(3 + len(found), 10)

    total = content + analysis + language

    if total >= 22:
        grade = "A"
    elif total >= 18:
        grade = "B"
    elif total >= 14:
        grade = "C"
    else:
        grade = "D"

    st.markdown("---")
    st.subheader("📊 A-Level GP Analysis")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Coverage", f"{coverage}%")
    col2.metric("Content", f"{content}/10")
    col3.metric("Analysis", f"{analysis}/10")
    col4.metric("Language", f"{language}/10")

    st.success(f"Estimated GP Grade: {grade}")

    st.subheader("✅ Ideas Remembered")

    if found:
        for item in found:
            st.write("•", item)
    else:
        st.write("None detected.")

    st.subheader("❌ Missing Ideas")

    if missing:
        for item in missing:
            st.write("•", item)
    else:
        st.write("Excellent recall!")

    st.subheader("💡 Improvements")

    st.write("• Add specific examples.")
    st.write("• Include evaluation and judgment.")
    st.write("• Develop deeper analysis.")
    st.write("• Link back to the question.")
    st.write("• Use stronger topic sentences.")

st.markdown("---")

st.subheader("Day 4 - Transfer Questions")

for question in TRANSFER_QUESTIONS:
    st.write("•", question)
