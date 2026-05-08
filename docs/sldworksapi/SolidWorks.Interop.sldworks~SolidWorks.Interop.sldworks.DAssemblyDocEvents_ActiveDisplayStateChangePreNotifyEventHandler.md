# DAssemblyDocEvents_ActiveDisplayStateChangePreNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ActiveDisplayStateChangePreNotifyEventHandler`

Fired before the display state of a configuration is changed or before a configuration is changed.
Fired before the display state of a configuration is changed or before a configuration is changed.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DAssemblyDocEvents_ActiveDisplayStateChangePreNotifyEventHandler() As System.Integer
```

```

Dim instance As New DAssemblyDocEvents_ActiveDisplayStateChangePreNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DAssemblyDocEvents_ActiveDisplayStateChangePreNotifyEventHandler()
```

```

public delegate System.int DAssemblyDocEvents_ActiveDisplayStateChangePreNotifyEventHandler();
```

Remarks

When changing configurations, the following events are fired in this order:

- [ActiveConfigChangeNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ActiveConfigChangeNotifyEventHandler.md)
- ActiveDisplayStateChangePreNotify
- [ActiveConfigChangePostNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ActiveConfigChangePostNotifyEventHandler.md)
- [ActiveDisplayStateChangePostNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ActiveDisplayStateChangePostNotifyEventHandler.md)

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

[DAssemblyDocEvents\_ActiveDisplayStateChangePreNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ActiveDisplayStateChangePreNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
