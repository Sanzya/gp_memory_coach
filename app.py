from flask import Flask, request

app = Flask(__name__)

ESSAY = {
    1: {
        "title": "Introduction",
        "text": """
Main Thesis:
 Technology is deeply integrated into modern life and creates both benefits and risks. While society depends heavily on technology, humans are not completely at its mercy because people can regulate, adapt, and shape technological development.

"text": """

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


@app.route("/", methods=["GET", "POST"])
def home():

    paragraph_no = int(request.values.get("paragraph", 1))

    if paragraph_no not in ESSAY:
        paragraph_no = 1

    current = ESSAY[paragraph_no]

    report = ""

    if request.method == "POST":

        answer = request.form.get("answer", "").lower()

        found = []
        missing = []

        for idea in current["ideas"]:

            first_word = idea.split()[0].lower()

            if first_word in answer:
                found.append(idea)
            else:
                missing.append(idea)

        coverage = int(
            len(found) / len(current["ideas"]) * 100
        )

        # Content
        if coverage >= 80:
            content = 8
        elif coverage >= 60:
            content = 6
        else:
            content = 4

        # Analysis
        word_count = len(answer.split())

        if word_count >= 60:
            analysis = 8
        elif word_count >= 30:
            analysis = 6
        else:
            analysis = 4

        # Language
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

        report = f"""
        <div class='card'>
            <h2>📊 A-Level GP Analysis</h2>

            <p><b>Coverage:</b> {coverage}%</p>
            <p><b>Content:</b> {content}/10</p>
            <p><b>Analysis:</b> {analysis}/10</p>
            <p><b>Language:</b> {language}/10</p>

            <h3>Estimated GP Grade: {grade}</h3>

            <h3>✅ Ideas Remembered</h3>
            <ul>
                {''.join(f'<li>{x}</li>' for x in found)}
            </ul>

            <h3>❌ Missing Ideas</h3>
            <ul>
                {''.join(f'<li>{x}</li>' for x in missing)}
            </ul>

            <h3>💡 Improvements</h3>
            <ul>
                <li>Add examples.</li>
                <li>Add evaluation.</li>
                <li>Develop analysis.</li>
                <li>Link back to the question.</li>
            </ul>
        </div>
        """

    options = ""

    for num in ESSAY:

        selected = ""

        if num == paragraph_no:
            selected = "selected"

        options += f"""
        <option value="{num}" {selected}>
        Paragraph {num} - {ESSAY[num]['title']}
        </option>
        """

    transfer_html = ""

    for q in TRANSFER_QUESTIONS:
        transfer_html += f"<li>{q}</li>"

    return f"""
<!DOCTYPE html>
<html>

<head>
<title>GP Memory Coach</title>

<style>

body {{
    font-family: Arial;
    margin:40px;
    background:#f5f6fa;
}}

.card {{
    background:white;
    padding:20px;
    margin-bottom:20px;
    border-radius:10px;
    box-shadow:0 0 8px rgba(0,0,0,0.1);
}}

textarea {{
    width:100%;
    height:300px;
}}

button {{
    background:#0078d7;
    color:white;
    border:none;
    padding:10px 20px;
    border-radius:5px;
}}

</style>
</head>

<body>

<h1>🎓 GP 4-Day Memory Coach</h1>

<div class="card">

<form method="POST">

<h2>Select Paragraph</h2>

<select name="paragraph" onchange="this.form.submit()">

{options}

</select>

<h2>
Paragraph {paragraph_no}: {current['title']}
</h2>

<p>{current['text']}</p>

<h3>Day 2 - Recall</h3>

<textarea
name="answer"
placeholder="Write the paragraph from memory here..."
></textarea>

<br><br>

<button type="submit">
Check My Answer
</button>

</form>

</div>

{report}

<div class="card">
<h2>Day 4 - Transfer Questions</h2>

<ul>
{transfer_html}
</ul>

</div>

</body>
</html>
"""


if __name__ == "__main__":
    app.run(debug=True)