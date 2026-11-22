# Site sandycrazyconcept.fr — Sérénita Gruissan

Site vitrine (une page) des massages et soins thérapeutiques de Sandy et Sandra, au Sunrise Beach Hôtel, à Gruissan.
Le QR code imprimé sur le matériel de Sandy ouvre `https://sandycrazyconcept.fr/` : ce site remplace la page Canva sans changer le QR code.

## Contenu
- `index.html` : la page d'accueil (textes et tarifs repris de la page Canva).
- `mentions-legales.html` : mentions légales (champs « à compléter » avant la mise en ligne).
- `css/style.css` : la mise en page (couleurs de la page Canva : brun #2e1e10, dorés #e1ba7d / #f1d051).
- `img/` : photos optimisées, sans métadonnées (EXIF).
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
5. Tester le QR code imprimé (https, avec et sans www).

## Points à valider
- Mentions légales : statut et SIRET, adresse professionnelle, e-mail.
- Le ® de « Skin & Soul by Sandy » a été retiré (à remettre seulement si la marque est déposée à l'INPI).
- Les liens vers l'hôtel pointent vers https://www.hotelsunrise-gruissan.com (la page Canva renvoyait aussi vers le site de Pasha Plage).
