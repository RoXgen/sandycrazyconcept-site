# Site sandycrazyconcept.fr — Sérénita Gruissan

Site vitrine (une page) des massages et soins thérapeutiques de Sandy et Sandra, au Sunrise Beach Hôtel, à Gruissan.
Le QR code imprimé sur le matériel de Sandy ouvre `https://sandycrazyconcept.fr/` : ce site remplace la page Canva sans changer le QR code.

## Contenu
- `index.html` : la page d'accueil, version « pro » mise en ligne le 22/11/2026 (en-tête avec logo et menu, photo d'accueil, approche, pour tous, tarifs, équipe, lieu avec adresse et itinéraire, contact, barre d'appel sur téléphone, données structurées).
- `mentions-legales.html` : mentions légales.
- `css/style.css` : la mise en page (couleurs de la page Canva : brun #2e1e10, dorés #e1ba7d / #f1d051).
- `img/logo-serenita.png` : logo doré sur fond transparent, extrait du bandeau Canva (en attendant le fichier d'origine du logo).
- `img/` : photos optimisées (JPEG + WebP), sans métadonnées (EXIF). `portrait-sandy` et `portrait-sandra` : découpés dans le bandeau Canva « Sandy / Sérénita / Sandra » (800 px de large : photos d'origine en meilleure qualité à demander). `palme.png` : palme dorée extraite de l'ancienne carte des tarifs, fond rendu transparent.
- `fonts/` : polices Marcellus, Alegreya Sans et Great Vibes (prénoms) — licence SIL Open Font License, hébergées ici : aucun appel externe, aucun cookie.

## Publication
GitHub Pages, branche `main`, dossier racine, domaine `sandycrazyconcept.fr` (fichier `CNAME`). Adresse GitHub d'origine : https://roxgen.github.io/sandycrazyconcept-site/ (redirige vers le domaine).

## Passage sur sandycrazyconcept.fr (fait le 22/11/2026, à la demande de Roméo, avant la fin du transfert du domaine)
1. Retirer la ligne `<meta name="robots" content="noindex">` de `index.html` et de `mentions-legales.html`.
2. GitHub : Settings › Pages › Custom domain = `sandycrazyconcept.fr`, puis « Enforce HTTPS ».
3. DNS chez one.com : supprimer les A `167.172.5.31` (@ et www) et les 2 TXT `fwd` (redirection forwarddomain.net) ;
   créer les A de `sandycrazyconcept.fr` vers `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   et le CNAME `www` vers `roxgen.github.io`. Garder le MX. Ne jamais cliquer « Réinitialisez les enregistrements DNS ».
4. GitHub : vérifier le domaine (Settings du compte › Pages › Verified domains) pour éviter qu'un autre compte puisse l'utiliser.
   Fait le 22/11/2026 : TXT `_github-pages-challenge-roxgen.sandycrazyconcept.fr` créé chez one.com, domaine « Verified ». Ne pas supprimer ce TXT.
5. Tester le QR code imprimé (https, avec et sans www).

## Points ouverts
- Mentions légales publiées le 22/11/2026 sans statut ni SIRET, adresse professionnelle et e-mail (choix de Roméo) : à compléter dès que possible (obligation légale pour un site professionnel).
- Le ® de « Skin & Soul by Sandy » a été retiré (à remettre seulement si la marque est déposée à l'INPI).
- Note Google écrite en dur dans l'accueil (« 5/5 sur Google, 26 avis », relevée le 22/11/2026) : à mettre à jour quand la note ou le nombre d'avis change.

## Décisions
- 22/11/2026 (Roméo) : version « pro » mise en ligne ; la prise de rendez-vous en ligne se fera avec Planningen (bouton « Réserver en ligne » vers la page de réservation de Sérénita, quand l'app sera publiée).
- 22/11/2026 (Roméo) : les liens et le texte renvoient vers le Sunrise Beach Hôtel (https://www.hotelsunrise-gruissan.com), où se trouve la salle de massage de Sandy. Pasha Plage n'est plus mentionné.
- 22/11/2026 (Roméo) : lien « 5/5 sur Google, 26 avis » dans l'accueil et bouton « Itinéraire » vers la fiche Google de Sandy (https://maps.google.com/?cid=7879985521520299105). Ses comptes Instagram et Facebook sont personnels : pas sur le site.
- 22/11/2026 (Roméo, d'après les demandes de Sandy) : accueil = Sandy et Sandra qui montrent le logo Sérénita (fond brun au lieu du blanc), un clic sur chaque photo mène à sa partie (#sandy, #sandra) ; « salle de massage » devient « espace soins » ; carte des soins refaite comme la carte imprimée (palmes dorées, points de conduite), sans la phrase du haut : Massage aux huiles essentielles chaudes bio 30 min 40 € / 60 min 70 €, Massage du dos et cervicales 40 min 50 €, Massages du monde 60 min 80 € (gardé), Visage Sérénita (ex-« Facial ») 20 min 30 €, Crânien Sérénita 20 min 30 €, Sérénita prénatal et postnatal 45 min 50 € (nouveau), Sérénita 4 mains 45 min 120 €, Duo Sérénita 60 min 140 € (au lieu de 150 €), Massage thérapeutique « Skin & Soul » by Sandy 90 min 110 € (à la place de 120 min 150 €, à confirmer), Ventouses (médecine chinoise) 45 min 60 €.
- 22/11/2026 (Roméo) : Sérénita reste en avant sur sandycrazyconcept.fr ; l'idée d'en faire le site « Skin & Soul » est remise à plus tard (le camping et le spa ouvrent en avril, sous un autre nom). Histoires de Sandy et de Sandra : textes à recevoir.
- 22/11/2026, 20 h 30 (Roméo, d'après Sandy) : logo doré en relief au centre de l'accueil (`img/logo-serenita-or`, détouré d'une image fournie par Roméo) ; Sandy et Sandra détourées (`img/detoure-*`, détourage automatique ISNet + fondu ovale) ; carte dans l'ordre demandé : huiles essentielles chaudes, visage, crânien, dos et cervicales, prénatal et postnatal (60 min 80 €), massages du monde (60 min 80 €), 4 mains, duo (« avec Sandy et Sandra »), ventouses, Skin & Soul, soin de dépouillement transgénérationnel (50 €, durée à préciser) ; histoire de Sandy (texte de Roméo) ; description de Sandra différente de celle de Sandy (son histoire reste à recevoir).
