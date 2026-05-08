# DAssemblyDocEvents_InterferenceNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_InterferenceNotifyEventHandler`

Notifies your program about an interference between parts in the assembly during the Move/Rotate Component command.
Notifies your program about an interference between parts in the assembly during the **Move/Rotate Component** command.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DAssemblyDocEvents_InterferenceNotifyEventHandler( _
   ByRef PComp As System.Object, _
   ByRef PFace As System.Object _
) As System.Integer
```

```

Dim instance As New DAssemblyDocEvents_InterferenceNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DAssemblyDocEvents_InterferenceNotifyEventHandler( 
   ref System.object PComp,
   ref System.object PFace
)
```

```

public delegate System.int DAssemblyDocEvents_InterferenceNotifyEventHandler( 
   System.Object^% PComp,
   System.Object^% PFace
)
```

#### Parameters

*PComp*
:   Array of [components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) that interfere

*PFace*
:   Array of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) that interfere

Remarks

If developing a C++ application, use [swAssemblyInterferenceNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

This notification is only sent when faces clash during the **Move/Rotate Component** command, which executes as an interactive drag of a component, and if collision detection is enabled in the user interface.

You can use this notification with [IAssemblyDoc::IToolsCheckInterference3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IToolsCheckInterference3.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DAssemblyDocEvents\_InterferenceNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_InterferenceNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
