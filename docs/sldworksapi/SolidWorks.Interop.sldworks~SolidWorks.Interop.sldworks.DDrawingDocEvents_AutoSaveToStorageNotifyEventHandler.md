# DDrawingDocEvents_AutoSaveToStorageNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_AutoSaveToStorageNotifyEventHandler`

Fired when the drawing document is automatically saved to third-party IStream storage.
Fired when the drawing document is automatically saved to third-party IStream storage.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DDrawingDocEvents_AutoSaveToStorageNotifyEventHandler() As System.Integer
```

```

Dim instance As New DDrawingDocEvents_AutoSaveToStorageNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DDrawingDocEvents_AutoSaveToStorageNotifyEventHandler()
```

```

public delegate System.int DDrawingDocEvents_AutoSaveToStorageNotifyEventHandler();
```

Remarks

If developing a C++ application, use [swDrawingAutoSaveToStorageNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DDrawingDocEvents\_AutoSaveToStorageNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_AutoSaveToStorageNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
