# DPartDocEvents_FeatureEditPreNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_FeatureEditPreNotifyEventHandler`

Pre-notifies the user program when the user edits the definition of a selected feature.
Pre-notifies the user program when the user edits the definition of a selected feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DPartDocEvents_FeatureEditPreNotifyEventHandler( _
   ByVal EditFeature As System.Object _
) As System.Integer
```

```

Dim instance As New DPartDocEvents_FeatureEditPreNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DPartDocEvents_FeatureEditPreNotifyEventHandler( 
   System.object EditFeature
)
```

```

public delegate System.int DPartDocEvents_FeatureEditPreNotifyEventHandler( 
   System.Object^ EditFeature
)
```

#### Parameters

*EditFeature*
:   Edited [feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

The interface pointer is passed as an IDispatch. You then have to do a QueryInterface for the IFeature interface. Next, call [IFeature::GetTypeName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetTypeName.md), and then call [IFeature::GetSpecificFeature2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetSpecificFeature2.md).

If developing a C++ application, use [swPartFeatureEditPreNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this event.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DPartDocEvents\_FeatureEditPreNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_FeatureEditPreNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
