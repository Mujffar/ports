PORTNAME=	deck
PORTVERSION=	1.8.2
DISTVERSIONPREFIX=	v
CATEGORIES=	www
MASTER_SITES=	https://github.com/nextcloud-releases/${PORTNAME}/releases/download/${DISTVERSIONPREFIX}${PORTVERSION}/
PKGNAMEPREFIX=	nextcloud-
PKGNAMESUFFIX=	${PHP_PKGNAMESUFFIX}
DIST_SUBDIR=	nextcloud

MAINTAINER=	brnrd@FreeBSD.org
COMMENT=	Kanban app for Nextcloud
WWW=		https://apps.nextcloud.com/apps/deck

LICENSE=	AGPLv3
LICENSE_FILE=	${WRKSRC}/LICENSE

RUN_DEPENDS=	nextcloud${PHP_PKGNAMESUFFIX}>=25:www/nextcloud@${PHP_FLAVOR}

USES=		cpe php:flavors
IGNORE_WITH_PHP=	82
NO_BUILD=	yes
NO_ARCH=	yes
CPE_VENDOR=	nextcloud

WRKSRC=		${WRKDIR}/${PORTNAME}

WWWDIR=		${PREFIX}/www/nextcloud/apps-pkg/${PORTNAME}

do-install:
	@${MKDIR} ${STAGEDIR}${WWWDIR}
	@(cd ${WRKSRC} && ${COPYTREE_SHARE} . ${STAGEDIR}${WWWDIR})
	@(cd ${WRKSRC}; ${FIND} . -not -type d) | ${SORT} | \
		${SED} -e 's,^\.,${WWWDIR_REL},' >> ${TMPPLIST}

.include <bsd.port.mk>
