PORTNAME=	pg.el
DISTVERSIONPREFIX=	v
DISTVERSION=	0.19
PORTREVISION=	1
CATEGORIES=	databases elisp
PKGNAMESUFFIX=	${EMACS_PKGNAMESUFFIX}

MAINTAINER=	yasu@FreeBSD.org
COMMENT=	PostgreSQL Elisp interface
WWW=		https://github.com/emarsden/pg-el

LICENSE=	GPLv2+

USES=		emacs

USE_GITHUB=	yes
GH_ACCOUNT=	emarsden
GH_PROJECT=	pg-el
GH_TAGNAME=	${DISTVERSIONPREFIX}${DISTVERSION}

CONFLICTS_INSTALL=	pg.el pg.el-emacs_* # share/doc/pg.el/README

NO_ARCH=	yes

PLIST_FILES=	${EMACS_VERSION_SITE_LISPDIR}/pg.el \
		${EMACS_VERSION_SITE_LISPDIR}/pg.elc

PORTDOCS=	CHANGELOG.md README.md

OPTIONS_DEFINE=	DOCS

do-build:
	(cd ${WRKSRC} \
	&& ${EMACS_CMD} -Q -batch -L . -f batch-byte-compile *.el)

do-install:
	${MKDIR} ${STAGEDIR}${PREFIX}/${EMACS_VERSION_SITE_LISPDIR}
	(cd ${WRKSRC} && ${INSTALL_DATA} *.el* \
	    ${STAGEDIR}${PREFIX}/${EMACS_VERSION_SITE_LISPDIR})

do-install-DOCS-on:
	@${MKDIR} ${STAGEDIR}${DOCSDIR}
	${INSTALL_DATA} ${PORTDOCS:C/^/${WRKSRC}\//g} ${STAGEDIR}${DOCSDIR}

.include <bsd.port.mk>
