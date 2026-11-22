# Site sandycrazyconcept.fr — Sérénita Gruissan

Site vitrine (une page) des massages et soins thérapeutiques de Sandy et Sandra, au Sunrise Beach Hôtel, à Gruissan.
Le QR code imprimé sur le matériel de Sandy ouvre `https://sandycrazyconcept.fr/` : ce site remplace la page Canva sans changer le QR code.

## Contenu
- `index.html` : la page d'accueil, version « pro » mise en ligne le 22/11/2026 (en-tête avec logo et menu, photo d'accueil, approche, pour tous, tarifs, équipe, lieu avec adresse et itinéraire, contact, barre d'appel sur téléphone, données structurées).
- `mentions-legales.html` : mentions légales.
- `css/style.css` : la mise en page (couleurs de la page Canva : brun #2e1e10, dorés #e1ba7d / #f1d051).
- `img/logo-serenita.png` : logo doré sur fond transparent, extrait du bandeau Canva (en attendant le fichier d'origine du logo).
- `img/` : photos optimisées (JPEG + WebP), sans métadonnées (EXIF).
- `fonts/` : polices Marcellus et Alegreya Sans (licence SIL Open Font License), hébergées ici : aucun appel externe, aucun cookie.

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
