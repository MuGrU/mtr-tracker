#!/usr/bin/env python3
# coding: utf-8

import json
import os
import sys
import getopt
import requests
import re
import pycurl


banner = ('''
 ##     ## ######## ########          ######## ########     ###     ######  ##    ## ######## ########  
 ###   ###    ##    ##     ##            ##    ##     ##   ## ##   ##    ## ##   ##  ##       ##     ## 
 #### ####    ##    ##     ##            ##    ##     ##  ##   ##  ##       ##  ##   ##       ##     ## 
 ## ### ##    ##    ########  #######    ##    ########  ##     ## ##       #####    ######   ########  
 ##     ##    ##    ##   ##              ##    ##   ##   ######### ##       ##  ##   ##       ##   ##   
 ##     ##    ##    ##    ##             ##    ##    ##  ##     ## ##    ## ##   ##  ##       ##    ##  
 ##     ##    ##    ##     ##            ##    ##     ## ##     ##  ######  ##    ## ######## ##     ##  
 _______________________________________________________________________________________________________
                                                                                                        ''')


def usage():
    print('Usage: ' + sys.argv[0] + ' -t foo.bar.com -c 10 -s for short mode')


def ttfbcheck(host):

    c = pycurl.Curl()
    c.setopt(pycurl.WRITEFUNCTION, lambda x: None)
    c.setopt(pycurl.URL, host)                                  #set url
    c.setopt(pycurl.FOLLOWLOCATION, 1)
    content = c.perform()                                       #execute
    dns_time = c.getinfo(pycurl.NAMELOOKUP_TIME)                #DNS time
    conn_time = c.getinfo(pycurl.CONNECT_TIME)                  #TCP/IP 3-way handshaking time
    starttransfer_time = c.getinfo(pycurl.STARTTRANSFER_TIME)   #time-to-first-byte time
    total_time = c.getinfo(pycurl.TOTAL_TIME)                   #last request time

    return {'ttfb': {
        'dns_time': dns_time,
        'conn_time': conn_time,
        'starttransfer_time': starttransfer_time,
        'total_time': total_time}}


def geolocation(host):
    try:
        r = requests.get('http://ip-api.com/json/' + host)
        data = r.json()

        if 'fail' in data['status']:
            if 'private range' or 'reserved range' in data['message']:
                raise Exception(print('\t[ Private range or Reserved range ]'))

            else:
                print('Search for http://ip-api.com/json/{0} [-] Status: {1}'.format(host, data['status']))
                print('Error: {}'.format(data))
                sys.exit(1)
        else:
            return {'data': {
                'hostname': host,
                'query': data['query'],
                'status': data['status'],
                'regionName': data['regionName'],
                'country': data['country'],
                'city': data['city'],
                'isp': data['isp'],
                'lat': data['lat'],
                'lon': data['lon'],
                'zip': data['zip'],
                'asname': data['as']}}

    except requests.exceptions.ConnectionError as err:
        print('[-]A Connection error occurred:\n\n{}'.format(err))
        sys.exit(1)

    except requests.exceptions.Timeout as err:
        print('[-]TimeoutError:\n\n{}'.format(err))
        sys.exit(1)

    except KeyboardInterrupt:
        print('\n')
        print('[-] User Interruption Detected..!')


# TODO add exception handler
def traceroute(host, count):
    hubs = {}

    try:
        print('\n\033[34mTracing route to: \033[0m{}'.format(host))
        print('It can take a while... Get some coffee :)')

        mtr = ('sudo mtr ' + '-4 -b -rwc ' + count + ' -j ' + host)

        proces = os.popen(mtr)
        results = proces.read()

        hubs = json.loads(results)

    except Exception:
        pass

    return hubs

