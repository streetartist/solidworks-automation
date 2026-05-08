# IInsertSketchForEdgeFlange Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IInsertSketchForEdgeFlange`

Inserts a sketch for IFeatureManager::InsertSheetMetalEdgeFlange2 in this sheet metal part.
Inserts a sketch for [IFeatureManager::InsertSheetMetalEdgeFlange2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSheetMetalEdgeFlange2.md) in this sheet metal part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IInsertSketchForEdgeFlange( _
   ByVal FlangeEdge As Edge, _
   ByVal DAngle As System.Double, _
   ByVal FlipDir As System.Boolean _
) As Feature
```

```

Dim instance As IModelDoc2
Dim FlangeEdge As Edge
Dim DAngle As System.Double
Dim FlipDir As System.Boolean
Dim value As Feature
 
value = instance.IInsertSketchForEdgeFlange(FlangeEdge, DAngle, FlipDir)
```

```

Feature IInsertSketchForEdgeFlange( 
   Edge FlangeEdge,
   System.double DAngle,
   System.bool FlipDir
)
```

```

Feature^ IInsertSketchForEdgeFlange( 
   Edge^ FlangeEdge,
   System.double DAngle,
   System.bool FlipDir
) 
```

#### Parameters

*FlangeEdge*
:   Edge to which to apply flange

*DAngle*
:   Angle of flange

*FlipDir*
:   True reverses the offset direction of the flange, false does not

#### Return Value

Sketch for the edge flagne, returned as a [feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

After calling this method, you must create the profile for the flange on the appropriate plane. After creating the profile, call [IFeatureManager::InsertSheetMetalEdgeFlange2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSheetMetalEdgeFlange2.md) to create the flange.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::InsertSheetMetalMiterFlange Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSheetMetalMiterFlange.md)
