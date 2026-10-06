# Cordonnerie Claude – maquette de site vitrine

Ce projet constitue une maquette de démonstration et ne doit pas être publié comme site officiel sans autorisation de l'entreprise.

Site statique : HTML + un fichier CSS, aucun JavaScript, aucune dépendance, aucun cookie, aucun tracker, aucune ressource tierce (polices système, pas de carte intégrée, pas de formulaire).

## Arborescence
```
public/            dossier à déployer
  index.html, services/, histoire/, contact/,
  mentions-legales/, politique-confidentialite/,
  politique-cookies/, conditions-utilisation/   (un index.html par dossier)
  style.css, favicon.svg, robots.txt, sitemap.xml
scripts/build_pages.py   génère les pages HTML (Python 3 standard)
scripts/audit.py         contrôle liens internes, H1, mots interdits
```
Les contenus se modifient dans `scripts/build_pages.py`, puis on régénère.

## Développement local
```
python3 scripts/build_pages.py
python3 -m http.server 8000 --directory public
python3 scripts/audit.py
```
Ouvrir http://localhost:8000.

## Build
Aucun build n'est requis : `public/` est déjà prêt. Pour changer le domaine dans canonical, Open Graph et sitemap :
`SITE_URL=https://domaine-de-l-entreprise.fr INDEXABLE=1 python3 scripts/build_pages.py`

Par défaut (`INDEXABLE` absent), les pages sont en `noindex` et `robots.txt` interdit l'exploration : c'est voulu pour une maquette. Le domaine par défaut est un placeholder (`DOMAINE-A-CONFIGURER.example`).

## Déploiement
- **Netlify / Cloudflare Pages / Vercel** : dépôt Git ou glisser-déposer, commande de build vide, dossier de sortie `public`.

## Connecter un domaine
Uniquement un domaine appartenant légalement à l'entreprise. Ajouter le domaine dans le tableau de bord de l'hébergeur, créer les enregistrements DNS indiqués (CNAME ou A), attendre le HTTPS automatique, puis relancer la commande de build ci-dessus avec `SITE_URL` et `INDEXABLE=1`. Aucun domaine n'a été acheté ni supposé disponible.

## À vérifier avant toute production
- Horaires : issus d'annuaires, à confirmer par l'entreprise.
- Mentions légales : raison sociale, forme juridique, SIREN, adresse, directeur de publication, hébergeur, e-mail (tous en placeholders).
- Politique de confidentialité et cookies : relire avec l'hébergeur choisi (journaux serveur, durée de conservation) et faire valider juridiquement. Ces textes ne garantissent aucune conformité.
- Photos : aucune image n'est utilisée. Si des photos réelles sont ajoutées, noter ici leur source et leur licence.
- Date « depuis 1950 » : information publique à faire confirmer.
- Tarifs, délais, e-mail : [À CONFIRMER].
- Schema.org LocalBusiness : nom, adresse, téléphone uniquement.
