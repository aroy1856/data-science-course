from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Helvetica has no ₹ glyph; Arial Unicode does (macOS system font).
pdfmetrics.registerFont(TTFont("ArialUnicode", "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"))

path = "Rajasthan_Desert_Trip_January_2027.pdf"

doc = SimpleDocTemplate(
    path, pagesize=A4,
    rightMargin=16*mm, leftMargin=16*mm,
    topMargin=15*mm, bottomMargin=15*mm
)

styles = getSampleStyleSheet()
title = ParagraphStyle("TitleCustom", parent=styles["Title"], fontSize=25, leading=30, alignment=TA_CENTER, spaceAfter=8)
subtitle = ParagraphStyle("Subtitle", parent=styles["Normal"], fontSize=11, leading=16, alignment=TA_CENTER, textColor=colors.HexColor("#555555"), spaceAfter=18)
h1 = ParagraphStyle("H1", parent=styles["Heading1"], fontSize=17, leading=21, spaceBefore=10, spaceAfter=8)
h2 = ParagraphStyle("H2", parent=styles["Heading2"], fontSize=12.5, leading=16, spaceBefore=6, spaceAfter=5)
body = ParagraphStyle("Body", parent=styles["BodyText"], fontName="ArialUnicode", fontSize=9.5, leading=14, spaceAfter=5)
small = ParagraphStyle("Small", parent=body, fontName="ArialUnicode", fontSize=8.5, leading=12)
day = ParagraphStyle("Day", parent=h2, fontSize=13, textColor=colors.HexColor("#8B5E34"))

story = []

story += [
    Paragraph("RAJASTHAN DESERT ESCAPE", title),
    Paragraph("8-Day Family Itinerary • January 2027", subtitle),
    Paragraph("<b>Kolkata → Jaipur → Jodhpur → Jaisalmer → Sam Sand Dunes → Kolkata</b>", 
              ParagraphStyle("route", parent=body, fontSize=12, alignment=TA_CENTER, spaceAfter=14)),
    Paragraph("A comfortable, family-friendly Rajasthan trip focused on forts, heritage cities and the Thar Desert.", 
              ParagraphStyle("intro", parent=body, fontSize=10.5, leading=16, alignment=TA_CENTER)),
    Spacer(1, 10),
]

overview = [
    ["Trip length", "8 days / 7 nights"],
    ["Suggested dates", "Around 16–24 January 2027"],
    ["Travellers", "Budget assumption: 4 people"],
    ["Best season", "January — pleasant days, cold desert nights"],
    ["Main route", "Jaipur → Jodhpur → Jaisalmer → Sam"],
    ["Transport", "Flights + private intercity cab"],
]
t = Table(overview, colWidths=[42*mm, 125*mm])
t.setStyle(TableStyle([
    ("BACKGROUND",(0,0),(0,-1),colors.HexColor("#F1E8DC")),
    ("GRID",(0,0),(-1,-1),0.4,colors.HexColor("#D5C7B7")),
    ("FONTNAME",(0,0),(0,-1),"Helvetica-Bold"),
    ("FONTNAME",(1,0),(1,-1),"Helvetica"),
    ("FONTSIZE",(0,0),(-1,-1),9.5),
    ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
    ("TOPPADDING",(0,0),(-1,-1),7),
    ("BOTTOMPADDING",(0,0),(-1,-1),7),
]))
story.append(t)

story += [PageBreak(), Paragraph("THE 8-DAY ITINERARY", h1)]

