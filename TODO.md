# Website redesign: notes and to-dos

## Context
- Reference site: https://mustafakarabag.github.io/ (Academic Pages / Jekyll template)
- Personal site for Mustafa Karabag; new design with a similar structure
- Publications source: an Excel file (not yet in this folder)

## Decisions so far (defaults, changeable)
- Stack: plain HTML/CSS/JS, no Jekyll; a Python script builds the publications page from the Excel file
- Hosting: GitHub Pages
- Structure: sidebar profile, 2-item nav (Projects & Publications, CV), about page
- Publications: compact list grouped by year, tag filter chips, no thumbnails unless wanted
- Drop unused template material (sample talks, comments providers, .idea files)
- Dislikes the current papers layout (exact reasons not yet given)

## To-dos
(add items below as they come)

- [ ] Update paper list (from the Excel file)
- [ ] Create a projects page
- [ ] First page structure, in this order:
  - About me
  - Contact info
  - Research interests
  - Prospective students
  - Teaching (no content for now)
  - Lab (no content for now)
- [ ] Links to relevant research labs and universities
- [ ] Figures, GIFs and videos for papers
- [ ] Order papers by year, not by paper type
- [ ] Keep the tag structure; change the link color to a darker shade of blue
- [ ] Confirm USF start date, office/address, and whether to switch the email from utexas.edu
- [ ] Add Center for Autonomy / Prof. Topcu links; write the prospective-students note (relevant now that this is a faculty role)
- [x] Publications now built from the Excel file (build/publications.xlsx)
- [ ] Add GIFs/videos: put files in media/ and set the paper's media field (13 of 31 papers have figures now)
