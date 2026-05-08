# DFeatMgrViewEvents_DeactivateNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DFeatMgrViewEvents_DeactivateNotifyEventHandler`

Post-notifies the user program once a FeatureManager design tree view is deactivated and returns the view handle.
Post-notifies the user program once a FeatureManager design tree view is deactivated and returns the view handle.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DFeatMgrViewEvents_DeactivateNotifyEventHandler( _
   ByRef View As System.Object _
) As System.Integer
```

```

Dim instance As New DFeatMgrViewEvents_DeactivateNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DFeatMgrViewEvents_DeactivateNotifyEventHandler( 
   ref System.object View
)
```

```

public delegate System.int DFeatMgrViewEvents_DeactivateNotifyEventHandler( 
   System.Object^% View
)
```

#### Parameters

*View*
:   [View](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)

Remarks

This notification is generated if you created the FeatureManager design tree view using [IModelViewManager::CreateFeatureMgrView2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrView2.md) instead of [IModelDoc2::AddFeatureMgrView3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddFeatureMgrView3.md).

If developing a C++ application, use [swFMViewDeactivateNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFMViewNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DFeatMgrViewEvents\_DeactivateNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DFeatMgrViewEvents_DeactivateNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
