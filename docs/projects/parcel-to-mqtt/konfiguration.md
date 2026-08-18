# Konfiguration

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

Die Home-Assistant-App zeigt die Optionen als gruppierte Anbieterbereiche an. DHL und Hermes sind aktiv nutzbar. GLS, DPD, UPS, Amazon Logistics, Deutsche Post Briefe und FedEx sind bereits als Konfigurationsbereiche vorbereitet, ihre aktiven Connectoren folgen schrittweise.

`dhl.login_url` ist die sichtbare Kopierhilfe für den DHL-Browser-Login.

`dhl.login_code` enthält optional die komplette `dhllogin://...` Weiterleitungs-URL aus dem DHL-Browser-Login. Nach dem ersten erfolgreichen Login speichert die App das Refresh-Token im App-Datenordner und liest die Paketliste des DHL-Kontos automatisch.

`dhl.tracking_numbers` enthält optionale manuelle DHL-Sendungsnummern, mit Komma getrennt.

`hermes.tracking_numbers` enthält eine oder mehrere Hermes-Sendungsnummern, mit Komma getrennt.

`gls.tracking_numbers` und `gls.postal_code` sind bereits als Konfigurationsfelder vorhanden. GLS Deutschland wird noch nicht aktiv abgefragt, weil dafür eine anonyme Guest-Bearer-Session implementiert werden muss.

`dpd`, `ups`, `amazon`, `deutsche_post` und `fedex` sind vorbereitet. Wenn sie aktiviert werden, schreibt die App klar ins Log, dass der jeweilige aktive Connector noch aussteht.

`general.interval` ist das Aktualisierungsintervall in Minuten.

`general.max_parcels` legt fest, wie viele Paket-Slot-Entitäten per MQTT Discovery angelegt werden.

`general.log_response_details` schreibt Provider-Anfragen und Antworten maskiert ins Add-on-Log und zusätzlich nach `/data/provider_debug.log`. Die Datei behält maximal 100 JSON-Zeilen. Tokens, Passwörter, Authorization-Header und DHL-Login-Codes werden maskiert. Diese Option sollte nach dem Testen wieder deaktiviert werden.

Benachrichtigungen werden über Home Assistant Automationen erstellt, zum Beispiel wenn `sensor.parcel_in_zustellung` größer als `0` wird.

## DHL-Konto-Login

Login über Browser-Code:

1. Unten auf den Link klicken und im Chrome-Browser einloggen.
2. Developer Console öffnen: `F12`.
3. Im Console-Tab die fehlgeschlagene Weiterleitung sehen und die komplette `dhllogin://...` URL kopieren.
4. Die URL unten bei `dhl.login_code` einfügen, speichern und die App neu starten.

[DHL Login URL HIER KLICKEN](https://login.dhl.de/af5f9bb6-27ad-4af4-9445-008e7a5cddb8/login/authorize?redirect_uri=dhllogin://de.deutschepost.dhl/login&state=eyJycyI6dHJ1ZSwicnYiOmZhbHNlLCJmaWQiOiJhcHAtbG9naW4tbWVoci1mb290ZXIiLCJoaWQiOiJhcHAtbG9naW4tbWVoci1oZWFkZXIiLCJycCI6ZmFsc2V9&client_id=83471082-5c13-4fce-8dcb-19d2a3fca413&response_type=code&scope=openid%20offline_access&claims=%7B%22id_token%22:%7B%22email%22:null,%22post_number%22:null,%22twofa%22:null,%22service_mask%22:null,%22deactivate_account%22:null,%22last_login%22:null,%22customer_type%22:null,%22display_name%22:null,%22data_confirmation_required%22:null%7D%7D&nonce=&login_hint=&prompt=login&ui_locales=de-DE&code_challenge=MAhrhXXZP-Owy-R7ruyB7Fn-Z8ODW6qxCoHg4uXELCw&code_challenge_method=S256)

```text
https://login.dhl.de/af5f9bb6-27ad-4af4-9445-008e7a5cddb8/login/authorize?redirect_uri=dhllogin://de.deutschepost.dhl/login&state=eyJycyI6dHJ1ZSwicnYiOmZhbHNlLCJmaWQiOiJhcHAtbG9naW4tbWVoci1mb290ZXIiLCJoaWQiOiJhcHAtbG9naW4tbWVoci1oZWFkZXIiLCJycCI6ZmFsc2V9&client_id=83471082-5c13-4fce-8dcb-19d2a3fca413&response_type=code&scope=openid%20offline_access&claims=%7B%22id_token%22:%7B%22email%22:null,%22post_number%22:null,%22twofa%22:null,%22service_mask%22:null,%22deactivate_account%22:null,%22last_login%22:null,%22customer_type%22:null,%22display_name%22:null,%22data_confirmation_required%22:null%7D%7D&nonce=&login_hint=&prompt=login&ui_locales=de-DE&code_challenge=MAhrhXXZP-Owy-R7ruyB7Fn-Z8ODW6qxCoHg4uXELCw&code_challenge_method=S256
```
