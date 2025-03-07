PORTNAME=	xwayland
DISTVERSIONPREFIX=	xorg-server-
DISTVERSION=	21.0.99.1-297
DISTVERSIONSUFFIX=	-g459e28557
CATEGORIES=	x11-servers
PKGNAMESUFFIX=	-devel

PATCH_SITES=	https://github.com/${GH_ACCOUNT}/${GH_PROJECT}/commit/
PATCHFILES+=	537acb3eb02f.patch:-p1 # https://gitlab.freedesktop.org/xorg/xserver/-/merge_requests/432
PATCHFILES+=	9e1ea1442d7f.patch:-p1 # https://gitlab.freedesktop.org/xorg/xserver/-/merge_requests/432
PATCHFILES+=	74813b4c09ca.patch:-p1 # https://gitlab.freedesktop.org/xorg/xserver/-/merge_requests/432

MAINTAINER=	jbeich@FreeBSD.org
COMMENT=	X11 server as Wayland client (development snapshot)
WWW=		https://wayland.freedesktop.org/xserver.html

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/COPYING

BUILD_DEPENDS=	evdev-proto>0:devel/evdev-proto \
		${LOCALBASE}/include/GL/internal/dri_interface.h:graphics/mesa-dri \
		wayland-protocols>=1.18:graphics/wayland-protocols
LIB_DEPENDS=	libdrm.so:graphics/libdrm \
		libepoxy.so:graphics/libepoxy \
		libwayland-client.so:graphics/wayland \
		libxcvt.so:x11/libxcvt
RUN_DEPENDS=	xkbcomp:x11/xkbcomp \
		xkeyboard-config>0:x11/xkeyboard-config

CONFLICTS_INSTALL=	${PORTNAME}

USES=		compiler:c11 gl meson pkgconfig xorg
USE_GITHUB=	yes
USE_GL=		gbm gl
USE_XORG=	pixman xau xdmcp xfont2 xkbfile xshmfence xtrans
GH_ACCOUNT=	freedesktop
GH_PROJECT=	xorg-xserver
GH_TUPLE=	freedesktop:xorg-xorgproto:xorgproto-2022.2:xorgproto/subprojects/xorgproto
MESON_ARGS=	-D${PORTNAME}=true \
		-Dxorg=false \
		-Dxnest=false \
		-Dxvfb=false \
		-Dudev=false \
		-Dudev_kms=false \
		-Dxcsecurity=true \
		-Ddefault_font_path="${DEFAULT_FONTPATH_LIST:ts,}"
PLIST_FILES=	bin/Xwayland \
		"@comment lib/xorg/protocol.txt" \
		libdata/pkgconfig/xwayland.pc \
		"@comment man/man1/Xserver.1.gz" \
		man/man1/Xwayland.1.gz \
		share/applications/org.freedesktop.Xwayland.desktop

# Keep in sync with xorg-server
FONTPATH_ROOT?=	${LOCALBASE}/share/fonts
FONTPATHD?=	${PREFIX}/etc/X11/fontpath.d
DEFAULT_FONTPATH_LIST= \
	${FONTPATH_ROOT}/misc/	\
	${FONTPATH_ROOT}/TTF/ \
	${FONTPATH_ROOT}/OTF/ \
	${FONTPATH_ROOT}/Type1/ \
	${FONTPATH_ROOT}/100dpi/ \
	${FONTPATH_ROOT}/75dpi/ \
	catalogue:${FONTPATHD}

OPTIONS_DEFINE=	CSD NVIDIA
OPTIONS_DEFAULT=CSD

CSD_DESC=		Client-side decorations via libdecor
CSD_LIB_DEPENDS=	libdecor-0.so:x11-toolkits/libdecor
CSD_MESON_TRUE=		libdecor

NVIDIA_DESC=		EGLStream support for glamor on Xwayland
NVIDIA_BUILD_DEPENDS=	egl-wayland>0:graphics/egl-wayland
NVIDIA_MESON_TRUE=	xwayland_eglstream

.ifdef GH_TUPLE
post-install:
# XXX USES=meson invokes ninja directly, so doesn't support --skip-subprojects
	@${RM} -r ${STAGEDIR}${PREFIX}/include/GL
	@${RM} -r ${STAGEDIR}${PREFIX}/include/X11
	@${RM} -r ${STAGEDIR}${PREFIX}/share/doc/xorgproto
	@${RM} -r ${STAGEDIR}${PREFIX}/share/pkgconfig
.endif

.include <bsd.port.mk>
