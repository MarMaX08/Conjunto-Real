from ._anvil_designer import Form3Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Form3(Form3Template):
  def __init__(self, **properties):
   
    super().__init__(**properties)


  @handle("button_1", "click")
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form1')
  def analizar_enfermedades(self):
      # 1. Obtenemos los últimos valores o síntomas del paciente 
      # (Supongamos que los buscas de la última fila de 'valores_corporales' o los pasas como parámetro)
      ultimo_valor = app_tables.valores_corporales.get_by_id(...) # O tu método para obtener los datos del paciente actual
    
      # 2. Definimos qué síntomas/alertas están activas (True) para este paciente
      # Ejemplo basado en tus columnas de la tabla de enfermedades:
      sintomas_paciente = {
          "Fiebre": True, # Esto vendría de lo que marcó en los formularios
          "Mareos": False,
          "Tos": True,
          # ... puedes mapear aquí todas las alertas que salieron del Form2
      }

      # 3. Traemos todas las enfermedades de la tabla
      todas_enfermedades = app_tables.enfermedades.search()
      enfermedades_posibles = []

      # 4. Recorremos cada enfermedad para evaluar
      for enfermedad in todas_enfermedades:
          nombre_enfermedad = enfermedad['Enfermedades']
          compatible = True
        
          # Revisamos cada columna de síntoma en la tabla de enfermedades
          # (Anvil permite leer las columnas de la fila como un diccionario)
          for sintoma, valor_requerido in sintomas_paciente.items():
              # Si la tabla tiene esa columna de síntoma
              if sintoma in enfermedad:
                  # Si la enfermedad requiere que el síntoma sea True, pero el paciente lo tiene en False
                  if enfermedad[sintoma] == True and valor_requerido == False:
                      compatible = False
                      break # Descartamos esta enfermedad y pasamos a la siguiente

          # Si pasó los filtros, es una candidata
          if compatible:
              enfermedades_posibles.append(nombre_enfermedad)

      # 5. Mostramos el resultado en el Form3 (por ejemplo, en un RepeatingPanel o Label)
      # Si tienes un RepeatingPanel llamado 'repeating_panel_1':
      self.repeating_panel_1.items = [{'nombre': e} for e in enfermedades_posibles]
    
      # O si prefieres mostrarlo en una etiqueta (Label):
      # self.label_resultado.text = ", ".join(enfermedades_posibles)