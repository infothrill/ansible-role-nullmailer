# Ansible Role: nullmailer

![Build status](https://github.com/infothrill/ansible-role-nullmailer/actions/workflows/tests.yml/badge.svg)
[![Ansible Role](https://img.shields.io/ansible/role/30364.svg)](https://galaxy.ansible.com/infothrill/nullmailer/)

An [Ansible](http://www.ansible.com) role to install [nullmailer](https://untroubled.org/nullmailer/),
a simple relay-only mail transport agent.

## Quick howto

requirements.yml:

    - src: infothrill.nullmailer
      version: v3.1.0

Install:

    ansible-galaxy install -r requirements.yml -p ./roles/

Playbook:

    - hosts: servers
        roles:
          - role: infothrill.nullmailer

## Role Variables

```yml
nullmailer_mail_recipient: john@example.com
```

The recipient for all mail messages sent through nullmailer. This should be an
address that will be accepted and relayed to by the `nullmailer_relay_host`.

```yml
nullmailer_relay_host: smtp.example.com
```

The smtp relay host that all smtp traffic will be directed to.

```yml
nullmailer_relay_port: 465
```

The port used to connect via SMTP to the `nullmailer_relay_host`.

```yml
nullmailer_relay_user: john@example.com
```

The SMTP username for authenticating with the `nullmailer_relay_host`. Can be set to empty string, in which case authentication is skipped entirely (useful for example in case you use IP based trust).

```yml
nullmailer_relay_pass: 50m3p455w0r6
```

The SMTP password for authenticating with the `nullmailer_relay_host`.

```yml
nullmailer_allmailfrom: spambot@example.com
```

If this is defined, its contents will override the envelope sender on
all messages. Please exercise caution with this setting as this determines bounce behaviour of undeliverable messages.

```yml
nullmailer_remote_ssl: true|false
```
Toggle to add --ssl parameter for remote, default true.


```yml
nullmailer_remote_starttls: true|false
```
Toggle to add --starttls parameter for remote, default false.


## Dependencies

None.

## License

MIT

## Author Information

This role was created in 2018 by Paul Kremer.

## Changes

### v3.1.0

* add: nullmailer_relay_user can be empty to skip relay authentication
* drop test support for Debian Jessie
* drop support for python 3.7
* drop support for ansible 2.9, 2.10, add ansible 4, 5
* switch to Github Actions for CI

### v3.0.1

* drop test support for python 3.6
* add test support for python 3.7, 3.8, 3.9
* drop support for ansible 2.8
* add support for ansible 2.10, 3.0

### v3.0.0

* add configuration switch for `--ssl` and `--starttls`
* upgrade to molecule version 3
* drop support for ansible 2.5, 2.6, 2.7
* add test for ubuntu 20.04

### v2.0.0

* switch testing framework to python3, drop support for python2
* testing support for Ansible 2.9

### v1.1.0

* add optional variable *nullmailer_allmailfrom*
* testing support for Ansible 2.8
* testing support for Debian 10 *Buster*

### v1.0.1

* testing fixes

### v1.0.0

* initial release
