# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from deutschland.berufssprachkurssuche.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from deutschland.berufssprachkurssuche.model.response import Response
from deutschland.berufssprachkurssuche.model.response_embedded import ResponseEmbedded
from deutschland.berufssprachkurssuche.model.response_embedded_aggregations import (
    ResponseEmbeddedAggregations,
)
from deutschland.berufssprachkurssuche.model.response_embedded_aggregations_anbieter_inner import (
    ResponseEmbeddedAggregationsANBIETERInner,
)
from deutschland.berufssprachkurssuche.model.response_embedded_aggregations_anzahlausgefiltert import (
    ResponseEmbeddedAggregationsANZAHLAUSGEFILTERT,
)
from deutschland.berufssprachkurssuche.model.response_embedded_aggregations_anzahlgesamt import (
    ResponseEmbeddedAggregationsANZAHLGESAMT,
)
from deutschland.berufssprachkurssuche.model.response_embedded_aggregations_beginntermin_inner import (
    ResponseEmbeddedAggregationsBEGINNTERMINInner,
)
from deutschland.berufssprachkurssuche.model.response_embedded_aggregations_regionen_inner import (
    ResponseEmbeddedAggregationsREGIONENInner,
)
from deutschland.berufssprachkurssuche.model.response_embedded_aggregations_sprachkurse_inner import (
    ResponseEmbeddedAggregationsSPRACHKURSEInner,
)
from deutschland.berufssprachkurssuche.model.response_embedded_aggregations_unterrichtsformen_inner import (
    ResponseEmbeddedAggregationsUNTERRICHTSFORMENInner,
)
from deutschland.berufssprachkurssuche.model.response_embedded_links import (
    ResponseEmbeddedLinks,
)
from deutschland.berufssprachkurssuche.model.response_embedded_links_first import (
    ResponseEmbeddedLinksFirst,
)
from deutschland.berufssprachkurssuche.model.response_embedded_page import (
    ResponseEmbeddedPage,
)
from deutschland.berufssprachkurssuche.model.response_embedded_termine_inner import (
    ResponseEmbeddedTermineInner,
)
from deutschland.berufssprachkurssuche.model.response_embedded_termine_inner_abstaende_inner import (
    ResponseEmbeddedTermineInnerAbstaendeInner,
)
from deutschland.berufssprachkurssuche.model.response_embedded_termine_inner_abstaende_inner_ort import (
    ResponseEmbeddedTermineInnerAbstaendeInnerOrt,
)
from deutschland.berufssprachkurssuche.model.response_embedded_termine_inner_adresse import (
    ResponseEmbeddedTermineInnerAdresse,
)
from deutschland.berufssprachkurssuche.model.response_embedded_termine_inner_adresse_koordinaten import (
    ResponseEmbeddedTermineInnerAdresseKoordinaten,
)
from deutschland.berufssprachkurssuche.model.response_embedded_termine_inner_angebot import (
    ResponseEmbeddedTermineInnerAngebot,
)
from deutschland.berufssprachkurssuche.model.response_embedded_termine_inner_angebot_bildungsanbieter import (
    ResponseEmbeddedTermineInnerAngebotBildungsanbieter,
)
from deutschland.berufssprachkurssuche.model.response_embedded_termine_inner_angebot_bildungsanbieter_adresse import (
    ResponseEmbeddedTermineInnerAngebotBildungsanbieterAdresse,
)
from deutschland.berufssprachkurssuche.model.response_embedded_termine_inner_angebot_bildungsanbieter_adresse_koordinaten import (
    ResponseEmbeddedTermineInnerAngebotBildungsanbieterAdresseKoordinaten,
)
from deutschland.berufssprachkurssuche.model.response_embedded_termine_inner_angebot_bildungsanbieter_adresse_ort_strasse import (
    ResponseEmbeddedTermineInnerAngebotBildungsanbieterAdresseOrtStrasse,
)
from deutschland.berufssprachkurssuche.model.response_embedded_termine_inner_angebot_bildungsanbieter_adresse_ort_strasse_land import (
    ResponseEmbeddedTermineInnerAngebotBildungsanbieterAdresseOrtStrasseLand,
)
from deutschland.berufssprachkurssuche.model.response_embedded_termine_inner_angebot_bildungsart import (
    ResponseEmbeddedTermineInnerAngebotBildungsart,
)
from deutschland.berufssprachkurssuche.model.response_embedded_termine_inner_angebot_schulart import (
    ResponseEmbeddedTermineInnerAngebotSchulart,
)
from deutschland.berufssprachkurssuche.model.response_embedded_termine_inner_angebot_suchworte_inner import (
    ResponseEmbeddedTermineInnerAngebotSuchworteInner,
)
from deutschland.berufssprachkurssuche.model.response_embedded_termine_inner_angebot_systematiken_inner import (
    ResponseEmbeddedTermineInnerAngebotSystematikenInner,
)
from deutschland.berufssprachkurssuche.model.response_embedded_termine_inner_dauer import (
    ResponseEmbeddedTermineInnerDauer,
)
from deutschland.berufssprachkurssuche.model.response_embedded_termine_inner_unterrichtsform import (
    ResponseEmbeddedTermineInnerUnterrichtsform,
)
