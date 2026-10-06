#!/usr/bin/env python3
"""Génère les pages statiques dans public/.
SITE_URL=https://votre-domaine.fr INDEXABLE=1 python3 scripts/build_pages.py"""
import os
SITE = os.environ.get("SITE_URL", "https://DOMAINE-A-CONFIGURER.example").rstrip("/")
INDEXABLE = os.environ.get("INDEXABLE") == "1"
TEL, TEL_HREF = "03 88 31 44 06", "tel:+33388314406"
MAPS = "https://www.google.com/maps/search/?api=1&query=3+rue+du+Chevalier+Robert+67000+Strasbourg"
TBC = "[À CONFIRMER]"
HOURS = [("Mardi", "08:00–12:00 / 14:00–19:00"), ("Mercredi", "08:00–12:00 / 14:00–19:00"),
         ("Jeudi", "08:00–12:00"), ("Vendredi", "08:00–12:00 / 14:00–19:00"), ("Samedi", "08:00–12:30")]
SERVICES = [("Réparation de chaussures", "Réparation et remise en état de chaussures."),
            ("Ressemelage", "Ressemelage, y compris ressemelage cousu."),
            ("Entretien et cirage", "Entretien et cirage de chaussures."),
            ("Maroquinerie", "Réparation d’articles de maroquinerie, petite maroquinerie, sacs, ceintures et parapluies."),
            ("Reproduction de clés", "Reproduction de clés."),
            ("Gravure et tampons", "Gravure, tampons et cartes de visite."),
            ("Produits d’entretien", "Produits d’entretien et accessoires pour chaussures.")]
NAV = [("/", "Accueil"), ("/services/", "Services"), ("/histoire/", "Notre histoire"), ("/contact/", "Contact")]
LEGAL = [("/mentions-legales/", "Mentions légales"), ("/politique-confidentialite/", "Politique de confidentialité"),
         ("/politique-cookies/", "Politique des cookies"), ("/conditions-utilisation/", "Conditions d’utilisation")]
LD = ('{"@context":"https://schema.org","@type":"LocalBusiness","name":"Cordonnerie Claude","telephone":"+33388314406",'
      '"address":{"@type":"PostalAddress","streetAddress":"3 rue du Chevalier Robert","postalCode":"67000",'
      '"addressLocality":"Strasbourg","addressCountry":"FR"}}')

def hours_table():
    rows = "".join(f"<tr><th scope='row'>{d}</th><td>{h}</td></tr>" for d, h in HOURS)
    return (f"<table><caption>Horaires d’ouverture</caption><tbody>{rows}</tbody></table>"
            "<p class='note'>Lundi et dimanche : fermé. Horaires à confirmer auprès de l’établissement.</p>")

def address():
    return ("<p><strong>Cordonnerie Claude</strong><br>3 rue du Chevalier Robert<br>67000 Strasbourg</p>"
            f"<p>Téléphone : <a href='{TEL_HREF}'>{TEL}</a></p>")

def page(path, title, desc, body, home=False):
    nav = "".join(f"<a href='{h}'{' aria-current=\"page\"' if h == path else ''}>{t}</a>" for h, t in NAV)
    legal = "".join(f"<li><a href='{h}'>{t}</a></li>" for h, t in LEGAL)
    robots = "" if INDEXABLE else "<meta name='robots' content='noindex, nofollow'>"
    ld = f"<script type='application/ld+json'>{LD}</script>" if home else ""
    return f"""<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">{robots}
<link rel="canonical" href="{SITE}{path}"><link rel="icon" href="/favicon.svg" type="image/svg+xml">
<meta property="og:type" content="website"><meta property="og:locale" content="fr_FR"><meta property="og:site_name" content="Cordonnerie Claude">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:url" content="{SITE}{path}">
<link rel="stylesheet" href="/style.css">{ld}</head><body>
<a class="skip" href="#contenu">Aller au contenu</a>
<header class="site"><div class="wrap"><a class="logo" href="/">CORDONNERIE<br>CLAUDE</a>
<nav aria-label="Navigation principale">{nav}</nav><a class="btn small" href="{TEL_HREF}">Appeler</a></div></header>
<main id="contenu">{body}</main>
<footer class="site"><div class="wrap"><p><strong>Cordonnerie Claude</strong><br>3 rue du Chevalier Robert<br>67000 Strasbourg</p>
<p><a href="{TEL_HREF}">{TEL}</a></p><nav aria-label="Informations légales"><ul>{legal}</ul></nav></div></footer></body></html>"""

def simple(h1, intro, sections):
    s = "".join(f"<h2>{t}</h2>{c}" for t, c in sections)
    return f"<section class='legal'><div class='wrap'><h1>{h1}</h1><p>{intro}</p>{s}</div></section>"

def infos():
    return (f"<section class='alt' id='infos'><div class='wrap'><h2>Informations pratiques</h2><div class='cols'><div>{address()}"
            f"<p><a class='btn alt' href='{MAPS}' target='_blank' rel='noopener noreferrer'>Ouvrir dans Google Maps (nouvel onglet)</a></p>"
            f"<p class='note'>Le lien ouvre Google Maps uniquement au clic. Aucune carte n’est chargée sur cette page.</p></div><div>{hours_table()}</div></div></div></section>")

