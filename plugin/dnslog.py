#!/usr/bin/env python
# -*- coding: utf-8 -*-
# project = https://github.com/Xyntax/POC-T
# author = i@cdxy.me


"""
DNSLog API

Usage:
    c = DnsLog()
    a = c.getRandomDomain('cdxy')
    try:
        requests.get('http://' + a, timeout=1)
    except Exception:
        pass
    print c.verifyDNS(delay=0)
    print c.verifyHTTP(delay=0)
    print c.getDnsRecord(delay=0)
    print c.getHttpRecord(delay=0)
"""

import random
import requests
import time
from string import ascii_lowercase
#from lib.utils.config import ConfigFileParser

# load once for all thread
#key = ConfigFileParser().CloudEyeApikey()
#uniq_domain = ConfigFileParser().ColudEyePersonaldomain().split('.')[0]
key = ""
uniq_domain = "test"

class DNSLog:
    def __init__(self):
        self.unique = uniq_domain
        self.random = ''.join([random.choice(ascii_lowercase) for _ in range(10)])

    def getRandomDomain(self, custom='poc'):
        """
        full domain = [random].[custom].[unique].dnslog.info
        e.g. fezarvgo.poc.ee8a6f.dnslog.info
        """
        self.custom = custom
        return '%s_%s.%s.wsxedc.top' % (self.random, self.custom, self.unique)

    def getDnsRecord(self, delay=2):
        time.sleep(delay)
        query = self.random + '_' + self.custom
        api_base = 'http://admin.leveryd.top/api/dns/{uniq}/{domain}/'.format(uniq=self.unique, domain=query)
        return requests.post(api_base).content

    def getHttpRecord(self, delay=2):
        time.sleep(delay)
        query = self.random + '.' + self.custom
        api_base = 'http://cloudeye.me/api/{key}/{domain}/ApacheLog/'.format(key=key, domain=query)
        return requests.post(api_base).content

    def verifyDNS(self, delay=2):
        return 'True' in self.getDnsRecord(delay)

    def verifyHTTP(self, delay=2):
        return 'True' in self.getHttpRecord(delay)


def queryDnsRecord(domain, delay=2):
    time.sleep(delay)
    domain = domain.replace(uniq_domain + '.dnslog.info', '').rstrip('.')
    api_base = 'http://cloudeye.me/api/{key}/{domain}/DNSLog/'.format(key=key, domain=domain)
    return requests.post(api_base).content


def queryHttpRecord(domain, delay=2):
    time.sleep(delay)
    domain = domain.replace(uniq_domain + '.dnslog.info', '').rstrip('.')
    api_base = 'http://cloudeye.me/api/{key}/{domain}/ApacheLog/'.format(key=key, domain=domain)
    return requests.post(api_base).content

if __name__ == "__main__":
    c = DnsLog()
    a = c.getRandomDomain('cdxy')
    try:
        requests.get('http://' + a, timeout=1)
    except Exception:
        pass
    print c.verifyDNS(delay=0)
    #print c.verifyHTTP(delay=0)
    #print c.getDnsRecord(delay=0)
    #print c.getHttpRecord(delay=0)