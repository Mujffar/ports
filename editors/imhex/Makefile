PORTNAME=	imhex
PORTVERSION=	1.25.0
DISTVERSIONPREFIX=	v
CATEGORIES=	editors
MASTER_SITES=	https://git.sr.ht/~danyspin97/xdgpp/blob/f01f810714443d0f10c333d4d1d9c0383be41375/:xdg
DISTFILES=	xdg.hpp:xdg
DIST_SUBDIR=	imhex

MAINTAINER=	nobutaka@FreeBSD.org
COMMENT=	Hex editor for reverse engineers and programmers
WWW=		https://github.com/WerWolv/ImHex

LICENSE=	GPLv2
LICENSE_FILE=	${WRKSRC}/LICENSE

NOT_FOR_ARCHS=	i386 powerpc
NOT_FOR_ARCHS_REASON=	__uint128_t and __int128_t are not supported
EXTRACT_ONLY=	${DISTNAME}${EXTRACT_SUFX} \
		btzy-nativefiledialog-extended-${GH_TAG_NATIVEFILEDIALOG}_GH0${EXTRACT_SUFX} \
		capstone-engine-capstone-${GH_TAG_CAPSTONE}_GH0${EXTRACT_SUFX} \
		CLIUtils-CLI11-${GH_TAG_CLI11}_GH0${EXTRACT_SUFX} \
		fmtlib-fmt-${GH_TAG_FMT}_GH0${EXTRACT_SUFX} \
		josuttis-jthread-${GH_TAG_JTHREAD}_GH0${EXTRACT_SUFX} \
		VirusTotal-yara-${GH_TAG_YARA}_GH0${EXTRACT_SUFX} \
		WerWolv-libromfs-${GH_TAG_LIBROMFS}_GH0${EXTRACT_SUFX} \
		WerWolv-ImHex-Patterns-${GH_TAG_IMHEX_PATTERNS}_GH0${EXTRACT_SUFX} \
		WerWolv-PatternLanguage-${GH_TAG_PATTERN_LANGUAGE}_GH0${EXTRACT_SUFX}

BUILD_DEPENDS=	glm>0:math/glm \
		nlohmann-json>0:devel/nlohmann-json \
		${LOCALBASE}/include/range/v3/range.hpp:devel/range-v3 \
		${LOCALBASE}/include/hpx/functional.hpp:devel/hpx
LIB_DEPENDS=	libcurl.so:ftp/curl \
		libglfw.so:graphics/glfw \
		libfreetype.so:print/freetype2 \
		libharfbuzz.so:print/harfbuzz \
		libmbedtls.so:security/mbedtls \
		libtre.so:textproc/libtre

USES=		cmake gl gnome pkgconfig python:3.8+ xorg
USE_GL=		gl
USE_GNOME=	cairo gdkpixbuf2 gtk30
USE_XORG=	x11 xcb xau xdmcp
USE_GITHUB=	yes

GH_ACCOUNT=	WerWolv
GH_PROJECT=	ImHex
GH_TUPLE=	btzy:nativefiledialog-extended:${GH_TAG_NATIVEFILEDIALOG}:nativefiledialog \
		capstone-engine:capstone:${GH_TAG_CAPSTONE}:capstone \
		CLIUtils:CLI11:${GH_TAG_CLI11}:cli11 \
		fmtlib:fmt:${GH_TAG_FMT}:fmt \
		josuttis:jthread:${GH_TAG_JTHREAD}:jthread \
		VirusTotal:yara:${GH_TAG_YARA}:yara \
		WerWolv:ImHex-Patterns:${GH_TAG_IMHEX_PATTERNS}:imhex_patterns \
		WerWolv:PatternLanguage:${GH_TAG_PATTERN_LANGUAGE}:pattern_language \
		WerWolv:libromfs:${GH_TAG_LIBROMFS}:libromfs

GH_TAG_CAPSTONE=	d5141c0
GH_TAG_CLI11=	faea921
GH_TAG_FMT=	a337011
GH_TAG_IMHEX_PATTERNS=	a9ada89
GH_TAG_JTHREAD=	0fa8d39
GH_TAG_LIBROMFS=	53a6bf5
GH_TAG_NATIVEFILEDIALOG=	d4df2b6
GH_TAG_PATTERN_LANGUAGE=	7aeac4a
GH_TAG_YARA=	ba94b4f

CMAKE_ARGS=	-DUSE_SYSTEM_CURL=ON -DUSE_SYSTEM_NLOHMANN_JSON=ON \
		-DIMHEX_STRIP_RELEASE=OFF -DIMHEX_PLUGINS_IN_SHARE=ON \
		-DIMHEX_OFFLINE_BUILD=ON

PORTDOCS=	README.md

OPTIONS_DEFINE=	DOCS NLS
NLS_USES=	gettext

.include <bsd.port.pre.mk>

OSMAJOR=${OSVERSION:C/([0-9]*)[0-9]{5}/\1/}

# Before LLVM13 import to the base system
.if (${OSMAJOR} == 12 && ${OSVERSION} < 1203505) \
    || (${OSMAJOR} == 14 && ${OSVERSION} < 1400042)
IGNORE=	will not build due to C++20 API functions unavailable in old libc++
.endif

post-extract:
	${CP} ${DISTDIR}/${DIST_SUBDIR}/xdg.hpp ${WRKSRC}/lib/external/xdgpp
	${CP} -R ${WRKSRC_capstone}/* ${WRKSRC}/lib/external/capstone
	${CP} -R ${WRKSRC_fmt}/* ${WRKSRC}/lib/external/fmt
	${CP} -R ${WRKSRC_jthread}/source/*.hpp ${WRKSRC}/lib/libimhex/include
	${CP} -R ${WRKSRC_libromfs}/* ${WRKSRC}/lib/external/libromfs
	${CP} -R ${WRKSRC_nativefiledialog}/* ${WRKSRC}/lib/external/nativefiledialog
	${CP} -R ${WRKSRC_pattern_language}/* ${WRKSRC}/lib/external/pattern_language
	${CP} -R ${WRKSRC_cli11}/* ${WRKSRC}/lib/external/pattern_language/external/cli11
	${CP} -R ${WRKSRC_yara}/* ${WRKSRC}/lib/external/yara/yara
	${MKDIR} ${WRKDIR}/.build/_deps/imhex_patterns_src
	${CP} -R ${WRKSRC_imhex_patterns}/* ${WRKDIR}/.build/_deps/imhex_patterns_src

post-install-DOCS-on:
	${MKDIR} ${STAGEDIR}${DOCSDIR}
	${INSTALL_DATA} ${WRKSRC}/README.md ${STAGEDIR}${DOCSDIR}

.include <bsd.port.post.mk>
