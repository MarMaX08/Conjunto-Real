from ._anvil_designer import ItemTemplate3Template
from anvil import *

class ItemTemplate3(ItemTemplate3Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)

    # Any code you write here will run before the form opens.
