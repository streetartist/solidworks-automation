# DPartDocEvents_RegenPostNotify2EventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_RegenPostNotify2EventHandler`

Post-notifies the user program when a part document has been rebuilt or rolled back.
Post-notifies the user program when a part document has been rebuilt or rolled back.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DPartDocEvents_RegenPostNotify2EventHandler( _
   ByVal stopFeature As System.Object _
) As System.Integer
```

```

Dim instance As New DPartDocEvents_RegenPostNotify2EventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DPartDocEvents_RegenPostNotify2EventHandler( 
   System.object stopFeature
)
```

```

public delegate System.int DPartDocEvents_RegenPostNotify2EventHandler( 
   System.Object^ stopFeature
)
```

#### Parameters

*stopFeature*
:   - If a rollback, [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) immediately below the rollback bar in the FeatureManager design tree
    - If a rebuild, NULL

Remarks

If developing a C++ application, use [swPartRegenPostNotify2](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DPartDocEvents\_RegenPostNotify2EventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_RegenPostNotify2EventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
