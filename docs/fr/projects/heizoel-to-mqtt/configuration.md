<a id="configuration"></a>
<a id="statut"></a>

# Configuration {#konfiguration}

Exemple :

```yaml
plz: "10115"
amount: "1000,2000,3000"
interval: 60
esyActive: true
deliveryTimes: ohne
payment_type: "EC-Karte"
prod: Normal Schwefelarm
unloading_points: 1
hose: 40m
short_vehicle: mit Anhänger möglich
hoDe: true
hoAt: false
log_response_details: false
```

`plz` correspond au code postal allemand ou autrichien utilisé pour la consultation des prix.

`amount` est une liste de quantités (en litres) séparées par des virgules.

`interval` représente l'intervalle de récupération des données, exprimé en minutes. La valeur minimale est `30`.

`esyActive`, `hoDe` et `hoAt` permettent d'activer les différentes sources.

`deliveryTimes`, `payment_type`, `prod`, `unloading_points`, `hose` et `short_vehicle` correspondent aux champs de sélection présents dans l'interface ioBroker. Les options détaillées sont utilisées pour Esyoil. Quant à Heizöl24, tout comme dans la version originale de l'adaptateur ioBroker, il se base principalement sur le code postal et la quantité.

L'application est conçue exclusivement pour l'Allemagne et l'Autriche. Veuillez utiliser des codes postaux allemands ou autrichiens correspondant aux fournisseurs activés.

`deliveryTimes` utilise les valeurs visibles depuis l'interface ioBroker : `ohne`, `7:00 - 12:00 Uhr`, `12:00 - 17:00 Uhr`, `2 Wochentage (Express)`, `3 - 5 Wochentage (Mo.-Fr.)` et `6 - 10 Wochentage (Mo.-Fr.)`.

`prod` utilise les types visibles depuis l'interface ioBroker : `Normal Schwefelarm`, `Premium Schwefelarm`, `Klimaneutral Premium`, `Klimaneutral Normal`, `Bio 10`, `Bio 15` et `Bio 10 Premium`.

`payment_type` utilise les modes de paiement visibles depuis l'interface ioBroker : `EC-Karte`, `Barzahlung`, `Ratenkauf`, `Rechnung`, `Lastschrift` et `Vorkasse`.

`hose` propose les valeurs `40m`, `60m` et `80m`. Les anciennes valeurs déjà enregistrées contenant des espaces, par exemple `40 m`, sont acceptées afin de permettre à Home Assistant de conserver les configurations existantes. `short_vehicle` s'affiche dans Home Assistant sous le nom `Tankwagen` et propose `mit Anhänger möglich` ou `ohne Anhänger`.

Dans l'interface allemande de Home Assistant, `esyActive` s'affiche sous le nom `EasyOil aktivieren`. `hoDe` et `hoAt` y apparaissent respectivement sous les noms `Heizöl24 Deutschland aktivieren (Nur PLZ und Menge wird übernommen)` et `Heizöl24 Österreich aktivieren (Nur PLZ und Menge wird übernommen)`.

Dans Home Assistant, lorsque la langue de l'interface est réglée sur l'allemand, les champs de configuration s'affichent avec des noms et des descriptions en allemand.

Les anciens noms d'options issus de `0.1.0` — concernant le code postal, la quantité, le type de produit et la date de livraison — restent pris en compte en tant que solution de repli (fallback). Les commutateurs de fournisseurs sont désormais désignés uniquement par `esyActive`, `hoDe` et `hoAt`.

`log_response_details` consigne les réponses brutes des fournisseurs dans le journal de l'application ; cette option ne doit être activée qu'à des fins de débogage.

## Protection des données {#datenschutz}

Le code postal, la quantité et les options de livraison configurés sont transmis aux sources de prix activées.
