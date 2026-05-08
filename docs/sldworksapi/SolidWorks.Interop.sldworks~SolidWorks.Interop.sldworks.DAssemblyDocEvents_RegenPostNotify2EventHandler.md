# DAssemblyDocEvents_RegenPostNotify2EventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_RegenPostNotify2EventHandler`

Post-notifies the user program when an assembly document is rebuilt.
Post-notifies the user program when an assembly document is rebuilt.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DAssemblyDocEvents_RegenPostNotify2EventHandler( _
   ByVal stopFeature As System.Object _
) As System.Integer
```

```

Dim instance As New DAssemblyDocEvents_RegenPostNotify2EventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DAssemblyDocEvents_RegenPostNotify2EventHandler( 
   System.object stopFeature
)
```

```

public delegate System.int DAssemblyDocEvents_RegenPostNotify2EventHandler( 
   System.Object^ stopFeature
)
```

#### Parameters

*stopFeature*
:   - If rolled back, the [assembly feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) below the rollback bar in the FeatureManager design tree

    - If rebuilt, Nothing or null

Remarks

If developing a C++ application, use [swAssemblyRegenPostNotify2](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

Use [DAssemblyDocEvents RegenNotifyEventHandler](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_RegenNotifyEventHandler.md) to fire an event before the assembly is about to be rebuilt.

You can also use [IModelDoc2::GetUpdateStamp](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetUpdateStamp.md) to determine when changes take place in this document.

Example

[Fire Assembly Rebuild Events (C#)](Regen_Post_Notify2_Event_Handler_Example_CSharp.htm)  
[Fire Assembly Rebuild Events (VB.NET)](Regen_Post_Notify2_Event_Handler_Example_VBNET.htm)  
[Fire Assembly Rebuild Events (VBA)](Regen_Post_Notify2_Event_Handler_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DAssemblyDocEvents\_RegenPostNotify2EventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_RegenPostNotify2EventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