# TODO add exception handler
def printresults(host, hubs, ttfb):

    dns_time = ttfb['ttfb']['dns_time']
    conn_time = ttfb['ttfb']['conn_time']
    starttransfer_time = ttfb['ttfb']['starttransfer_time']
    total_time = ttfb['ttfb']['total_time']

    print('\n[WEB]: {}'.format(host))
    print('\t[+] \033[34mDNS Resolution: {}\033[0m'.format(dns_time))
    print('\t[+] \033[34mConnetion Time: {}\033[0m'.format(conn_time))
    print('\t[+] \033[34mStart Transfer: {}\033[0m'.format(starttransfer_time))
    print('\t[+] \033[34mTotal Time: {}\033[0m'.format(total_time))

    for h in hubs['report']['hubs']:
        try:
            hop = h['count']
            router = re.sub('[()]', '', h['host']).split()
            host = router[-1]
            name = router[0]

            if '???' not in h['host']:

                print('\n {0}.|-- {1} ({2})'.format(hop, name, host))
                print(
                    '\t[+] \033[34mLoss%:\033[0m [{}] \033[34mSnt:\033[0m [{}]\033[34m Last:\033[0m [{}] \033['
                    '34mAvg:\033[0m [{}] \033[34mBest:\033[0m [{}] \033[34mWrst%:\033[0m [{}] \033[34mStDev%:\033[0m '
                    '[{}] \033[0m'.format(
                        h['Loss%'], h['Snt'], h['Last'], h['Avg'], h['Best'], h['Wrst'], h['StDev']))

                system_information = geolocation(host)

                region_name = system_information['data']['regionName']
                country = system_information['data']['country']
                city = system_information['data']['city']
                isp = system_information['data']['isp']
                lat = system_information['data']['lat']
                lon = system_information['data']['lon']
                dzip = system_information['data']['zip']
                asname = system_information['data']['asname']

                print('\t[+] \033[34mRegion: {}\033[0m'.format(region_name))
                print('\t[+] \033[34mCountry: {}\033[0m'.format(country))
                print('\t[+] \033[34mCity: {}\033[0m'.format(city))
                print('\t[+] \033[34mISP: {}\033[0m'.format(isp))
                print('\t[+] \033[34mLat & Lon: {0} {1}\033[0m'.format(lat, lon))
                print('\t[+] \033[34mZipcode: {}\033[0m'.format(dzip))
                print('\t[+] \033[34mAS: {}\033[0m'.format(asname))

        except Exception:
            pass

    else:
        print('\n')
        sys.exit(0)


def printlocation(system_information):

    hostname = system_information['data']['hostname']
    query = system_information['data']['query']
    region_name = system_information['data']['regionName']
    country = system_information['data']['country']
    city = system_information['data']['city']
    isp = system_information['data']['isp']
    lat = system_information['data']['lat']
    lon = system_information['data']['lon']
    dzip = system_information['data']['zip']
    asname = system_information['data']['asname']

    print('\t[+] \033[34mHostname: {}\033[0m'.format(hostname))
    print('\t[+] \033[34mIP: {}\033[0m'.format(query))
    print('\t[+] \033[34mRegion: {}\033[0m'.format(region_name))
    print('\t[+] \033[34mCountry: {}\033[0m'.format(country))
    print('\t[+] \033[34mCity: {}\033[0m'.format(city))
    print('\t[+] \033[34mISP: {}\033[0m'.format(isp))
    print('\t[+] \033[34mLat & Lon: {0} {1}\033[0m'.format(lat, lon))
    print('\t[+] \033[34mZipcode: {}\033[0m'.format(dzip))
    print('\t[+] \033[34mAS: {}\033[0m\n'.format(asname))

    sys.exit(0)


def main():
    host = None
    short = False
    locate = False
    trace = False
    count = '1'

    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hl:t:c:s', ['--help', 'locate=', 'trace=', '--count', '--short'])

    except getopt.error as err:
        print('Error: {}'.format(err))
        usage()
        sys.exit(2)

    for option, argument in opts:
        if option in ('h', '--help'):
            usage()
            exit(1)

        elif option in ('-l', '--locate'):
            short = True
            locate = True
            host = str(argument)

        elif option in ('-t', '--trace'):
            trace = True
            host = str(argument)

        elif option in ('-c', '--count'):
            count = str(argument)

        elif option in ('-s', '--short'):
            short = True

        else:
            assert False, 'Invalid option'

    if not short:
        os.system('reset')
        print('{}'.format(banner))

    if locate:
        system_information = geolocation(host)
        printlocation(system_information)

    if trace:
        ttfb = ttfbcheck(host)
        hubs = traceroute(host, count)
        printresults(host, hubs, ttfb)


if __name__ == '__main__':
    main()
