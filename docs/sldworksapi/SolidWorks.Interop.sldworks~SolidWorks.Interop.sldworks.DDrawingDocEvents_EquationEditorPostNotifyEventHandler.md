# DDrawingDocEvents_EquationEditorPostNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_EquationEditorPostNotifyEventHandler`

Notifies your application that the equation editor is being destroyed.
Notifies your application that the equation editor is being destroyed.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DDrawingDocEvents_EquationEditorPostNotifyEventHandler( _
   ByVal Changed As System.Boolean _
) As System.Integer
```

```

Dim instance As New DDrawingDocEvents_EquationEditorPostNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DDrawingDocEvents_EquationEditorPostNotifyEventHandler( 
   System.bool Changed
)
```

```

public delegate System.int DDrawingDocEvents_EquationEditorPostNotifyEventHandler( 
   System.bool Changed
)
```

#### Parameters

*Changed*
:   True if equations have changed, false if not

Remarks

The IDrawingDoc event [EquationEditorPreNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_EquationEditorPreNotifyEventHandler.md) notifies your application that the equation editor has been constructed.

If developing a C++ application, use [swDrawingEquationEditorPostNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DDrawingDocEvents\_EquationEditorPostNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_EquationEditorPostNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
