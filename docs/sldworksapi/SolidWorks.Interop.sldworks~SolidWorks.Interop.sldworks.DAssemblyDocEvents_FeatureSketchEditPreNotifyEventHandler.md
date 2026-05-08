# DAssemblyDocEvents_FeatureSketchEditPreNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_FeatureSketchEditPreNotifyEventHandler`

Pre-notifies the user program when the user edits the definition of a sketch.
Pre-notifies the user program when the user edits the definition of a sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DAssemblyDocEvents_FeatureSketchEditPreNotifyEventHandler( _
   ByVal EditFeature As System.Object, _
   ByVal featureSketch As System.Object _
) As System.Integer
```

```

Dim instance As New DAssemblyDocEvents_FeatureSketchEditPreNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DAssemblyDocEvents_FeatureSketchEditPreNotifyEventHandler( 
   System.object EditFeature,
   System.object featureSketch
)
```

```

public delegate System.int DAssemblyDocEvents_FeatureSketchEditPreNotifyEventHandler( 
   System.Object^ EditFeature,
   System.Object^ featureSketch
)
```

#### Parameters

*EditFeature*
:   [Feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) that contains the sketch

*featureSketch*
:   Edited [sketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)

Remarks

If developing a C++ application, use [swAssemblyFeatureSketchEditPreNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

If the sketch is not part of a feature, then the editFeature object is NULL.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DAssemblyDocEvents\_FeatureSketchEditPreNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_FeatureSketchEditPreNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
