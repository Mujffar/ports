PORTNAME=	storj
PORTVERSION=	1.67.3
DISTVERSIONPREFIX=	v
CATEGORIES=	net

MAINTAINER=	danfe@FreeBSD.org
COMMENT=	Decentralized cloud object storage
WWW=		https://storj.io/

LICENSE=	AGPLv3

USES=		go:modules
USE_GITHUB=	yes

.include "${.CURDIR}/Makefile.deps"

STORJ_CMDS=	certificates crashcollect identity inspector metric-receiver \
		multinode satellite storagenode storagenode-updater \
		storj-admin storj-sim uplink versioncontrol

GO_TARGET=	${STORJ_CMDS:S,^,./cmd/,}

post-stage:
# Avoid conflict with `graphics/mesa-demos'
	@${MV} ${STAGEDIR}${PREFIX}/bin/identity \
		${STAGEDIR}${PREFIX}/bin/${PORTNAME}-identity

.include <bsd.port.mk>
