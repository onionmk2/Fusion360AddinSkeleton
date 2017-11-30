import adsk.core
import adsk.fusion
import traceback

import json

from .Fusion360Utilities.Fusion360CommandBase import Fusion360CommandBase, Fusion360PaletteCommandBase
from .Fusion360Utilities.Fusion360Utilities import AppObjects


# Class for a Fusion 360 Palette Command
class DemoPaletteShowCommand(Fusion360PaletteCommandBase):

    # Run when user executes command in UI, useful for handling extra tasks on palette like docking
    def on_palette_execute(self, palette: adsk.core.Palette):

        # Dock the palette to the right side of Fusion window.
        palette.dockingState = adsk.core.PaletteDockingStates.PaletteDockStateRight

    # Run when ever a fusion event is fired from the corresponding web page
    def on_html_event(self, html_args: adsk.core.HTMLEventArgs):

        # Parse incoming message and build message for Fusion message box
        data = json.loads(html_args.data)
        msg = "An event has been fired from the html to Fusion with the following data:\n"
        msg += '    Command: {}\n    arg1: {}\n    arg2: {}'.format(html_args.action, data['arg1'], data['arg2'])

        # Display Message
        ao = AppObjects()
        ao.ui.messageBox(msg)

    # Handle any extra cleanup when user closes palette here
    def on_palette_close(self):
        pass


# This is a standard Fusion Command that will send data to the palette
class DemoPaletteSendCommand(Fusion360CommandBase):

    def __init__(self, cmd_def, debug):
        super().__init__(cmd_def, debug)

        # Pass in the palette_id as extra data in command definition
        # A generally useful technique to make commands more re-usable
        self.palette_id = cmd_def.get('palette_id', None)

    # When the command is clicked it will send this message to the HTML Palette
    def on_execute(self, command: adsk.core.Command, command_inputs: adsk.core.CommandInputs, args, input_values):

        # Get Reference to Palette
        ao = AppObjects()
        palette = ao.ui.palettes.itemById(self.palette_id)

        # Get input value from string input
        message = input_values['palette_string']

        # Send message to the HTML Page
        if palette:
            palette.sendInfoToHTML('send', message)

    # Run when the user selects your command icon from the Fusion 360 UI
    def on_create(self, command: adsk.core.Command, command_inputs: adsk.core.CommandInputs):

        command_inputs.addStringValueInput('palette_string', 'Palette Message', 'Some text to send to Palette')
