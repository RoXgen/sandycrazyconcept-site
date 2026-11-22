"""Construit en/index.html (version anglaise) à partir de index.html.

Usage : python3 outils/version-anglaise.py
Chaque texte français doit être trouvé tel quel dans index.html : si un texte change
en français, mettre à jour sa traduction ici, puis relancer le script.
"""
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
CID = "https://maps.google.com/?cid=7879985521520299105"

SOINS = [
    dict(cle="huiles", nom="Warm organic essential oil massage", lignes=[("30&nbsp;min", "€40"), ("60&nbsp;min", "€70")],
         histoire="Scented oils have accompanied massage since Antiquity, from Egypt to Greece. The word “aromatherapy” was coined in France in the 1930s by the chemist René-Maurice Gattefossé. Here, the organic oils are warmed before the treatment: their warmth envelops the whole body.",
         bienfaits=["Helps release everyday tension", "A warmth that relaxes deeply", "Nourished, delicately scented skin"]),
    dict(cle="cranien", nom="Sérénita head massage", lignes=[("20&nbsp;min", "€30")],
         histoire="Head massage comes from an Indian family tradition, passed down through the generations. It became known in the West in the late 20th century as “champissage”. Fingers work over the scalp, the neck and the shoulders.",
         bienfaits=["Calms a busy mind", "Relaxes the neck and shoulders", "A short, restorative break"]),
    dict(cle="visage", nom="Sérénita facial", detail="with Chilean rosehip oil", lignes=[("20&nbsp;min", "€30")],
         histoire="Rosehip grows wild in the Andes. In Chile, its seeds are pressed to make a precious oil, known for caring for the skin. The treatment pairs it with slow movements across the whole face.",
         bienfaits=["Relaxes the features and the jaw", "Nourished, supple skin", "Twenty minutes of complete calm"]),
    dict(cle="reflexologie", nom="Sérénita foot and hand reflexology", lignes=[("20&nbsp;min", "€30")],
         histoire="Massaging the feet and hands is a very old practice. Modern reflexology was born in 1913 in the United States, when the physician William Fitzgerald described “zones” of the body linked to the feet and hands. In the 1930s, Eunice Ingham drew the maps of the feet still used today. The treatment uses gentle pressure on the feet and hands.",
         bienfaits=["Deep relaxation, from head to toe", "Lighter feet and hands", "Twenty minutes to refocus"]),
    dict(cle="dos", nom="Back and neck massage", lignes=[("40&nbsp;min", "€50")],
         histoire="Our backs carry the weight of our days: screens, lifting, stress. This treatment focuses where tension builds up most, from the lower back to the neck.",
         bienfaits=["Targets the tensest areas", "Helps loosen the neck and shoulders", "A feeling of lightness as you leave"]),
    dict(cle="prenatal", nom="Sérénita pregnancy and postnatal", lignes=[("60&nbsp;min", "€80")],
         histoire="In many cultures, pregnant women and new mothers receive massages to see them through this unique time. This treatment carries on that tradition: a suitable set-up, gentle movements and time for yourself.",
         bienfaits=["Eases the feeling of heavy legs and a loaded back", "A calm moment during pregnancy", "After the birth, reconnect with your body"],
         note="During pregnancy, talk to your midwife or doctor before your appointment."),
    dict(cle="monde", nom="Massages of the world", detail="Intuitive, energy-based treatment", lignes=[("60&nbsp;min", "€80")],
         histoire="Hawaiian lomi-lomi, Indian abhyanga, Swedish massage: every continent has its own way of touch. This intuitive, energy-based treatment draws on them and adapts to what your body expresses that day.",
         bienfaits=["A journey for the senses, without leaving Gruissan", "A treatment tuned to how you feel that day", "Deep relaxation of body and mind"]),
    dict(cle="quatre_mains", nom="Sérénita four-hand massage", detail="with Sandy and Sandra", lignes=[("45&nbsp;min", "€120")],
         histoire="Two companions, mirrored movements: with four hands, the body no longer knows which hand to follow and finally lets go. Sandy and Sandra synchronise their movements so that they become one.",
         bienfaits=["Letting go, faster", "A fully enveloping sensation", "A rare experience, to try at least once"]),
    dict(cle="duo", nom="Sérénita Duo", detail="with Sandy and Sandra", lignes=[("60&nbsp;min", "€140")],
         histoire="The duo is enjoyed by two, side by side: each person receives their own massage at the same time. A shared moment, as a couple, with friends or with family.",
         bienfaits=["Share a true moment of relaxation", "A lovely gift idea for two", "Each with their own massage, at the same pace"]),
    dict(cle="ventouses", nom="Cupping", detail="Chinese medicine", lignes=[("45&nbsp;min", "€60")],
         histoire="Cupping is one of the oldest known practices: traces of it are found in ancient Egypt and in ancient China, where animal horns, then bamboo, were used. Placed on the skin, the cups create a gentle suction.",
         bienfaits=["A feeling of release in tense areas", "An ancestral technique, revisited", "An invigorating treatment, unlike a classic massage"],
         note="Cupping can leave round marks for a few days."),
    dict(cle="skin_soul", nom="“Skin &amp; Soul” therapeutic massage", detail="by Sandy", lignes=[("90&nbsp;min", "€110")],
         histoire="“Skin &amp; Soul”, from the skin to the soul: Sandy’s signature massage, a treatment that is both physical and energetic, for the body, the soul and the mind. She puts her knowledge of the body and her attentiveness at the service of your well-being.",
         bienfaits=["The most complete treatment on the menu", "Body and mind, together", "All of Sandy’s expertise"]),
    dict(cle="transgenerationnel", nom="Transgenerational release session", lignes=[(None, "€50")],
         histoire="Transgenerational work starts from one idea: we also inherit the history of our ancestors. This session is the fruit of Sandy’s experience and her own research, after the things left unsaid about her father. It helps free and realign the maternal and feminine lines: that is the meaning of this release and realignment session.",
         bienfaits=["Step back from your family history", "Let go of what does not belong to you", "A caring time to listen and to talk"],
         note="This session does not replace medical or psychological care."),
]


