# DPartDocEvents_ClearSelectionsNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_ClearSelectionsNotifyEventHandler`

Notifies the user program when selections are cleared using Clear Selections.
Notifies the user program when selections are cleared using Clear Selections.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DPartDocEvents_ClearSelectionsNotifyEventHandler() As System.Integer
```

```

Dim instance As New DPartDocEvents_ClearSelectionsNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DPartDocEvents_ClearSelectionsNotifyEventHandler()
```

```

public delegate System.int DPartDocEvents_ClearSelectionsNotifyEventHandler();
```

Remarks

If developing a C++ application, use [swPartClearSelectionsNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this event.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DPartDocEvents\_ClearSelectionsNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_ClearSelectionsNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
