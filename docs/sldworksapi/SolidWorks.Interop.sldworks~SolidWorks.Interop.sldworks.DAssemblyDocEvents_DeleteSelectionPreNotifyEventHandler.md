# DAssemblyDocEvents_DeleteSelectionPreNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_DeleteSelectionPreNotifyEventHandler`

Pre-notifies the user program when the selection is deleted.
Pre-notifies the user program when the selection is deleted.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DAssemblyDocEvents_DeleteSelectionPreNotifyEventHandler() As System.Integer
```

```

Dim instance As New DAssemblyDocEvents_DeleteSelectionPreNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DAssemblyDocEvents_DeleteSelectionPreNotifyEventHandler()
```

```

public delegate System.int DAssemblyDocEvents_DeleteSelectionPreNotifyEventHandler();
```

Remarks

If developing a C++ application, use [swAssemblyDeleteSelectionPreNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

Returning S\_false from your notification handler prevents deletion of the selected item.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DAssemblyDocEvents\_DeleteSelectionPreNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_DeleteSelectionPreNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
