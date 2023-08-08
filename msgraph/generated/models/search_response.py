from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .alteration_response import AlterationResponse
    from .result_template_dictionary import ResultTemplateDictionary
    from .search_hits_container import SearchHitsContainer

@dataclass
class SearchResponse(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # A collection of search results.
    hits_containers: Optional[List[SearchHitsContainer]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Provides information related to spelling corrections in the alteration response.
    query_alteration_response: Optional[AlterationResponse] = None
    # A dictionary of resultTemplateIds and associated values, which include the name and JSON schema of the result templates.
    result_templates: Optional[ResultTemplateDictionary] = None
    # Contains the search terms sent in the initial search query.
    search_terms: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SearchResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SearchResponse
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SearchResponse()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .alteration_response import AlterationResponse
        from .result_template_dictionary import ResultTemplateDictionary
        from .search_hits_container import SearchHitsContainer

        from .alteration_response import AlterationResponse
        from .result_template_dictionary import ResultTemplateDictionary
        from .search_hits_container import SearchHitsContainer

        fields: Dict[str, Callable[[Any], None]] = {
            "hitsContainers": lambda n : setattr(self, 'hits_containers', n.get_collection_of_object_values(SearchHitsContainer)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "queryAlterationResponse": lambda n : setattr(self, 'query_alteration_response', n.get_object_value(AlterationResponse)),
            "resultTemplates": lambda n : setattr(self, 'result_templates', n.get_object_value(ResultTemplateDictionary)),
            "searchTerms": lambda n : setattr(self, 'search_terms', n.get_collection_of_primitive_values(str)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_collection_of_object_values("hitsContainers", self.hits_containers)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("queryAlterationResponse", self.query_alteration_response)
        writer.write_object_value("resultTemplates", self.result_templates)
        writer.write_collection_of_primitive_values("searchTerms", self.search_terms)
        writer.write_additional_data_value(self.additional_data)
    

