# DSldWorksEvents_ActiveDocChangeNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_ActiveDocChangeNotifyEventHandler`

Post-notifies the user program when the active window has changed. This change can be between windows of the same document or between windows of different documents.
Post-notifies the user program when the active window has changed. This change can be between windows of the same document or between windows of different documents.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DSldWorksEvents_ActiveDocChangeNotifyEventHandler() As System.Integer
```

```

Dim instance As New DSldWorksEvents_ActiveDocChangeNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DSldWorksEvents_ActiveDocChangeNotifyEventHandler()
```

```

public delegate System.int DSldWorksEvents_ActiveDocChangeNotifyEventHandler();
```

Remarks

For example, if you open two documents and then select Window, New Window for one of the documents, you will have three windows visible in your SOLIDWORKS session. This event is sent when you switch between any combination of those windows.

This event is only sent when the active window in the SOLIDWORKS session actually changes to a new active window. Window activations are not guaranteed during, for example, the shutdown of the SOLIDWORKS application. For example, if the SOLIDWORKS application closes a non-active document, then there re is no need to activate a new window.

If developing a C++ application, use [swAppDocChangeNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DSldWorksEvents\_ActiveDocChangeNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_ActiveDocChangeNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
