PORTNAME=	containernetworking-plugins
DISTVERSION=	0.1
CATEGORIES=	net

MAINTAINER=	dfr@FreeBSD.org
COMMENT=	Networking plugins for container networking support
WWW=		https://www.cni.dev/

LICENSE=	GPLv2

USES=		go:no_targets
BUILD_DEPENDS=	bash:shells/bash

USE_GITHUB=	yes
GH_ACCOUNT=	dfr
GH_PROJECT=	plugins
GH_TAGNAME=	60b0a2b

do-build:
	cd ${WRKSRC} && ${SETENV} XDG_CACHE_HOME=${WRKDIR}/.cache GO=${GO_CMD} ./build_freebsd.sh

do-install:
	${MKDIR} ${STAGEDIR}${PREFIX}/libexec/cni
	${MKDIR} ${STAGEDIR}${PREFIX}/etc/containers
	cd ${WRKSRC} && ${INSTALL_PROGRAM} bin/* ${STAGEDIR}${PREFIX}/libexec/cni
	${INSTALL_DATA} files/pf.conf.sample ${STAGEDIR}${PREFIX}/etc/containers

.include <bsd.port.mk>
