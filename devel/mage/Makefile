PORTNAME=	mage
DISTVERSIONPREFIX=	v
DISTVERSION=	1.14.0
PORTREVISION=	1
PORTEPOCH=	1
CATEGORIES=	devel

MAINTAINER=	gspurki@gmail.com
COMMENT=	Command-line make-like build tool using Go as input files
WWW=		https://magefile.org/

LICENSE=	APACHE20
LICENSE_FILE=	${WRKSRC}/LICENSE

USES=		go:modules

USE_GITHUB=	yes
GH_ACCOUNT=	magefile

PLIST_FILES=	bin/mage

post-patch:
	@${REINPLACE_CMD} -e "s|%%GH_TAGNAME%%|${GH_TAGNAME}|g; s|%%GH_TAG_COMMIT%%|${GH_TAG_COMMIT}|g" \
		${WRKSRC}/magefile.go

do-build:
	@cd ${WRKSRC} && ${SETENV} ${MAKE_ENV} ${GO_ENV} \
	${GO_CMD} run bootstrap.go

.include <bsd.port.mk>
