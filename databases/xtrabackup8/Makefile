PORTNAME=	xtrabackup
PORTVERSION=	8.0.14
PORTREVISION=	6
CATEGORIES=	databases
MASTER_SITES=	https://www.percona.com/downloads/Percona-XtraBackup-${PORTVERSION:R}/Percona-XtraBackup-${PORTVERSION}/source/tarball/:precona \
		https://github.com/percona/percona-xtrabackup/archive/:percona \
		SF/boost/boost/${BOOST_VERSION}:boost
PKGNAMESUFFIX=	8
DISTNAME=	percona-${PORTNAME}-${PORTVERSION}
DISTFILES=	percona-${PORTNAME}-${DISTVERSION}${EXTRACT_SUFX}:percona \
		boost_${BOOST_VERSION_UNDER}${EXTRACT_SUFX}:boost

MAINTAINER=	eugene@zhegan.in
COMMENT=	Open-source backup tool for InnoDB and XtraDB
WWW=		https://www.percona.com/doc/percona-xtrabackup/

LICENSE=	GPLv2
LICENSE_FILE=	${WRKSRC}/LICENSE

BUILD_DEPENDS=	xxd:editors/vim \
		protobuf>=3.0:devel/protobuf \
		rapidjson>=1.1.0:devel/rapidjson \
		libevent>=2.1:devel/libevent
LIB_DEPENDS=	libcurl.so:ftp/curl \
		libev.so:devel/libev \
		libgcrypt.so:security/libgcrypt \
		libgpg-error.so:security/libgpg-error \
		libicudata.so:devel/icu \
		libunwind.so:devel/libunwind \
		libzstd.so:archivers/zstd
RUN_DEPENDS=	qpress:archivers/qpress

CONFLICTS_INSTALL=	${PORTNAME}

USES=		bison cmake compiler:c++14-lang cpe pkgconfig ssl
CPE_VENDOR=	percona
CMAKE_ARGS=	-DBUILD_CONFIG:STRING=xtrabackup_release
.for component in EDITLINE ICU LIBEVENT PROTOBUF RAPIDJSON ZSTD
CMAKE_ARGS+=	-DWITH_${component}:STRING=system
.endfor

# Bundle last supported Boost release
BOOST_VERSION=	1.72.0
BOOST_VERSION_UNDER=	${BOOST_VERSION:C/\./_/g}

CMAKE_ARGS+=	-DWITH_BOOST=${WRKDIR}/boost_${BOOST_VERSION_UNDER}

.include <bsd.port.pre.mk>

# Since MySQL 8.0.20 InnoDB engine uses new memory alligned allocator
# which is broken on i386 due to different size of types and causes a
# 'static_assert(alignof(T) <= alignof(std::max_align_t))' error
.if ${ARCH} == i386
CMAKE_ARGS+=	-DDISABLE_PSI_MEMORY=1
.endif

post-extract:
# Delete bundled components so we won't accidentally use them, except LZ4
# which cannot be removed just yet
	@${MV} ${WRKSRC}/extra/lz4 ${WRKSRC}
	@${RM} -r ${WRKSRC}/extra/*
	@${MV} ${WRKSRC}/lz4 ${WRKSRC}/extra

post-patch:
	@${REINPLACE_CMD} -e 's,TRUE,true,' ${WRKSRC}/sql/mysqld.cc

post-stage:
	@${RM} -r ${STAGEDIR}${PREFIX}/docs
	@${RMDIR} ${STAGEDIR}${PREFIX}/lib/plugin/debug

.include <bsd.port.post.mk>
