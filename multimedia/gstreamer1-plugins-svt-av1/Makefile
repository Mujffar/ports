PORTNAME=	svt-av1
DISTVERSIONPREFIX=	v
DISTVERSION=	1.3.0
CATEGORIES=	multimedia
PKGNAMEPREFIX=	gstreamer1-plugins-

MAINTAINER=	jbeich@FreeBSD.org
COMMENT=	GStreamer (svt-av1) plugin
WWW=		https://01.org/svt

LICENSE=	LGPL21+ # based on SPDX header
LICENSE_FILE=	${_LICENSE_STORE}/LGPL21

LIB_DEPENDS=	libSvtAv1Enc.so:multimedia/svt-av1

USES=		gnome gstreamer meson pkgconfig
USE_GITLAB=	yes
USE_GNOME=	glib20
GL_ACCOUNT=	AOMediaCodec
GL_PROJECT=	SVT-AV1
GL_COMMIT=	91b94efb2809e83d9bf041d8575b32f234dfef27
WRKSRC_SUBDIR=	gstreamer-plugin
PLIST_FILES=	lib/gstreamer-1.0/libgstsvtav1enc.so

post-patch:
	@${REINPLACE_CMD} '/-O2/d' ${WRKSRC}/meson.build

.include <bsd.port.mk>
