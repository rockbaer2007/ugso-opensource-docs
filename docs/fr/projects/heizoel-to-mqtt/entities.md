<a id="entites"></a>
<a id="statut"></a>

# Entités {#entitaten}

Les entités sont créées via la découverte MQTT (MQTT Discovery).

Pour chaque source activée et chaque quantité configurée (en litres), les éléments suivants sont générés :

- Prix pour 100 litres
- Prix total
- Distributeur
- Délai de livraison
- Nombre d'offres
- Fournisseurs 01 à 06
- Prix total pour les fournisseurs 01 à 06
- Prix au litre pour les fournisseurs 01 à 06
- Prix pour 100 litres pour les fournisseurs 01 à 06

S'y ajoutent :

- Connexion « Fioul domestique »
- Dernière mise à jour des prix du fioul

Pour chaque offre, quatre entités sont créées : nom du fournisseur, prix total, prix au litre et prix pour 100 litres. Les attributs incluent le rang, le délai de livraison, la date de livraison, l'évaluation et la devise.

Les entités de prix sont publiées avec deux décimales et annoncées via la découverte MQTT (« MQTT Discovery ») en utilisant `suggested_display_precision: 2`.

Les attributs détaillés du « meilleur prix » incluent la source, la quantité, le code postal, le distributeur, la date de livraison, l'évaluation et le nombre d'offres.
