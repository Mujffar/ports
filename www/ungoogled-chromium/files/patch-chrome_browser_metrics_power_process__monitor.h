--- chrome/browser/metrics/power/process_monitor.h.orig	2022-10-29 17:50:56 UTC
+++ chrome/browser/metrics/power/process_monitor.h
@@ -71,7 +71,7 @@ class ProcessMonitor : public content::BrowserChildPro
     double cpu_usage = 0.0;
 
 #if BUILDFLAG(IS_MAC) || BUILDFLAG(IS_LINUX) || BUILDFLAG(IS_CHROMEOS) || \
-    BUILDFLAG(IS_AIX)
+    BUILDFLAG(IS_AIX) || BUILDFLAG(IS_BSD)
     // Returns the number of average idle cpu wakeups per second since the last
     // time the metric was sampled.
     int idle_wakeups = 0;
