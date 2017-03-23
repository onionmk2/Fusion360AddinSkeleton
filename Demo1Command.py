import adsk.core
import adsk.fusion
import traceback

from .Fusion360Utilities.Fusion360Utilities import get_app_objects
from .Fusion360Utilities.Fusion360CommandBase import Fusion360CommandBase


# Class for a Fusion 360 Command
# Place your program logic here
# Delete the line that says "pass" for any method you want to use
class Demo1Command(Fusion360CommandBase):

    # Run whenever a user makes any change to a value or selection in the addin UI
    # Commands in here will be run through the Fusion processor and changes will be reflected in  Fusion graphics area
    def on_preview(self, command, inputs, args, input_values):
        pass

    # Run after the command is finished.
    # Can be used to launch another command automatically or do other clean up.
    def on_destroy(self, command, inputs, reason, input_values):
        pass

    # Run when any input is changed.
    # Can be used to check a value and then update the add-in UI accordingly
    def on_input_changed(self, command_, command_inputs, changed_input, input_values):
        pass

    # Run when the user presses OK
    # This is typically where your main program logic would go
    def on_execute(self, command, inputs, args, input_values):

        # Get the values from the user input
        the_value = input_values['value_input']
        the_boolean = input_values['bool_input']
        the_string = input_values['string_input']
        all_selections = input_values['selection_input']

        # Selections are returned as a list so lets get the first one and its name
        the_first_selection = all_selections[0]
        the_selection_name = the_first_selection.name

        # Get a reference to all relevant application objects in a dictionary
        app_objects = get_app_objects()
        ui = app_objects['ui']

        ui.messageBox('The numeric value you entered was:   {} \n'.format(the_value) +
                      'The boolean value checked was:       {} \n'.format(the_boolean) +
                      'The string you typed was:    {} \n'.format(the_string) +
                      'The name of the first object you selected is:    {}'.format(the_selection_name))



    # Run when the user selects your command icon from the Fusion 360 UI
    # Typically used to create and display a command dialog box
    # The following is a basic sample of a dialog UI
    def on_create(self, command, command_inputs):

        # Create a default value using a string
        default_value = adsk.core.ValueInput.createByString('1.0 cm')

        # Create a few inputs in the UI
        command_inputs.addValueInput('value_input', '***Sample***Value', 'cm', default_value)
        command_inputs.addBoolValueInput('bool_input', '***Sample***Checked', True)
        command_inputs.addStringValueInput('string_input', '***Sample***String Value', 'Default value')
        command_inputs.addSelectionInput('selection_input', '***Sample***Selection', 'Select Something')