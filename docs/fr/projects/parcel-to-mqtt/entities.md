<a id="entites"></a>
<a id="statut"></a>

# Entités {#entitaten}

Les entités sont créées via la découverte MQTT (MQTT Discovery).

Entités générales :

- Connexion Parcel
- Dernière mise à jour Parcel
- Expéditions Parcel
- Total Parcel
- Parcel Enregistré
- Parcel En transit
- Parcel En cours de livraison
- Parcel Point de retrait
- Parcel Livré
- Parcel Retour
- Parcel Problème
- Parcel Inconnu

Emplacements (slots) pour colis :

- Parcel 01
- Parcel 02
- autres emplacements, jusqu'au nombre configuré

Chaque emplacement de colis utilise son statut comme état principal et dispose d'attributs pour : le numéro d'expédition, le transporteur, le groupe de statut, le dernier événement, l'horodatage du dernier événement et le pays de destination.

La liste JSON de tous les envois est disponible en tant qu'attribut sur le capteur `Parcel Sendungen`.
