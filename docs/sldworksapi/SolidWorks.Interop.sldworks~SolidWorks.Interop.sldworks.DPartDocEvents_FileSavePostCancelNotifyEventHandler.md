# DPartDocEvents_FileSavePostCancelNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_FileSavePostCancelNotifyEventHandler`

Fired if FileSavePostNotify is not fired.
Fired if [FileSavePostNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_FileSavePostNotifyEventHandler.md) is not fired.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DPartDocEvents_FileSavePostCancelNotifyEventHandler() As System.Integer
```

```

Dim instance As New DPartDocEvents_FileSavePostCancelNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DPartDocEvents_FileSavePostCancelNotifyEventHandler()
```

```

public delegate System.int DPartDocEvents_FileSavePostCancelNotifyEventHandler();
```

Remarks

If developing a C++ application, use [swPartFileSavePostCancelNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DPartDocEvents\_FileSavePostCancelNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_FileSavePostCancelNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
