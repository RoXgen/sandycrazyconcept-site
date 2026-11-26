/* Sérénita Gruissan — aperçu du bon cadeau.
   Le soin choisi (et, pour le duo, le style du massage) s'inscrit sur la carte du bon,
   comme sur le bon remis au client ; l'occasion (Noël, Saint-Valentin…) change l'image de la carte
   (Noël proposé d'office du 15 novembre au 25 décembre, Saint-Valentin du 20 janvier au 14 février) ;
   le message de la personne qui offre s'écrit sur l'aperçu.
   Sans JavaScript, la carte montre le duo « Massage du monde », toutes occasions.
   Aucun cookie, aucun appel externe : le message reste dans le navigateur. */
(function () {
  "use strict";

  var choix = document.querySelector(".bon-choix");
  var carte = document.querySelector(".bon-carte");
  if (!choix || !carte) { return; }

  var soin = document.getElementById("bon-soin");
  var style = document.getElementById("bon-style");
  var occasions = document.querySelector(".bon-occasions");
  var radios = occasions ? occasions.querySelectorAll('input[name="bon-occasion"]') : [];
  var champMessage = document.getElementById("bon-message");
  var image = carte.querySelector("img");
  var source = carte.querySelector("source");
  var dossier = image.getAttribute("src").replace(/[^\/]*$/, "");
  // Une image par occasion : img/bon-cadeau-<occasion>-768|1536.webp|jpg (toutes occasions : img/bon-cadeau-…)
  var OCCASIONS = ["noel", "anniversaire", "saint-valentin", "fete-des-meres", "fete-des-peres"];
  var blocStyle = choix.querySelector(".bon-choix-style");
  var format = carte.querySelector(".bon-format");
  var nom = carte.querySelector(".bon-style");
  var message = carte.querySelector(".bon-message");
  var resume = choix.querySelector(".bon-resume");
  var anglais = document.documentElement.lang === "en";

  // Textes du bon, toujours en français comme le bon imprimé : [ligne du format, nom ou style du soin]
  var BONS = {
    "huiles-30": ["Massage de 30 minutes", "Huiles essentielles chaudes bio"],
    "huiles-60": ["Massage d’une heure", "Huiles essentielles chaudes bio"],
    cranien: ["Soin de 20 minutes", "Crânien Sérénita"],
    visage: ["Soin de 20 minutes", "Visage Sérénita"],
    reflexologie: ["Soin de 20 minutes", "Réflexologie plantaire et palmaire"],
    dos: ["Massage de 40 minutes", "Dos et cervicales"],
    prenatal: ["Massage d’une heure", "Prénatal et postnatal"],
    monde: ["Massage d’une heure", "Massage du monde"],
    quatre_mains: ["Massage de 45 minutes", "À quatre mains"],
    duo: ["Massage en duo d’une heure", null],
    ventouses: ["Soin de 45 minutes", "Ventouses"],
    skin_soul: ["Massage de 90 minutes", "Skin & Soul"],
    transgenerationnel: ["Soin de dépouillement", "Transgénérationnel"]
  };
  var STYLES = { monde: "Massage du monde", huiles: "Huiles essentielles chaudes bio" };

  // Réduit la taille du texte s'il dépasse la largeur prévue sur la carte.
  function ajuster(el) {
    el.style.setProperty("--ajuste", "1");
    var largeur = el.clientWidth;
    var besoin = el.scrollWidth;
    if (largeur && besoin > largeur) {
      el.style.setProperty("--ajuste", String(Math.max(0.55, (largeur / besoin) * 0.97)));
    }
  }

  // Le message tient sur deux lignes au plus : on réduit la taille jusqu'à ce qu'il rentre.
  function ajusterMessage() {
    if (!message) { return; }
    var facteur = 1;
    message.style.setProperty("--ajuste", "1");
    var taille = parseFloat(getComputedStyle(message).fontSize) || 1;
    while (facteur > 0.55 && message.scrollHeight > taille * facteur * 1.08 * 2 + 2) {
      facteur -= 0.05;
      message.style.setProperty("--ajuste", String(facteur));
    }
  }

  function dessiner() {
    var cle = soin.value;
    var def = BONS[cle] || BONS.duo;
    var duo = cle === "duo";
    blocStyle.hidden = !duo;
    format.textContent = def[0];
    nom.textContent = "“" + (duo ? STYLES[style.value] : def[1]) + "”";
    ajuster(format);
    ajuster(nom);
    ajusterMessage();
  }

  function occasionChoisie() {
    for (var i = 0; i < radios.length; i++) {
      if (radios[i].checked) { return radios[i]; }
    }
    return null;
  }

  function poserImage() {
    var choisie = occasionChoisie();
    var cle = choisie ? choisie.value : "";
    var base = dossier + (OCCASIONS.indexOf(cle) >= 0 ? "bon-cadeau-" + cle : "bon-cadeau");
    if (source) { source.srcset = base + "-768.webp 768w, " + base + "-1536.webp 1536w"; }
    image.srcset = base + "-768.jpg 768w, " + base + "-1536.jpg 1536w";
    image.src = base + "-768.jpg";
  }

  function annoncer() {
    var texte = soin.options[soin.selectedIndex].text;
    if (soin.value === "duo") { texte += ", " + style.options[style.selectedIndex].text; }
    var choisie = occasionChoisie();
    if (choisie && OCCASIONS.indexOf(choisie.value) >= 0) {
      texte += ", " + choisie.parentNode.textContent.trim();
    }
    resume.textContent = (anglais ? "Voucher preview: " : "Aperçu du bon : ") + texte + ".";
  }

  function ecrireMessage() {
    if (!message || !champMessage) { return; }
    message.textContent = champMessage.value.replace(/\s+/g, " ").trim();
    ajusterMessage();
  }

  // Occasion du moment, proposée à l'ouverture de la page.
  function occasionDuMoment(date) {
    var mois = date.getMonth() + 1;
    var jour = date.getDate();
    if ((mois === 11 && jour >= 15) || (mois === 12 && jour <= 25)) { return "noel"; }
    if ((mois === 1 && jour >= 20) || (mois === 2 && jour <= 14)) { return "saint-valentin"; }
    return "classique";
  }

  function changer() {
    dessiner();
    annoncer();
  }

  choix.hidden = false;
  if (occasions) {
    occasions.hidden = false;
    var actuelle = occasionChoisie();
    if (!actuelle || actuelle.value === "classique") {
      var saison = occasionDuMoment(new Date());
      for (var i = 0; i < radios.length; i++) { radios[i].checked = radios[i].value === saison; }
    }
    for (var j = 0; j < radios.length; j++) {
      radios[j].addEventListener("change", function () { poserImage(); annoncer(); });
    }
    poserImage();
  }
  soin.addEventListener("change", changer);
  style.addEventListener("change", changer);
  if (champMessage) { champMessage.addEventListener("input", ecrireMessage); }
  dessiner();
  ecrireMessage();
  annoncer();
  if (document.fonts && document.fonts.ready) { document.fonts.ready.then(function () { dessiner(); }); }
  if ("ResizeObserver" in window) {
    new ResizeObserver(function () { ajuster(format); ajuster(nom); ajusterMessage(); }).observe(carte);
  }
})();
