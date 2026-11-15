from ._anvil_designer import Form2_copyTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import plotly.graph_objects as go
import random


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

        # Radiación acumulada (en microsieverts, mSv)
       self.radiacion_total = 0
        self.segundos = 0

        # El timer se ejecuta cada 1 segundo
        self.timer_radiacion.interval = 1

        self.label_radiacion_total.text = "Radiación acumulada: 0.00 mSv"
        self.label_radiacion_actual.text = "Radiación actual: 0.00 mSv/s"
        self.label_imc.text = "IMC: --"

    # ---------- RADIACIÓN ----------
    ERROR_EXPERIMENTAL = 0.10  # 10 %

    @handle("timer_radiacion", "tick")
    def timer_radiacion_tick(self, **event_args):
      """Se ejecuta cada segundo"""
      # Valor simulado: en el espacio ronda ~0.5 a 1.5 mSv por segundo
      # (si tenés un sensor real, reemplazá esta línea por su lectura)
      lectura = random.uniform(0.5, 1.5)

      # Error experimental: la lectura puede variar ±10 %
      error = lectura * ERROR_EXPERIMENTAL
      radiacion_actual = lectura + random.uniform(-error, error)

      self.radiacion_total += radiacion_actual
      self.segundos += 1

      self.label_radiacion_actual.text = f"Radiación actual: {radiacion_actual:.2f} ± {error:.2f} mSv/s"
      self.label_radiacion_total.text = f"Radiación acumulada: {self.radiacion_total:.2f} mSv"

      # Alerta si supera un límite
      if self.radiacion_total > 600:
        self.label_radiacion_total.foreground = "red"

      # ---------- IMC ----------
      @handle("button_imc", "click")
      def button_imc_click(self, **event_args):
        peso = self.text_box_peso.text
        altura = self.text_box_altura.text

        if not peso or not altura or altura <= 0:
          alert("Ingresá un peso y una altura válidos.")
          return

        imc = peso / (altura ** 2)

        if imc < 18.5:
          categoria = "Bajo peso"
        elif imc < 25:
          categoria = "Peso normal"
        elif imc < 30:
          categoria = "Sobrepeso"
        else:
          categoria = "Obesidad"

        self.label_imc.text = f"IMC: {imc:.1f} ({categoria})"

      @handle("check_box_39", "change")
      def check_box_39_change(self, **event_args):
        pass

      @handle("button_1", "click")
      def button_1_click(self, **event_args):
        open_form('Form1')
while 