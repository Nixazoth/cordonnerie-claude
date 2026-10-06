#!/usr/bin/env python3
"""Vérifie liens internes, H1 uniques, mots interdits, ressources externes."""
import re, os, glob, sys
bad = 0
for f in glob.glob("public/**/index.html", recursive=True):
    h = open(f, encoding="utf-8").read()
    if len(re.findall(r"<h1[ >]", h)) != 1: print("H1 != 1:", f); bad += 1
    for l in re.findall(r"""(?:href|src)=["']([^"']+)""", h):
        if l.startswith("/"):
            p = "public" + l.split("#")[0]
            if not (os.path.isfile(p) or os.path.isfile(os.path.join(p, "index.html"))): print("Lien cassé:", f, l); bad += 1
    if re.search(r"<script[^>]+src=|<img|<iframe|googletagmanager|fbq\(|gradient|localStorage|document\.cookie|site officiel", h, re.I): print("À revoir:", f); bad += 1
print("Problèmes:", bad); sys.exit(bad > 0)
