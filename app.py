def fetch_notion_data(title, objective):
    return [
        {"title": title, "objective": objective, "content": "Sample content related to " + title}
    ]

def generate_logic_tree(data):
    logic_tree = "Logic Tree for Data:\n"
    for item in data:
        logic_tree += f"- {item['title']}: {item['content']}\n"
    return logic_tree

def generate_mermaid_code(logic_tree):
    mermaid_code = "graph TD;\n"
    lines = logic_tree.split("\n")
    for line in lines:
        if line and line.startswith("-"):
            mermaid_code += "    " + line.replace("-", "node -->") + "\n"
    return mermaid_code

def create_excalidraw_diagram(mermaid_code):
    return f"Excalidraw Diagram:\n{mermaid_code}"

def refine_diagram(diagram, prompts, images):
    refined_diagram = diagram
    for prompt in prompts:
        refined_diagram += f"\nRefinement based on prompt: {prompt}" 
    for image in images:
        refined_diagram += f"\nImage: {image}"  
    return refined_diagram

if __name__ == "__main__":
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
