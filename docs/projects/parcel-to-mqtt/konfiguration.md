# Konfiguration

```yaml
dhl_tracking_numbers: "00340434123456789012,00340434123456789013"
dhl_login_url: "https://login.dhl.de/..."
dhl_login_code: ""
hermes_tracking_numbers: "12345678901234"
gls_tracking_numbers: ""
gls_postal_code: ""
interval: 60
max_parcels: 6
log_response_details: false
```

`dhl_login_url` ist die sichtbare Kopierhilfe für den DHL-Browser-Login.

`dhl_login_code` enthält optional die komplette `dhllogin://...` Weiterleitungs-URL aus dem DHL-Browser-Login. Nach dem ersten erfolgreichen Login speichert die App das Refresh-Token im App-Datenordner und liest die Paketliste des DHL-Kontos automatisch.

`dhl_tracking_numbers` enthält optionale manuelle DHL-Sendungsnummern, mit Komma getrennt.

`hermes_tracking_numbers` enthält eine oder mehrere Hermes-Sendungsnummern, mit Komma getrennt.

`gls_tracking_numbers` und `gls_postal_code` sind bereits als Konfigurationsfelder vorhanden. GLS Deutschland wird noch nicht aktiv abgefragt, weil dafür eine anonyme Guest-Bearer-Session implementiert werden muss.

`interval` ist das Aktualisierungsintervall in Minuten.

`max_parcels` legt fest, wie viele Paket-Slot-Entitäten per MQTT Discovery angelegt werden.

`log_response_details` schreibt Rohantworten zur Fehlersuche ins Log. Diese Option sollte nach dem Testen wieder deaktiviert werden.

Benachrichtigungen werden über Home Assistant Automationen erstellt, zum Beispiel wenn `sensor.parcel_in_zustellung` größer als `0` wird.

## DHL-Konto-Login

Login über Browser-Code:

1. Unten auf den Link klicken und im Chrome-Browser einloggen.
2. Developer Console öffnen: `F12`.
3. Im Console-Tab die fehlgeschlagene Weiterleitung sehen und die komplette `dhllogin://...` URL kopieren.
4. Die URL unten bei `dhl_login_code` einfügen, speichern und die App neu starten.

[DHL Login URL HIER KLICKEN](https://login.dhl.de/af5f9bb6-27ad-4af4-9445-008e7a5cddb8/login/authorize?redirect_uri=dhllogin://de.deutschepost.dhl/login&state=eyJycyI6dHJ1ZSwicnYiOmZhbHNlLCJmaWQiOiJhcHAtbG9naW4tbWVoci1mb290ZXIiLCJoaWQiOiJhcHAtbG9naW4tbWVoci1oZWFkZXIiLCJycCI6ZmFsc2V9&client_id=83471082-5c13-4fce-8dcb-19d2a3fca413&response_type=code&scope=openid%20offline_access&claims=%7B%22id_token%22:%7B%22email%22:null,%22post_number%22:null,%22twofa%22:null,%22service_mask%22:null,%22deactivate_account%22:null,%22last_login%22:null,%22customer_type%22:null,%22display_name%22:null,%22data_confirmation_required%22:null%7D%7D&nonce=&login_hint=&prompt=login&ui_locales=de-DE&code_challenge=MAhrhXXZP-Owy-R7ruyB7Fn-Z8ODW6qxCoHg4uXELCw&code_challenge_method=S256)

```text
https://login.dhl.de/af5f9bb6-27ad-4af4-9445-008e7a5cddb8/login/authorize?redirect_uri=dhllogin://de.deutschepost.dhl/login&state=eyJycyI6dHJ1ZSwicnYiOmZhbHNlLCJmaWQiOiJhcHAtbG9naW4tbWVoci1mb290ZXIiLCJoaWQiOiJhcHAtbG9naW4tbWVoci1oZWFkZXIiLCJycCI6ZmFsc2V9&client_id=83471082-5c13-4fce-8dcb-19d2a3fca413&response_type=code&scope=openid%20offline_access&claims=%7B%22id_token%22:%7B%22email%22:null,%22post_number%22:null,%22twofa%22:null,%22service_mask%22:null,%22deactivate_account%22:null,%22last_login%22:null,%22customer_type%22:null,%22display_name%22:null,%22data_confirmation_required%22:null%7D%7D&nonce=&login_hint=&prompt=login&ui_locales=de-DE&code_challenge=MAhrhXXZP-Owy-R7ruyB7Fn-Z8ODW6qxCoHg4uXELCw&code_challenge_method=S256
```
