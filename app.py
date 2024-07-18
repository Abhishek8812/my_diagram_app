def fetch_notion_data(title, objective):
    if not isinstance(title, str) or not isinstance(objective, str):
        raise ValueError("Title and Objective must be strings.")
    return [
        {"title": title, "objective": objective, "content": "Sample content related to " + title}
    ]

def generate_logic_tree(data):
    if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
        raise ValueError("Data must be a list of dictionaries.")
    logic_tree = "Logic Tree for Data:\n"
    for item in data:
        if 'title' not in item or 'content' not in item:
            raise KeyError("Each item in data must contain 'title' and 'content'.")
        logic_tree += f"- {item['title']}: {item['content']}\n"
    return logic_tree

def generate_mermaid_code(logic_tree):
    if not isinstance(logic_tree, str):
        raise ValueError("Logic tree must be a string.")
    mermaid_code = "graph TD;\n"
    lines = logic_tree.split("\n")
    for line in lines:
        if line and line.startswith("-"):
            mermaid_code += "    " + line.replace("-", "node -->") + "\n"
    return mermaid_code

def create_excalidraw_diagram(mermaid_code):
    if not isinstance(mermaid_code, str):
        raise ValueError("Mermaid code must be a string.")
    return f"Excalidraw Diagram:\n{mermaid_code}"

def refine_diagram(diagram, prompts, images):
    if not isinstance(diagram, str):
        raise ValueError("Diagram must be a string.")
    if not isinstance(prompts, list) or not all(isinstance(prompt, str) for prompt in prompts):
        raise ValueError("Prompts must be a list of strings.")
    if not isinstance(images, list) or not all(isinstance(image, str) for image in images):
        raise ValueError("Images must be a list of strings.")
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
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
