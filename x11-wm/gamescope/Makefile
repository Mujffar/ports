PORTNAME=	gamescope
DISTVERSION=	3.11.49
PORTREVISION=	2
CATEGORIES=	x11-wm # wayland: depends on https://github.com/Plagman/gamescope/issues/543

PATCH_SITES=	https://github.com/${GH_ACCOUNT}/${GH_PROJECT}/commit/
PATCHFILES+=	2a84a44f6897.patch:-p1 # https://github.com/Plagman/gamescope/pull/119
PATCHFILES+=	e0927f7bce95.patch:-p1 # https://github.com/Plagman/gamescope/pull/119
PATCHFILES+=	a618ea074660.patch:-p1 # https://github.com/Plagman/gamescope/issues/120
PATCHFILES+=	91fbb22bda68.patch:-p1 # https://github.com/Plagman/gamescope/pull/677
PATCHFILES+=	f4a33bd37e49.patch:-p1 # https://github.com/Plagman/gamescope/pull/632
PATCHFILES+=	be5e7d23e49e.patch:-p1 # wlroots 0.16 (black screen fix)
PATCHFILES+=	bb67298e95a1.patch:-p1 # wlroots 0.16 (xwayland hang fix)

MAINTAINER=	jbeich@FreeBSD.org
COMMENT=	Micro-compositor from SteamOS
WWW=		https://github.com/Plagman/gamescope

LICENSE=	BSD2CLAUSE
LICENSE_FILE=	${WRKSRC}/LICENSE

BUILD_DEPENDS=	glslangValidator:graphics/glslang \
		evdev-proto>0:devel/evdev-proto \
		libliftoff>=0.3.0<0.4.0:graphics/libliftoff \
		vulkan-headers>0:graphics/vulkan-headers \
		wayland-protocols>=1.17:graphics/wayland-protocols \
		wlroots>=0.16.0<0.17.0:x11-toolkits/wlroots
LIB_DEPENDS=	libepoll-shim.so:devel/libepoll-shim \
		libdrm.so:graphics/libdrm \
		libliftoff.so:graphics/libliftoff \
		libvulkan.so:graphics/vulkan-loader \
		libwayland-server.so:graphics/wayland \
		libwlroots.so:x11-toolkits/wlroots \
		libxkbcommon.so:x11/libxkbcommon

USES=		compiler:c++11-lib meson pkgconfig sdl xorg
USE_GITHUB=	yes
USE_SDL=	sdl2
USE_XORG=	x11 xcomposite xdamage xext xfixes xrender xres xtst xxf86vm
GH_ACCOUNT=	Plagman
GH_TUPLE=	nothings:stb:af1a5bc:stb/subprojects/stb
PLIST_FILES=	bin/${PORTNAME}
MESON_ARGS=	--force-fallback-for= # allow system wlroots + libliftoff

OPTIONS_DEFINE=	PIPEWIRE
OPTIONS_DEFAULT=PIPEWIRE

PIPEWIRE_DESC=		Screen capture via PipeWire
PIPEWIRE_LIB_DEPENDS=	libpipewire-0.3.so:multimedia/pipewire
PIPEWIRE_MESON_ENABLED=	pipewire

post-extract:
# Merge patch_directory for subprojects without meson.build
	@(cd ${WRKSRC}/subprojects/packagefiles && ${COPYTREE_SHARE} . ..)
.if defined(PATCHFILES) && ${PATCHFILES:M91fbb22bda68*}
# Pretend to be a regular file for vendor patch to apply as is
	@${RMDIR} ${WRKSRC}/subprojects/wlroots
	@${ECHO_CMD} "Subproject commit 9f41627aa10a94d9427bc315fa3d363a61b94d7c" \
		>${WRKSRC}/subprojects/wlroots
.endif

.include <bsd.port.mk>
