from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import plotly.graph_objects as go
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    super().__init__(**properties)

  @handle("button_1", "click")
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form2')

  @handle("button_2", "click")
  def button_2_click(self, **event_args):
    

    fila = app_tables.astronautas.add_row(
        **{
          "ID"=2,
        "Nombre completo"="a",
        "edad=75,
        estatura=98
    )
    open_form('Form2_copy')
