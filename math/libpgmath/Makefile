PORTNAME=	libpgmath
DISTVERSION=	g20191020
PORTREVISION=	1
CATEGORIES=	math

MAINTAINER=	jmd@FreeBSD.org
COMMENT=	Compiler-callable math intrinsics library
WWW=		https://github.com/flang-compiler/flang

LICENSE=	APACHE20
LICENSE_FILE=	${WRKSRC}/LICENSE.txt

DEPRECATED=	Depends on end of life devel/llvm70
EXPIRATION_DATE=2022-12-31

ONLY_FOR_ARCHS=	amd64

LLVM_VER=	70
BUILD_DEPENDS=	llvm${LLVM_VER}>=0:devel/llvm${LLVM_VER}
RUN_DEPENDS=	llvm${LLVM_VER}>=0:devel/llvm${LLVM_VER}

USES=		cmake
USE_LDCONFIG=	yes

USE_GITHUB=	yes
GH_ACCOUNT=	flang-compiler
GH_PROJECT=	flang
GH_TAGNAME=	d07daf3

CC=		${LOCALBASE}/llvm${LLVM_VER}/bin/clang
CXX=		${LOCALBASE}/llvm${LLVM_VER}/bin/clang++

CMAKE_ARGS+=	-DLLVM_CONFIG=${LOCALBASE}/bin/llvm-config${LLVM_VER} -DLIBPGMATH_LLVM_LIT_EXECUTABLE=${LOCALBASE}/llvm${LLVM_VER}/bin/llvm-lit

WRKSRC_SUBDIR=	runtime/libpgmath

PLIST_FILES=	lib/libpgmath.a \
		lib/libpgmath.so

.include <bsd.port.mk>
