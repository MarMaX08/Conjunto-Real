from ._anvil_designer import Form2_copyTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import plotly.graph_objects as go

class Form2_copy(Form2_copyTemplate):
  def __init__(self id, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)
    self.init_components(**properties)
    self.id = id
    # Any code you write here will run before the form opens.

  @handle("check_box_39", "change")
  def check_box_39_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    fila = app_tables.astronautas.add_row(
      **{
      "ID": int(),
      "Nombre completo": self.nombre.text,
      "Edad": int(self.edad.text),
      "Estatura": int(self.estatura.text),
      "Masa": int(self.masa.text),
      "Presión arterial sistólica": int(self.presiona.text),
      "Presión arterial diastólica": int(self.presionb.text),
      "Glucosa en sangre": float(self.glucosa.text),
      "Frecuencia cardíaca": int(self.pulso.text),
      "Saturación de O2": float(self.o2.text)
      }
    )
    open_form('Form3')

  @handle("button_1", "click")
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form1')
