# Arbeitsagentur Berufssprachkurssuche API 
Die Bundesagentur für Arbeit verfügt über eine der größten Datenbanken für Berufssprachkurse. Obwohl sie vollständig staatlich ist und es sich dabei um einen sehr spannenden Basisdatensatz handelt, mit dem viele Analysen möglich wären, bietet die Bundesagentur für Arbeit dafür bis heute keine offizielle API an.
	

## Authentifizierung
Die Authentifizierung funktioniert per OAuth 2 Client Credentials mit JWTs.
Client Credentials sind, wie sich z.B. einem GET-request an https://web.arbeitsagentur.de/sprachfoerderung/suche/berufssprachkurse entnehmen lässt (oder an https://web.arbeitsagentur.de/sprachfoerderung/suche/anerkennungen, oder an https://web.arbeitsagentur.de/sprachfoerderung/suche/sonstige-kurse), folgende:

**client_id:** bd24f42e-ad0b-4005-b834-23bb6800dc6c

**client_secret:** 6776b89e-5728-4643-8cd5-c93aefb5314b

**grant_type:** client_credentials

Die Credentials sind im body POST-request an https://rest.arbeitsagentur.de/oauth/gettoken_cc zu senden.

```bash
token=$(curl \
-d "client_id=bd24f42e-ad0b-4005-b834-23bb6800dc6c&client_secret=6776b89e-5728-4643-8cd5-c93aefb5314b&grant_type=client_credentials" \
-X POST 'https://rest.arbeitsagentur.de/oauth/gettoken_cc' |grep -Eo '[^"]{500,}'|head -n 1)
```

Der Token ist via POST-request von https://rest.arbeitsagentur.de/oauth/gettoken_cc zu beziehen und muss bei folgenden GET-requests an https://rest.arbeitsagentur.de/infosysbub/sprachfoerderung/pc/v1/bildungsangebot im header als 'OAuthAccessToken' inkludiert werden.


## Berufssprachkurssuche

**URL:** https://rest.arbeitsagentur.de/infosysbub/sprachfoerderung/pc/v1/bildungsangebot


Die Berufssprachkurssuche ermöglicht verfügbare Berufssprachkursangebote und andere Kursarten (z..B. Bildungsangebote Migration oder Angebote in Zusammenhang mit der Anerkennung ausländischer Berufsabschlüsse) mit verschiedenen GET-Parametern zu filtern:


### Filter


**Parameter:** systematiken (Optional)

- MC
- A8
- MQ

Kursart: MC=Berufssprachkurse; A8 = Bildungsangebote Migration; MQ = Anerkennung ausländischer Berufsabschlüsse.


**Parameter:** suchworte (Optional)

Suchworte (z.B. Deutschsprachf%25C3%25B6rderung,Berufsbezogener%2520Englischkurs). Mehrere Komma-getrennte Angaben möglich.


**Parameter:** *orte* (Optional)

Ortsangabe nebst Postleitzahl und Koordinaten (z.B. Feucht_90537_11.224918_49.376701,N%C3%BCrnberg;%20Mittelfranken_11.0753_49.4508). Mehrere Komma-getrennte Angaben möglich.


**Parameter:** *systematiken* (Optional)

Systematiken (z.B. MC) 


**Parameter:** *page* (Optional)

Seite (beginnend mit 0 für die erste Seite).


**Parameter:** *sort* (Optional)

Sortierungskriterium (z.B. basc)


**Parameter:** *umkreis* (Optional)
- Bundesweit
- 25
- 50
- 100
- 150
- 200


**Parameter:** *sprachniveau* (Optional)
- MC%2001%201
- MC%2001%202
- MC%2001%203
- MC%2001%204
- MC%2001%205

Sprachzielniveau: MC%2001%201=A2, MC%2001%202=B1, MC%2001%203=B2, MC%2001%204=C1, MC%2001%205=C2. Mehrere Komma-getrennte Angaben möglich.


**Parameter:** *berufsfachsprachkurse*  (Optional)
- MC%2002
- MC%2003

Berufsfachsprachkurse: MC%2002=Spezialberufskurs, MC%2003=Berufsanerkennung. Mehrere Komma-getrennte Angaben möglich. 
Suchhinweis: Für spezielle Berufe oder Berufsbereiche kann ergänzend die Suchwort­suche genutzt werden. 


**Parameter:** *beginntermine*  (Optional)
- 0
- 1
- 2
- 3
- 4
- 5
- 6

Beginntermin: 0=regelmäßiger Start, 1=diesen Monat, 2=nächster Monat, 3=übernächster Monat, 4=überübernächster Monat, 5=spätere Termine, 6=frühere Termine. Mehrere Komma-getrennte Angaben möglich.


**Parameter:** *unterrichtsformen*  (Optional)
- 1
- 2
- 6
- 3
- 5
- 0

Lernform: 1=Vollzeit, 2=Teilzeit, 6=Blockunterricht, 3=Wochenendveranstaltung, 5=E-Learning, 0=Auf Anfrage. Mehrere Komma-getrennte Angaben möglich.


**Parameter:** *anbieter*  (Optional)

Anbieter-ID: numerische ID (z.B. 16574). Mehrere Komma-getrennte Angaben möglich.
Bei größeren Treffermengen ist für die Verwendung des Filters nach Anbietern eine Einschränkung auf Ort, Suchbegriff oder Umkreis erforderlich. 


### Beispiel:

```bash
bs=$(curl -m 60 \
-H "OAuthAccessToken: $token" \
'https://rest.arbeitsagentur.de/infosysbub/sprachfoerderung/pc/v1/bildungsangebot?systematiken=MC&page=0&umkreis=50&orte=Feucht_11.2147_49.375&sort=basc')
```
