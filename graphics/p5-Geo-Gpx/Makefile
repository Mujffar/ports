PORTNAME=	Geo-Gpx
PORTVERSION=	1.00
CATEGORIES=	graphics perl5
MASTER_SITES=	CPAN
PKGNAMEPREFIX=	p5-

MAINTAINER=	perl@FreeBSD.org
COMMENT=	Perl Module to Create and Parse GPX Files
WWW=		https://metacpan.org/release/Geo-Gpx

LICENSE=	ART10 GPLv1+
LICENSE_COMB=	dual

BUILD_DEPENDS=	${RUN_DEPENDS}
RUN_DEPENDS=	p5-DateTime-Format-ISO8601>=0:devel/p5-DateTime-Format-ISO8601 \
		p5-ExtUtils-MakeMaker-Coverage>=0:devel/p5-ExtUtils-MakeMaker-Coverage \
		p5-HTML-Parser>=0:www/p5-HTML-Parser \
		p5-TimeDate>=0:devel/p5-TimeDate \
		p5-XML-Descent>=0:textproc/p5-XML-Descent

USES=		perl5
USE_PERL5=	configure

NO_ARCH=	yes

.include <bsd.port.mk>
