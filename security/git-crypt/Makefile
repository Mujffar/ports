PORTNAME=	git-crypt
PORTVERSION=	0.7.0
CATEGORIES=	security
MASTER_SITES=	https://www.agwa.name/projects/git-crypt/downloads/ \
		LOCAL/ashish/

MAINTAINER=	ashish@FreeBSD.org
COMMENT=	Transparent file encryption in git
WWW=		https://www.agwa.name/projects/git-crypt/

LICENSE=	GPLv3
LICENSE_FILE=	${WRKSRC}/COPYING

RUN_DEPENDS=	git:devel/git \
		gpg:security/gnupg

OPTIONS_DEFINE=	MANPAGES

MAKE_ENV+=	PREFIX=${PREFIX} "CXXFLAGS=${CXXFLAGS}" \
		"LDFLAGS=${LDFLAGS}"

MANPAGES_BUILD_DEPENDS=	xsltproc:textproc/libxslt \
			docbook-xsl>=0:textproc/docbook-xsl
MANPAGES_MAKE_ARGS=		ENABLE_MAN=yes \
			MANDIR=${MANPREFIX}/man \
			DOCBOOK_XSL=${LOCALBASE}/share/xsl/docbook/manpages/docbook.xsl
MANPAGES_PLIST_FILES=	man/man1/${PORTNAME}.1.gz

USES=		compiler:c++11-lang gmake ssl

PLIST_FILES=	bin/${PORTNAME}

.include <bsd.port.pre.mk>

.if ${SSL_DEFAULT} != base
CXXFLAGS+=	-I${OPENSSLINC}
LDFLAGS+=	-L${OPENSSLLIB}
.endif

post-extract:
	@${GREP} -Rl '"gpg"' ${WRKSRC} |${XARGS} ${REINPLACE_CMD} -e 's,"gpg","${LOCALBASE}/bin/gpg",'
	@${GREP} -Rl '"git"' ${WRKSRC} |${XARGS} ${REINPLACE_CMD} -e 's,"git","${LOCALBASE}/bin/git",'

post-install:
	${STRIP_CMD} ${STAGEDIR}${PREFIX}/bin/git-crypt

.include <bsd.port.post.mk>
