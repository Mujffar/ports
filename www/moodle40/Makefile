PORTNAME=	moodle
PORTVERSION=	4.0.5
CATEGORIES=	www education
MASTER_SITES=	SF/moodle/Moodle/stable400/
PKGNAMESUFFIX=	${PKGORIGIN:T:S/moodle//}${PHP_PKGNAMESUFFIX}

MAINTAINER=	wen@FreeBSD.org
COMMENT=	Course management system based on social constructionism
WWW=		https://www.moodle.org/

LICENSE=	GPLv3

CONFLICTS=	moodle39-3.9.[0-9]* moodle311-3.11.[0-9]* moodle41-4.1

USES=		cpe php:flavors tar:tgz
USE_PHP=	ctype curl dom exif fileinfo filter gd hash \
		iconv intl json mbstring opcache openssl \
		pcre session simplexml soap sodium spl tokenizer \
		xml xmlreader xmlrpc zip zlib
IGNORE_WITH_PHP=	81 82

WRKSRC=		${WRKDIR}/moodle

OPTIONS_SINGLE=		BACKEND
OPTIONS_SINGLE_BACKEND=	MYSQL PGSQL MSSQL
OPTIONS_DEFINE=		LDAP
OPTIONS_DEFAULT=	MYSQL

MYSQL_USES=	mysql
MYSQL_USE=	php=mysqli
PGSQL_USE=	php=pgsql
MSSQL_USE=	php=mssql
LDAP_USE=	php=ldap

NO_BUILD=	yes
PLIST=		${WRKDIR}/plist
SUB_FILES=	pkg-message
SUB_LIST=	MOODLEDIR=${MOODLEDIR} \
		MOODLEDATADIR=${MOODLEDATADIR}

MOODLEDIR?=	www/moodle
MOODLEDATADIR?=	moodledata

pre-install:
	@${ECHO_CMD} "@owner ${WWWOWN}" >> ${PLIST}
	@${ECHO_CMD} "@group ${WWWGRP}" >> ${PLIST}
	@${ECHO_CMD} "@mode 755" >> ${PLIST}
	@${ECHO} @dir ${MOODLEDATADIR} >> ${PLIST}
	@${ECHO_CMD} "@mode" >> ${PLIST}
	@${ECHO_CMD} "@group" >> ${PLIST}
	@${ECHO_CMD} "@owner" >> ${PLIST}

#  Here for safety I do not set moodle diretory 0755 permission
#  It require user write config.php manually then.
	@${FIND} -s -d ${WRKSRC} -type f | ${SED} "s?${WRKSRC}?${MOODLEDIR}?g" >>${PLIST}
	@${FIND} -s -d ${WRKSRC} -type d  | ${SED} "s?${WRKSRC}?@dir ${MOODLEDIR}?g" >> ${PLIST}

do-install:
	@cd ${WRKSRC} && ${COPYTREE_SHARE} . ${STAGEDIR}${PREFIX}/${MOODLEDIR}
	@${INSTALL} -d ${STAGEDIR}${PREFIX}/${MOODLEDATADIR}

.include <bsd.port.mk>