days = [
("Day 1 — Kolkata → Jaipur", [
    "<b>Morning/Afternoon:</b> Fly Kolkata (CCU) → Jaipur (JAI).",
    "<b>Check-in:</b> Comfortable hotel in Jaipur.",
    "<b>Evening:</b> Hawa Mahal exterior, Johari/Bapu Bazaar and relaxed local dinner.",
    "<b>Stay:</b> Jaipur."
]),
("Day 2 — Jaipur Heritage Day", [
    "Amber Fort → Jaigarh Fort → City Palace → Jantar Mantar → Hawa Mahal.",
    "Optional: Nahargarh Fort around sunset if the family still has energy.",
    "Keep the evening relaxed rather than adding too many attractions.",
    "<b>Stay:</b> Jaipur."
]),
("Day 3 — Jaipur → Jodhpur", [
    "<b>Morning:</b> Depart Jaipur by private car.",
    "Drive to Jodhpur; stop for lunch en route.",
    "<b>Evening:</b> Clock Tower and Sardar Market; explore the Blue City/old lanes.",
    "<b>Stay:</b> Jodhpur."
]),
("Day 4 — Jodhpur Forts & Palaces", [
    "Mehrangarh Fort → Jaswant Thada → Umaid Bhawan Palace museum.",
    "Late afternoon: Blue City viewpoint / old-city walk.",
    "Optional: rooftop dinner with a Mehrangarh view.",
    "<b>Stay:</b> Jodhpur."
]),
("Day 5 — Jodhpur → Jaisalmer", [
    "<b>Morning:</b> Drive to Jaisalmer.",
    "Optional stop at Osian if the family wants another heritage/temple experience.",
    "<b>Evening:</b> Jaisalmer Fort and surrounding lanes.",
    "<b>Stay:</b> Jaisalmer."
]),
("Day 6 — Jaisalmer City", [
    "Gadisar Lake → Patwon Ki Haveli → Salim Singh Ki Haveli → Nathmal Ki Haveli.",
    "Relaxed afternoon at the hotel.",
    "Evening: Fort/market walk and local Rajasthani dinner.",
    "<b>Stay:</b> Jaisalmer."
]),
("Day 7 — Sam Sand Dunes Desert Experience", [
    "<b>2:30–3:00 PM:</b> Leave Jaisalmer for Sam Sand Dunes.",
    "<b>Late afternoon:</b> Camel safari (about 30–60 minutes).",
    "Optional jeep safari if the family wants more adventure.",
    "<b>Sunset:</b> Watch the dunes at sunset.",
    "<b>Night:</b> Desert camp, Rajasthani dinner, folk dance/puppet show, bonfire and stargazing.",
    "<b>Stay:</b> Desert camp."
]),
("Day 8 — Desert Sunrise → Return", [
    "Early desert sunrise and breakfast.",
    "Return to Jaisalmer.",
    "Optional: Kuldhara or Desert National Park if flight timing permits.",
    "<b>Return:</b> Prefer Jaisalmer → Delhi → Kolkata if the fare is attractive; otherwise compare other one-stop options."
]),
]

for heading, bullets in days:
    elems = [Paragraph(heading, day)]
    elems += [Paragraph("• " + x, body) for x in bullets]
    story.append(KeepTogether(elems))
    story.append(Spacer(1, 4))

story += [PageBreak(), Paragraph("HOTEL PLAN", h1)]
hotel_rows = [
    ["City", "Recommended style", "Planning target / night"],
    ["Jaipur", "WelcomHeritage Traditional Haveli or similar", "₹5,000–₹7,000"],
    ["Jodhpur", "Ajit Bhawan or similar", "₹6,000–₹9,000"],
    ["Jaisalmer", "WelcomHeritage Mandir Palace or similar", "₹5,000–₹8,000"],
    ["Sam Dunes", "Good-quality AC desert camp", "₹8,000–₹12,000+ / tent"],
]
ht = Table(hotel_rows, colWidths=[28*mm, 88*mm, 51*mm], repeatRows=1)
ht.setStyle(TableStyle([
    ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#6B4F3A")),
    ("TEXTCOLOR",(0,0),(-1,0),colors.white),
    ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),
    ("FONTNAME",(0,1),(-1,-1),"ArialUnicode"),
    ("GRID",(0,0),(-1,-1),0.4,colors.HexColor("#D5C7B7")),
    ("FONTSIZE",(0,0),(-1,-1),8.8),
    ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
    ("TOPPADDING",(0,0),(-1,-1),7),
    ("BOTTOMPADDING",(0,0),(-1,-1),7),
]))
story.append(ht)
story += [
    Spacer(1,10),
    Paragraph("Budget notes", h2),
    Paragraph("These are planning targets rather than guaranteed January quotes. January prices vary by exact date, room configuration and availability. Travelling after the New Year period generally avoids the highest festive-season rates.", body),
    Paragraph("RTDC reference pricing found for the 2026–27 season indicates that Moomal Jaisalmer and Sam Dhani can be substantially cheaper alternatives, although availability and exact January tariffs should be checked before booking.", body),
]

