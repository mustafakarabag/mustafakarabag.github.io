"""Writes index.html and publications.html (shared header + sidebar)."""
from pathlib import Path
root = Path(__file__).resolve().parent.parent

def page(title, active, body, scripts=""):
    nav = lambda f, l: f'<a href="{f}"{" class=active" if f == active else ""}>{l}</a>'
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | Mustafa O. Karabag</title><link rel="stylesheet" href="style.css"></head>
<body>
<header class="topbar"><nav><a class="name" href="index.html">Mustafa O. Karabag</a>
{nav("index.html", "About me")}{nav("publications.html", "Publications")}</nav></header>
<div class="layout">
<aside class="sidebar"><div class="photo"><img src="media/photo.jpg" alt="Mustafa O. Karabag"></div><h1>Mustafa O. Karabag</h1>
<p class="role">Research Associate<br><a href="https://oden.utexas.edu">Oden Institute</a>, <a href="https://www.utexas.edu">UT Austin</a></p><p class="role">Joining <a href="https://www.usf.edu/engineering/ece/">Electrical &amp; Computer Engineering</a>, <a href="https://www.usf.edu">University of South Florida</a>, Spring 2027</p>
<ul class="contact-links"><li><a href="mailto:karabag@utexas.edu"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg>Email</a></li>
<li><a href="https://scholar.google.com/citations?user=PbKuWIwAAAAJ&hl=en&oi=sra"><svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true"><path d="M12 3L1 9l11 6 9-4.9V17h2V9L12 3zM5 13.2v4L12 21l7-3.8v-4L12 17l-7-3.8z"/></svg>Google Scholar</a></li>
<li><a href="https://github.com/mustafakarabag"><svg viewBox="0 0 16 16" width="18" height="18" fill="currentColor" aria-hidden="true"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>GitHub</a></li>
</ul></aside>
<main>{body}</main></div>{scripts}</body></html>'''

index = '''<h2>About me</h2>
<p>I am a Research Associate at the <a href="https://oden.utexas.edu">Oden Institute</a> at the University of Texas at Austin. I will join the <a href="https://www.usf.edu/engineering/ece/">Department of Electrical and Computer Engineering</a> at the University of South Florida as an Assistant Professor in Spring 2027. My research develops theoretical foundations and algorithms for decision-making and learning in strategic autonomous systems, drawing on control theory, artificial intelligence, optimization, and game theory.</p>
<p>Previously, I was a postdoctoral fellow at the Oden Institute and a lecturer in the Department of Aerospace Engineering and Engineering Mechanics at the University of Texas at Austin. I did my PhD in Electrical &amp; Computer Engineering at the University of Texas at Austin, advised by <a href="https://ae.utexas.edu/person/ufuk-topcu/">Prof. Ufuk Topcu</a>, as a member of the <a href="https://autonomy.oden.utexas.edu">Center for Autonomy</a>. Prior to my PhD, I obtained a BSc degree in Electrical &amp; Electronics Engineering and a minor degree in Economics from <a href="https://www.boun.edu.tr">Bogazici University</a>.</p>
<h2>Research interests and current research areas</h2>
<p>I am interested in developing theoretical foundations and algorithms for multiagent interactions in information-scarce and adversarial environments. Some of my current research areas are:</p>
<ul>
<li>analyzing deception and counter-deception in sequential decision-making, and safeguarding systems against adversaries</li>
<li>developing decision-making, optimization, and learning methods that rely on minimal information from other agents</li>
<li>understanding and improving how generative AI models interact in strategic, multiagent settings</li>
<li>designing agent behavior that conveys intent to other agents and humans, and characterizing the optimal tradeoff between task performance and signaling</li>
</ul>
<h2>Contact info</h2>
<p>Email: <a href="mailto:karabag@utexas.edu">karabag@utexas.edu</a><br>
Oden Institute, The University of Texas at Austin<br>Starting Spring 2027: Department of Electrical and Computer Engineering, University of South Florida<!-- TODO: office / address; the utexas.edu email may change after the move --></p>
<h2>Prospective students</h2>
<p><strong>I am looking to recruit PhD students to join my group at USF ECE in Fall 2027.</strong> If you are interested, send me an email at karabag@utexas.edu with (i) a description of your research interests, (ii) your transcript (an unofficial copy), (iii) your CV, and (iv) any supporting document related to your background and research expertise.</p>
<p>Please use the title &ldquo;USF - Prospective PhD Student&rdquo; for your email. Emails entirely written by AI tools are likely to be ignored.</p>
<h2>Teaching</h2>
<ul>
<li>[UT Austin] ASE 370C - Feedback Control Systems - Spring 2025</li>
</ul>'''

pubs = '''<h2>Publications</h2>
<p>Papers are listed by year, newest first. Filter by topic with the tags below.</p>
<div class="chips" id="chips"></div><div id="pubs"></div>'''

(root / "index.html").write_text(page("About", "index.html", index))
(root / "publications.html").write_text(page("Publications", "publications.html", pubs, '<script src="data/publications.js"></script><script src="app.js"></script>'))
