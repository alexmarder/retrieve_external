#!/usr/bin/env python
from argparse import ArgumentParser

from external.caidatraceroute import get_caidateam, get_caidaprefix
import external.ris as ris


def main():
    parser = ArgumentParser()
    parser.add_argument('-b', '--begin', help='Beginning date.', required=True)
    parser.add_argument('-e', '--end', help='Ending date.', required=True)
    parser.add_argument('-u', '--username', help='Username.')
    parser.add_argument('-p', '--password', help='Password.')
    parser.add_argument('-n', '--processes', type=int, default=5, help='Number of processes to use.')
    parser.add_argument('-d', '--dir', required=True, help='Output directory for the traceroute files.')
    sub = parser.add_subparsers()

    caidat = sub.add_parser('caida-team', help='Retrieve the CAIDA team probing traceroutes.')
    caidat.set_defaults(func=get_caidateam)

    caidap = sub.add_parser('caida-prefix', help='Retrieve the CAIDA prefix probing traceroutes.')
    caidap.set_defaults(func=get_caidaprefix)

    riperis = sub.add_parser('riperis', help='Retrieve the RIPE RIS bgp RIBs.')
    riperis.set_defaults(func=ris.get)

    args = parser.parse_args()
    args.func(args)
    # print(args.func)


if __name__ == '__main__':
    main()