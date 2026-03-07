import re
from PyQt6.QtWidgets import QMainWindow, QTextEdit, QVBoxLayout, QWidget, QPushButton, QLineEdit, QLabel
from PyQt6.QtGui import QTextCursor, QFont
from PyQt6.QtCore import Qt

class PrismEditor(QTextEdit):
    def keyPressEvent(self, event):
        # TAB NAVIGATION: Jump between [placeholders]
        if event.key() == Qt.Key.Key_Tab:
            cursor = self.textCursor()
            text = self.toPlainText()
            pattern = re.compile(r"\[.*?\]")
            match = pattern.search(text, cursor.position())
            
            if not match: # Wrap around
                match = pattern.search(text, 0)
                
            if match:
                start, end = match.span()
                new_cursor = self.textCursor()
                new_cursor.setPosition(start)
                new_cursor.setPosition(end, QTextCursor.MoveMode.KeepAnchor)
                self.setTextCursor(new_cursor)
            return
        super().keyPressEvent(event)

class GraphenePrismUI(QMainWindow):
    def __init__(self, engine_callback):
        super().__init__()
        self.engine_callback = engine_callback
        self.setWindowTitle("Graphene Prism v1.0")
        self.resize(800, 600)
        
        layout = QVBoxLayout()
        self.input_hint = QLineEdit()
        self.input_hint.setPlaceholderText("Enter your prompt intent/hints here...")
        
        self.generate_btn = QPushButton("Generate Master Prompt")
        self.generate_btn.clicked.connect(self.run_generation)
        
        self.editor = PrismEditor()
        self.editor.setFont(QFont("Consolas", 12))
        
        layout.addWidget(QLabel("1. Input Intent:"))
        layout.addWidget(self.input_hint)
        layout.addWidget(self.generate_btn)
        layout.addWidget(QLabel("2. Refine (Use TAB to navigate [variables]):"))
        layout.addWidget(self.editor)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def run_generation(self):
        intent = self.input_hint.text()
        self.editor.setPlainText("Engine is thinking...")
        result = self.engine_callback(intent)
        self.editor.setPlainText(result)