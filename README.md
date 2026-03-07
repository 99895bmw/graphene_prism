# 💎 graphene Prism
**Rapid prompt generation and prompt editing**

Did you ever have to make use of AI to get your work done? and so you detail the work and get it done; but then you need a bit of modification and hit that detailed retyping frustration? you miss the key elements to point out?

Ever spent 20 minutes crafting the 'perfect' AI prompt, only to realize you need one tiny modification? Then comes the frustration: retyping the boilerplate, missing key variables, and losing your creative flow. Graphene Prism fixes the friction.
**graphene prism** gets you covered!

Graphene Prism is a local RAG-powered prompt editor designed for high-precision prompt engineering. Built with **PyQt6**, **LangChain**, and **Ollama**, it leverages local LLMs to transform vague intents into structured, high-fidelity master prompts.

PS: Ignore the basic UI 

## 🚀 Key Features
* **Semantic Retrieval:** Uses `mxbai-embed-large` to pull engineering principles from your PDF library.
* **Interactive UI:** Custom `QTextCursor` logic for tabbing through `[placeholders]`.
* **Local-First:** Privacy-focused inference using `Llama 3.2` via Ollama.
* **Modular Architecture:** Designed for future **MCP (Model Context Protocol)** integration.
* **Highly personalized:** Works on your own resources, your own project files and your own rules (files placed in `/resources` folder)

## ✨ Samples
* **Flying horse :**
  
  Model used: Gemini nano banana 2 pro
  
  Prompt: `generate image of a cartoonish flying horse`
  
  <img width="2816" height="1536" alt="Gemini_Generated_Image_ntcm5cntcm5cntcm" src="https://github.com/user-attachments/assets/ec506912-fbfd-4570-adf5-4648f96961ae" />

  graphene_prompt: `generate image of a cartoonish flying horse`
  
  **With Modified prompt:**
  ```
  "Create a vibrant, whimsical illustration of a cartoonish flying horse, with a mix of 2D and 3D elements. The horse should have a slender, elongated body, a flowing mane, and a pair of large, expressive eyes. Its wings should be colorful, feathery, and slightly translucent, with a subtle gradient effect to give them a sense of depth.
  
  The background should be a bright, sunny sky with fluffy white clouds, and a few wispy strands of cloud should be trailing behind the horse as it flies. The horse's hooves should be bare, with a subtle glow effect to indicate its magical flying abilities.
  
  The style should be reminiscent of classic cartoons, with bold lines, bright colors, and a playful, exaggerated aesthetic. The overall mood should be one of joy, freedom, and wonder.
  
  [Color Palette: [insert desired color palette or specific colors]]
  [Style: [insert desired style, e.g. 'classic cartoon', 'whimsical', 'fantasy']]
  
  Please generate an image that meets these specifications, and feel free to add any additional details or elements that you think would enhance the illustration." 
  ```
  
  <img width="2816" height="1536" alt="Gemini_Generated_Image_9sjg849sjg849sjg" src="https://github.com/user-attachments/assets/75ec6584-5248-472c-b083-c2bf8fb55ddb" />

  Model used: Gemini nano banana 2 pro

* **Angry cat :**
 
  Model used: Gemini nano banana 2 pro
  
  Prompt: `create image of an angry cat`
  
  <img width="2816" height="1536" alt="Gemini_Generated_Image_3u0sog3u0sog3u0s" src="https://github.com/user-attachments/assets/5143b1fe-2362-4a10-9e53-ee786a92c720" />

  graphene_prompt: `create image of an angry cat`
  
  **With Modified prompt:**
  ```
    Create a digital image of a cat with a scowling expression, exhibiting a mix of emotions that convey anger and frustration. The cat should be depicted in a dynamic pose, with its fur ruffled and its ears laid back. Consider incorporating subtle visual cues that suggest the cat is about to lash out or swat at something.
  
  dark and moody
  
  realistic
  
  [Composition: isolate in a room]
  
  [Additional Elements: a couch in blurred background]
  ```
  <img width="2816" height="1536" alt="Gemini_Generated_Image_g46i58g46i58g46i" src="https://github.com/user-attachments/assets/c1c3fd8b-8f36-4acf-b6d2-98937d1aeca8" />

  Model used: Gemini nano banana 2 pro


## 💎 graphene Prism: User Instruction Manual
Graphene Prism is a local, AI-powered prompt engineering workbench. It uses Retrieval-Augmented Generation (RAG) to inject technical knowledge into your prompts and provides a frictionless UI for rapid editing.

The UI looks like :

<img width="1001" height="782" alt="Screenshot 2026-03-07 130108" src="https://github.com/user-attachments/assets/485b0233-f1bb-4b94-81e9-12e469cf7db2" />


## 1. Prerequisites & Installation
Before launching, ensure your local environment is ready:
* **Install Ollama:** Download from `ollama.com`.
* **Pull the Models:** Open your terminal and run:
  * `ollama pull llama3.2:3b` (The "Brain" for generation)
  * `ollama pull mxbai-embed-large:335m` (The "Librarian" for RAG)
* **Install Python Dependencies:**
  * `pip install -r requirements.txt`

## 2. Setting Up Your Knowledge Base
The "RAG" power of this tool comes from the documents you provide.
* **Create the `resources/` folder:** If it doesn't exist, create a folder named `resources` in the project root.
* **Add Your Files:** Drop your reference materials here.
* **Accepted File Types:** Currently, the system is optimized for PDFs (research papers, technical manuals, style guides).
* **Plain Text:** You can also add `.txt` files for simple lists of keywords or brand guidelines.
* **Pro Tip:** For the best results, use "Cheat Sheets" or "Framework Papers" (e.g., a PDF on the Midjourney V6 Parameter Guide).

## 3. Step-by-Step Workflow
1. **Launch the App:** Run `python main.py`.
2. **Enter Your Intent:** In the top input box, type a "hint" of what you want (e.g., "A futuristic dental clinic in Tuni with cyberpunk lighting").
3. **Generate:** Click "Generate Master Prompt". The engine will search your `resources/` folder, find relevant technical data, and use Llama 3.2 to build a "Master Prompt."
4. **Refine (The Tab-Through Feature):**
   * The generated prompt will appear in the editor with variables in brackets like `[lighting_type]` or `[camera_angle]`.
   * Press `Tab` on your keyboard. The cursor will automatically jump to the first `[...]`, highlight it, and allow you to type over it instantly.
   * Press `Tab` again to jump to the next variable.

## 4. Technical Insight: Our RAG Implementation

To make this project "Research-Grade," we didn't just use a simple search. We implemented Local Semantic Retrieval.
* **Embedding Model (`mxbai-embed-large`):** This model converts your PDFs into high-dimensional mathematical vectors. It doesn't just look for "words"; it understands "concepts".
* **Vector Database (ChromaDB):** This acts as a long-term memory. It stores the "meaning" of your research papers so they can be queried in milliseconds.
* **Context Injection:** When you type an intent, the system performs a "Similarity Search." It pulls the top 3 most relevant "chunks" of knowledge from your PDFs and feeds them into the LLM's "Hidden Context".
* **Zero-Cloud Privacy:** Because we use Ollama, your research PDFs and your generated prompts never leave your local machine.

## 5. Troubleshooting
* **10,000 Changes in Git:** Ensure your `.gitignore` is present in the root folder before committing.
* **404 Model Not Found:** Double-check that the model names in `rag_core.py` match your `ollama list` exactly (e.g., check for the `:335m` tag).
* **UI Crashing:** Check the terminal for errors. It usually means a PDF in your `resources/` folder is corrupted or Ollama isn't running.
