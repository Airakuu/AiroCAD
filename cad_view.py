from PySide6.QtWidgets import QGraphicsView
from PySide6.QtCore import Qt


class CadView(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.min_zoom = 0.7
        self.max_zoom = 5.0

        self.setTransformationAnchor(
            QGraphicsView.ViewportAnchor.AnchorUnderMouse
        )

        self.dragging = False
        self.last_mouse_pos = None

    def wheelEvent(self, event):
        zoom_factor = 1.2 if event.angleDelta().y() > 0 else 1 / 1.2

        current_zoom = abs(self.transform().m11())
        target_zoom = current_zoom * zoom_factor

        target_zoom = max(self.min_zoom, min(target_zoom, self.max_zoom))

        self.scale(
            target_zoom / current_zoom,
            target_zoom / current_zoom
        )

        event.accept()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.MiddleButton:
            self.dragging = True
            self.last_mouse_pos = event.position().toPoint()
            self.viewport().setCursor(Qt.CursorShape.ClosedHandCursor)
            event.accept()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.dragging:
            current_pos = event.position().toPoint()
            delta = current_pos - self.last_mouse_pos

            self.horizontalScrollBar().setValue(
                self.horizontalScrollBar().value() - delta.x()
            )

            self.verticalScrollBar().setValue(
                self.verticalScrollBar().value() - delta.y()
            )

            self.last_mouse_pos = current_pos
            event.accept()
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.MiddleButton:
            self.dragging = False
            self.viewport().unsetCursor()
            event.accept()
        else:
            super().mouseReleaseEvent(event)