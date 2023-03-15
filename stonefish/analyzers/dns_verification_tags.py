""" Module contain a DNS verification tags analyzer """
from typing import List

from dns import resolver, rdatatype

from stonefish.analyzers.base import BaseAnalyzer


class DnsVerificationTagsAnalyzer(BaseAnalyzer):
    """ DNS verification tags analyzer """
    name = 'DNS верификация'
    description = 'Проверка наличие тегов верификации'
    factor = 1

    def execute(self) -> int:
        """ Method execute analyzer and return a points """
        verification_tags = ("facebook-domain-verification", "google-site-verification", "apple-domain-verification",
                             "google-site-verification", "yandex-verification", "have-i-been-pwned-verification",
                             "mailru-verification", "_globalsign-domain-verification", "wmail-verification")
        answer = resolver.resolve('.'.join(self.url.hostname.split('.')[-2:]), rdtype=rdatatype.TXT,
                                  raise_on_no_answer=False)
        intersection_counter = 0
        for tag in verification_tags:
            if tag in '$$$'.join([str(record) for record in answer.rrset or []]):
                intersection_counter += 1

        if intersection_counter > 4:
            intersection_counter = 4
        return intersection_counter * 20 + 20
