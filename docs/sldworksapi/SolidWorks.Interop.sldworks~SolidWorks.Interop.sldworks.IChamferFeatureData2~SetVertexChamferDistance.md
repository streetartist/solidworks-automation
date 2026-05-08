# SetVertexChamferDistance Method (IChamferFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~SetVertexChamferDistance`

Sets the vertex chamfer distance.
Sets the vertex chamfer distance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetVertexChamferDistance( _
   ByVal Side As System.Integer, _
   ByVal Distance As System.Double _
) 
```

```

Dim instance As IChamferFeatureData2
Dim Side As System.Integer
Dim Distance As System.Double
 
instance.SetVertexChamferDistance(Side, Distance)
```

```

void SetVertexChamferDistance( 
   System.int Side,
   System.double Distance
)
```

```

void SetVertexChamferDistance( 
   System.int Side,
   System.double Distance
) 
```

#### Parameters

*Side*
:   Feature direction (see **Remarks**)

*Distance*
:   Vertex chamfer distance

Remarks

There are three edges of a vertex. Set the Side parameter to 0, 1, or 2 to specify the edge. The Side parameter is relevant only for vertex-type chamfers.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IChamferFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2.md)  
[IChamferFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2_members.md)  
[IChamferFeatureData2::GetVertexChamferDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~GetVertexChamferDistance.md)
