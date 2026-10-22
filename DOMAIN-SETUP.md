# ugso-opensource.net: STRATO und GitHub Pages

## DE

Die bisherige Seite `https://opensource.ugso-software.de/` bleibt unverändert.
Die zweite Veröffentlichung verwendet `https://ugso-opensource.net/` direkt.
Alle drei Sprachen stammen automatisch aus demselben Build.

Bei STRATO unter **Domains → Domainverwaltung → ugso-opensource.net → DNS**:

| Name | Typ | Wert |
| --- | --- | --- |
| @ | A | 185.199.108.153 |
| @ | A | 185.199.109.153 |
| @ | A | 185.199.110.153 |
| @ | A | 185.199.111.153 |
| www | CNAME | rockbaer2007.github.io. |

Die bisherige externe Web-Weiterleitung dieser Domain deaktivieren. Falls STRATO
nur eine IPv4-Adresse zulässt, `185.199.108.153` eintragen. Wenn mehrere A-Records
möglich sind, alle vier setzen. Andere bisherige A-/AAAA-Webziele der neuen Domain
ersetzen; MX-, Mail-TXT-Records und die DNS-Einträge der bisherigen Domain erhalten.
Für IPv6 optional die vier GitHub-AAAA-Ziele verwenden: `2606:50c0:8000::153`,
`2606:50c0:8001::153`, `2606:50c0:8002::153`, `2606:50c0:8003::153`.

GitHub Pages im zweiten Repository ist auf `ugso-opensource.net` eingestellt.
Nach erfolgreicher DNS-Prüfung und Ausstellung des GitHub-Zertifikats dort
**Enforce HTTPS** aktivieren. Kein STRATO-Zertifikat für diesen GitHub-Webserver
installieren. `www.ugso-opensource.net` wird von GitHub auf die neue Hauptadresse
ohne www vereinheitlicht; es erfolgt keine Weiterleitung zur bisherigen Domain.

Anschließend `/`, `/en/`, `/fr/` und eine Unterseite auf beiden Domains prüfen.
Auf der zweiten Domain zeigt `/deployment.json` die veröffentlichte Quellrevision.
Die neue Domain ist erst nach DNS-Umstellung und gültigem Zertifikat einsatzbereit.

## EN

Keep the existing site and its DNS unchanged. Disable the STRATO web redirect for
the new domain and configure the DNS records above. Preserve mail records. If the
STRATO UI accepts only one IPv4 address, use `185.199.108.153`; otherwise set all four.
Remove obsolete web A/AAAA targets for this new domain. IPv6 records are optional.
Once GitHub validates DNS and issues its certificate, enable **Enforce HTTPS** in
the second repository. Both sites receive the same DE/EN/FR build automatically;
`www` redirects only to the new apex domain, never to the original site. Check
all locales and `deployment.json` after the DNS change.

## FR

Conserver le site existant et son DNS. Désactiver la redirection Web STRATO du
nouveau domaine et configurer les enregistrements ci-dessus, sans modifier les
enregistrements de messagerie. Si STRATO accepte une seule IPv4, utiliser
`185.199.108.153` ; sinon, renseigner les quatre. Remplacer les anciennes cibles
Web A/AAAA du nouveau domaine. IPv6 est facultatif. Après validation DNS et émission
du certificat par GitHub, activer **Enforce HTTPS** dans le second dépôt. Les deux
sites reçoivent automatiquement le même résultat DE/EN/FR. `www` redirige uniquement
vers le nouveau domaine sans www, jamais vers le site initial. Vérifier les trois
langues et `deployment.json` après la modification DNS.

## References

- [GitHub Pages custom domains and DNS](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)
- [STRATO DNS administration](https://www.strato.de/faq/domains/wie-kann-ich-bei-strato-meine-dns-eintraege-verwalten/)
