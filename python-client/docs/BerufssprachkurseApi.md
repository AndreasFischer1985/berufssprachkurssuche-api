# berufssprachkurssuche.BerufssprachkurseApi

All URIs are relative to *https://rest.arbeitsagentur.de/infosysbub/sprachfoerderung*

Method | HTTP request | Description
------------- | ------------- | -------------
[**berufssprachkurssuche**](BerufssprachkurseApi.md#berufssprachkurssuche) | **GET** /pc/v1/bildungsangebot | Berufssprachkurssuche


# **berufssprachkurssuche**
> Response berufssprachkurssuche()

Berufssprachkurssuche

Die Berufssprachkurssuche ermöglicht verfügbare Berufssprachkursangebote mit verschiedenen GET-Parametern zu filtern.

### Example

* OAuth Authentication (clientCredAuth):

```python
import time
from deutschland import berufssprachkurssuche
from deutschland.berufssprachkurssuche.api import berufssprachkurse_api
from deutschland.berufssprachkurssuche.model.response import Response
from pprint import pprint
# Defining the host is optional and defaults to https://rest.arbeitsagentur.de/infosysbub/sprachfoerderung
# See configuration.py for a list of all supported configuration parameters.
configuration = berufssprachkurssuche.Configuration(
    host = "https://rest.arbeitsagentur.de/infosysbub/sprachfoerderung"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: clientCredAuth
configuration = berufssprachkurssuche.Configuration(
    host = "https://rest.arbeitsagentur.de/infosysbub/sprachfoerderung"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with berufssprachkurssuche.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = berufssprachkurse_api.BerufssprachkurseApi(api_client)
    systematiken = "MC" # str | Kursart - MC=Berufssprachkurse; MB=Integrationskurse; A8 = Bildungsangebote Migration; MQ = Anerkennung ausländischer Berufsabschlüsse. (optional)
    suchworte = "Deutschsprachf%25C3%25B6rderung" # str | Suchworte (z.B. Deutschsprachf%25C3%25B6rderung,Berufsbezogener%2520Englischkurs). Mehrere Komma-getrennte Angaben möglich. (optional)
    orte = "Feucht_90537_11.224918_49.376701" # str | Ortsangabe nebst Postleitzahl und Koordinaten (longitude und latitude) jeweils durch Unterstriche getrennt (z.B. Feucht_90537_11.224918_49.376701,N%C3%BCrnberg;%20Mittelfranken_11.0753_49.4508). Mehrere Komma-getrennte Angaben möglich. (optional)
    page = 1 # int | Seite (beginnend mit 0 für die erste Seite). (optional)
    umkreis = "Bundesweit" # str | Umkreis - Bundesweit=Bundesweit, 25=25 km, 50=50 km, 100=100 km, 150=150 km, 200=200 km. (optional)
    sprachniveau = "MC%2001%201" # str | Sprachzielniveau - MC%2001%201=A2, MC%2001%202=B1, MC%2001%203=B2, MC%2001%204=C1, MC%2001%205=C2. Mehrere Komma-getrennte Angaben möglich. (optional)
    berufsfachsprachkurse = "MC%2003" # str | Berufsfachsprachkurse - MC%2002=Spezialberufskurs, MC%2003=Berufsanerkennung. Mehrere Komma-getrennte Angaben möglich. (optional)
    beginntermine = 1 # int | Beginntermin - 0=regelmäßiger Start, 1=diesen Monat, 2=nächster Monat, 3=übernächster Monat, 4=überübernächster Monat, 5=spätere Termine, 6=frühere Termine. Mehrere Komma-getrennte Angaben möglich. (optional)
    unterrichtsformen = 0 # int | Lernform - 1=Vollzeit, 2=Teilzeit, 6=Blockunterricht, 3=Wochenendveranstaltung, 5=E-Learning, 0=Auf Anfrage. Mehrere Komma-getrennte Angaben möglich. (optional)
    anbieter = 16574 # int | Anbieter-ID - numerische ID (z.B. 16574). Mehrere Komma-getrennte Angaben möglich. Bei größeren Treffermengen ist für die Verwendung des Filters nach Anbietern eine Einschränkung auf Ort, Suchbegriff oder Umkreis erforderlich. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Berufssprachkurssuche
        api_response = api_instance.berufssprachkurssuche(systematiken=systematiken, suchworte=suchworte, orte=orte, page=page, umkreis=umkreis, sprachniveau=sprachniveau, berufsfachsprachkurse=berufsfachsprachkurse, beginntermine=beginntermine, unterrichtsformen=unterrichtsformen, anbieter=anbieter)
        pprint(api_response)
    except berufssprachkurssuche.ApiException as e:
        print("Exception when calling BerufssprachkurseApi->berufssprachkurssuche: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **systematiken** | **str**| Kursart - MC&#x3D;Berufssprachkurse; MB&#x3D;Integrationskurse; A8 &#x3D; Bildungsangebote Migration; MQ &#x3D; Anerkennung ausländischer Berufsabschlüsse. | [optional]
 **suchworte** | **str**| Suchworte (z.B. Deutschsprachf%25C3%25B6rderung,Berufsbezogener%2520Englischkurs). Mehrere Komma-getrennte Angaben möglich. | [optional]
 **orte** | **str**| Ortsangabe nebst Postleitzahl und Koordinaten (longitude und latitude) jeweils durch Unterstriche getrennt (z.B. Feucht_90537_11.224918_49.376701,N%C3%BCrnberg;%20Mittelfranken_11.0753_49.4508). Mehrere Komma-getrennte Angaben möglich. | [optional]
 **page** | **int**| Seite (beginnend mit 0 für die erste Seite). | [optional]
 **umkreis** | **str**| Umkreis - Bundesweit&#x3D;Bundesweit, 25&#x3D;25 km, 50&#x3D;50 km, 100&#x3D;100 km, 150&#x3D;150 km, 200&#x3D;200 km. | [optional]
 **sprachniveau** | **str**| Sprachzielniveau - MC%2001%201&#x3D;A2, MC%2001%202&#x3D;B1, MC%2001%203&#x3D;B2, MC%2001%204&#x3D;C1, MC%2001%205&#x3D;C2. Mehrere Komma-getrennte Angaben möglich. | [optional]
 **berufsfachsprachkurse** | **str**| Berufsfachsprachkurse - MC%2002&#x3D;Spezialberufskurs, MC%2003&#x3D;Berufsanerkennung. Mehrere Komma-getrennte Angaben möglich. | [optional]
 **beginntermine** | **int**| Beginntermin - 0&#x3D;regelmäßiger Start, 1&#x3D;diesen Monat, 2&#x3D;nächster Monat, 3&#x3D;übernächster Monat, 4&#x3D;überübernächster Monat, 5&#x3D;spätere Termine, 6&#x3D;frühere Termine. Mehrere Komma-getrennte Angaben möglich. | [optional]
 **unterrichtsformen** | **int**| Lernform - 1&#x3D;Vollzeit, 2&#x3D;Teilzeit, 6&#x3D;Blockunterricht, 3&#x3D;Wochenendveranstaltung, 5&#x3D;E-Learning, 0&#x3D;Auf Anfrage. Mehrere Komma-getrennte Angaben möglich. | [optional]
 **anbieter** | **int**| Anbieter-ID - numerische ID (z.B. 16574). Mehrere Komma-getrennte Angaben möglich. Bei größeren Treffermengen ist für die Verwendung des Filters nach Anbietern eine Einschränkung auf Ort, Suchbegriff oder Umkreis erforderlich. | [optional]

### Return type

[**Response**](Response.md)

### Authorization

[clientCredAuth](../README.md#clientCredAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

