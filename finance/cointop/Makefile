PORTNAME=	cointop
DISTVERSIONPREFIX=	v
DISTVERSION=	1.6.10
PORTREVISION=	6
CATEGORIES=	finance

MAINTAINER=	lcook@FreeBSD.org
COMMENT=	Cryptocurrency coin stats
WWW=		https://github.com/miguelmota/cointop

LICENSE=	APACHE20
LICENSE_FILE=	${WRKSRC}/LICENSE

USES=		go:modules
GO_MODULE=	github.com/${PORTNAME}-sh/${PORTNAME}
GO_BUILDFLAGS=	-ldflags "\
		-s -w \
		-X ${GO_MODULE}/cointop.version=${DISTVERSION}"

PLIST_FILES=	bin/${PORTNAME}

.include <bsd.port.mk>