def soin_html(soin):
    out = ['          <li class="soin">',
           '            <h3><button class="soin-bouton" type="button" data-fiche="%s" aria-haspopup="dialog">'
           '<span class="soin-nom">%s</span><span class="soin-plus" aria-hidden="true"></span></button></h3>' % (soin["cle"], soin["nom"])]
    if soin.get("detail"):
        out.append('            <p class="detail">%s</p>' % soin["detail"])
    for duree, prix in soin["lignes"]:
        if duree:
            out.append('            <p class="ligne"><span>%s</span><span class="points" aria-hidden="true"></span>'
                       '<span class="prix">%s</span></p>' % (duree, prix))
        else:
            out.append('            <p class="ligne ligne-seule"><span class="prix">%s</span></p>' % prix)
    out.append('            <div class="fiche" id="fiche-%s">' % soin["cle"])
    out.append('              <h4>Its story</h4>')
    out.append('              <p>%s</p>' % soin["histoire"])
    out.append('              <h4>Its benefits</h4>')
    out.append('              <ul class="fiche-bienfaits">')
    out.extend('                <li>%s</li>' % b for b in soin["bienfaits"])
    out.append('              </ul>')
    if soin.get("note"):
        out.append('              <p class="fiche-note">%s</p>' % soin["note"])
    out.append('            </div>')
    out.append('          </li>')
    return "\n".join(out) + "\n"