story += [PageBreak(), Paragraph("BUDGET — FAMILY OF 4", h1)]
budget_rows = [
    ["Category", "Estimated total"],
    ["Kolkata → Jaipur flights", "₹45,000–₹60,000"],
    ["Return flights (JSA → DEL → CCU target)", "₹44,000–₹52,000"],
    ["Private intercity cab", "₹35,000–₹45,000"],
    ["City hotels", "₹40,000–₹55,000"],
    ["Desert camp", "₹10,000–₹18,000"],
    ["Food", "₹20,000–₹25,000"],
    ["Sightseeing / activities", "₹10,000–₹15,000"],
    ["Miscellaneous", "₹5,000–₹8,000"],
    ["Comfortable target", "≈ ₹2.3–₹2.7 lakh"],
]
bt = Table(budget_rows, colWidths=[110*mm, 57*mm], repeatRows=1)
bt.setStyle(TableStyle([
    ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#6B4F3A")),
    ("TEXTCOLOR",(0,0),(-1,0),colors.white),
    ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),
    ("FONTNAME",(0,1),(-1,-1),"ArialUnicode"),
    ("GRID",(0,0),(-1,-1),0.4,colors.HexColor("#D5C7B7")),
    ("FONTSIZE",(0,0),(-1,-1),9),
    ("BACKGROUND",(0,-1),(-1,-1),colors.HexColor("#F1E8DC")),
    ("TOPPADDING",(0,0),(-1,-1),7),
    ("BOTTOMPADDING",(0,0),(-1,-1),7),
]))
story.append(bt)
story += [
    Spacer(1,12),
    Paragraph("Flight strategy", h2),
    Paragraph("Because Jaisalmer → Kolkata can be expensive, compare a protected one-stop JSA → DEL → CCU itinerary against other one-stop options. A target of roughly ₹11,000–₹13,000 per person for the return is reasonable to watch for. If buying separate JSA → DEL and DEL → CCU tickets, leave a large buffer in Delhi.", body),
    Paragraph("The earlier Skyscanner search link appeared to have an unusual date encoding, so exact fares should be rechecked using the intended January dates and the correct number of passengers.", small),
]

story += [PageBreak(), Paragraph("JANUARY TRAVEL TIPS", h1)]
tips = [
    ("Desert nights", "Carry thermals, a fleece/jacket, warm socks and a cap. The desert can feel much colder after sunset."),
    ("Desert camp", "For a family trip, prioritize clean bathrooms, proper bedding, heating arrangements and good reviews over the cheapest tent."),
    ("Camel safari", "A 30–60 minute ride is enough for most families; combine it with sunset rather than making the safari the whole experience."),
    ("Driving", "Use a private cab for Jaipur → Jodhpur → Jaisalmer. It gives flexibility for stops and avoids train/taxi coordination."),
    ("Pacing", "Do not overload Jaisalmer. The desert overnight is the highlight, so keep Day 6 relatively relaxed."),
    ("Flights", "Book the return only after comparing JSA → DEL → CCU with JSA → CCU and JSA → JAI/JDH alternatives."),
]
for title_txt, text in tips:
    story.append(Paragraph(f"<b>{title_txt}:</b> {text}", body))

story += [
    Spacer(1,12),
    Paragraph("TRIP AT A GLANCE", h1),
    Paragraph("<b>Jaipur:</b> forts + palaces + markets", body),
    Paragraph("<b>Jodhpur:</b> Mehrangarh + Blue City + royal heritage", body),
    Paragraph("<b>Jaisalmer:</b> Golden Fort + havelis + Gadisar Lake", body),
    Paragraph("<b>Sam:</b> camel safari + sunset + desert camp + folk culture + stargazing", body),
    Spacer(1,15),
    Paragraph("Planning assumption: family of 4, January 2027, comfortable rather than luxury travel. Airfares and hotel prices are dynamic and should be checked again before booking.", small),
]

def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(colors.HexColor("#777777"))
    canvas.drawCentredString(A4[0]/2, 8*mm, f"Rajasthan Desert Escape • Page {doc.page}")
    canvas.restoreState()

doc.build(story, onFirstPage=footer, onLaterPages=footer)

print(f"[Download the PDF](sandbox:{path})")
