PORTNAME=	elgg
PORTVERSION=	4.3.4
CATEGORIES=	www
MASTER_SITES=	http://elgg.org/download/

MAINTAINER=	wen@FreeBSD.org
COMMENT=	Blogging and social networking platform
WWW=		https://www.elgg.org/

LICENSE=	GPLv2

USES=		cpe gettext shebangfix zip php
USE_PHP=	curl dom fileinfo filter gd hash intl \
		json mbstring pdo_mysql \
		session simplexml soap sqlite3 xml xmlrpc
IGNORE_WITH_PHP=	81 82

NO_BUILD=	yes
PLIST_SUB=	WWWOWN="${WWWOWN}" WWWGRP="${WWWGRP}"
SUB_FILES=	pkg-message
ELGGDATADIR=	${WWWDIR}/data

do-install:
	${MKDIR} ${STAGEDIR}${WWWDIR}
	@cd ${WRKSRC} && ${COPYTREE_SHARE} . ${STAGEDIR}${WWWDIR}

	@${INSTALL} -d ${STAGEDIR}${ELGGDATADIR}
	@${CHMOD} 755 ${STAGEDIR}${ELGGDATADIR}
	@${CHMOD} 755 ${STAGEDIR}${WWWDIR}/elgg-config

.include <bsd.port.mk>
