# coding:utf-8
import csv

FILE_RULE = "tag_rules.csv"
no_lib_prefix = list()
labeled_prefix = list()
file_rules = open(FILE_RULE, 'r')
csv_rules_reader = csv.reader(file_rules, delimiter=',', quotechar='|')
for row in csv_rules_reader:
    if row[1] == "no":
        no_lib_prefix.append(row[0])
    else:
        labeled_prefix.append(row[0])


file_rules_w = open(FILE_RULE, 'a')
csv_rule_writer = csv.writer(file_rules_w, delimiter=',', quotechar='|')

potential_libs = open("potential_libs.csv")
potential_lines = potential_libs.readlines()
line_num = len(potential_lines)
for line_id in range(line_num):
    line = potential_lines[line_id]
    potential_package_name = line.split(',')[3].strip()
    flag = False
    for no_lib in no_lib_prefix:
        if no_lib.startswith(potential_package_name):
            flag = True
            print ("Ignoring:" + potential_package_name)
            break
    if flag:
        continue
    for lib in labeled_prefix:
        flag = False
        if potential_package_name.startswith(lib):
            flag = True
            print ("Ignoring:" + potential_package_name)
            break
    if flag:
        continue
    print("Progress %d/%d" % (line_id, line_num))
    print("Package Name:" + potential_package_name)
    status = ""
    while True:
        str = raw_input("Is that package belongs to a library?\n y -> yes or part of lib; n -> no; d -> don't know; q -> quit :")
        if str == "y":
            status = "y"
            break
        elif str == "n":
            status = "n"
            break
        elif str == "d":
            status = "d"
            break
        elif str == "q":
            status = "q"
            break
        else:
            print ("Pardon?")
            continue
    if status == "y":
        package_name = raw_input("Library's root package name: ")
        lib_name = raw_input("Library's name: ")
        lib_type = raw_input("Type: ")
        website = raw_input("Website: ")
        labeled_prefix.append(package_name)
        csv_rule_writer.writerow([package_name, lib_name, lib_type, website])
    elif status == "n":
        no_lib_prefix.append(potential_package_name)
        csv_rule_writer.writerow([potential_package_name, "no", "no", "no"])
    elif status == "q":
        break
    file_rules_w.flush()
file_rules_w.close()
