class Node:
    def __init__(self, data, priority=None):
        self.data = data
        self.priority = priority
        self.next = None
        
class PriorityQueue:
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head is None
    
    def leng(self):
        cnt = 0
        current = self.head

        while current is not None:
            cnt+=1
            current = current.next

        return cnt
    
    def push(self, data, priority):
        """Добавление элемента с приоритетом"""
        new_node = Node(data, priority)
        
        if self.is_empty() or priority > self.head.priority:
            new_node.next = self.head
            self.head = new_node
        else:
            # Ищем место для вставки
            current = self.head
            while (current.next is not None and 
                   current.next.priority >= priority):
                current = current.next
            
            new_node.next = current.next
            current.next = new_node
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Приоритетная очередь пуста")
        
        data = self.head.data
        if self.head.next is None:
            self.head = None  
        else:
            self.head = self.head.next

        return data
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Приоритетная очередь пуста")
        return self.head.data
    
    def display(self):
        
        if self.is_empty():
            print("Приоритетная очередь пуста")
            return
        
        current = self.head
        elements = []
        while current:
            elements.append(f"({current.data}, приоритет: {current.priority})")
            current = current.next
        print(" -> ".join(elements))
        
    def dop(self, nazv):
        if self.is_empty():
            raise IndexError("Приоритетная очередь пуста")
        
        if self.head.data == nazv:
            self.head = self.head.next
            return 
        current  = self.head

        while current.next is not None:
            if current.next.data == nazv:
                current.next = current.next.next
                return
            current = current.next
        
        raise ValueError(f"Элемент с данными '{nazv}' не найден")






class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def is_empty(self):
        return self.head is None
    
    def leng(self):
        cnt = 0
        current = self.head

        while current is not None:
            cnt+=1
            current = current.next

        return cnt
    
    def append(self, data):
        new_node = Node(data)
        
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def popleft(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        
        data = self.head.data
        self.head = self.head.next
        
        # Если после извлечения очередь стала пустой
        if self.head is None:
            self.tail = None
            
        return data
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self.head.data
    
    def display(self):
        if self.is_empty():
            print("Очередь пуста")
            return
        
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements))

    def dop(self, nazv):
        if self.is_empty():
            raise IndexError("очередь пуста")
        
        if self.head.data == nazv:
            self.head = self.head.next
            return 
        current  = self.head

        while current.next is not None:
            if current.next.data == nazv:
                current.next = current.next.next
                return
            current = current.next
        
        raise ValueError(f"Элемент с данными '{nazv}' не найден")

class Stack:
    def __init__(self):
        self.top = None
    
    def leng(self):
        cnt = 0
        current = self.head

        while current is not None:
            cnt+=1
            current = current.next

        return cnt
    
    def is_empty(self):
        return self.top is None
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Стек пуст")
        
        data = self.top.data
        self.top = self.top.next
        return data
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self.top.data
    
    def display(self):
        if self.is_empty():
            print("Стек пуст")
            return
        
        current = self.top
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print("""\n  |
  V
""".join(elements))
    
    def dop(self, nazv):
        if self.is_empty():
            raise IndexError("стек пуст")
        
        if self.top.data == nazv:
            self.top = self.top.next
            return 
        current  = self.top

        while current.next is not None:
            if current.next.data == nazv:
                current.next = current.next.next
                return
            current = current.next
        
        raise ValueError(f"Элемент с данными '{nazv}' не найден")
def vvod(start, end):
    while True:
        try:
            print(f"Введите число от {start} до {end}")
            chis = int(input())
            if chis>end or chis<start:
                print(f"ЧИСЛО ОТ {start} до {end}")
            else: return chis
        except:
            print("Введите число")

# Демонстрация работы всех структур
if __name__ == "__main__":
    print("=== ДЕМОНСТРАЦИЯ РАБОТЫ СТРУКТУР ДАННЫХ ===\n")
    var = vvod(1, 3)


    if var==1:

        print("1.ПРИОРИТЕТНАЯ ОЧЕРЕДЬ:")
        pq = PriorityQueue()
        for i in range(1, 10):
            pq.push(f"Задача{i}", i)
            print("Содержимое после добавления:")
            pq.display()
        pq.pop()
        print("Содержимое после удаления элемента с высшим приоритетом:")
        pq.display()
        pq.dop("Задача3")
        print("Содержимое после удаления элемента с определённым значением:")
        pq.display()
        
    if var ==2:
        print("2.ОЧЕРЕДЬ:")
        q = Queue()
        for i in range(1, 10):
            q.enqueue(f"Задача{i}")
            print("Содержимое после добавления:")
            q.display()
        q.dequeue()
        print("Содержимое после удаления первого элемента:")
        q.display()
        q.dop("Задача3")
        print("Содержимое после удаления элемента с определённым значением:")
        q.display()


    if var == 3:
        print("3.CТЕК:")
        st = Stack()
        for i in range(1, 10):
            st.push(f"Задача{i}")
            print("Содержимое после добавления:")
            st.display()
        st.pop()
        print("Содержимое после верхнего элемента:")    
        st.display()
        st.dop("Задача3")
        print("Содержимое после удаления элемента с определённым значением:")
        st.display()