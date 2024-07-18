class CustomError(Exception):
    pass

class BodyNotAStringFromFunctionError(CustomError):
    pass

class EdgeFunctionInvocationFailedError(CustomError):
    pass

class InternalEdgeFunctionInvocationFailedError(CustomError):
    pass

class InternalEdgeFunctionInvocationTimeoutError(CustomError):
    pass

class EdgeFunctionInvocationTimeoutError(CustomError):
    pass

class FunctionInvocationFailedError(CustomError):
    pass

class FunctionInvocationTimeoutError(CustomError):
    pass

class FunctionPayloadTooLargeError(CustomError):
    pass

class FunctionResponsePayloadTooLargeError(CustomError):
    pass

class FunctionRateLimitError(CustomError):
    pass

class InternalFunctionInvocationFailedError(CustomError):
    pass

class InternalFunctionInvocationTimeoutError(CustomError):
    pass

class InternalFunctionNotFoundError(CustomError):
    pass

class InternalFunctionNotReadyError(CustomError):
    pass

class NoResponseFromFunctionError(CustomError):
    pass

class DeploymentBlockedError(CustomError):
    pass

class DeploymentPausedError(CustomError):
    pass

class DeploymentDisabledError(CustomError):
    pass

class DeploymentNotFoundError(CustomError):
    pass

class DeploymentNotReadyRedirectingError(CustomError):
    pass

class InternalDeploymentFetchFailedError(CustomError):
    pass

class InternalUnarchiveFailedError(CustomError):
    pass

class InfiniteLoopDetectedError(CustomError):
    pass

class InternalUnexpectedError(CustomError):
    pass

class DnsHostnameEmptyError(CustomError):
    pass

class DnsHostnameNotFoundError(CustomError):
    pass

class DnsHostnameResolveFailedError(CustomError):
    pass

class DnsHostnameResolvedPrivateError(CustomError):
    pass

class DnsHostnameServerError(CustomError):
    pass

class TooManyForksError(CustomError):
    pass

class TooManyFilesystemChecksError(CustomError):
    pass

class InternalRouterCannotParsePathError(CustomError):
    pass

class RouterCannotMatchError(CustomError):
    pass

class RouterExternalTargetConnectionError(CustomError):
    pass

class RouterExternalTargetError(CustomError):
    pass

class RouterTooManyHasSelectionsError(CustomError):
    pass

class RouterExternalTargetHandshakeError(CustomError):
    pass

class InvalidRequestMethodError(CustomError):
    pass

class MalformedRequestHeaderError(CustomError):
    pass

class RequestHeaderTooLargeError(CustomError):
    pass

class InternalStaticRequestFailedError(CustomError):
    pass

class ResourceNotFoundError(CustomError):
    pass

class RangeEndNotValidError(CustomError):
    pass

class RangeGroupNotValidError(CustomError):
    pass

class RangeMissingUnitError(CustomError):
    pass

class RangeStartNotValidError(CustomError):
    pass

class RangeUnitNotSupportedError(CustomError):
    pass

class TooManyRangesError(CustomError):
    pass

class UrlTooLongError(CustomError):
    pass

class InvalidImageOptimizeRequestError(CustomError):
    pass

class InternalOptimizedImageRequestFailedError(CustomError):
    pass

class OptimizedExternalImageRequestFailedError(CustomError):
    pass

class OptimizedExternalImageRequestInvalidError(CustomError):
    pass

class OptimizedExternalImageRequestUnauthorizedError(CustomError):
    pass

class OptimizedExternalImageTooManyRedirectsError(CustomError):
    pass

class FallbackBodyTooLargeError(CustomError):
    pass

class InternalCacheError(CustomError):
    pass

class InternalCacheKeyTooLongError(CustomError):
    pass

class InternalCacheLockFullError(CustomError):
    pass

class InternalCacheLockTimeoutError(CustomError):
    pass

class InternalMissingResponseFromCacheError(CustomError):
    pass

def fetch_notion_data(title, objective):
    if not isinstance(title, str) or not isinstance(objective, str):
        raise BodyNotAStringFromFunctionError("Title and Objective must be strings.")
    return [
        {"title": title, "objective": objective, "content": "Sample content related to " + title}
    ]

def generate_logic_tree(data):
    if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
        raise FunctionInvocationFailedError("Data must be a list of dictionaries.")
    logic_tree = "Logic Tree for Data:\n"
    for item in data:
        if 'title' not in item or 'content' not in item:
            raise InternalUnexpectedError("Each item in data must contain 'title' and 'content'.")
        logic_tree += f"- {item['title']}: {item['content']}\n"
    return logic_tree

def generate_mermaid_code(logic_tree):
    if not isinstance(logic_tree, str):
        raise BodyNotAStringFromFunctionError("Logic tree must be a string.")
    mermaid_code = "graph TD;\n"
    lines = logic_tree.split("\n")
    for line in lines:
        if line and line.startswith("-"):
            mermaid_code += "    " + line.replace("-", "node -->") + "\n"
    return mermaid_code

def create_excalidraw_diagram(mermaid_code):
    if not isinstance(mermaid_code, str):
        raise BodyNotAStringFromFunctionError("Mermaid code must be a string.")
    return f"Excalidraw Diagram:\n{mermaid_code}"

def refine_diagram(diagram, prompts, images):
    if not isinstance(diagram, str):
        raise BodyNotAStringFromFunctionError("Diagram must be a string.")
    if not isinstance(prompts, list) or not all(isinstance(prompt, str) for prompt in prompts):
        raise FunctionInvocationFailedError("Prompts must be a list of strings.")
    if not isinstance(images, list) or not all(isinstance(image, str) for image in images):
        raise FunctionInvocationFailedError("Images must be a list of strings.")
    refined_diagram = diagram
    for prompt in prompts:
        refined_diagram += f"\nRefinement based on prompt: {prompt}" 
    for image in images:
        refined_diagram += f"\nImage: {image}"  
    return refined_diagram

if __name__ == "__main__":
    try:
        title = 'Sample Title'
        objective = 'Sample Objective'
       
        data = fetch_notion_data(title, objective)    
        logic_tree = generate_logic_tree(data)    
        mermaid_code = generate_mermaid_code(logic_tree)    
        diagram = create_excalidraw_diagram(mermaid_code)    
        
        prompts = ["Add a detailed explanation of each node", "Include examples"]
        images = ["image1.png", "image2.png"]    
        
        final_diagram = refine_diagram(diagram, prompts, images)    
        print(final_diagram)
    except CustomError as e:
        print(f"Error: {e}")
