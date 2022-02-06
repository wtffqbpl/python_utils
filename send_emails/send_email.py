#!/usr/bin/env python
# coding: utf-8


import os
import json
import configparser
import smtplib
from email.mime.text import MIMEText
from email.header import Header


class MailConfigInfo:
    def __init__(self, config_file='./email_configuration.cfg'):
        self._config = configparser.ConfigParser()
        self._config.read([os.path.expanduser(config_file)])

    @property
    def smtp_hostname(self):
        return self._config.get('mailaccountinfo', 'smtphostname')

    @property
    def smtp_username(self):
        return self._config.get('mailaccountinfo', 'smtpusername')

    @property
    def smtp_password(self):
        return self._config.get('mailaccountinfo', 'smtppassword')

    @property
    def sender(self):
        return self._config.get('mail_content', 'sender')

    @property
    def receivers(self):
        return [receiver.lstrip().rstrip() \
                for receiver in self._config.get('mail_content', 'receivers').split(',')]

    @property
    def title(self):
        return self._config.get('mail_content', 'title')

    @property
    def attachments(self):
        attachments_str = self._config.get('mail_content', 'attachments')
        if attachments_str == 'None':
            return None
        return [attachemnt.lstrip().rstrip() for attachemnt in attachments_str.split(',')]

    def __str__(self):
        mail_account_info, mail_content = {}, {}

        # mail account info
        mail_account_info['smtp_hostname'] = self.smtp_hostname
        mail_account_info['smtp_username'] = self.smtp_username
        mail_account_info['smtp_password'] = self.smtp_password

        # mail content
        mail_content['sender'] = self.sender
        mail_content['receivers'] = self.receivers
        mail_content['title'] = self.title
        mail_content['attachemnt'] = self.attachments

        # all results.
        res = {'mail_account_info': mail_account_info,
               'mail_content': mail_content}

        return json.dumps(res)


class MailUtils:
    def __init__(self, config_file='./email_configuration.cfg'):
        mail_config_info = MailConfigInfo(config_file)
        pass


if __name__ == "__main__":
    mail_config_info = MailConfigInfo()
    print(mail_config_info)

