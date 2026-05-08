# DDrawingDocEvents_FeatureManagerTabActivatedPreNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_FeatureManagerTabActivatedPreNotifyEventHandler`

Fired before the active tab in the Manager Pane changes.
Fired before the active tab in the Manager Pane changes.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DDrawingDocEvents_FeatureManagerTabActivatedPreNotifyEventHandler( _
   ByVal CommandIndex As System.Integer, _
   ByVal CommandTabName As System.String _
) As System.Integer
```

```

Dim instance As New DDrawingDocEvents_FeatureManagerTabActivatedPreNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DDrawingDocEvents_FeatureManagerTabActivatedPreNotifyEventHandler( 
   System.int CommandIndex,
   System.string CommandTabName
)
```

```

public delegate System.int DDrawingDocEvents_FeatureManagerTabActivatedPreNotifyEventHandler( 
   System.int CommandIndex,
   System.String^ CommandTabName
)
```

#### Parameters

*CommandIndex*
:   Index of the active tab in the Manager Pane

*CommandTabName*
:   Name of the active tab in the Manager Pane

Remarks

If developing a C++ application, use [swDrawingFeatureManagerTabActivatedPreNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DDrawingDocEvents\_FeatureManagerTabActivatedPreNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_FeatureManagerTabActivatedPreNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
