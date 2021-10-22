import basics.output.simple_message as simple_message
import basics.output.multiline_message as multiline_message
import basics.output.escape_characters as escape_characters
import basics.output.ascii_art as ascii_art
import basics.input.basics.data_types as data_types
import basics.input.basics.review as input_review
import basics.input.basics.string_operators as string_operators
import basics.input.ascii_robot as ascii_robot
import basics.input.user_input as user_input
import basics.repetitions.for_loop.characters as characters
import basics.repetitions.for_loop.count_down as count_down
import basics.repetitions.for_loop.count_letters as count_letters
import basics.repetitions.for_loop.membership_operators as membership_operators
import basics.repetitions.for_loop.brightness_range as brightness_range
import basics.repetitions.for_loop.reverse as reverse
import basics.repetitions.for_loop.for_simple as for_simple
import basics.repetitions.nested_loop.nested as nested
import basics.repetitions.nested_loop.nesting as nesting
import basics.repetitions.while_loop.while_ascii as while_ascii
import basics.repetitions.while_loop.count as count
import basics.repetitions.while_loop.factorial as factorial
import basics.repetitions.while_loop.len as len
import basics.repetitions.while_loop.while_simple as while_simple
import basics.repetitions.while_loop.sum_100 as sum_100
import basics.repetitions.while_loop.sumnum as sumnum
import basics.repetitions.while_loop.sum_user as sum_user
import basics.functions.ascii_character as ascii_character
import basics.functions.ascii_code as ascii_code
import basics.functions.function_calls as function_calls
import basics.functions.function_with_loop as function_with_loop
import basics.functions.function_with_nesting as function_with_nesting
import basics.functions.function_with_parameter as function_with_parameter
import basics.functions.multiple_functions as multiple_functions
import basics.functions.multiple_parameters as multiple_parameters
import basics.functions.return_values as return_values
import basics.functions.simple_functions as simple_functions
import basics.modules.guess_the_number as guess_the_number


def run_block_a():
    print("Which program in 'Block A: basics' do you wish to run?")
    response = input()
    if response == "simple_message":
        simple_message.run()
    elif response == "multiline_message":
        multiline_message.run()
    elif response == "escape_characters":
        escape_characters.run()
    elif response == "ascii_art":
        ascii_art.run()
    elif response == "data_types":
        data_types.run()
    elif response == "input_review":
        input_review.run()
    elif response == "string_operators":
        string_operators.run()
    elif response == "ascii_robot":
        ascii_robot.run()
    elif response == "user_input":
        user_input.run()
    elif characters == "characters":
        characters.run()
    elif count_down == "count_down":
        count_down.run()
    elif count_letters == "count_letters":
        count_letters.run()
    elif membership_operators == "membership_operators":
        membership_operators.run()
    elif brightness_range == "brightness_range":
        brightness_range.run()
    elif reverse == "reverse":
        reverse.run()
    elif for_simple == "for_simple":
        for_simple.run()
    elif nested == "nested":
        nested.run()
    elif nesting == "nesting":
        nesting.run()
    elif while_ascii == "while_ascii":
        while_ascii.run()
    elif count == "count":
        count.run()
    elif factorial == "factorial":
        factorial.run()
    elif len == "len":
        len.run()
    elif while_simple == "while_simple":
        while_simple.run()
    elif sum_100 == "sum_100":
        sum_100.run()
    elif sumnum == "sumnum":
        sumnum.run()
    elif sum_user == "sum_user":
        sum_user.run()
    elif ascii_character == "ascii_character":
        ascii_character.run()
    elif ascii_code == "ascii_code":
        ascii_code.run()
    elif function_calls == "function_calls":
        function_calls.run()
    elif function_with_loop == "function_with_loop":
        function_with_loop.run()
    elif function_with_nesting == "function_with_nesting":
        function_with_nesting.run()
    elif function_with_parameter == "function_with_parameter":
        function_with_parameter.run()
    elif multiple_functions == "multiple_functions":
        multiple_functions.run()
    elif multiple_parameters == "multiple_parameters":
        multiple_parameters.run()
    elif return_values == "return_values":
        return_values.run()
    elif simple_functions == "simple_functions":
        simple_functions.run()
    elif guess_the_number == "guess_the_number":
        guess_the_number.run()




def run():

    while(True):
        print("What would you like to do?")
        print("[a] Run 'Block A: basics' programs")
        print("[q] Quit")
        response = input()

        if response == "a":
            run_block_a()
        elif response == "q":
            break
        else:
            print("Invalid option! Please try again.")

run()
