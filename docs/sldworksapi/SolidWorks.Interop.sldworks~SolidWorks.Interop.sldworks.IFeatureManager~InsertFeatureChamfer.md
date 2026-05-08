# InsertFeatureChamfer Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertFeatureChamfer`

Inserts a chamfer.
Inserts a chamfer.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertFeatureChamfer( _
   ByVal Options As System.Integer, _
   ByVal ChamferType As System.Integer, _
   ByVal Width As System.Double, _
   ByVal Angle As System.Double, _
   ByVal OtherDist As System.Double, _
   ByVal VertexChamDist1 As System.Double, _
   ByVal VertexChamDist2 As System.Double, _
   ByVal VertexChamDist3 As System.Double _
) As Feature
```

```

Dim instance As IFeatureManager
Dim Options As System.Integer
Dim ChamferType As System.Integer
Dim Width As System.Double
Dim Angle As System.Double
Dim OtherDist As System.Double
Dim VertexChamDist1 As System.Double
Dim VertexChamDist2 As System.Double
Dim VertexChamDist3 As System.Double
Dim value As Feature
 
value = instance.InsertFeatureChamfer(Options, ChamferType, Width, Angle, OtherDist, VertexChamDist1, VertexChamDist2, VertexChamDist3)
```

```

Feature InsertFeatureChamfer( 
   System.int Options,
   System.int ChamferType,
   System.double Width,
   System.double Angle,
   System.double OtherDist,
   System.double VertexChamDist1,
   System.double VertexChamDist2,
   System.double VertexChamDist3
)
```

```

Feature^ InsertFeatureChamfer( 
   System.int Options,
   System.int ChamferType,
   System.double Width,
   System.double Angle,
   System.double OtherDist,
   System.double VertexChamDist1,
   System.double VertexChamDist2,
   System.double VertexChamDist3
) 
```

#### Parameters

*Options*
:   Options as defined by [swFeatureChamferOption\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureChamferOption_e.html)

*ChamferType*
:   Chamfer type as defined by [swChamferType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swChamferType_e.html)

*Width*
:   If ChamferType is swChamferAngleDistance, then specify width of chamfer

*Angle*
:   If ChamferType is swChamferAngleDistance, then specify the angle of the chamfer

*OtherDist*
:   If ChamferType is swChamferEqualDistance, then you can specify a single value so that all distances are equal

*VertexChamDist1*
:   If ChamferType is swChamferDistanceDistance or swChamferVertex, then specify a value for the distance on first side

*VertexChamDist2*
:   If ChamferType is swChamferDistanceDistance or swChamferVertex, then specify a value for the distance on second side

*VertexChamDist3*
:   If ChamferType is swChamferVertex, then specify a value for the distance on third side

#### Return Value

Pointer to the [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) object

Remarks

Both swChamferType\_e.swChamferAngleDistance and swChamferType\_e.swChamferDistanceDistance are edge chamfers. This means that all measurements are from edges. An angle-distance chamfer requires an angle and a distance; a distance-distance chamfer requires two distances, one for each side of the chamfered edge.

A swChamferType\_e.swChamferVertex chamfer only works on a vertex with three adjacent edges of the same convexity. A vertex chamfer requires three distances along three adjacent edges. For non-linear edges, this value is an arc length value; it is not a chordal value. See [IVertex::EnumEdgesOriented](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~EnumEdgesOriented.md) to determine the edge order used by this method.

Example

See the [IChamferFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)
