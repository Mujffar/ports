PORTNAME=	labplot
DISTVERSION=	2.9.0
PORTREVISION=	3
CATEGORIES=	math kde
MASTER_SITES=	KDE/stable/${PORTNAME}/${PORTVERSION}

MAINTAINER=	kde@FreeBSD.org
COMMENT=	Data plotting and function analysis tool by KDE
WWW=		https://labplot.kde.org/

LICENSE=	GPLv2+
LICENSE_FILE=	${WRKSRC}/LICENSES/GPL-2.0-or-later.txt

LIB_DEPENDS=	libgsl.so:math/gsl \
		liblz4.so:archivers/liblz4 \
		libspectre.so:print/libspectre \
		libsz.so:science/libaec \
		libreadstat.so:math/readstat

USES=		bison cmake compiler:c++11-lang desktop-file-utils kde:5 qt:5 \
		shared-mime-info tar:xz xorg
USE_KDE=	archive attica auth bookmarks codecs completion config configwidgets \
		coreaddons crash guiaddons i18n iconthemes itemviews \
		jobwidgets kio newstuff notifications parts \
		service solid sonnet syntaxhighlighting textwidgets unitconversion \
		widgetsaddons windowsystem xmlgui \
		doctools:build ecm:build
USE_QT=		concurrent core dbus gui network printsupport serialport \
		sql svg widgets xml \
		buildtools:build qmake:build testlib:build
USE_XORG=	x11

CMAKE_OFF=	ENABLE_LIBCERF
CMAKE_ON=	CMAKE_DISABLE_FIND_PACKAGE_KUserFeedback

DATADIR=	${PREFIX}/share/labplot2

OPTIONS_DEFINE=		CANTOR FITS FFTW3 HDF5 NETCDF
OPTIONS_DEFAULT=	${OPTIONS_DEFINE}

CANTOR_DESC=		Build with Cantor support
CANTOR_CMAKE_BOOL=	ENABLE_CANTOR
CANTOR_LIB_DEPENDS=	libcantorlibs.so:math/cantor \
			libpoppler.so:graphics/poppler \
			libpoppler-qt5.so:graphics/poppler-qt5
FITS_DESC=		Flexible Image Transport System Data Format (FITS) Library
FITS_CMAKE_BOOL=	ENABLE_FITS
FITS_LIB_DEPENDS=	libcfitsio.so:astro/cfitsio
FFTW3_DESC=		Build with FFTW support
FFTW3_CMAKE_BOOL=	ENABLE_FFTW
FFTW3_LIB_DEPENDS=	libfftw3.so:math/fftw3
HDF5_DESC=		Build with HDF5 support
HDF5_CMAKE_BOOL=	ENABLE_HDF5
HDF5_LIB_DEPENDS=	libhdf5.so:science/hdf5
NETCDF_DESC=		Build with NetCDF support
NETCDF_CMAKE_BOOL=	ENABLE_NETCDF
NETCDF_LIB_DEPENDS=	libnetcdf.so:science/netcdf

.include <bsd.port.mk>
