#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

project_dir = r"D:\codes\TTEntertainment"
# project_dir = r"D:\codes\TTLiveHouse"
# project_dir = r"D:\codes\Navigator-Android"

def count_error(file_name):
    """统计，并返回checkstyle的结果中的错误总数"""
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


def update_error_to_pom(module_dir, error_count):
    """更新最新的错误数到pom.xml"""
    pom_file = module_dir + r"\pom.xml"
    _content = ''
    with open(pom_file, 'r') as f:
        for line in f:
            if line.find(r"maxAllowedViolations") > 0:
                lss = line.split('maxAllowedViolations')
                # for s in lss:
                    # print s
                line = lss[0] + "maxAllowedViolations>" + str(error_count) + "</maxAllowedViolations" + lss[2]
                print line
            _content += line
    open(pom_file, 'wb').writelines(_content)


def checkstyle_result_path(project_path):
    """查找checkstyle result，并统计错误总数"""
    error_count = 0
    root_result_file = project_path + r"\target\checkstyle-result.xml"
    error_count += count_error(root_result_file)
    print root_result_file, error_count
    if os.path.isdir(project_path):
        for module_name in os.listdir(project_path):
            module_dir = project_path + '\\' + module_name
            check_file = module_dir + r"\target\checkstyle-result.xml"
            if os.path.exists(check_file):
                module_error_count = count_error(check_file)
                error_count += module_error_count
                update_error_to_pom(module_dir, module_error_count)
                print check_file, module_error_count
    else:
        print project_path, "not dir"

    print "==============="
    print project_path, error_count


checkstyle_result_path(project_dir)

