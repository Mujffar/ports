PORTNAME=	fet
DISTVERSION=	6.7.0
CATEGORIES=	deskutils education
MASTER_SITES=	https://lalescu.ro/liviu/fet/download/ \
		https://lalescu.ro/liviu/fet/download/old/ \
		https://timetabling.de/download/ \
		https://timetabling.de/download/old/

MAINTAINER=	uzsolt@uzsolt.hu
COMMENT=	Free timetabling software
WWW=		https://lalescu.ro/liviu/fet/

LICENSE=	GPLv3+
LICENSE_FILE=	${WRKSRC}/COPYING

USES=		compiler:c++14-lang gl qmake qt:5 tar:bzip2
USE_GL=		gl
USE_QT=		core printsupport widgets buildtools:build

INSTALL_TARGET=	${WRKSRC}/fet-cl

DESKTOP_ENTRIES=	"FET" \
			"Free timetable software" \
			"" \
			"fet" \
			"Education;Qt;" \
			true

PORTEXAMPLES=	*

OPTIONS_DEFINE=	EXAMPLES NLS ONLYCL
OPTIONS_SUB=	yes

ONLYCL_DESC=	Build only command line version (without Qt GUI)

ONLYCL_VARS=		QMAKE_SOURCE_PATH=${WRKSRC}/src/src-cl.pro
ONLYCL_VARS_OFF=	INSTALL_TARGET+=${WRKSRC}/fet \
			USE_QT+="gui network"

post-patch:
	@${REINPLACE_CMD} -e 's|/usr/share/fet|${DATADIR}|g' \
		${WRKSRC}/src/interface/fet.cpp

do-install:
	${INSTALL_PROGRAM} ${INSTALL_TARGET} ${STAGEDIR}${PREFIX}/bin
	${INSTALL_PROGRAM} ${WRKSRC}/fet-cl ${STAGEDIR}${PREFIX}/bin
	${INSTALL_MAN} ${WRKSRC}/man/fet*.gz ${STAGEDIR}${MANPREFIX}/man/man1

do-install-EXAMPLES-on:
	@${MKDIR} ${STAGEDIR}${EXAMPLESDIR}
	cd ${WRKSRC}/examples && ${COPYTREE_SHARE} . ${STAGEDIR}${EXAMPLESDIR}

do-install-NLS-on:
	@${MKDIR} ${STAGEDIR}${DATADIR}/translations
	cd ${WRKSRC}/translations && ${INSTALL_DATA} *.qm ${STAGEDIR}${DATADIR}/translations

.include <bsd.port.mk>
