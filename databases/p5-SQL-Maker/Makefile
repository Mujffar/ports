PORTNAME=	SQL-Maker
PORTVERSION=	1.22
CATEGORIES=	databases perl5
MASTER_SITES=	CPAN
MASTER_SITE_SUBDIR=	CPAN:TOKUHIROM
PKGNAMEPREFIX=	p5-

MAINTAINER=	perl@FreeBSD.org
COMMENT=	Perl extension for yet another SQL builder
WWW=		https://metacpan.org/release/SQL-Maker

LICENSE=	ART10 GPLv1+
LICENSE_COMB=	dual

BUILD_DEPENDS=	${RUN_DEPENDS}
RUN_DEPENDS=	\
	p5-Class-Accessor-Lite>=0.05:devel/p5-Class-Accessor-Lite \
	p5-DBI>0:databases/p5-DBI
TEST_DEPENDS=	p5-Test-Simple>=0.96:devel/p5-Test-Simple \
		p5-Test-Requires>=0:devel/p5-Test-Requires \
		p5-Tie-IxHash>=0:devel/p5-Tie-IxHash

USES=	perl5
USE_PERL5=	modbuildtiny
NO_ARCH=	YES

.include <bsd.port.mk>