FAQ = [
    ("How do I book?", 'By phone, 7 days a week: Sandy on <a href="tel:+33677797272">+33 6 77 79 72 72</a> or Sandra on <a href="tel:+33646584847">+33 6 46 58 48 47</a>.'),
    ("Where is the treatment room?", 'Inside the Sunrise Beach Hôtel, 1 avenue des Courlis, Gruissan, facing Plage des Chalets. <a href="%s" target="_blank" rel="noopener">Get directions</a>.' % CID),
    ("What happens during a session?", "Each massage is adapted to your needs, your pain and how you feel. You talk it through with Sandy or Sandra before you begin."),
    ("What if I need to cancel?", "Please let us know at least 24&nbsp;hours in advance, by phone."),
    ("Can I have a massage while pregnant?", "Yes, that is what the Sérénita pregnancy and postnatal treatment (60&nbsp;min, €80) is for. Talk to your midwife or doctor before your appointment."),
    ("Are the massages suitable for children?", "Yes. Sérénita massages young and old alike, from babies to adults, including people with disabilities."),
    ("Can I give a massage as a gift?", 'Yes, with a <a href="#offrir">gift voucher</a> valid for 1&nbsp;year, paid at the salon by cash or card.'),
    ("How much does a massage cost?", 'From €30 for a 20-minute treatment to €140 for the Sérénita Duo. All prices are on <a href="#tarifs">the treatment menu</a>.'),
    ("Are these medical treatments?", "No. They are well-being treatments: they do not replace medical advice or treatment."),
]

