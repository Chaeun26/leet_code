class ListNode:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key=key
        self.val=val
        self.next=next
        self.prev=prev
class LRUCache:

    def __init__(self, capacity: int):
        self.cache={}
        self.capacity = capacity
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: ListNode):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _remove_least(self, node: ListNode):
        node.prev.next = self.tail
        self.tail.prev = node.prev

    def _add_to_front(self, node: ListNode):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self._remove(node)
        self._add_to_front(node)

        return node.val

    def put(self, key: int, value: int) -> None:

        if key not in self.cache:
            new_node = ListNode(key,value)
            self.cache[key] = new_node
            self._add_to_front(new_node)

            if len(self.cache) > self.capacity:
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key] 
        else:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._add_to_front(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)