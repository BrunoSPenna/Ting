from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._queue = []

    def __len__(self):
        return len(self._queue)

    def enqueue(self, value):
        self._queue.append(value)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("A fila está vazia")
        return self._queue.pop(0)

    def search(self, index):
        if not 0 <= index < len(self._queue):
            raise IndexError("Índice Inválido ou Inexistente")
        return self._queue[index]

    def is_empty(self):
        return len(self._queue) == 0
