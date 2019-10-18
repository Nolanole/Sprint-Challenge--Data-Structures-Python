class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

  def reverse_list(self):
    #start at the head
    current = self.head
    #if list is empty (no head) or has a head but no next (1 item), nothing to reverse so just return
    if current is None or current.get_next() is None:
      return

    else:
      #first traverse to the next item in the list
      current = current.get_next()

      #the head is going to be the new tail, so set its next attribute to None
      self.head.set_next(None)
    
    #whlie loop to traverse the list until the old tail has been reached  
    while current:
      #assign the value of the current node to variable
      val = current.get_value()
      
      #update the current var (aka traverse to next item in list)- when tail reached, loop breaks:
      current = current.get_next()
      
      #add the value of current node to the head of the list
      self.add_to_head(val)