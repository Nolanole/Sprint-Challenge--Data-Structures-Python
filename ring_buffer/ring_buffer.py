#### Method 1: Python List

class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    self.storage[self.current] = item
    if self.current == self.capacity-1:
      self.current = 0
    else:
      self.current += 1

  def get(self):
    return [item for item in self.storage if item is not None]


#### Method 2: Q and Stack:
from doubly_linked_list import DoublyLinkedList

class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = None
    self.dll = DoublyLinkedList()
    self.storage = [None]*capacity

  def append(self, item):
    #if its the first item, add to head and update <current last-in item> as the head
    if self.dll.length == 0:
      self.dll.add_to_head(item)
      self.current = self.dll.head
    #if list has items but not yet reached capacity: add to tail
    elif self.dll.length < self.capacity:
      self.dll.add_to_tail(item)
      #if its now at capacity after adding this item, have the nodes 'next' attribute point to the head
      if self.dll.length == self.capacity:
        self.dll.tail.next = self.dll.head
    #if list is already at capacity, overwrite the last in node (current) with the new item
    else:
      self.current.value = item
      #update the node which last in (current) points to
      self.current = self.current.next
    #call the update storage function to update the storage list to reflect the correct values in the right order
    self.update_storage()

  def update_storage(self):
    l = []
    if self.dll.head is not None:
      current = True
      curr_item = self.dll.head
    while current:
      l.append(curr_item.value)
      if curr_item.next == self.dll.head:
        current = False
      else:
        if curr_item.next is None:
          current=False
        else:
          curr_item = curr_item.next

    if len(l) < self.capacity:
      l += [None]*(self.capacity - len(l))
    
    self.storage = l

  def get(self):
    return [item for item in self.storage if item is not None]