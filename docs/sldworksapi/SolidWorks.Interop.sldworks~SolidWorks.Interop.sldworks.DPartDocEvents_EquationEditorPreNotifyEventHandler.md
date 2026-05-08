# DPartDocEvents_EquationEditorPreNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_EquationEditorPreNotifyEventHandler`

Notifies your application that an the equation editor has been constructed.
Notifies your application that an the equation editor has been constructed.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DPartDocEvents_EquationEditorPreNotifyEventHandler() As System.Integer
```

```

Dim instance As New DPartDocEvents_EquationEditorPreNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DPartDocEvents_EquationEditorPreNotifyEventHandler()
```

```

public delegate System.int DPartDocEvents_EquationEditorPreNotifyEventHandler();
```

Remarks

The PartDoc event [EquationEditorPostNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_EquationEditorPostNotifyEventHandler.md) notifies your application that is being destroyed.

If developing a C++ application, use [swPartEquationPreNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DPartDocEvents\_EquationEditorPreNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_EquationEditorPreNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
