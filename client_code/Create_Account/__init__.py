from ._anvil_designer import Create_AccountTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Create_Account(Create_AccountTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
   name = self.name_box.text
   email = self.email_box.text
   password = self.password_box.text

   anvil.server.call('add_feedback', name, email, password)
   Notification("Account Created succesfully!").show()
   open_form('Create_Account.Form1')
   
   self.clear_inputs()

  
  def clear_inputs(self):
    self.name_box.text=""
    self.email_box.text=""
    self.password_box.text=""

  def name_box_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass
    
    
    
   

  
