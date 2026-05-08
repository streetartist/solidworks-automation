# DAssemblyDocEvents_FeatureManagerFilterStringChangeNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_FeatureManagerFilterStringChangeNotifyEventHandler`

Fired when text is typed in the FeatureManager design tree filter or IModelDocExtension::FeatureManagerFilterString is called.
Fired when text is typed in the FeatureManager design tree filter or [IModelDocExtension::FeatureManagerFilterString](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~FeatureManagerFilterString.md) is called.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DAssemblyDocEvents_FeatureManagerFilterStringChangeNotifyEventHandler( _
   ByVal FilterString As System.String _
) As System.Integer
```

```

Dim instance As New DAssemblyDocEvents_FeatureManagerFilterStringChangeNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DAssemblyDocEvents_FeatureManagerFilterStringChangeNotifyEventHandler( 
   System.string FilterString
)
```

```

public delegate System.int DAssemblyDocEvents_FeatureManagerFilterStringChangeNotifyEventHandler( 
   System.String^ FilterString
)
```

#### Parameters

*FilterString*
:   String

Remarks

If developing a C++ application, use [swAssemblyFeatureManagerFilterStringChangeNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DAssemblyDocEvents\_FeatureManagerFilterStringChangeNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_FeatureManagerFilterStringChangeNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[DPartDocEvents\_FeatureManagerTreeRebuildNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_FeatureManagerTreeRebuildNotifyEventHandler.md)
