# Configuration

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

`dhl_login_url` is the visible copy helper for the DHL browser login.

`dhl_login_code` optionally contains the complete `dhllogin://...` redirect URL from the DHL browser login. After the first successful login the app stores the refresh token in the app data folder and reads the DHL account parcel list automatically.

`dhl_tracking_numbers` contains optional manual DHL tracking numbers separated by commas.

`hermes_tracking_numbers` contains one or more Hermes tracking numbers separated by commas.

`gls_tracking_numbers` and `gls_postal_code` are already available as configuration fields. GLS Germany is not polled yet because it still needs an anonymous guest bearer session.

`interval` is the update interval in minutes.

`max_parcels` controls how many parcel slot entities are created through MQTT Discovery.

`log_response_details` writes masked provider requests and responses to the add-on log and additionally to `/data/provider_debug.log`. The file keeps at most 100 JSON lines. Tokens, passwords, authorization headers and DHL login codes are masked. Disable this option again after testing.

Notifications are created through Home Assistant automations, for example when `sensor.parcel_in_zustellung` becomes greater than `0`.

## DHL Account Login

Login through browser code:

1. Click the link below and sign in with Chrome.
2. Open the developer console with `F12`.
3. In the console tab, copy the failed `dhllogin://...` redirect URL.
4. Paste the URL into `dhl_login_code`, save and restart the app.

[OPEN DHL LOGIN URL](https://login.dhl.de/af5f9bb6-27ad-4af4-9445-008e7a5cddb8/login/authorize?redirect_uri=dhllogin://de.deutschepost.dhl/login&state=eyJycyI6dHJ1ZSwicnYiOmZhbHNlLCJmaWQiOiJhcHAtbG9naW4tbWVoci1mb290ZXIiLCJoaWQiOiJhcHAtbG9naW4tbWVoci1oZWFkZXIiLCJycCI6ZmFsc2V9&client_id=83471082-5c13-4fce-8dcb-19d2a3fca413&response_type=code&scope=openid%20offline_access&claims=%7B%22id_token%22:%7B%22email%22:null,%22post_number%22:null,%22twofa%22:null,%22service_mask%22:null,%22deactivate_account%22:null,%22last_login%22:null,%22customer_type%22:null,%22display_name%22:null,%22data_confirmation_required%22:null%7D%7D&nonce=&login_hint=&prompt=login&ui_locales=de-DE&code_challenge=MAhrhXXZP-Owy-R7ruyB7Fn-Z8ODW6qxCoHg4uXELCw&code_challenge_method=S256)

```text
https://login.dhl.de/af5f9bb6-27ad-4af4-9445-008e7a5cddb8/login/authorize?redirect_uri=dhllogin://de.deutschepost.dhl/login&state=eyJycyI6dHJ1ZSwicnYiOmZhbHNlLCJmaWQiOiJhcHAtbG9naW4tbWVoci1mb290ZXIiLCJoaWQiOiJhcHAtbG9naW4tbWVoci1oZWFkZXIiLCJycCI6ZmFsc2V9&client_id=83471082-5c13-4fce-8dcb-19d2a3fca413&response_type=code&scope=openid%20offline_access&claims=%7B%22id_token%22:%7B%22email%22:null,%22post_number%22:null,%22twofa%22:null,%22service_mask%22:null,%22deactivate_account%22:null,%22last_login%22:null,%22customer_type%22:null,%22display_name%22:null,%22data_confirmation_required%22:null%7D%7D&nonce=&login_hint=&prompt=login&ui_locales=de-DE&code_challenge=MAhrhXXZP-Owy-R7ruyB7Fn-Z8ODW6qxCoHg4uXELCw&code_challenge_method=S256
```
