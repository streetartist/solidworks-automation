# DSldWorksEvents_CommandCloseNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_CommandCloseNotifyEventHandler`

Fired when a command, including a PropertyManager page, is okay'd or canceled by a user.
Fired when a command, including a PropertyManager page, is okay'd or canceled by a user.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DSldWorksEvents_CommandCloseNotifyEventHandler( _
   ByVal Command As System.Integer, _
   ByVal reason As System.Integer _
) As System.Integer
```

```

Dim instance As New DSldWorksEvents_CommandCloseNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DSldWorksEvents_CommandCloseNotifyEventHandler( 
   System.int Command,
   System.int reason
)
```

```

public delegate System.int DSldWorksEvents_CommandCloseNotifyEventHandler( 
   System.int Command,
   System.int reason
)
```

#### Parameters

*Command*
:   Command as defined in [swCommands\_e](SolidWorks.Interop.swcommands~SolidWorks.Interop.swcommands.swCommands_e.md)

*reason*
:   Reason as defined by:

    - swCommands\_e.swCommands\_PmOK or swCommands\_e.swCommands\_PmCancel (for PropertyManager page closures)

    - swCommands\_e.swCommands\_Exit\_Measure (for Measure dialog closures)

    - swCommands\_Comp\_Isolate\_Exit (for Isolate dialog closures)

Remarks

If developing a C++ application, use [swAppCommandCloseNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

You can combine:

- the IAssemblyDoc [FeatureEditPreNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_FeatureEditPreNotifyEventHandler.md) event or the IPartDoc [FeatureEditPreNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_EquationEditorPreNotifyEventHandler.md) event with the ISldWorks CommandCloseNotify event and swCommands\_e.swCommands\_EditFeature.
- the IAssemblyDoc [FeatureSketchEditPreNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_FeatureSketchEditPreNotifyEventHandler.md) event or the IPartDoc [FeatureSketchEditPreNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_FeatureSketchEditPreNotifyEventHandler.md) event with the ISldWorks CommandCloseNotify event and swCommands\_e.swCommands\_Sketch.

Call [CommandOpenPreNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_CommandOpenPreNotifyEventHandler.md) to fire an event before a command executes or a PropertyManager page opens.

Example

[Fire Events When PropertyManager Page Opened and Canceled (VBA)](Fire_Events_When_PropertyManager_Page_Opened_and_Canceled_Example_VB.htm)  
[Fire Events When PropertyManager Page Opened and Canceled (VB.NET)](Fire_Events_When_PropertyManager_Page_Opened_and_Canceled_Example_VBNET.htm)  
[Fire Events When PropertyManager Page Opened and Canceled (C#)](Fire_Events_When_PropertyManager_Page_Opened_and_Canceled_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DSldWorksEvents\_CommandCloseNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_CommandCloseNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[ISldWorks::RunCommand Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RunCommand.md)  
[ISldWorks::GetRunningCommandInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetRunningCommandInfo.md)  
[DSldWorksEvents\_CommandOpenPreNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_CommandOpenPreNotifyEventHandler.md)
