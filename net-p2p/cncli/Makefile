PORTNAME=		cncli
DISTVERSIONPREFIX=	v
DISTVERSION=		5.2.0
PORTREVISION=	2
CATEGORIES=		net-p2p

MAINTAINER=		boris@zfs.ninja
COMMENT=		A community-based cardano-node CLI tool
WWW=			https://cardano-community.github.io/guild-operators/

LICENSE=		APACHE20
LICENSE_FILE=		${WRKSRC}/LICENSE

NOT_FOR_ARCHS=		i386
NOT_FOR_ARCHS_REASON=	cryptoxide Rust crate uses AVX2 instructions

USES=		autoreconf:build cargo gmake libtool pkgconfig ssl

USE_GITHUB=	yes
GH_ACCOUNT=	cardano-community input-output-hk:sodium
GH_PROJECT=	${PORTNAME} libsodium:sodium
GH_TAGNAME=	${LIBSODIUM_HASH}:sodium

LIBSODIUM_HASH=	66f017f16633f2060db25e17c170c2afa0f2a8a1
LIBS_PREFIX=	${WRKDIR}/libs_install

CARGO_ENV=	SODIUM_LIB_DIR=${LIBS_PREFIX}${PREFIX}/lib SODIUM_INCLUDE_DIR=${LIBS_PREFIX}${PREFIX}/include \
		OPENSSL_LIB_DIR=${OPENSSLLIB} OPENSSL_INCLUDE_DIR=${OPENSSLINC}

.sinclude "${.CURDIR}/Makefile.crates"

PLIST_FILES=	bin/cncli

pre-build:
		cd ${WRKSRC_sodium} && ./autogen.sh
		cd ${WRKSRC_sodium} && ./configure --prefix=${PREFIX} --with-pthreads --disable-shared
		cd ${WRKSRC_sodium} && gmake -j${MAKE_JOBS_NUMBER} && gmake DESTDIR=${LIBS_PREFIX} install
		${MKDIR} ${LIBS_PREFIX}${PREFIX}/libdata/pkgconfig
		${MV} ${LIBS_PREFIX}${PREFIX}/lib/pkgconfig/libsodium.pc ${LIBS_PREFIX}${PREFIX}/libdata/pkgconfig/libsodium.pc

.include <bsd.port.mk>
