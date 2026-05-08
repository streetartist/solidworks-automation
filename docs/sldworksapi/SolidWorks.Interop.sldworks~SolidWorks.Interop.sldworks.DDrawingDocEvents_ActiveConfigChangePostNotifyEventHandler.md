# DDrawingDocEvents_ActiveConfigChangePostNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_ActiveConfigChangePostNotifyEventHandler`

Post-notifies the user program when the user has switched to a different configuration.
Post-notifies the user program when the user has switched to a different configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DDrawingDocEvents_ActiveConfigChangePostNotifyEventHandler() As System.Integer
```

```

Dim instance As New DDrawingDocEvents_ActiveConfigChangePostNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DDrawingDocEvents_ActiveConfigChangePostNotifyEventHandler()
```

```

public delegate System.int DDrawingDocEvents_ActiveConfigChangePostNotifyEventHandler();
```

Remarks

If developing a C++ application, use [swDrawingConfigChangePostNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DDrawingDocEvents\_ActiveConfigChangePostNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_ActiveConfigChangePostNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
