PORTNAME=	HTML-Restrict
PORTVERSION=	3.0.1
DISTVERSIONPREFIX=	v
CATEGORIES=	www perl5
MASTER_SITES=	CPAN
PKGNAMEPREFIX=	p5-

MAINTAINER=	perl@FreeBSD.org
COMMENT=	Perl extension to strip unwanted HTML tags and attributes
WWW=		https://metacpan.org/release/HTML-Restrict

LICENSE=	ART10 GPLv1+
LICENSE_COMB=	dual
LICENSE_FILE=	${WRKSRC}/LICENSE

BUILD_DEPENDS=	${RUN_DEPENDS}
RUN_DEPENDS=	p5-Data-Dump>=0:devel/p5-Data-Dump \
		p5-HTML-Parser>=0:www/p5-HTML-Parser \
		p5-Moo>=1.002000:devel/p5-Moo \
		p5-Sub-Quote>=0:devel/p5-Sub-Quote \
		p5-Type-Tiny>=1.002001:devel/p5-Type-Tiny \
		p5-URI>=0:net/p5-URI \
		p5-namespace-clean>=0:devel/p5-namespace-clean
TEST_DEPENDS=	p5-Test-Fatal>=0:devel/p5-Test-Fatal

USES=		perl5
USE_PERL5=	configure

NO_ARCH=	yes

.include <bsd.port.mk>
