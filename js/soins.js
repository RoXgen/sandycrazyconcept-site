/* Sérénita Gruissan — fiches des soins.
   Un clic sur un soin ouvre sa fiche : sa constellation dorée s'anime,
   puis son histoire et ses bienfaits apparaissent. Aucun cookie, aucun appel externe. */
(function () {
  "use strict";

  var dialogue = document.getElementById("fiche-soin");
  if (!dialogue || typeof dialogue.showModal !== "function") {
    // Navigateur trop ancien : les fiches restent lisibles sous chaque soin.
    document.documentElement.classList.add("sans-dialog");
    return;
  }

  var ciel = dialogue.querySelector(".constellation");
  var titre = dialogue.querySelector("#fiche-titre");
  var detail = dialogue.querySelector(".fiche-detail");
  var prix = dialogue.querySelector(".fiche-prix");
  var contenu = dialogue.querySelector(".fiche-contenu");
  var fermer = dialogue.querySelector(".fiche-fermer");
  var dernierBouton = null;
  var SVG = "http://www.w3.org/2000/svg";

  // Une constellation par soin : points (x, y) dans un cadre de 200 x 120, puis les traits.
  var CONSTELLATIONS = {
    huiles: { p: [[100, 14], [88, 38], [78, 60], [76, 80], [86, 98], [100, 104], [114, 98], [124, 80], [122, 60], [112, 38]],
              l: [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]] },
    visage: { p: [[100, 14], [76, 24], [64, 50], [70, 80], [100, 104], [130, 80], [136, 50], [124, 24], [88, 54], [112, 54]],
              l: [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 0], [8, 9]] },
    cranien: { p: [[54, 94], [58, 60], [74, 36], [100, 24], [126, 36], [142, 60], [146, 94], [100, 70]],
               l: [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [1, 7], [5, 7], [3, 7]] },
    reflexologie: { p: [[100, 110], [86, 100], [80, 80], [84, 60], [82, 42], [90, 28], [104, 26], [116, 32], [118, 48], [112, 66], [112, 86], [110, 102],
                          [82, 14], [94, 10], [106, 11], [118, 16], [128, 24]],
                    l: [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 0]] },
    dos: { p: [[100, 10], [97, 28], [102, 46], [97, 64], [102, 82], [99, 100], [100, 114], [64, 24], [136, 24]],
           l: [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [7, 1], [8, 1]] },
    prenatal: { p: [[120, 12], [94, 20], [76, 40], [72, 64], [82, 88], [104, 104], [130, 106], [112, 62]],
                l: [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]] },
    monde: { p: [[144, 60], [131, 91], [100, 104], [69, 91], [56, 60], [69, 29], [100, 16], [131, 29], [116, 38], [120, 60], [116, 82]],
             l: [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 0], [4, 0], [6, 8], [8, 9], [9, 10], [10, 2]] },
    quatre_mains: { p: [[64, 24], [136, 24], [136, 96], [64, 96], [100, 60]],
                    l: [[0, 1], [1, 2], [2, 3], [3, 0], [0, 4], [1, 4], [2, 4], [3, 4]] },
    duo: { p: [[56, 28], [36, 86], [76, 86], [144, 28], [124, 86], [164, 86]],
           l: [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5], [5, 3], [0, 3]] },
    ventouses: { p: [[60, 46], [48, 70], [72, 70], [100, 28], [88, 52], [112, 52], [140, 46], [128, 70], [152, 70]],
                 l: [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5], [5, 3], [6, 7], [7, 8], [8, 6]] },
    skin_soul: { p: [[100, 60], [108, 55], [111, 67], [97, 74], [86, 61], [93, 43], [117, 40], [131, 61], [117, 88], [84, 91], [65, 64], [75, 30], [108, 16]],
                 l: [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12]] },
    transgenerationnel: { p: [[100, 106], [100, 76], [100, 48], [78, 30], [122, 30], [66, 52], [134, 52], [100, 14], [78, 116], [122, 116]],
                          l: [[0, 1], [1, 2], [2, 7], [2, 3], [2, 4], [1, 5], [1, 6], [0, 8], [0, 9]] }
  };

  function element(nom, attributs) {
    var el = document.createElementNS(SVG, nom);
    Object.keys(attributs).forEach(function (cle) { el.setAttribute(cle, attributs[cle]); });
    return el;
  }

  function dessiner(cle) {
    var def = CONSTELLATIONS[cle] || CONSTELLATIONS.huiles;
    while (ciel.firstChild) { ciel.removeChild(ciel.firstChild); }
    ciel.appendChild(element("circle", { "class": "orbite", cx: 100, cy: 60, r: 54 }));
    ciel.appendChild(element("circle", { "class": "orbite orbite-2", cx: 100, cy: 60, r: 40 }));
    def.l.forEach(function (paire, i) {
      var a = def.p[paire[0]], b = def.p[paire[1]];
      var trait = element("line", { "class": "trait", x1: a[0], y1: a[1], x2: b[0], y2: b[1], pathLength: 100 });
      trait.style.setProperty("--i", i);
      ciel.appendChild(trait);
    });
    def.p.forEach(function (point, i) {
      var etoile = element("circle", { "class": "etoile", cx: point[0], cy: point[1], r: i % 3 === 0 ? 2.6 : 1.9 });
      etoile.style.setProperty("--i", i);
      ciel.appendChild(etoile);
    });
  }

  function ouvrir(bouton) {
    var soin = bouton.closest(".soin");
    var fiche = soin.querySelector(".fiche");
    var sousTitre = soin.querySelector(".detail");

    titre.textContent = bouton.querySelector(".soin-nom").textContent;
    detail.textContent = sousTitre ? sousTitre.textContent : "";
    detail.hidden = !sousTitre;
    while (prix.firstChild) { prix.removeChild(prix.firstChild); }
    soin.querySelectorAll(".ligne").forEach(function (ligne) { prix.appendChild(ligne.cloneNode(true)); });
    contenu.innerHTML = fiche ? fiche.innerHTML : "";
    dessiner(bouton.getAttribute("data-fiche"));

    dernierBouton = bouton;
    dialogue.classList.remove("anime");
    dialogue.showModal();
    dialogue.scrollTop = 0;
    void dialogue.offsetWidth; // relance les animations à chaque ouverture
    dialogue.classList.add("anime");
  }

  document.querySelectorAll(".soin-bouton").forEach(function (bouton) {
    bouton.addEventListener("click", function () { ouvrir(bouton); });
  });

  // Fermer : bouton, touche Échap (natif) ou clic à côté de la fiche.
  fermer.addEventListener("click", function () { dialogue.close(); });
  dialogue.addEventListener("click", function (evenement) {
    if (evenement.target === dialogue) { dialogue.close(); }
  });
  dialogue.addEventListener("close", function () {
    dialogue.classList.remove("anime");
    if (dernierBouton) { dernierBouton.focus(); }
  });
})();
