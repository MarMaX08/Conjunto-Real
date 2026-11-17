from ._anvil_designer import Form2_copyTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import plotly.graph_objects as go
import random

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
      "D. Cabeza": self.cabeza.checked,
      "Dolores": self.dolores.checked,
      "D. Cuello": self.cuello.checked,
      "D. Abdomen": self.abdomen.checked,
      "D. Oído": self.oido.checked,
      "D. Estómago": self.estomago.checked,
      "D. Pecho": self.pecho.checked,
      "D. Espalda": self.espalda.checked,
      "D. Músculo": self.musculo.checked,
      "D. Articulaciones": self.articulaciones.checked,
      "Náuseas": self.nauseas.checked,
      "Hinchazón": self.hinchazon.checked,
      "Mareos": self.mareos.checked,
      "Vértigo": self.vertigo.checked,
      "Desorientación": self.desorientacion.checked,
      "Dificultad para concentrarse": self.dificultadparaconcentrarse.checked,
      "Debilidad": self.debilidad.checked,
      "Visión borrosa": self.visionborrosa.checked,
      "Tos": self.tos.checked,
      "Dificultad para respirar": self.dificultadpararespirar.checked,
      "Sensación de falta de aire": self.sensaciondefaltadeaire.checked,
      "Dolor al respirar": self.doloralrespirar.checked,
      "Palpitaciones": self.palpitaciones.checked,
      "Sensación de desmayo": self.sensaciondedesmayo.checked,
      "Hinchazón de extremidades": self.hinchazondeextremidades.checked,
      "Dolor articular": self.dolorarticular.checked,
      "Disminución de la cantidad de la orina": self.disminuciondelacantidaddelaorina.checked,
      "Sudoración excesiva": self.sudoracionexcesiva.checked,
      "Sensación de fiebre": self.sensaciondefiebre.checked,
      "Fatiga persistente": self.fatigapersistente.checked,
      "Enrojecimiento": self.enrojecimiento.checked, 
      "Masa alta": (float(fila['Masa']) > float(app_tables.astronautas.get(ID=self.id)['Masa']) + float(self.tiempo.text)*0.00208 or float(fila['Masa']) > int(app_tables.astronautas.get(ID=self.id)['Masa']) + 20),
      "Temperatura alta": (float(fila['Temperatura corporal']) > 310),
      "Temperatura baja": (float(fila['Temperatura corporal']) < 308),
      "Presión alta baja": (float(fila['Presión arterial sistólica']) < 90),
      "Presión alta alta": (float(fila['Presión arterial sistólica']) > 140),
      "Presión baja alta": (float(fila['Presión arterial diastólica']) > 90),
      "Presión baja baja": (float(fila['Presión arterial diastólica']) < 60),
      "Pulso bajo": (float(fila['Frecuencia cardíaca']) < 60),
      "Pulso alto": (float(fila['Frecuencia cardíaca']) > 110),
      }
    )
    fila = app_tables.valores_ambientales.add_row(
      **{
      "ID": int(self.id),
      "N": int(len(filas) + 1),
      "Radiación acumulada": int(self.radiacion.text),
      "Tasa de radiación": int(self.tasaradiacion.text)
      }
    )

    
    id2=self.id
    fsintomas=self.fila
    open_form('Form3', id2)