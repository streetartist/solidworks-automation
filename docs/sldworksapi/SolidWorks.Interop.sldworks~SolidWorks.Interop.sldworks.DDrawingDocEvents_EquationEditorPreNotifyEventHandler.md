# DDrawingDocEvents_EquationEditorPreNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_EquationEditorPreNotifyEventHandler`

Notifies your application that an the equation editor has been constructed.
Notifies your application that an the equation editor has been constructed.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DDrawingDocEvents_EquationEditorPreNotifyEventHandler() As System.Integer
```

```

Dim instance As New DDrawingDocEvents_EquationEditorPreNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DDrawingDocEvents_EquationEditorPreNotifyEventHandler()
```

```

public delegate System.int DDrawingDocEvents_EquationEditorPreNotifyEventHandler();
```

Remarks

The IDrawingDoc event [EquationEditorPostNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_EquationEditorPostNotifyEventHandler.md) notifies your application that is being destroyed.

If developing a C++ application, use [swDrawingEquationEditorPreNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

Example

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DDrawingDocEvents\_EquationEditorPreNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_EquationEditorPreNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
