PORTNAME=	flightgear-data
PORTVERSION=	2020.3.17
CATEGORIES=	games
MASTER_SITES=	SF/flightgear/release-${PORTVERSION:R}
DISTNAME=	FlightGear-${PORTVERSION}-data

MAINTAINER=	martymac@FreeBSD.org
COMMENT=	FlightGear scenery, textures, and aircraft models
WWW=		https://www.flightgear.org/

LICENSE=	GPLv2

BROKEN_mips64=		fails to install: runaway process

USES=		tar:txz

NO_BUILD=	yes
NO_ARCH=	yes
WRKSRC=		${WRKDIR}/fgdata
DATADIR=	${PREFIX}/share/flightgear

PLIST=		${WRKDIR}/pkg-plist
PLIST_DIRS=	%%DATADIR%%

post-patch:
	@${RM} ${WRKSRC}/COPYING

pre-install:
	@${RM} ${PLIST}
	@cd ${WRKSRC} && \
	${FIND} * -type d -empty | ${SORT} \
		| ${SED} -e 's|^|@preexec ${MKDIR} %D/share/flightgear/|' >> ${PLIST} && \
	${FIND} * -type f | ${SORT} \
		| ${SED} -e 's|^|%%DATADIR%%/|' >> ${PLIST} && \
	${FIND} * -type d -empty | ${SORT} -r \
		| ${SED} -e 's|^|@dir %%DATADIR%%/|' >> ${PLIST}

do-install:
	${MKDIR} ${STAGEDIR}${DATADIR}
	(cd ${WRKSRC}/ && ${COPYTREE_SHARE} . ${STAGEDIR}${DATADIR} "! ( -name .git -o -name .gitignore )")

.include <bsd.port.mk>
