import sys
from PyQt6.QtWidgets import QApplication
from engine.rag_core import GrapheneEngine
from ui.main_window import GraphenePrismUI

def main():
    app = QApplication(sys.argv)
    
    # Initialize Engine
    engine = GrapheneEngine()
    
    # Initialize UI with Engine hook
    window = GraphenePrismUI(engine_callback=engine.generate_prompt)
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()