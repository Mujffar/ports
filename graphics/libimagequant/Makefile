PORTNAME=	libimagequant
PORTVERSION=	4.0.4
PORTREVISION=	1
CATEGORIES=	graphics

MAINTAINER=	jbeich@FreeBSD.org
COMMENT=	Image Quantization Library
WWW=		https://pngquant.org/lib/

LICENSE=	GPLv3+
LICENSE_FILE=	${WRKSRC}/COPYRIGHT

BUILD_DEPENDS=	cargo-cbuild:devel/cargo-c

USES=		cargo
USE_GITHUB=	yes
GH_ACCOUNT=	ImageOptim
WRKSRC_SUBDIR=	imagequant-sys
USE_LDCONFIG=	yes
PLIST_FILES=	include/libimagequant.h \
		lib/libimagequant.a \
		lib/libimagequant.so \
		lib/libimagequant.so.0 \
		lib/libimagequant.so.0.0.0 \
		libdata/pkgconfig/imagequant.pc

do-build:
	@${CARGO_CARGO_RUN} cbuild \
		--verbose \
		--verbose \
		${CARGO_BUILD_ARGS}

do-install:
	@${CARGO_CARGO_RUN} cinstall \
		--verbose \
		--verbose \
		--destdir "${STAGEDIR}" \
		--prefix "${PREFIX}" \
		${CARGO_INSTALL_ARGS}
	@${STRIP_CMD} ${STAGEDIR}${PREFIX}/lib/*.so

.include <bsd.port.mk>
