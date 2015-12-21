#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


def count_error(file_name):
    line_counts = 0
    error_counts = 0
    character_counts = 0

    with open(file_name, 'r') as f:
        for line in f:
            if line.find(r"severity=") > 0:
                error_counts += 1
            line_counts += 1
            character_counts += len(line)
    return error_counts


def checkstyle_result_path(project_path):
    error_count = 0
    root_result_file = project_path + r"\target\checkstyle-result.xml"
    error_count += count_error(root_result_file)
    print root_result_file, error_count
    if os.path.isdir(project_path):
        for d in os.listdir(project_path):
            check_file = project_path + '\\' + d + r"\target\checkstyle-result.xml"
            if os.path.exists(check_file):
                file_error = count_error(check_file)
                error_count += file_error
                print check_file, file_error

    print "==============="
    print project_path, error_count


# count_error(r"D:\codes\TTEntertainment\Music\target\checkstyle-result.xml")

checkstyle_result_path(r"D:\codes\Navigator-Android")

