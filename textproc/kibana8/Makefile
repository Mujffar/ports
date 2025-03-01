PORTNAME=	kibana
DISTVERSION=	8.5.2
DISTVERSIONSUFFIX=	-darwin-x86_64
CATEGORIES=	textproc www
MASTER_SITES=	https://artifacts.elastic.co/downloads/kibana/ \
		http://artifacts.elastic.co/downloads/kibana/
PKGNAMESUFFIX=	8
DISTFILES=	${DISTNAME}${EXTRACT_SUFX}

MAINTAINER=	elastic@FreeBSD.org
COMMENT=	Browser based analytics and search interface to ElasticSearch
WWW=		https://www.elastic.co/products/kibana

LICENSE=	APACHE20

BUILD_DEPENDS=	${LOCALBASE}/bin/npm:www/npm-node16
LIB_DEPENDS=	libre2.so:devel/re2 \
		libuv.so:devel/libuv
RUN_DEPENDS=	${LOCALBASE}/bin/node:www/node16

USES=		compiler:c++14-lang cpe nodejs:16,build,run python:build
CPE_VENDOR=	elastic

USE_GITHUB=	nodefault
GH_TUPLE=	nodejs:nan:v${_NODE_NAN_VER}:node_nan \
		uhop:node-re2:${_NODE_RE2_VER}:node_re2

USE_RC_SUBR=	${PORTNAME}

CONFLICTS=	kibana7

WWWDIR=		${PREFIX}/www/${PORTNAME}${PKGNAMESUFFIX}

PORTSCOUT=	limit:^8

SUB_FILES=	pkg-deinstall pkg-message
SUB_LIST+=	BINDIR=${PREFIX}/bin \
		PKGNAMESUFFIX=${PKGNAMESUFFIX} \
		PORTNAME=${PORTNAME}

WRKSRC=		${WRKDIR}/${PORTNAME}-${DISTVERSION}

BINS=		kibana-encryption-keys kibana-keystore kibana-plugin \
		kibana-setup kibana-verification-code

#######################################################################
# Set node-nan version here
_NODE_NAN_VER=	2.17.0
# Set node-re version here
_NODE_RE2_VER=	1.17.8
#######################################################################

_NODECMD=	${LOCALBASE}/bin/node --version
_DEVDIR:=	${WRKDIR}/.devdir

_RE2DIR=	${WRKDIR}/node-re2-${_NODE_RE2_VER}

# Extra patch files must be updated whenever node-re2 changes
_RE2PATCHES=	${PATCHDIR}/extra-node-re2-binding-gyp.patch

post-patch:
	${FIND} -s ${WRKSRC}/node_modules -type d -empty -delete
	cd ${_RE2DIR} && ${PATCH} -p0 < ${_RE2PATCHES}
	${REINPLACE_CMD} -e "s|%%PREFIX%%|${PREFIX}|g" \
	-e "s|%%DEVDIR%%|${_DEVDIR}|g" ${_RE2DIR}/binding.gyp \

pre-configure:
	( \
	_NODEVER=$$(${_NODECMD} | ${SED} -n 's|^v\(.*\)|\1|p') && \
	${MKDIR} ${_DEVDIR}/$${_NODEVER}/include && \
	${RLN} ${LOCALBASE}/include/node ${_DEVDIR}/$${_NODEVER}/include/node && \
	${ECHO} "9" > ${_DEVDIR}/$${_NODEVER}/installVersion \
	)

do-configure:
	${MKDIR} ${_DEVDIR}/nan
	(cd ${WRKDIR}/nan-${_NODE_NAN_VER} && ${COPYTREE_SHARE} . \
		${_DEVDIR}/nan \
		"! ( -name \.* -or -path *\/test\/* -or -name test )")
	(cd ${_RE2DIR} && \
		${SETENV} HOME=${WRKDIR} \
		${LOCALBASE}/lib/node_modules/npm/bin/node-gyp-bin/node-gyp configure \
		--python=${PYTHON_CMD} \
		--devdir=${_DEVDIR})

do-build:
	(cd ${_RE2DIR} && \
		${SETENV} HOME=${WRKDIR} \
		${LOCALBASE}/lib/node_modules/npm/bin/node-gyp-bin/node-gyp build \
		--devdir=${_DEVDIR})

do-install:
	${MKDIR} ${STAGEDIR}${WWWDIR} ${STAGEDIR}${ETCDIR}
	${INSTALL_DATA} ${WRKSRC}/config/kibana.yml ${STAGEDIR}${ETCDIR}/kibana.yml.sample
	(cd ${WRKSRC} && \
		${RM} -r config node optimize && \
		${COPYTREE_SHARE} . ${STAGEDIR}${WWWDIR} && \
		${COPYTREE_BIN} bin ${STAGEDIR}${WWWDIR})
	${INSTALL} -lrs ${STAGEDIR}${ETCDIR} ${STAGEDIR}${WWWDIR}/config
	${MKDIR} ${STAGEDIR}${WWWDIR}/node/bin
	${LN} -s ${LOCALBASE}/bin/node ${STAGEDIR}${WWWDIR}/node/bin/node
	${RM} ${STAGEDIR}${WWWDIR}/node_modules/re2/build/Release/re2.node
	${INSTALL_LIB} ${_RE2DIR}/build/Release/re2.node \
		${STAGEDIR}${WWWDIR}/node_modules/re2/build/Release/re2.node
.for f in ${BINS}
	${INSTALL} -l rs ${STAGEDIR}${WWWDIR}/bin/${f} ${STAGEDIR}${PREFIX}/bin/${f}
	${ECHO} "bin/${f}" >> ${TMPPLIST}
.endfor

post-install:
	${ECHO} "@sample ${ETCDIR}/kibana.yml.sample" >> ${TMPPLIST}
	${FIND} -s ${STAGEDIR}${WWWDIR} -not -type d | ${SORT} | \
		${SED} -e 's#^${STAGEDIR}${PREFIX}/##' >> ${TMPPLIST}
	${ECHO} "@dir(www,www) ${WWWDIR}/data" >> ${TMPPLIST}
	${ECHO} "@dir ${WWWDIR}/plugins" >> ${TMPPLIST}
	${ECHO} "@dir ${WWWDIR}/logs" >> ${TMPPLIST}

.include <bsd.port.mk>
