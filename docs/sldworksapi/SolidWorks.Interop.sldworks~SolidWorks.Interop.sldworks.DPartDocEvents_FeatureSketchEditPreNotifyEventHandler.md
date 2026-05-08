# DPartDocEvents_FeatureSketchEditPreNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_FeatureSketchEditPreNotifyEventHandler`

Pre-notifies the user program when the user edits the definition of a sketch.
Pre-notifies the user program when the user edits the definition of a sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DPartDocEvents_FeatureSketchEditPreNotifyEventHandler( _
   ByVal EditFeature As System.Object, _
   ByVal featureSketch As System.Object _
) As System.Integer
```

```

Dim instance As New DPartDocEvents_FeatureSketchEditPreNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DPartDocEvents_FeatureSketchEditPreNotifyEventHandler( 
   System.object EditFeature,
   System.object featureSketch
)
```

```

public delegate System.int DPartDocEvents_FeatureSketchEditPreNotifyEventHandler( 
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

The interface pointer is passed as an IDispatch. You then have to do a QueryInterface for the ISketch interface. If the sketch is not part of a feature, then EditFeature is NULL.

If developing a C++ application, use [swPartFeatureSketchEditPreNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DPartDocEvents\_FeatureSketchEditPreNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_FeatureSketchEditPreNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