# (texte français exact, traduction) — appliqués dans cet ordre
PAIRES = [
    ('<html lang="fr">', '<html lang="en">'),
    ("<title>Sérénita Gruissan – Massages et soins thérapeutiques avec Sandy et Sandra</title>",
     "<title>Sérénita Gruissan – Massages and therapeutic treatments with Sandy and Sandra</title>"),
    ('content="Massages et soins thérapeutiques à Gruissan avec Sandy et Sandra, 7 jours sur 7, dans leur espace soins du Sunrise Beach Hôtel, plage des Chalets. Massages aux huiles chaudes bio, visage, crânien, dos et cervicales, prénatal et postnatal, massages du monde, 4 mains, duo, ventouses, Skin &amp; Soul, soin transgénérationnel. Réservation par téléphone."',
     'content="Massages and therapeutic treatments in Gruissan with Sandy and Sandra, 7 days a week, in their treatment room at the Sunrise Beach Hôtel, Plage des Chalets. Warm organic oil massage, facial, head, back and neck, pregnancy and postnatal, massages of the world, four-hand, duo, cupping, Skin &amp; Soul, transgenerational session. Booking by phone."'),
    ('<link rel="canonical" href="https://sandycrazyconcept.fr/">', '<link rel="canonical" href="https://sandycrazyconcept.fr/en/">'),
    ('<meta property="og:url" content="https://sandycrazyconcept.fr/">', '<meta property="og:url" content="https://sandycrazyconcept.fr/en/">'),
    ('<meta property="og:locale" content="fr_FR">', '<meta property="og:locale" content="en_GB">'),
    ('content="Sérénita Gruissan – Massages et soins thérapeutiques"', 'content="Sérénita Gruissan – Massages and therapeutic treatments"'),
    ('content="Sandy et Sandra vous accueillent 7 jours sur 7 au Sunrise Beach Hôtel, à Gruissan."',
     'content="Sandy and Sandra welcome you 7 days a week at the Sunrise Beach Hôtel in Gruissan."'),
    ('"description": "Massages et soins thérapeutiques avec Sandy et Sandra, dans leur espace soins du Sunrise Beach Hôtel, à Gruissan."',
     '"description": "Massages and therapeutic treatments with Sandy and Sandra, in their treatment room at the Sunrise Beach Hôtel, Gruissan."'),
    ("Aller au contenu", "Skip to content"),
    ('aria-label="Sérénita Gruissan, retour en haut de la page"', 'aria-label="Sérénita Gruissan, back to top"'),
    ('aria-label="Menu principal"', 'aria-label="Main menu"'),
    ('<li><a href="#tarifs">Soins et tarifs</a></li>', '<li><a href="#tarifs">Treatments &amp; prices</a></li>'),
    ('<li><a href="#offrir">Bons cadeaux</a></li>', '<li><a href="#offrir">Gift vouchers</a></li>'),
    ('<li><a href="#lieu">Le lieu</a></li>', '<li><a href="#lieu">The place</a></li>'),
    ('<li><a href="#questions">Questions</a></li>', '<li><a href="#questions">FAQ</a></li>'),
    ('<a class="langue" href="en/" hreflang="en" lang="en" aria-label="English version">EN</a>',
     '<a class="langue" href="../" hreflang="fr" lang="fr" aria-label="Version française">FR</a>'),
    ('<a class="bouton bouton-plein" href="#contact">Prendre rendez-vous</a>', '<a class="bouton bouton-plein" href="#contact">Book now</a>'),
    ('aria-label="Sandy : découvrir son histoire"', 'aria-label="Sandy: discover her story"'),
    ('<span class="decouvrir">Son histoire</span>', '<span class="decouvrir">Her story</span>'),
    ('aria-label="Sandra : la découvrir"', 'aria-label="Sandra: discover"'),
    ('<span class="decouvrir">Découvrir</span>', '<span class="decouvrir">Discover</span>'),
    ("Massages &amp; soins thérapeutiques à Gruissan</h1>", "Massages &amp; therapeutic treatments in Gruissan</h1>"),
    ("Revenir à soi par le corps, le toucher et la présence, par des mains expertes qui écoutent là où les mots ne suffisent plus.",
     "Come back to yourself through the body, touch and presence, with expert hands that listen where words are no longer enough."),
    ('aria-label="Appeler pour prendre rendez-vous"', 'aria-label="Call to book"'),
    ('<span class="numero">06 77 79 72 72</span>', '<span class="numero">+33 6 77 79 72 72</span>'),
    ('<span class="numero">06 46 58 48 47</span>', '<span class="numero">+33 6 46 58 48 47</span>'),
    ("7 jours sur 7, au Sunrise Beach Hôtel, plage des Chalets", "7 days a week, at the Sunrise Beach Hôtel, Plage des Chalets"),
    ("5/5 sur Google, 26&nbsp;avis", "5/5 on Google, 26&nbsp;reviews"),
    (" (ouvre Google Maps)", " (opens Google Maps)"),
    ('alt="Ailes dorées sculptées sur un mur végétal"', 'alt="Golden carved wings on a plant wall"'),
    (">Notre approche</h2>", ">Our approach</h2>"),
    ("Chaque geste est une réponse. Votre corps parle, il est temps de l’écouter.", "Every gesture is an answer. Your body is speaking; it is time to listen."),
    ("«&#8239;Nous prenons soin de l’être dans sa globalité&#8239;: corps physique, corps émotionnel et corps énergétique.&#8239;»",
     "“We care for the whole person: physical body, emotional body and energy body.”"),
    ('alt="Une accompagnante Sérénita masse la nuque d’un client allongé, les yeux couverts"', 'alt="A Sérénita companion massages the neck of a client lying down, eyes covered"'),
    (">Des soins pour tous</h2>", ">Treatments for everyone</h2>"),
    ("Le bien-être n’a pas d’âge, ni de différence. Des massages et des soins pour tous, à chaque étape de la vie.",
     "Well-being has no age and makes no distinction. Massages and treatments for everyone, at every stage of life."),
    ("<li>Nourrissons</li>", "<li>Babies</li>"),
    ("<li>Enfants</li>", "<li>Children</li>"),
    ("<li>Femmes enceintes</li>", "<li>Pregnant women</li>"),
    ("<li>Adultes</li>", "<li>Adults</li>"),
    ("<li>Personnes en situation de handicap</li>", "<li>People with disabilities</li>"),
    ("<li>Personnes malades ou en accompagnement de fin de vie</li>", "<li>People who are ill or receiving end-of-life care</li>"),
    ('class="titre-centre">Soins et tarifs</h2>', 'class="titre-centre">Treatments &amp; prices</h2>'),
    ("Choisissez un soin pour découvrir son histoire et ses bienfaits.", "Choose a treatment to discover its story and its benefits."),
    ("Sur rendez-vous&nbsp;: appelez Sandy ou Sandra.</p>", "By appointment: call Sandy or Sandra.</p>"),
    ("Nos soins sont des soins de bien-être&nbsp;: ils ne remplacent pas un avis ou un traitement médical.",
     "Our treatments are well-being treatments: they do not replace medical advice or treatment."),
    ('<h3 id="fiche-titre">Soin</h3>', '<h3 id="fiche-titre">Treatment</h3>'),
    ('aria-label="Fermer la fiche"', 'aria-label="Close"'),
    ("Appeler Sandy", "Call Sandy"),
    ("Appeler Sandra", "Call Sandra"),
    # Bon cadeau : la carte reste en français (comme le bon remis au client) ; seuls les choix sont traduits
    ("<label for=\"bon-soin\">Adapter le bon au soin choisi</label>", "<label for=\"bon-soin\">Adapt the voucher to the chosen treatment</label>"),
    ('<option value="huiles-30">Massage aux huiles essentielles chaudes bio — 30 min</option>', '<option value="huiles-30">Warm organic essential oil massage — 30 min</option>'),
    ('<option value="huiles-60">Massage aux huiles essentielles chaudes bio — 60 min</option>', '<option value="huiles-60">Warm organic essential oil massage — 60 min</option>'),
    ('<option value="cranien">Crânien Sérénita — 20 min</option>', '<option value="cranien">Sérénita head massage — 20 min</option>'),
    ('<option value="visage">Visage Sérénita — 20 min</option>', '<option value="visage">Sérénita facial — 20 min</option>'),
    ('<option value="reflexologie">Réflexologie plantaire et palmaire Sérénita — 20 min</option>', '<option value="reflexologie">Sérénita foot and hand reflexology — 20 min</option>'),
    ('<option value="dos">Massage du dos et cervicales — 40 min</option>', '<option value="dos">Back and neck massage — 40 min</option>'),
    ('<option value="prenatal">Sérénita prénatal et postnatal — 60 min</option>', '<option value="prenatal">Sérénita pregnancy and postnatal — 60 min</option>'),
    ('<option value="monde">Massages du monde — 60 min</option>', '<option value="monde">Massages of the world — 60 min</option>'),
    ('<option value="quatre_mains">Sérénita 4 mains — 45 min</option>', '<option value="quatre_mains">Sérénita four-hand massage — 45 min</option>'),
    ('<option value="duo" selected>Duo Sérénita — 60 min</option>', '<option value="duo" selected>Sérénita Duo — 60 min</option>'),
    ('<option value="ventouses">Ventouses — 45 min</option>', '<option value="ventouses">Cupping — 45 min</option>'),
    ('<option value="skin_soul">Massage thérapeutique «&#8239;Skin &amp; Soul&#8239;» — 90 min</option>', '<option value="skin_soul">“Skin &amp; Soul” therapeutic massage — 90 min</option>'),
    ('<option value="transgenerationnel">Soin de dépouillement transgénérationnel</option>', '<option value="transgenerationnel">Transgenerational release session</option>'),
    ("<label for=\"bon-style\">Style du massage en duo</label>", "<label for=\"bon-style\">Duo massage style</label>"),
    ('<option value="monde" selected>Massage du monde</option>', '<option value="monde" selected>Massages of the world</option>'),
    ('<option value="huiles">Huiles essentielles chaudes bio</option>', '<option value="huiles">Warm organic essential oils</option>'),
    ("Aperçu du bon&nbsp;: Duo Sérénita — 60 min, Massage du monde.", "Voucher preview: Sérénita Duo — 60 min, Massages of the world."),
    (">Offrir un massage</h2>", ">Give a massage</h2>"),
    ("Un anniversaire, une future maman, un merci&nbsp;: offrez le soin de votre choix avec un bon cadeau Sérénita.",
     "A birthday, a mum-to-be, a thank-you: give the treatment of your choice with a Sérénita gift voucher."),
    ('<li>Choisissez le soin à offrir dans <a href="#tarifs">la carte</a>.</li>', '<li>Choose the treatment from <a href="#tarifs">the menu</a>.</li>'),
    ("<li>Appelez Sandy ou Sandra pour commander le bon.</li>", "<li>Call Sandy or Sandra to order the voucher.</li>"),
    ("<p>Le bon est valable 1&nbsp;an.</p>", "<p>The voucher is valid for 1&nbsp;year.</p>"),
    ("Sandy et Sandra vous reçoivent pour un massage en solo, en duo ou à quatre mains.", "Sandy and Sandra welcome you for a solo, duo or four-hand massage."),
    ('alt="Sandy et Sandra, de dos, en tenue Sérénita, pendant un massage à quatre mains"',
     'alt="Sandy and Sandra, seen from behind in Sérénita tops, during a four-hand massage"'),
    ('alt="Portrait de Sandra"', 'alt="Portrait of Sandra"'),
    ('<span class="parcours-quand">À 16&nbsp;ans</span>', '<span class="parcours-quand">At 16</span>'),
    ("Opérée d’une hernie discale (L5-S1), elle vit avec un handicap. Elle y gagne une connaissance profonde du corps.",
     "After surgery for a herniated disc (L5-S1), she lives with a disability. It gives her a deep knowledge of the body."),
    ('<span class="parcours-quand">Au laboratoire</span>', '<span class="parcours-quand">In the laboratory</span>'),
    ("Salariée du laboratoire (le plus ancien en prescription de phytothérapie et d’aromathérapie), elle suit des formations scientifiques très poussées sur le corps humain et l’ensemble de ses systèmes.",
     "Employed by the laboratory (the oldest in prescription herbal medicine and aromatherapy), she completes advanced scientific training on the human body and all of its systems."),
    ('<span class="parcours-quand">À la naissance</span>', '<span class="parcours-quand">At birth</span>'),
    ("Elle naît en siège&nbsp;: déjà, elle ne voulait pas venir au monde.", "She is born breech: already, she did not want to come into the world."),
    ('<span class="parcours-quand">À 40&nbsp;ans</span>', '<span class="parcours-quand">At 40</span>'),
    ("Elle apprend que son père n’est pas son père biologique. Cette découverte la pousse à étudier le transgénérationnel, devenu sa spécialité&nbsp;: il permet de libérer les lignées maternelle et paternelle, chez la femme comme chez l’homme. C’est le sens de son soin de dépouillement et de réalignement.",
     "She learns that her father is not her biological father. This discovery leads her to study transgenerational work, which has become her speciality: it helps free the maternal and paternal lines, for women and men alike. That is the meaning of her release and realignment session."),
    ('<span class="parcours-quand">Aujourd’hui</span>', '<span class="parcours-quand">Today</span>'),
    ("Maman de quatre enfants, sapeur-pompier volontaire et coach sportive diplômée d’État. Brisée dans tous ses corps, elle en tire une expertise juste et humble.",
     "Mother of four, volunteer firefighter and state-certified sports coach. Broken in all her bodies, she draws from it a fair and humble expertise."),
    ("Son massage signature&nbsp;: «&#8239;Skin &amp; Soul&#8239;».<br>Son soin signature&nbsp;: le dépouillement.", "Her signature massage: “Skin &amp; Soul”.<br>Her signature treatment: the transgenerational release."),
    ("«&#8239;Tu es la personne la plus importante de ta vie.&#8239;»", "“You are the most important person in your life.”"),
    ('<h2 id="titre-avis">Avis clients</h2>', '<h2 id="titre-avis">Customer reviews</h2>'),
    ('<span class="note-nombre">26 avis sur Google</span>', '<span class="note-nombre">26 reviews on Google</span>'),
    ("Vous êtes venu nous voir&nbsp;? Votre avis aide d’autres personnes à nous trouver.", "Have you visited us? Your review helps others find us."),
    (">Lire les avis</a>", ">Read the reviews</a>"),
    (">Donner votre avis</a>", ">Leave a review</a>"),
    ('alt="Massage dans l’espace soins Sérénita, face à la mer"', 'alt="Massage in the Sérénita treatment room, facing the sea"'),
    ('<h2 id="titre-lieu">Le lieu</h2>', '<h2 id="titre-lieu">The place</h2>'),
    ("«&#8239;Entre ciel et terre face à la mer, bercé par l’énergie de la Méditerranée.&#8239;»",
     "“Between sky and earth, facing the sea, cradled by the energy of the Mediterranean.”"),
    ("Notre espace soins se trouve à l’intérieur du Sunrise Beach Hôtel, face à la plage des Chalets.",
     "Our treatment room is inside the Sunrise Beach Hôtel, facing Plage des Chalets."),
    ('rel="noopener">Itinéraire</a>', 'rel="noopener">Directions</a>'),
    ('alt="Sunrise Beach Hôtel – ouvrir le site de l’hôtel"', 'alt="Sunrise Beach Hôtel – open the hotel’s website"'),
    ('<h2 id="titre-questions">Questions fréquentes</h2>', '<h2 id="titre-questions">Frequently asked questions</h2>'),
    ('<h2 id="titre-contact">Prendre rendez-vous</h2>', '<h2 id="titre-contact">Book an appointment</h2>'),
    ("Sur rendez-vous, 7 jours sur 7. Appelez Sandy ou Sandra.", "By appointment, 7 days a week. Call Sandy or Sandra."),
    ("<p>Sérénita Gruissan, massages et soins thérapeutiques</p>", "<p>Sérénita Gruissan, massages and therapeutic treatments</p>"),
    ('<p><a href="mentions-legales.html">Mentions légales</a></p>', '<p><a href="../mentions-legales.html" hreflang="fr">Legal notice (in French)</a></p>'),
    ('<nav class="barre-appel" aria-label="Appeler">', '<nav class="barre-appel" aria-label="Call">'),
]

