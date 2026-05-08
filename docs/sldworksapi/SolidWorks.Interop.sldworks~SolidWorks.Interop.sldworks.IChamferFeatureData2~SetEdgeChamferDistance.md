# SetEdgeChamferDistance Method (IChamferFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~SetEdgeChamferDistance`

Sets the edge chamfer distance on either side of the edge.
Sets the edge chamfer distance on either side of the edge.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetEdgeChamferDistance( _
   ByVal Side As System.Integer, _
   ByVal Distance As System.Double _
) 
```

```

Dim instance As IChamferFeatureData2
Dim Side As System.Integer
Dim Distance As System.Double
 
instance.SetEdgeChamferDistance(Side, Distance)
```

```

void SetEdgeChamferDistance( 
   System.int Side,
   System.double Distance
)
```

```

void SetEdgeChamferDistance( 
   System.int Side,
   System.double Distance
) 
```

#### Parameters

*Side*
:   Feature direction (see **Remarks**)

*Distance*
:   Edge chamfer distance

Remarks

Set the Side parameter to 0 or 1. For angle-distance chamfers, set side to 0.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IChamferFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2.md)  
[IChamferFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2_members.md)  
[IChamferFeatureData2::GetEdgeChamferDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~GetEdgeChamferDistance.md)
