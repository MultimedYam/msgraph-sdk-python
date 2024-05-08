from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .......models.partners.billing.attribute_set import AttributeSet

@dataclass
class ExportPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The attributeSet property
    attribute_set: Optional[AttributeSet] = None
    # The invoiceId property
    invoice_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ExportPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExportPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ExportPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .......models.partners.billing.attribute_set import AttributeSet

        from .......models.partners.billing.attribute_set import AttributeSet

        fields: Dict[str, Callable[[Any], None]] = {
            "attributeSet": lambda n : setattr(self, 'attribute_set', n.get_enum_value(AttributeSet)),
            "invoiceId": lambda n : setattr(self, 'invoice_id', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("attributeSet", self.attribute_set)
        writer.write_str_value("invoiceId", self.invoice_id)
        writer.write_additional_data_value(self.additional_data)
    