pages = {}
cards = "".join(f"<div class='item'><h3>{t}</h3><p>{d}</p></div>" for t, d in SERVICES)
pages["/"] = page("/", "Cordonnerie Claude | Cordonnier à Strasbourg",
    "Cordonnerie Claude, artisan cordonnier à Strasbourg : réparation de chaussures, ressemelage, maroquinerie, clés et gravure.",
    f"""<div class="hero"><div class="wrap"><div><p class="kicker">CORDONNERIE CLAUDE</p>
<h1>Artisan cordonnier à Strasbourg</h1><p>Réparation, entretien et savoir-faire artisanal pour vos chaussures, articles de maroquinerie et accessoires.</p>
<div class="actions"><a class="btn" href="/services/">Découvrir les services</a><a class="btn alt" href="#infos">Nous trouver</a></div></div></div></div>
<section><div class="wrap"><h2>Savoir-faire</h2><div class="grid">{cards}</div></div></section>
<section class="alt"><div class="wrap"><h2>L’atelier</h2><div class="grid">
<div class="ph" role="img" aria-label="Emplacement réservé pour une photo de l’atelier">[Photo réelle de l’atelier à ajouter]</div>
<div class="ph" role="img" aria-label="Emplacement réservé pour une photo des outils">[Photo réelle des outils à ajouter]</div>
<div class="ph" role="img" aria-label="Emplacement réservé pour une photo d’une réparation">[Photo réelle d’une réparation à ajouter]</div></div></div></section>
<section><div class="wrap"><h2>Une histoire familiale</h2><p>Le savoir-faire de la Cordonnerie Claude s’inscrit dans une histoire familiale de cordonniers depuis 1950.</p><p><a href="/histoire/">Lire la suite</a></p></div></section>
{infos()}""", home=True)
pages["/services/"] = page("/services/", "Services de cordonnerie à Strasbourg | Cordonnerie Claude",
    "Réparation de chaussures, ressemelage, entretien, maroquinerie, reproduction de clés, gravure et tampons à Strasbourg.",
    f"<section><div class='wrap'><h1>Nos services</h1><p>Les prestations ci-dessous sont celles présentées publiquement pour la cordonnerie. Tarifs et délais : {TBC}</p><div class='grid'>{cards}</div>"
    f"<p style='margin-top:2rem'>Pour un devis ou un renseignement, le plus simple est d’appeler : <a href='{TEL_HREF}'>{TEL}</a>.</p></div></section>")
pages["/histoire/"] = page("/histoire/", "Notre histoire | Cordonnerie Claude, Strasbourg",
    "Un savoir-faire de cordonnier transmis depuis plusieurs générations, à Strasbourg.",
    f"<section><div class='wrap'><h1>Notre histoire</h1><p>Le savoir-faire de la Cordonnerie Claude s’inscrit dans une histoire familiale de cordonniers depuis 1950.</p>"
    f"<p>Un savoir-faire de cordonnier transmis depuis plusieurs générations : la réparation et le ressemelage cousu font partie des gestes de l’artisan cordonnier.</p>"
    f"<p>Autres éléments historiques (fondation, lieux, personnes) : {TBC}</p></div></section>"
    "<section class='alt'><div class='wrap'><div class='ph' role='img' aria-label='Emplacement réservé pour une photo'>[Photo réelle de l’atelier à ajouter]</div></div></section>")
pages["/contact/"] = page("/contact/", "Contact et horaires | Cordonnerie Claude, Strasbourg",
    "Adresse, téléphone et horaires de la Cordonnerie Claude, 3 rue du Chevalier Robert à Strasbourg.",
    f"<section><div class='wrap'><h1>Contact</h1><p>Le téléphone est le moyen le plus direct de joindre la cordonnerie.</p>"
    f"<p><a class='btn' href='{TEL_HREF}'>Appeler la cordonnerie</a></p><p>E-mail : {TBC}</p></div></section>{infos()}")

pages["/mentions-legales/"] = page("/mentions-legales/", "Mentions légales | Cordonnerie Claude",
    "Mentions légales de la Cordonnerie Claude.",
    simple("Mentions légales", "Informations à compléter et à vérifier par l’entreprise avant toute mise en ligne.", [
    ("Éditeur du site", f"<ul><li>Nom commercial : Cordonnerie Claude</li><li>Raison sociale : [RAISON SOCIALE À CONFIRMER]</li><li>Forme juridique : [FORME JURIDIQUE À CONFIRMER]</li><li>SIREN : [SIREN À CONFIRMER]</li><li>Adresse du responsable : [ADRESSE À CONFIRMER]</li><li>Adresse de la boutique : 3 rue du Chevalier Robert, 67000 Strasbourg</li><li>Téléphone : {TEL}</li><li>E-mail : [EMAIL À CONFIRMER]</li><li>Directeur de la publication : [À CONFIRMER]</li></ul>"),
    ("Hébergeur", "<p>[HÉBERGEUR À CONFIRMER] (nom, adresse, contact)</p>"),
    ("Propriété intellectuelle", "<p>Les textes, la mise en page et le logo typographique de ce site sont propres à celui-ci. Toute reproduction sans autorisation est à éviter. Crédits des images : aucune photographie n’est utilisée à ce stade.</p>"),
    ("Statut de cette version", "<p>Cette version est une maquette de démonstration. Elle n’a pas été publiée par l’entreprise et ne l’engage pas.</p>")]))
