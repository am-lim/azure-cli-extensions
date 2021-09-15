import collections
from colorama import Fore
from azure.cli.core.style import print_styled_text, Style, is_modern_terminal

def read_int(default_value=0):
    ret = input()
    if ret == '' or ret is None:
        return default_value
    while not ret.isnumeric():
        ret = input("Please input a legal numbersdf: ")
        if ret == '' or ret is None:
            return default_value
    return int(ret)
    
def get_int_option(option_description, min_option, max_option, default_option):
    print(Fore.LIGHTBLUE_EX + ' ? ' + Fore.RESET + option_description, end='')
    option = read_int(default_option)
    while option < min_option or option > max_option:
        print("Please enter a valid option ({}-{}): ".format(min_option, max_option), end='')
        option = read_int(default_option)
    return option

def resources_exist(description, dict):
    if (len(dict) == 0):
        print()
        print(description)
        print()
        return False
    return True

def create_dict(iterator): 
    resource_dict = dict({})
    for resource in iterator:
        resource_dict[resource.id] = resource
    return resource_dict

def create_sorted_dict(dict):
    return collections.OrderedDict(sorted(dict.items(), key=lambda x: x[0].lower()))

def print_prompt_and_options(prompt, dict):
    print()
    print(prompt)
    ind = 1
    for k, v in dict.items():
        print_styled_text([(Style.ACTION, str(ind) + ": "), (Style.PRIMARY, v.name)])
        ind += 1

def get_selected_resource(dict):
    option = get_int_option("Please select your option " + Fore.LIGHTBLACK_EX + "(enter 0 to exit)" +
                            Fore.RESET + ": ", 0, len(dict), -1)
    if (option == 0):
        return
    tuple_list = list(dict.items())
    resource = tuple_list[option-1][1]
    print()
    print_styled_text([(Style.ACTION, "Your selection "), (Style.PRIMARY, str(option) + ": " + resource.name)])
    return resource

def get_resource_group(id):
    return id.split("/resourceGroups/")[1].split("/")[0]

def region_prompt():
    print()
    print(Fore.LIGHTBLUE_EX + ' ? ' + Fore.RESET + "Which region should the environment be deployed into?")
    print_styled_text([(Style.PRIMARY, "See region list at "), (Style.HYPERLINK, "https://azure.microsoft.com/global-infrastructure/geographies/"), (Style.PRIMARY, "."),])
    print("Please input the region " + Fore.LIGHTBLACK_EX + '(input "quit" to exit)' +
                            Fore.RESET + ": ", end='')
    option = read_region()
    return option

#to do add validations for subscription regions
def read_region(default_value="quit"):
    ret = input()
    if ret == '' or ret is None:
        return default_value
    while not ret.isalpha():
        ret = input("Please input a valid region: ")
        if ret == '' or ret is None:
            return default_value
    return ret.strip()

def has_deployment_params_prompt():
    print()
    print(Fore.LIGHTBLUE_EX + ' ? ' + Fore.RESET + "Does the environment have deployment parameters (y/n)? ", end='')
    option = read_yn_option()
    return option

def read_yn_option():
    ret = input()
    while not (ret == "y" or ret== "n"):
        ret = input("Please input a valid response: ")
    return ret.strip()

def deployment_params_prompt():
    print()
    print("Input the deployment parameters: ", end='')
    option = read_deploy_params()
    return option

def read_deploy_params():
    ret = input()
    while (ret == '' or ret is None):
        ret = input("Please input a valid response: ")
    return ret

def print_successful_styled_text(message):
    prefix_text = '\nDone: '
    if is_modern_terminal():
        prefix_text = '\n(✓ )Done: '
    print_styled_text([(Style.SUCCESS, prefix_text), (Style.PRIMARY, message)])

def add_tags_prompt():
    print()
    print(Fore.LIGHTBLUE_EX + ' ? ' + Fore.RESET + "Would you like to add tags or notes to this environment (y/n)? ", end='')
    option = read_yn_option()
    return option

def input_tags_prompt():
    print()
    print("Input the tags: ", end='')
    option = read_tags_input()
    return option

def read_tags_input():
    ret = input()
    while (ret == '' or ret is None):
        ret = input("Please input a valid response: ")
    return ret
