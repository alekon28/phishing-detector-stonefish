""" Module contain a DNS verification tags analyzer """

from dns import resolver, rdatatype

from stonefish.analyzers.base import BaseAnalyzer
from stonefish.analyzers.normalizers import ThNormalizer


class DnsVerificationTagsAnalyzer(BaseAnalyzer):
    """ DNS verification tags analyzer """
    name = 'DNS верификация'
    description = 'Проверка наличие тегов верификации'
    normalizer = ThNormalizer(shift=0, factor=0.8)

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
        return intersection_counter
