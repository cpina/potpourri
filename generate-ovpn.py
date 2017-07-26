#!/usr/bin/python

"""
Any questions: Carles Pina i Estany <carles@pina.cat>
"""

import argparse
import glob

def get_certificate(text):
    position_begin_certificate = text.index("-----BEGIN CERTIFICATE-----")
    certificate = text[position_begin_certificate:]
    return certificate

def read_file(filepath):
    return open(filepath).read().rstrip()

def read_files(basename):
    files = {}
    files['template'] = read_file('template.tmpl')
    files['ca'] = read_file('keys/ca.crt')
    files['cert'] = get_certificate(read_file('keys/%s.crt' % basename))
    files['key'] = read_file('keys/%s.key' % basename)
    files['tls_auth'] = read_file('keys/ta.key')

    return files

def create_ovpn(basename):
    files = read_files(basename)

    template = files['template']
    del files['template']

    ovpn = template % files

    output_file = 'keys/%s.ovpn' % basename
    file = open(output_file, 'w')
    file.write(ovpn)
    file.close()
    print "File generated: %s" % (output_file)
    return True

def main():
    parser = argparse.ArgumentParser('Creates a .ovpn file based on the keys/ files',
                    epilog="""This is to generate a file for OpenVPN instead of different files""")

    parser.add_argument('name', type=str, help="Uses keys/name.{crt,csr,key},*.pem to generate keys/name.ovpn")
    args = parser.parse_args()

    create_ovpn(args.name)

if __name__ == "__main__":
    main()

