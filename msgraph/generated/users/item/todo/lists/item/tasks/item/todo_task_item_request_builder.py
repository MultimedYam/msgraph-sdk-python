from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ........models.odata_errors.odata_error import ODataError
    from ........models.todo_task import TodoTask
    from .attachments.attachments_request_builder import AttachmentsRequestBuilder
    from .attachment_sessions.attachment_sessions_request_builder import AttachmentSessionsRequestBuilder
    from .checklist_items.checklist_items_request_builder import ChecklistItemsRequestBuilder
    from .extensions.extensions_request_builder import ExtensionsRequestBuilder
    from .linked_resources.linked_resources_request_builder import LinkedResourcesRequestBuilder

class TodoTaskItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the tasks property of the microsoft.graph.todoTaskList entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new TodoTaskItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/todo/lists/{todoTaskList%2Did}/tasks/{todoTask%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property tasks for users
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ........models.odata_errors.odata_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[TodoTaskItemRequestBuilderGetQueryParameters]] = None) -> Optional[TodoTask]:
        """
        The tasks in this task list. Read-only. Nullable.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TodoTask]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ........models.odata_errors.odata_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ........models.todo_task import TodoTask

        return await self.request_adapter.send_async(request_info, TodoTask, error_mapping)
    
    async def patch(self,body: TodoTask, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[TodoTask]:
        """
        Update the navigation property tasks in users
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TodoTask]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ........models.odata_errors.odata_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ........models.todo_task import TodoTask

        return await self.request_adapter.send_async(request_info, TodoTask, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property tasks for users
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[TodoTaskItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        The tasks in this task list. Read-only. Nullable.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: TodoTask, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property tasks in users
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> TodoTaskItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: TodoTaskItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return TodoTaskItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def attachment_sessions(self) -> AttachmentSessionsRequestBuilder:
        """
        Provides operations to manage the attachmentSessions property of the microsoft.graph.todoTask entity.
        """
        from .attachment_sessions.attachment_sessions_request_builder import AttachmentSessionsRequestBuilder

        return AttachmentSessionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def attachments(self) -> AttachmentsRequestBuilder:
        """
        Provides operations to manage the attachments property of the microsoft.graph.todoTask entity.
        """
        from .attachments.attachments_request_builder import AttachmentsRequestBuilder

        return AttachmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def checklist_items(self) -> ChecklistItemsRequestBuilder:
        """
        Provides operations to manage the checklistItems property of the microsoft.graph.todoTask entity.
        """
        from .checklist_items.checklist_items_request_builder import ChecklistItemsRequestBuilder

        return ChecklistItemsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def extensions(self) -> ExtensionsRequestBuilder:
        """
        Provides operations to manage the extensions property of the microsoft.graph.todoTask entity.
        """
        from .extensions.extensions_request_builder import ExtensionsRequestBuilder

        return ExtensionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def linked_resources(self) -> LinkedResourcesRequestBuilder:
        """
        Provides operations to manage the linkedResources property of the microsoft.graph.todoTask entity.
        """
        from .linked_resources.linked_resources_request_builder import LinkedResourcesRequestBuilder

        return LinkedResourcesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class TodoTaskItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class TodoTaskItemRequestBuilderGetQueryParameters():
        """
        The tasks in this task list. Read-only. Nullable.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    @dataclass
    class TodoTaskItemRequestBuilderGetRequestConfiguration(RequestConfiguration[TodoTaskItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class TodoTaskItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

