PORTNAME=	shibboleth
PORTVERSION=	4.2.1
CATEGORIES=	security www
MASTER_SITES=	http://shibboleth.net/downloads/identity-provider/${PORTVERSION}/ \
		http://shibboleth.net/downloads/identity-provider/latest4/${PORTVERSION}/ \
		http://shibboleth.net/downloads/identity-provider/archive/${PORTVERSION}/ \
		https://repo1.maven.org/maven2/ch/qos/logback/logback-core/${LOGBACKVER}/:logback_core \
		https://repo1.maven.org/maven2/ch/qos/logback/logback-classic/${LOGBACKVER}/:logback_classic
PKGNAMESUFFIX=	-idp
DISTFILES=	shibboleth-identity-provider-${PORTVERSION}.tar.gz \
		logback-classic-${LOGBACKVER}.jar:logback_classic \
		logback-core-${LOGBACKVER}.jar:logback_core
EXTRACT_ONLY=	shibboleth-identity-provider-${PORTVERSION}.tar.gz

MAINTAINER=	zi@FreeBSD.org
COMMENT=	Shibboleth Identity Provider (Internet2)
WWW=		http://shibboleth.internet2.edu/

LICENSE=	APACHE20

BUILD_DEPENDS=	jetty10>=0:www/jetty10
RUN_DEPENDS=	bash:shells/bash \
		jetty10>=0:www/jetty10

USE_RC_SUBR=	shibboleth-idp
CPE_VENDOR=	shibboleth
WRKSRC=		${WRKDIR}/shibboleth-identity-provider-${PORTVERSION}

NO_ARCH=	yes
NO_BUILD=	yes

LOGBACKVER=	1.4.0
SHIBUSER=	shibd
SHIBGROUP=	shibd
LOGDIR=		/var/log/${PORTNAME}
RUNDIR=		/var/run/${PORTNAME}
USERS=		${SHIBUSER}
GROUPS=		${SHIBGROUP}

SUB_FILES=	shibboleth

SUB_LIST+=	SHIBUSER=${SHIBUSER} SHIBGROUP=${SHIBGROUP} \
		RUNDIR=${RUNDIR} LOGDIR=${LOGDIR}
PLIST_SUB+=	SHIBUSER=${SHIBUSER} SHIBGROUP=${SHIBGROUP} \
		RUNDIR=${RUNDIR} LOGDIR=${LOGDIR} LOGBACKVER=${LOGBACKVER}

do-install:
	@${MKDIR} ${STAGEDIR}${DATADIR} ${STAGEDIR}${ETCDIR}
	@${MKDIR} ${STAGEDIR}${LOGDIR} ${STAGEDIR}${RUNDIR}
	@${MKDIR} ${STAGEDIR}${WWWDIR}/lib/logging
	@${MKDIR} ${STAGEDIR}${EXAMPLESDIR}
.for dir in conf credentials etc modules resources start.d webapps/ROOT
	@${MKDIR} ${STAGEDIR}${WWWDIR}/${dir}
.endfor
	(cd ${WRKSRC} && ${COPYTREE_SHARE} . ${STAGEDIR}${DATADIR})
	(cd ${FILESDIR}/jetty-base && ${COPYTREE_SHARE} . ${STAGEDIR}${EXAMPLESDIR})
	@${FIND} ${STAGEDIR}${DATADIR} -type f -name '*.sh' -exec ${CHMOD} +x {} \;
.for jar in logback-classic-${LOGBACKVER}.jar logback-core-${LOGBACKVER}.jar
	${INSTALL_DATA} ${DISTDIR}/${jar} ${STAGEDIR}${WWWDIR}/lib/logging
.endfor
	${INSTALL_DATA} ${WRKDIR}/shibboleth ${STAGEDIR}${ETCDIR}/shibboleth-idp
	${INSTALL_DATA} ${FILESDIR}/index.html ${STAGEDIR}${EXAMPLESDIR}/index.html
	${INSTALL_SCRIPT} ${FILESDIR}/shibboleth-idp.sh ${STAGEDIR}${PREFIX}/sbin

.include <bsd.port.mk>
