PORTNAME=	bingrep
DISTVERSIONPREFIX=	v
DISTVERSION=	0.10.1
PORTREVISION=	2
CATEGORIES=	devel

MAINTAINER=	eduardo@FreeBSD.org
COMMENT=	Grep through binaries
WWW=		https://github.com/m4b/bingrep

LICENSE=	MIT

USES=		cargo cpe
CPE_VENDOR=	bingrep_project
USE_GITHUB=	yes
GH_ACCOUNT=	m4b

PLIST_FILES=	bin/bingrep

PORTDOCS=	README.md
PORTEXAMPLES=	*.png

OPTIONS_DEFINE=	DOCS EXAMPLES

do-install-DOCS-on:
	@${MKDIR} ${STAGEDIR}${DOCSDIR}
	${INSTALL_DATA} ${WRKSRC}/${PORTDOCS} ${STAGEDIR}${DOCSDIR}

do-install-EXAMPLES-on:
	@${MKDIR} ${STAGEDIR}${EXAMPLESDIR}
	(cd ${WRKSRC}/etc && ${COPYTREE_SHARE} . ${STAGEDIR}${EXAMPLESDIR})

post-install:
	${STRIP_CMD} ${STAGEDIR}${PREFIX}/bin/${PORTNAME}

.include <bsd.port.mk>
