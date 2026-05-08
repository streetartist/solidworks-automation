# DAssemblyDocEvents_DragStateChangeNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_DragStateChangeNotifyEventHandler`

Fired when starting or stopping the dragging of an Instant3D manipulator.
Fired when starting or stopping the dragging of an Instant3D manipulator.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DAssemblyDocEvents_DragStateChangeNotifyEventHandler( _
   ByVal State As System.Boolean _
) As System.Integer
```

```

Dim instance As New DAssemblyDocEvents_DragStateChangeNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DAssemblyDocEvents_DragStateChangeNotifyEventHandler( 
   System.bool State
)
```

```

public delegate System.int DAssemblyDocEvents_DragStateChangeNotifyEventHandler( 
   System.bool State
)
```

#### Parameters

*State*
:   True if dragging of the Instant3D manipulator has started, false if dragging of the Instant3D manipulator has stopped

Remarks

If developing a C++ application, use [swAssemblyDragStateChangeNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

Example

[Fire Events When Dragging Instant3D Manipulator in an Assembly (C#)](Fire_Events_When_Dragging_Instant3D_Manipulator_in_an_Assembly_Example_CSharp.htm)  
[Fire Events When Dragging Instant3D Manipulator in an Assembly (VB.NET)](Fire_Events_When_Dragging_Instant3D_Manipulator_in_an_Assembly_Example_VBNET.htm)  
[Fire Events When Dragging Instant3D Manipulator in an Assembly (VBA)](Fire_Events_When_Dragging_Instant3D_Manipulator_in_an_Assembly_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DAssemblyDocEvents\_DragStateChangeNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_DragStateChangeNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[DPartDocEvents\_DragStateChangeNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_DragStateChangeNotifyEventHandler.md)
