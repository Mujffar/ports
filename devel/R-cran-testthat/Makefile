PORTNAME=	testthat
DISTVERSION=	3.1.5
CATEGORIES=	devel
DISTNAME=	${PORTNAME}_${DISTVERSION}

MAINTAINER=	ygy@FreeBSD.org
COMMENT=	Unit Testing for R
WWW=		https://testthat.r-lib.org

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

BUILD_DEPENDS=	R-cran-knitr>0:print/R-cran-knitr
RUN_DEPENDS=	R-cran-jsonlite>0:converters/R-cran-jsonlite \
		R-cran-R6>=2.2.0:devel/R-cran-R6 \
		R-cran-brio>0:devel/R-cran-brio \
		R-cran-callr>=3.5.1:devel/R-cran-callr \
		R-cran-cli>=3.4.0:devel/R-cran-cli \
		R-cran-desc>0:devel/R-cran-desc \
		R-cran-ellipsis>=0.2.0:devel/R-cran-ellipsis \
		R-cran-evaluate>0:devel/R-cran-evaluate \
		R-cran-lifecycle>0:devel/R-cran-lifecycle \
		R-cran-magrittr>0:devel/R-cran-magrittr \
		R-cran-pkgload>0:devel/R-cran-pkgload \
		R-cran-praise>0:devel/R-cran-praise \
		R-cran-rlang>=1.0.1:devel/R-cran-rlang \
		R-cran-waldo>=0.4.0:devel/R-cran-waldo \
		R-cran-withr>=2.4.3:devel/R-cran-withr \
		R-cran-digest>0:security/R-cran-digest \
		R-cran-processx>0:sysutils/R-cran-processx \
		R-cran-ps>=1.3.4:sysutils/R-cran-ps
TEST_DEPENDS=	R-cran-covr>0:devel/R-cran-covr \
		R-cran-mockery>0:devel/R-cran-mockery \
		R-cran-rstudioapi>0:devel/R-cran-rstudioapi \
		R-cran-usethis>0:devel/R-cran-usethis \
		R-cran-curl>=0.9.5:ftp/R-cran-curl \
		R-cran-knitr>0:print/R-cran-knitr \
		R-cran-rmarkdown>0:textproc/R-cran-rmarkdown \
		R-cran-shiny>0:www/R-cran-shiny

USES=		cran:auto-plist,compiles

.include <bsd.port.mk>
