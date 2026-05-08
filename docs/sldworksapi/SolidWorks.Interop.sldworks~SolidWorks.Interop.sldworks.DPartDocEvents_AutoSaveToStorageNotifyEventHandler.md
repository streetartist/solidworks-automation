# DPartDocEvents_AutoSaveToStorageNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_AutoSaveToStorageNotifyEventHandler`

Fired when the part document is automatically saved to third-party IStream storage.
Fired when the part document is automatically saved to third-party IStream storage.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DPartDocEvents_AutoSaveToStorageNotifyEventHandler() As System.Integer
```

```

Dim instance As New DPartDocEvents_AutoSaveToStorageNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DPartDocEvents_AutoSaveToStorageNotifyEventHandler()
```

```

public delegate System.int DPartDocEvents_AutoSaveToStorageNotifyEventHandler();
```

Remarks

If developing a C++ application, use [swAutoSaveToStorageNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DPartDocEvents\_AutoSaveToStorageNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_AutoSaveToStorageNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
