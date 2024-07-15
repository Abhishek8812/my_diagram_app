from flask import Flask, render_template, request

app = Flask(__name__)

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
        if line:
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

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        objective = request.form['objective']
        
        data = fetch_notion_data(title, objective)
        logic_tree = generate_logic_tree(data)
        mermaid_code = generate_mermaid_code(logic_tree)
        diagram = create_excalidraw_diagram(mermaid_code)
        
        prompts = ["Add a detailed explanation of each node", "Include examples"]
        images = ["image1.jpeg", "image2.jpeg"]
        
        final_diagram = refine_diagram(diagram, prompts, images)
        
        return render_template('index.html', final_diagram=final_diagram)
    
    return render_template('index.html', final_diagram=None)

if __name__ == "__main__":
    app.run(debug=True)
