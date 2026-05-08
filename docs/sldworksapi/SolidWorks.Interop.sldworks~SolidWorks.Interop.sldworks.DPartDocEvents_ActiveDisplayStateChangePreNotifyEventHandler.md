# DPartDocEvents_ActiveDisplayStateChangePreNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_ActiveDisplayStateChangePreNotifyEventHandler`

Fired before the display state of a configuration is changed or before a configuration is changed.
Fired before the display state of a configuration is changed or before a configuration is changed.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DPartDocEvents_ActiveDisplayStateChangePreNotifyEventHandler() As System.Integer
```

```

Dim instance As New DPartDocEvents_ActiveDisplayStateChangePreNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DPartDocEvents_ActiveDisplayStateChangePreNotifyEventHandler()
```

```

public delegate System.int DPartDocEvents_ActiveDisplayStateChangePreNotifyEventHandler();
```

Remarks

When changing configurations, the following events are fired in this order:

- [ActiveConfigChangeNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_ActiveConfigChangeNotifyEventHandler.md)
- ActiveDisplayStateChangePreNotify
- [ActiveConfigChangePostNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_ActiveConfigChangePostNotifyEventHandler.md)
- [ActiveDisplayStateChangePostNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_ActiveDisplayStateChangePostNotifyEventHandler.md)

When changing the display state of a configuration, only ActiveDisplayStateChangePreNotify and ActiveDisplayStateChangePostNotify are fired.

This event is fired even when configurations and display states are not linked; however, the initial and final display states will be the same.

Example

[Fire Events When Display State Changes in Part Document (C#)](Fire_Events_When_Display_State_Changes_in_Part_Document_Example_CSharp.htm)  
[Fire Events When Display State Changes in Part Document (VB.NET)](Fire_Events_When_Display_State_Changes_in_Part_Document_Example_VBNET.htm)  
[Fire Events When Display State Changes in Part Document (VBA)](Fire_Events_When_Display_State_Changes_in_Part_Document_Example_VB6.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DPartDocEvents\_ActiveDisplayStateChangePreNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_ActiveDisplayStateChangePreNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
