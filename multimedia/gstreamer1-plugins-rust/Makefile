PORTNAME=	gstreamer1-plugins-rust
DISTVERSION=	0.9.1
PORTREVISION=	1
CATEGORIES=	multimedia

MAINTAINER=	jbeich@FreeBSD.org
COMMENT=	Various GStreamer plugins written in Rust
WWW=		https://gitlab.freedesktop.org/gstreamer/gst-plugins-rs

LICENSE=	LGPL21+ MIT
LICENSE_COMB=	multi
LICENSE_FILE_MIT=	${WRKSRC}/LICENSE-MIT
LICENSE_FILE_LGPL21+ =	${WRKSRC}/LICENSE-LGPLv2

BUILD_DEPENDS=	cargo-cbuild:devel/cargo-c

USES=		cargo gnome gstreamer meson pkgconfig python:build shebangfix ssl
USE_GITLAB=	yes
USE_GNOME=	glib20
USE_GSTREAMER=	bad # webrtc
GL_SITE=	https://gitlab.freedesktop.org
GL_ACCOUNT=	gstreamer
GL_PROJECT=	gst-plugins-rs
GL_COMMIT=	274e57a536e5e5c29c92dd0d4485a787c8fec395
SHEBANG_FILES=	dependencies.py
MAKE_ENV=	${CARGO_ENV}
CARGO_BUILD=	no
CARGO_INSTALL=	no
CARGO_TEST=	no

OPTIONS_DEFINE=	CAIRO CSOUND DAV1D GTK4 PANGO SODIUM
OPTIONS_DEFAULT=CAIRO CSOUND DAV1D GTK4 PANGO SODIUM
OPTIONS_EXCLUDE_aarch64=	CSOUND # https://github.com/neithanmo/csound-rs/commit/8962b89d7bda
OPTIONS_EXCLUDE_armv7=	CSOUND # https://github.com/neithanmo/csound-rs/commit/8962b89d7bda
OPTIONS_EXCLUDE_powerpc64le=	CSOUND
OPTIONS_EXCLUDE_powerpc64=	CSOUND
OPTIONS_EXCLUDE_powerpc=	CSOUND DAV1D
OPTIONS_SUB=	yes

CAIRO_USE=		GNOME=cairo
CAIRO_MESON_ENABLED=	videofx

CSOUND_DESC=		Audio filtering via Csound
CSOUND_LIB_DEPENDS=	libcsound64.so:audio/csound
CSOUND_CONFIGURE_ENV=	CSOUND_LIB_DIR="${LOCALBASE}/lib"
CSOUND_MESON_ENABLED=	csound

DAV1D_DESC=		AV1 video decoding via libdav1d
DAV1D_LIB_DEPENDS=	libdav1d.so:multimedia/dav1d
DAV1D_MESON_ENABLED=	dav1d

GTK4_DESC=		${GTK3_DESC:S/3/4/}
GTK4_LIB_DEPENDS=	libgraphene-1.0.so:graphics/graphene
GTK4_USE=		GNOME=gtk40
GTK4_MESON_ENABLED=	gtk4

PANGO_USE=		GNOME=cairo,pango
PANGO_MESON_ENABLED=	closedcaption onvif

SODIUM_DESC=		File encryption and decryption via libsodium
SODIUM_LIB_DEPENDS=	libsodium.so:security/libsodium
SODIUM_MESON_ON=	-Dsodium=system
SODIUM_MESON_OFF=	-Dsodium=disabled

post-patch:
# Make each cargo subcommand very verbose
	@${REINPLACE_CMD} -e "/'cargo'/s/]/, '--verbose', '--verbose'&/" \
		${WRKSRC}/cargo_wrapper.py

post-install:
	@${STRIP_CMD} ${STAGEDIR}${PREFIX}/lib/gstreamer-1.0/*.so

.include <bsd.port.pre.mk>

.if ${PYTHON_REL} < 31100
BUILD_DEPENDS+=	${PYTHON_PKGNAMEPREFIX}tomli>0:textproc/py-tomli@${PY_FLAVOR}
.endif

.include <bsd.port.post.mk>
