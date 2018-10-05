# -*- coding: utf-8 -*-
import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_nullmailer_deployed(host):
    assert host.file("/etc/nullmailer/adminaddr").is_file
    assert host.file("/etc/nullmailer/remotes").is_file
    assert host.package("nullmailer").is_installed