pages["/politique-confidentialite/"] = page("/politique-confidentialite/", "Politique de confidentialité | Cordonnerie Claude",
    "Politique de confidentialité de la Cordonnerie Claude.",
    simple("Politique de confidentialité", "Cette page est un modèle à faire valider par l’entreprise ; elle ne constitue pas une garantie de conformité juridique.", [
    ("Responsable du traitement", "<p>[IDENTITÉ DU RESPONSABLE]<br>[ADRESSE]<br>[EMAIL]</p>"),
    ("Données collectées", "<p>La collecte de données est volontairement minimale. Ce site ne comporte ni formulaire, ni compte, ni outil de mesure d’audience, ni publicité. Le site ne dépose pas de cookie et ne collecte pas directement de données personnelles.</p><p>Comme tout serveur web, l’hébergeur peut enregistrer des journaux techniques (adresse IP, date, page demandée). [INFORMATIONS À CONFIRMER auprès de l’hébergeur : contenu et durée de conservation des journaux]</p>"),
    ("Finalités et utilisation", "<p>Les journaux techniques éventuels servent au fonctionnement et à la sécurité du site. Aucune autre utilisation n’est prévue.</p>"),
    ("Durée de conservation", "<p>[À CONFIRMER]</p>"),
    ("Appel téléphonique et liens externes", f"<p>Le numéro {TEL} est un lien d’appel : l’appel est géré par votre téléphone. Le lien « Ouvrir dans Google Maps » ouvre un service tiers uniquement lorsque vous cliquez dessus ; ce service applique ses propres règles.</p>"),
    ("Sous-traitants", "<p>Hébergeur : [HÉBERGEUR À CONFIRMER]. Aucun autre sous-traitant n’est utilisé par le site.</p>"),
    ("Vos droits", "<p>Vous pouvez demander l’accès, la rectification ou l’effacement de vos données, et vous opposer à leur traitement, en écrivant à [EMAIL]. Vous pouvez aussi saisir la CNIL (cnil.fr).</p>")]))
pages["/politique-cookies/"] = page("/politique-cookies/", "Politique des cookies | Cordonnerie Claude",
    "Politique des cookies de la Cordonnerie Claude.",
    simple("Politique des cookies", "Cette page décrit les technologies présentes sur ce site dans sa version actuelle.", [
    ("Ce que le site utilise", "<p>Le site ne dépose aucun cookie et n’utilise aucun traceur, outil de mesure d’audience, pixel publicitaire ou contenu tiers chargé automatiquement. Il n’utilise pas non plus de stockage local dans votre navigateur. C’est pourquoi aucun bandeau de consentement n’est affiché.</p>"),
    ("Ressources", "<p>Les polices utilisées sont celles de votre appareil. Aucune carte n’est intégrée.</p>"),
    ("Si cela change", "<p>Tout ajout futur d’un outil de mesure ou d’un contenu tiers devra s’accompagner d’une mise à jour de cette page et, si nécessaire, d’un recueil de consentement. [À CONFIRMER] : l’hébergeur peut appliquer sa propre configuration.</p>")]))
pages["/conditions-utilisation/"] = page("/conditions-utilisation/", "Conditions d’utilisation | Cordonnerie Claude",
    "Conditions d’utilisation du site de la Cordonnerie Claude.",
    simple("Conditions d’utilisation", "Ces conditions sont un modèle à faire valider par l’entreprise.", [
    ("Objet", "<p>Ce site présente l’activité de la Cordonnerie Claude. Il ne permet ni commande ni paiement en ligne.</p>"),
    ("Informations", f"<p>Les informations (services, horaires) sont données à titre indicatif et peuvent évoluer. Pour les confirmer, appelez le {TEL}.</p>"),
    ("Propriété intellectuelle", "<p>Les contenus du site ne peuvent pas être réutilisés sans autorisation.</p>"),
    ("Liens externes", "<p>Le site peut renvoyer vers des services tiers, dont le contenu n’est pas maîtrisé par l’éditeur.</p>"),
    ("Contact", "<p>Pour toute question : [EMAIL À CONFIRMER] ou par téléphone.</p>")]))

for path, html in pages.items():
    d = os.path.join("public", path.strip("/"))
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(html)
urls = "".join(f"<url><loc>{SITE}{p}</loc></url>" for p in pages)
open("public/sitemap.xml", "w").write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
open("public/robots.txt", "w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n" if INDEXABLE else "User-agent: *\nDisallow: /\n")
print(len(pages), "pages générées")
