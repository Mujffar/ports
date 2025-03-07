PORTNAME=	onedrive
DISTVERSIONPREFIX=	v
DISTVERSION=	2.4.21
CATEGORIES=	net

MAINTAINER=	hiroo.ono+freebsd@gmail.com
COMMENT=	OneDrive Free client
WWW=		https://github.com/abraunegg/onedrive

LICENSE=	GPLv3
LICENSE_FILE=	${WRKSRC}/LICENSE

BUILD_DEPENDS=	ldc2:lang/ldc
LIB_DEPENDS=	libcurl.so:ftp/curl \
		libinotify.so:devel/libinotify
RUN_DEPENDS=	${LOCALBASE}/sbin/logrotate:sysutils/logrotate

USES=		autoreconf gmake pkgconfig sqlite

USE_GITHUB=	yes
GH_ACCOUNT=	abraunegg

GNU_CONFIGURE=	yes
PKGCONFIG=	pkgconf

PORTDOCS=	*

OPTIONS_DEFINE=		DOCS NOTIFY COMPLETION
OPTIONS_DEFAULT=	NOTIFY COMPLETION
OPTIONS_SUB=		yes

COMPLETION_DESC=		Install completion for BASH, FISH and ZSH
COMPLETION_BUILD_DEPENDS=	bash-completion>0:shells/bash-completion
COMPLETION_RUN_DEPENDS=		bash-completion>0:shells/bash-completion
COMPLETION_CONFIGURE_ENABLE=	completions

NOTIFY_LIB_DEPENDS=	libnotify.so:devel/libnotify
NOTIFY_USES=		gnome
NOTIFY_USE=		GNOME=glib20,gdkpixbuf2
NOTIFY_CONFIGURE_ENABLE=	notifications

ONEDRIVE_LOGDIR=	/var/log/${PORTNAME}

post-extract:
	${CP} ${FILESDIR}/freebsd_inotify.d ${WRKSRC}/src

post-install:
	${INSTALL} -d -m 0775 ${STAGEDIR}${ONEDRIVE_LOGDIR}

.include <bsd.port.pre.mk>

# llvm 13.0 and above.
.if (${OSVERSION} >= 1400042) || \
	(${OSVERSION} < 1400000 && ${OSVERSION} >= 1300522)
CONFIGURE_ARGS+=	DCFLAGS=-L=-Wl,-z,nostart-stop-gc
.endif

.include <bsd.port.post.mk>
