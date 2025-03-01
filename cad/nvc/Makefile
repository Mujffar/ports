PORTNAME=	nvc
DISTVERSIONPREFIX=	r
DISTVERSION=	1.7.1
CATEGORIES=	cad

MAINTAINER=	yuri@FreeBSD.org
COMMENT=	VHDL compiler and simulator
WWW=		https://github.com/nickg/nvc

LICENSE=	GPLv3
LICENSE_FILE=	${WRKSRC}/COPYING

BROKEN_armv6=	compilation fails: no member named '_gregs' in 'mcontext_t'; did you mean '__gregs', see https://github.com/nickg/nvc/issues/534
BROKEN_armv7=	compilation fails: no member named '_gregs' in 'mcontext_t'; did you mean '__gregs', see https://github.com/nickg/nvc/issues/534
BROKEN_FreeBSD_14_i386=	clang creashes, see https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=265826

BUILD_DEPENDS=	llvm-config${LLVM_VERSION}:devel/llvm${LLVM_VERSION}
RUN_DEPENDS=	llvm${LLVM_VERSION}>0:devel/llvm${LLVM_VERSION} \
		bash:shells/bash
TEST_DEPENDS=	check>0:devel/check
.if !exists(/usr/include/unwind.h)
LIB_DEPENDS=	libunwind.so:devel/libunwind
.endif

USES=		autoreconf compiler:c++14-lang localbase pkgconfig shebangfix

USE_GITHUB=	yes
GH_ACCOUNT=	nickg

SHEBANG_FILES=	contrib/functions.sh

GNU_CONFIGURE=	yes

LDFLAGS+=	-lexecinfo

CONFIGURE_ARGS=	--with-llvm=${LOCALBASE}/bin/llvm-config${LLVM_VERSION}

TEST_TARGET=	check # several tests fail, see https://github.com/nickg/nvc/issues/530
TEST_WRKSRC=	${WRKSRC}/.build

MAKE_ARGS=	CFLAGS="${CFLAGS}" # only for tests

LLVM_VERSION=	${LLVM_DEFAULT}

# outsource build is required by the project
BUILD_DIR=		${WRKSRC}/.build
BUILD_WRKSRC=		${BUILD_DIR}
CONFIGURE_WRKSRC=	${BUILD_DIR}
INSTALL_WRKSRC=		${BUILD_DIR}
CONFIGURE_CMD=		${WRKSRC}/configure

.include <bsd.port.options.mk>

.if ${ARCH} == powerpc64
CONFIGURE_ARGS+=	--enable-lto=no
.endif

post-install:
	@${FIND} ${STAGEDIR}${PREFIX} -name "*.so" | ${XARGS} ${STRIP_CMD}

.include <bsd.port.mk>
