# DDrawingDocEvents_FeatureManagerTabActivatedNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_FeatureManagerTabActivatedNotifyEventHandler`

Fired when the active tab in the Manager Pane changes.
Fired when the active tab in the Manager Pane changes.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DDrawingDocEvents_FeatureManagerTabActivatedNotifyEventHandler( _
   ByVal CommandIndex As System.Integer, _
   ByVal CommandTabName As System.String _
) As System.Integer
```

```

Dim instance As New DDrawingDocEvents_FeatureManagerTabActivatedNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DDrawingDocEvents_FeatureManagerTabActivatedNotifyEventHandler( 
   System.int CommandIndex,
   System.string CommandTabName
)
```

```

public delegate System.int DDrawingDocEvents_FeatureManagerTabActivatedNotifyEventHandler( 
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

If developing a C++ application, use [swDrawingFeatureManagerTabActivatedNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DDrawingDocEvents\_FeatureManagerTabActivatedNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_FeatureManagerTabActivatedNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
