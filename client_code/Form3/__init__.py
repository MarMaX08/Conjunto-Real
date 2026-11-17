from ._anvil_designer import Form3Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Form3(Form3Template):
  def __init__(self, id2, fs, **properties):
   
    super().__init__(**properties)
    self.init_components(**properties)
    self.id2 = id2
    self.fs=fs
    self.analizar_enfermedades()
    
  @handle("button_1", "click")
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form1')
    
  def analizar_enfermedades(self):
  

    # 3. Traemos todas las enfermedades de la tabla
   todas_enfermedades = app_tables.enfermedades.search()
   enfermedades_posibles = []

  
   sintomas = {columna['name']: self.fs[columna['name']] for columna in app_tables.sintomas.list_columns()}

   for enfermedad in todas_enfermedades:
      nombre_enfermedad = enfermedad['Enfermedades']
      agregada = False
      # Revisamos cada síntoma indicado por el paciente
      for sintoma, valor_requerido in sintomas.items():
        if sintoma in enfermedad:
          # Si el paciente SÍ tiene el síntoma (valor_requerido == True), 
          # PERO la enfermedad en la tabla dice que NO lo tiene (enfermedad[sintoma] == False)
          if valor_requerido and enfermedad[sintoma]:
            agregada = True
            break # Descargamos esta enfermedad porque le falta un síntoma obligatorio

            # Si cumplió con todo y no falló en ningún síntoma requerido, la agregamos
      if agregada:
        enfermedades_posibles.append(nombre_enfermedad)

      # 5. Mostramos el resultado en el Form3 (por ejemplo, en un RepeatingPanel o Label)
      # Si tienes un RepeatingPanel llamado 'repeating_panel_1':
      # 5. Mostramos el resultado en la etiqueta (Label)
   self.lista.text = "\n".join([f"- {e}" for e in enfermedades_posibles])
    # O si prefieres mostrarlo en una etiqueta (Label):
    # self.label_resultado.text = ", ".join(enfermedades_posibles)