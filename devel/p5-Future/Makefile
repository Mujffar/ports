PORTNAME=	Future
PORTVERSION=	0.48
CATEGORIES=	devel perl5
MASTER_SITES=	CPAN
MASTER_SITE_SUBDIR=	CPAN:PEVANS
PKGNAMEPREFIX=	p5-

MAINTAINER=	perl@FreeBSD.org
COMMENT=	Build objects representing outstanding operations
WWW=		https://metacpan.org/release/Future

LICENSE=	ART10 GPLv1+
LICENSE_COMB=	dual

TEST_DEPENDS=	p5-Test-Fatal>0:devel/p5-Test-Fatal \
		p5-Test-Identity>0:devel/p5-Test-Identity \
		p5-Test-Refcount>0:devel/p5-Test-Refcount

USES=		perl5
USE_PERL5=	modbuild

NO_ARCH=	yes

PORTSCOUT=	limit:^[0-9\.]*$$

.include <bsd.port.mk>
