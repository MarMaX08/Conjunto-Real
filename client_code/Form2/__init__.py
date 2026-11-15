from ._anvil_designer import Form2Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import plotly.graph_objects as go

class Form2(Form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)

    # Any code you write here will run before the form opens.

  @handle("button_2", "click")
  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    fila = app_tables.astronautas.add_row(
      **{
      "ID": 1,
      "Nombre completo": self.nombre,
      "Edad": int(,
      "Estatura": 1.75,
      "Masa": 70,
      "Presión arterial sistólica": 120,
      "Presión arterial diastólica": 80,
      "Glucosa en sangre": 90,
      "Frecuencia cardíaca": 70,
      "Saturación de O2": 98
      }
    )
    open_form('Form1')

  @handle("button_1", "click")
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form1')