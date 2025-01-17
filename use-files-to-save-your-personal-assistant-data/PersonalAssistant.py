class PersonalAssistant:

  def __init__(self, todos):
    self.todos = todos
    
  def add_todo(self, new_item):
    self.todos.append(new_item)

  def remove_todo(self, todo_item):
    if todo_item in self.todos:
    # Get the todo_item index in list
      index = self.todos.index(todo_item)
    # pop the index for todo_item in todos list
      self.todos.pop(index)
    else:
      print("Todo is not in list!")

  def get_todos(self):
    return self.todos

  def get_birthday(self, name):
    if name == "Jose":
      print("Birthday is 18/7/1981")
    elif name == "Nadia":
      print("Birthday is 12/4/2011")
    elif user_input == "Martin":
      print("Birthday is 17/11/2013")
    else: 
      print("Can't find a birthday for this person...")

  def get_contact(self, name):
    if name in self.contacts:
      return self.contacts[name]
    else:
      return "There is no contact with that name."


# # Code to test output of the class
# assistant = PersonalAssistant()
# assistant.add_todo("Pick up groceries")
# # Change name to one from your contacts
# print(assistant.get_contact("Ann"))
# print(assistant.get_todos())
# print(assistant.get_birthday("Jose"))