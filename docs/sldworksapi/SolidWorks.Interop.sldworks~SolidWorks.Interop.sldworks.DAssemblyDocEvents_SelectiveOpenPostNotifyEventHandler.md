# DAssemblyDocEvents_SelectiveOpenPostNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_SelectiveOpenPostNotifyEventHandler`

Post-notifies the user program when assembly components are selected for Quick View/Selective Open.
Post-notifies the user program when assembly components are selected for Quick View/Selective Open.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DAssemblyDocEvents_SelectiveOpenPostNotifyEventHandler( _
   ByVal NewAddedDisplayStateName As System.String, _
   ByRef SelectedComponentNames As System.Object _
) As System.Integer
```

```

Dim instance As New DAssemblyDocEvents_SelectiveOpenPostNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DAssemblyDocEvents_SelectiveOpenPostNotifyEventHandler( 
   System.string NewAddedDisplayStateName,
   ref System.object SelectedComponentNames
)
```

```

public delegate System.int DAssemblyDocEvents_SelectiveOpenPostNotifyEventHandler( 
   System.String^ NewAddedDisplayStateName,
   System.Object^% SelectedComponentNames
)
```

#### Parameters

*NewAddedDisplayStateName*
:   Name of the new display state

*SelectedComponentNames*
:   Array of selected component names

Remarks

If developing a C++ application, use [swAssemblySelectiveOpenPostNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

Example

[Selective Open Post-Notify Event (VBA)](Selective_Open_Post_Notify_Event_Example_VB.htm)  
[Selective Open Post-Notify Event (VB.NET)](Selective_Open_Post_Notify_Event_Example_VBNET.htm)  
[Selective Open Post-Notify Event (C#)](Selective_Open_Post_Notify_Event_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DAssemblyDocEvents\_SelectiveOpenPostNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_SelectiveOpenPostNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
