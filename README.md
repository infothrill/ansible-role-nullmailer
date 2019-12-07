# Ansible Role: nullmailer

[![Build Status](https://img.shields.io/travis/infothrill/ansible-role-nullmailer/master.svg?label=travis_master)](https://travis-ci.org/infothrill/ansible-role-nullmailer)
[![Build Status](https://img.shields.io/travis/infothrill/ansible-role-nullmailer/develop.svg?label=travis_develop)](https://travis-ci.org/infothrill/ansible-role-nullmailer)
[![Updates](https://pyup.io/repos/github/infothrill/ansible-role-nullmailer/shield.svg)](https://pyup.io/repos/github/infothrill/ansible-role-nullmailer/)
[![Ansible Role](https://img.shields.io/ansible/role/30364.svg)](https://galaxy.ansible.com/infothrill/nullmailer/)

An [Ansible](http://www.ansible.com) role to install [nullmailer](https://untroubled.org/nullmailer/),
a simple relay-only mail transport agent.

## Quick howto

requirements.yml:

    - src: infothrill.nullmailer
      version: v1.1.0

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

The SMTP username for authenticating with the `nullmailer_relay_host`.

```yml
nullmailer_relay_pass: 50m3p455w0r6
```

The SMTP password for authenticating with the `nullmailer_relay_host`.

```yml
nullmailer_allmailfrom: spambot@example.com
```

If this is defined, its contents will override the envelope sender on
all messages. Please exercise caution with this setting as this determines bounce behaviour of undeliverable messages.


## Dependencies

None.

## License

MIT

## Author Information

This role was created in 2018 by Paul Kremer.

## Changes

### v2.0.0

* switch testing framework to python3, drop support for python2

### v1.1.0

* add optional variable *nullmailer_allmailfrom*
* testing support for Ansible 2.8
* testing support for Debian 10 *Buster*

### v1.0.1

* testing fixes

### v1.0.0

* initial release
