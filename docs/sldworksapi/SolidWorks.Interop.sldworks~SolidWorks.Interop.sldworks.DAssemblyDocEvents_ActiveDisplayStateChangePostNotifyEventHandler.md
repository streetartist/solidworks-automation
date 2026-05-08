# DAssemblyDocEvents_ActiveDisplayStateChangePostNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ActiveDisplayStateChangePostNotifyEventHandler`

Fired after the display state of a configuration is changed or after a configuration is changed.
Fired after the display state of a configuration is changed or after a configuration is changed.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DAssemblyDocEvents_ActiveDisplayStateChangePostNotifyEventHandler( _
   ByVal DisplayStateName As System.String _
) As System.Integer
```

```

Dim instance As New DAssemblyDocEvents_ActiveDisplayStateChangePostNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DAssemblyDocEvents_ActiveDisplayStateChangePostNotifyEventHandler( 
   System.string DisplayStateName
)
```

```

public delegate System.int DAssemblyDocEvents_ActiveDisplayStateChangePostNotifyEventHandler( 
   System.String^ DisplayStateName
)
```

#### Parameters

*DisplayStateName*
:   Name of the active display state

Remarks

When changing configurations, the following events are fired in this order:

- [ActiveConfigChangeNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ActiveConfigChangeNotifyEventHandler.md)
- [ActiveDisplayStateChangePreNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ActiveDisplayStateChangePreNotifyEventHandler.md)
- [ActiveConfigChangePostNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ActiveConfigChangePostNotifyEventHandler.md)
- ActiveDisplayStateChangePostNotify

When changing the display state of a configuration, only ActiveDisplayStateChangePreNotify and ActiveDisplayStateChangePostNotify are fired.

This event is fired even when configurations and display states are not linked; however, the initial and final display states will be the same.

Example

[Fire Events When Display State Changes (C#)](Fire_Events_When_Display_State_Changes_Example_CSharp.htm)  
[Fire Events When Display State Changes (VB.NET)](Fire_Events_When_Display_State_Changes_Example_VBNET.htm)  
[Fire Events When Display State Changes (VBA)](Fire_Events_When_Display_State_Changes_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DAssemblyDocEvents\_ActiveDisplayStateChangePostNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ActiveDisplayStateChangePostNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
