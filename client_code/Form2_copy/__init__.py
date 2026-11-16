from ._anvil_designer import Form2_copyTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import plotly.graph_objects as go

class Form2_copy(Form2_copyTemplate):
  def __init__(self, id, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)
    self.init_components(**properties)
    self.id = id
    # Any code you write here will run before the form opens.

  @handle("check_box_39", "change")
  def check_box_39_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    pass
    

  @handle("button_1", "click")
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form1')

  @handle("button_2", "click")
  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    filas = app_tables.valores_corporales.search(ID=self.id)
    fila = app_tables.valores_corporales.add_row(
      **{
      "ID": int(self.id),
      "N": int(len(filas) + 1),
      "Edad": int(self.edad.text),
      "Estatura": int(self.estatura.text),
      "Masa": int(self.masa.text),
      "Presión arterial sistólica": int(self.presiona.text),
      "Presión arterial diastólica": int(self.presionb.text),
      "Glucosa en sangre": float(self.glucosa.text),
      "Frecuencia cardíaca": int(self.pulso.text),
      "Saturación de O2": float(self.o2.text),
      "Temperatura corporal": int(self.temperatura.text),
      "Tiempo en el espacio": int(self.tiempo.text)
      }
    )

    fila1 = app_tables.sintomas.add_row(
      **{
      "ID": int(self.id),
      "N": int(len(filas) + 1),
      "D. Cabeza": self.cabeza,
      "Dolores": self.dolores,
      "D. Cuello": self.cuello,
      "D. Abdomen": self.abdomen,
      "D. Oído": self.oido,
      "D. Estómago": self.estomago,
      "D. Pecho": self.pecho,
      "D. Espalda": self.espalda,
      "D. Músculo": self.musculo,
      "D. Articulaciones": self.articulaciones,
      "Vómitos": self.nauseas,
      "Hinchazón": self.hinchazón,
      "Mareos": self.mareos,
      "Vértigo": self.vértigo,
      "Desorientación": self.desorientación,
      "Dificultad para concentrarse": self.dificultadparaconcentrarse,
      "Debilidad": self.Debilidad,
      "Visión borrosa": self.visiónborrosa,
      "Tos": self.tos,
      "Dificultad para respirar": self.dificultadpararespirar,
      "Sensación de falta de aire": self.sensacióndefaltadeaire,
      "Dolor al respirar": self.doloralrespirar,
      "Palpitaciones": self.palpitaciones,
      "Sensación de desmayo": self.sensacióndedesmayo,
      "Hinchazón de extremidades": self.hinchazóndeextremidades,
      "Dolor articular": self.dolorarticular,
      "Disminución de la cantidad de la orina": self.disminucióndelacantidaddelaorina,
      "Sudoración excesiva": self.sudoraciónexcesiva,
      "Sensación de fiebre": self.sensacióndefiebre,
      "Fatiga persistente": self.Fatigapersistente,
      "Dificultad de concentración": self.dificultaddeconcentracion,
      "Masa alta": self.masaalta,
      "Temperatura alta": self.temperaturaalta,
      "Temperatura baja": self.temperaturabaja,
      "Presión alta baja": self
      }
    )
    id2=self.id
    open_form('Form3', id2)