# DFeatMgrViewEvents_DestroyNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DFeatMgrViewEvents_DestroyNotifyEventHandler`

Pre-notifies the user program when a FeatureManager design tree view is about to be destroyed and returns the view handle.
Pre-notifies the user program when a FeatureManager design tree view is about to be destroyed and returns the view handle.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DFeatMgrViewEvents_DestroyNotifyEventHandler( _
   ByRef View As System.Object _
) As System.Integer
```

```

Dim instance As New DFeatMgrViewEvents_DestroyNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DFeatMgrViewEvents_DestroyNotifyEventHandler( 
   ref System.object View
)
```

```

public delegate System.int DFeatMgrViewEvents_DestroyNotifyEventHandler( 
   System.Object^% View
)
```

#### Parameters

*View*
:   [View](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)

Remarks

If developing a C++ application, use [swFMViewDestroyNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFMViewNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DFeatMgrViewEvents\_DestroyNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DFeatMgrViewEvents_DestroyNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
