from ._anvil_designer import Form2_copyTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form2_copy(Form2_copyTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)

    # Any code you write here will run before the form opens.

  @handle("check_box_39", "change")
  def check_box_39_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    pass  # Write Code Here
