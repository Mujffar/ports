PORTNAME=	irb
PORTVERSION=	1.5.0
CATEGORIES=	devel rubygems
MASTER_SITES=	RG

MAINTAINER=	ruby@FreeBSD.org
COMMENT=	Interactive Ruby
WWW=		https://github.com/ruby/irb

LICENSE=	BSD2CLAUSE
LICENSE_FILE=	${WRKSRC}/LICENSE.txt

RUN_DEPENDS=	rubygem-reline>=0.3.0:devel/rubygem-reline

USES=		gem
USE_RUBY=	yes

NO_ARCH=	yes

PLIST_FILES=	bin/irb \
		share/man/man1/irb.1.gz

post-install:
	${MKDIR} ${STAGEDIR}${PREFIX}/share/man/man1
	${INSTALL_DATA} ${WRKSRC}/man/irb.1 ${STAGEDIR}${PREFIX}/share/man/man1

.include <bsd.port.mk>
