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
    filas = app_tables.astronautas.search()

    self.selector.items = [
      fila['Nombre completo'] for fila in filas
    ]

  @handle("button_1", "click")
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form2')

  @handle("button_2", "click")
  def button_2_click(self, **event_args):
    id=app_tables.astronautas.get(**{'Nombre completo': self.selector.selected_value})['ID']
    open_form('Form2_copy')