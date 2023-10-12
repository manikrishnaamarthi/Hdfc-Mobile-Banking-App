from ._anvil_designer import FeedbackTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Feedback(FeedbackTemplate):
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
   self.clear_inputs()

  
  def clear_inputs(self):
    self.name_box.text=""
    self.email_box.text=""
    self.password_box.text=""
    
   

  
