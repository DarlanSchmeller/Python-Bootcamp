from MyMainPackage import some_main_script
from MyMainPackage.SubPackage import my_sub_script

some_main_script.report_main()
my_sub_script.sub_report()


## Executing this code directly assigns this:
# __name__ = "__main__"


# If the user runs the code directly the code below runs
if __name__ == "__main__":
    print('35_modules&packages.py is being run directly!')
else:
    print('35_modules&packages.py has been imported!')
