# DPartDocEvents_EquationEditorPostNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_EquationEditorPostNotifyEventHandler`

Notifies your application that the equation editor is being destroyed.
Notifies your application that the equation editor is being destroyed.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DPartDocEvents_EquationEditorPostNotifyEventHandler( _
   ByVal Changed As System.Boolean _
) As System.Integer
```

```

Dim instance As New DPartDocEvents_EquationEditorPostNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DPartDocEvents_EquationEditorPostNotifyEventHandler( 
   System.bool Changed
)
```

```

public delegate System.int DPartDocEvents_EquationEditorPostNotifyEventHandler( 
   System.bool Changed
)
```

#### Parameters

*Changed*
:   True if equations have changed, false if not

Remarks

The PartDoc event [EquationEditorPreNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_EquationEditorPreNotifyEventHandler.md) notifies your application that the equation editor has been constructed.

If developing a C++ application, use [swPartEquationPostNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DPartDocEvents\_EquationEditorPostNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_EquationEditorPostNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
