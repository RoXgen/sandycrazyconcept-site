/* Sérénita Gruissan — aperçu du bon cadeau.
   Le soin choisi (et, pour le duo, le style du massage) s'inscrit sur la carte du bon,
   comme sur le bon remis au client ; l'occasion (Noël, anniversaire…) change l'image de la carte.
   Sans JavaScript, la carte montre le duo « Massage du monde », toutes occasions.
   Aucun cookie, aucun appel externe. */
(function () {
  "use strict";

  var choix = document.querySelector(".bon-choix");
  var carte = document.querySelector(".bon-carte");
  if (!choix || !carte) { return; }

  var soin = document.getElementById("bon-soin");
  var style = document.getElementById("bon-style");
  var occasion = document.getElementById("bon-occasion");
  var image = carte.querySelector("img");
  var source = carte.querySelector("source");
  var dossier = image.getAttribute("src").replace(/[^\/]*$/, "");
  // Une image par occasion : img/bon-cadeau-<occasion>-768|1536.webp|jpg (sans occasion : img/bon-cadeau-…)
  var OCCASIONS = ["noel", "anniversaire", "saint-valentin", "fete-des-meres", "fete-des-peres"];
  var blocStyle = choix.querySelector(".bon-choix-style");
  var format = carte.querySelector(".bon-format");
  var nom = carte.querySelector(".bon-style");
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

  function dessiner() {
    var cle = soin.value;
    var def = BONS[cle] || BONS.duo;
    var duo = cle === "duo";
    blocStyle.hidden = !duo;
    format.textContent = def[0];
    nom.textContent = "“" + (duo ? STYLES[style.value] : def[1]) + "”";
    ajuster(format);
    ajuster(nom);
  }

  function poserImage() {
    var cle = occasion ? occasion.value : "";
    var base = dossier + (OCCASIONS.indexOf(cle) >= 0 ? "bon-cadeau-" + cle : "bon-cadeau");
    if (source) { source.srcset = base + "-768.webp 768w, " + base + "-1536.webp 1536w"; }
    image.srcset = base + "-768.jpg 768w, " + base + "-1536.jpg 1536w";
    image.src = base + "-768.jpg";
  }

  function annoncer() {
    var texte = soin.options[soin.selectedIndex].text;
    if (soin.value === "duo") { texte += ", " + style.options[style.selectedIndex].text; }
    if (occasion && OCCASIONS.indexOf(occasion.value) >= 0) { texte += ", " + occasion.options[occasion.selectedIndex].text; }
    resume.textContent = (anglais ? "Voucher preview: " : "Aperçu du bon : ") + texte + ".";
  }

  function changer() {
    dessiner();
    annoncer();
  }

  choix.hidden = false;
  soin.addEventListener("change", changer);
  style.addEventListener("change", changer);
  if (occasion) {
    occasion.addEventListener("change", function () { poserImage(); annoncer(); });
    if (occasion.value !== "classique") { poserImage(); }
  }
  dessiner();
  if (document.fonts && document.fonts.ready) { document.fonts.ready.then(dessiner); }
  if ("ResizeObserver" in window) {
    new ResizeObserver(function () { ajuster(format); ajuster(nom); }).observe(carte);
  }
})();
