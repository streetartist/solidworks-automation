# InsertSketchForEdgeFlange Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSketchForEdgeFlange`

Inserts a profile sketch of an edge flange in this sheet metal part.
Inserts a profile sketch of an edge flange in this sheet metal part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertSketchForEdgeFlange( _
   ByVal FlangeEdge As System.Object, _
   ByVal DAngle As System.Double, _
   ByVal FlipDir As System.Boolean _
) As System.Object
```

```

Dim instance As IModelDoc2
Dim FlangeEdge As System.Object
Dim DAngle As System.Double
Dim FlipDir As System.Boolean
Dim value As System.Object
 
value = instance.InsertSketchForEdgeFlange(FlangeEdge, DAngle, FlipDir)
```

```

System.object InsertSketchForEdgeFlange( 
   System.object FlangeEdge,
   System.double DAngle,
   System.bool FlipDir
)
```

```

System.Object^ InsertSketchForEdgeFlange( 
   System.Object^ FlangeEdge,
   System.double DAngle,
   System.bool FlipDir
) 
```

#### Parameters

*FlangeEdge*
:   Edge with which to create an edge flange

*DAngle*
:   Angle of flange

*FlipDir*
:   True reverses the offset direction of the flange, false does not

#### Return Value

Sketch for the edge flange, returned as a [feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

After calling this method, you must create the profile for the flange on the appropriate plane. Then use [IFeatureManager::CreateDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateDefinition.md), [IEdgeFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.md), and [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.md) to create the edge flange.

Example

See the [IEdgeFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