CHEMINS = [
    ('href="favicon.png"', 'href="../favicon.png"'),
    ('href="apple-touch-icon.png"', 'href="../apple-touch-icon.png"'),
    ('href="fonts/', 'href="../fonts/'),
    ('href="css/', 'href="../css/'),
    ('src="js/', 'src="../js/'),
    ('src="img/', 'src="../img/'),
    ('srcset="img/', 'srcset="../img/'),
    (', img/', ', ../img/'),
]


def main():
    fr = (RACINE / "index.html").read_text(encoding="utf-8")
    en = fr

    # Carte des soins
    a = en.index('<ul class="soins">\n')
    b = en.index('        </ul>\n        <p class="rappel">', a)
    en = en[:a] + '<ul class="soins">\n' + "".join(soin_html(s) for s in SOINS) + en[b:]

    # Questions fréquentes
    a = en.index('<div class="faq">\n')
    b = en.index('        </div>\n      </div>\n    </section>', a)
    items = "\n".join('          <details>\n            <summary>%s</summary>\n            <p>%s</p>\n          </details>' % qr for qr in FAQ)
    en = en[:a] + '<div class="faq">\n' + items + "\n" + en[b:]

    manquants = []
    for avant, apres in PAIRES:
        if avant not in en:
            manquants.append(avant[:90])
            continue
        en = en.replace(avant, apres)
    for avant, apres in CHEMINS:
        en = en.replace(avant, apres)

    if manquants:
        print("Textes français introuvables (traduction à mettre à jour) :")
        for m in manquants:
            print("  -", m)
        sys.exit(1)

    # Contrôle : reste-t-il du français visible ?
    texte = re.sub(r"<script.*?</script>|<[^>]+>", " ", en, flags=re.S)
    suspects = re.findall(r"\b(?:les|des|vous|votre|avec|pour|dans|sur|une|est|sont|nous|soin|soins)\b", texte)
    if suspects:
        print("Mots français restants :", sorted(set(suspects)))

    (RACINE / "en").mkdir(exist_ok=True)
    (RACINE / "en" / "index.html").write_text(en, encoding="utf-8")
    print("en/index.html écrit")


if __name__ == "__main__":
    main()
