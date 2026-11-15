from ._anvil_designer import Form2_copyTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import plotly.graph_objects as go

class Form2_copy(Form2_copyTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)

    # Any code you write here will run before the form opens.

  @handle("check_box_39", "change")
  def check_box_39_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    pass  # Write Code Here

  @handle("button_1", "click")
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form1')

  @handle("button_2", "click")
  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    open_form('Form3')
