<a id="configuration"></a>
<a id="statut"></a>

# Configuration {#konfiguration}

```yaml
dhl:
  enabled: true
  tracking_numbers: "00340434123456789012,00340434123456789013"
  login_url: "https://login.dhl.de/..."
  login_code: ""
hermes:
  enabled: true
  tracking_numbers: "12345678901234"
gls:
  enabled: false
  tracking_numbers: ""
  postal_code: ""
dpd:
  enabled: false
  tracking_numbers: ""
  username: ""
  password: ""
ups:
  enabled: false
  tracking_numbers: ""
  username: ""
  password: ""
amazon:
  enabled: false
  email: ""
  password: ""
  otp_token: ""
deutsche_post:
  enabled: false
  tracking_numbers: ""
fedex:
  enabled: false
  tracking_numbers: ""
general:
  interval: 60
  max_parcels: 6
  log_response_details: false
```

L'application Home Assistant affiche les options sous forme de sections regroupées par transporteur. DHL et Hermes sont d'ores et déjà opérationnels. GLS, DPD, UPS, Amazon Logistics, Deutsche Post (courriers) et FedEx sont prévus en tant que sections de configuration ; leurs connecteurs actifs respectifs seront ajoutés progressivement.

`dhl.login_url` sert d'aide à la copie pour la connexion via le navigateur pour DHL.

`dhl.login_code` peut contenir l'URL de redirection complète (`dhllogin://...`) issue de la procédure de connexion DHL via le navigateur. Une fois la première connexion réussie, l'application enregistre le jeton d'actualisation (*refresh token*) dans son dossier de données et récupère automatiquement la liste des colis associés au compte DHL.

`dhl.tracking_numbers` permet de saisir manuellement des numéros de suivi DHL, séparés par des virgules.

`hermes.tracking_numbers` permet de saisir un ou plusieurs numéros de suivi Hermes, séparés par des virgules.

`gls.tracking_numbers` et `gls.postal_code` sont déjà disponibles en tant que champs de configuration. GLS Allemagne n'est pas encore interrogé activement, car cela nécessite la mise en œuvre d'une session « invité » (*Guest-Bearer-Session*) anonyme.

`dpd`, `ups`, `amazon`, `deutsche_post` et `fedex` sont prêts à être utilisés. S'ils sont activés, l'application indique clairement dans le journal (*log*) que le connecteur correspondant n'est pas encore disponible.

`general.interval` définit l'intervalle de mise à jour, exprimé en minutes.

`general.max_parcels` définit le nombre d'entités « emplacement de colis » (package slot) créées via la découverte MQTT (MQTT Discovery).

`general.log_response_details` consigne les requêtes et réponses du fournisseur dans le journal (log) de l'add-on — avec des données masquées — et les écrit également dans `/data/provider_debug.log`. Le fichier conserve un maximum de 100 lignes au format JSON. Les jetons (tokens), mots de passe, en-têtes d'autorisation (Authorization headers) et codes de connexion DHL sont masqués. Il est recommandé de désactiver cette option une fois les tests terminés.

Les notifications sont générées via des automatisations Home Assistant ; par exemple, lorsque `sensor.parcel_in_zustellung` devient supérieur à `0`.

## Connexion au compte DHL {#dhl-konto-login}

Connexion via un code récupéré dans le navigateur :

1. Cliquez sur le lien ci-dessous et connectez-vous via le navigateur Chrome.
2. Ouvrez la console de développement (Developer Console) : `F12`.
3. Dans l'onglet « Console », repérez la redirection ayant échoué et copiez l'URL complète `dhllogin://...`.
4. Collez cette URL dans le champ `dhl.login_code` ci-dessous, enregistrez, puis redémarrez l'application.

[URL de connexion DHL – CLIQUEZ ICI](https://login.dhl.de/af5f9bb6-27ad-4af4-9445-008e7a5cddb8/login/authorize?redirect_uri=dhllogin://de.deutschepost.dhl/login&state=eyJycyI6dHJ1ZSwicnYiOmZhbHNlLCJmaWQiOiJhcHAtbG9naW4tbWVoci1mb290ZXIiLCJoaWQiOiJhcHAtbG9naW4tbWVoci1oZWFkZXIiLCJycCI6ZmFsc2V9&client_id=83471082-5c13-4fce-8dcb-19d2a3fca413&response_type=code&scope=openid%20offline_access&claims=%7B%22id_token%22:%7B%22email%22:null,%22post_number%22:null,%22twofa%22:null,%22service_mask%22:null,%22deactivate_account%22:null,%22last_login%22:null,%22customer_type%22:null,%22display_name%22:null,%22data_confirmation_required%22:null%7D%7D&nonce=&login_hint=&prompt=login&ui_locales=de-DE&code_challenge=MAhrhXXZP-Owy-R7ruyB7Fn-Z8ODW6qxCoHg4uXELCw&code_challenge_method=S256)

```text
https://login.dhl.de/af5f9bb6-27ad-4af4-9445-008e7a5cddb8/login/authorize?redirect_uri=dhllogin://de.deutschepost.dhl/login&state=eyJycyI6dHJ1ZSwicnYiOmZhbHNlLCJmaWQiOiJhcHAtbG9naW4tbWVoci1mb290ZXIiLCJoaWQiOiJhcHAtbG9naW4tbWVoci1oZWFkZXIiLCJycCI6ZmFsc2V9&client_id=83471082-5c13-4fce-8dcb-19d2a3fca413&response_type=code&scope=openid%20offline_access&claims=%7B%22id_token%22:%7B%22email%22:null,%22post_number%22:null,%22twofa%22:null,%22service_mask%22:null,%22deactivate_account%22:null,%22last_login%22:null,%22customer_type%22:null,%22display_name%22:null,%22data_confirmation_required%22:null%7D%7D&nonce=&login_hint=&prompt=login&ui_locales=de-DE&code_challenge=MAhrhXXZP-Owy-R7ruyB7Fn-Z8ODW6qxCoHg4uXELCw&code_challenge_method=S256
```
