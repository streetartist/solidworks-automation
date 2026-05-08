# GetEdgeChamferDistance Method (IChamferFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~GetEdgeChamferDistance`

Gets the edge chamfer distance on either side of the edge.
Gets the edge chamfer distance on either side of the edge.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetEdgeChamferDistance( _
   ByVal Side As System.Integer _
) As System.Double
```

```

Dim instance As IChamferFeatureData2
Dim Side As System.Integer
Dim value As System.Double
 
value = instance.GetEdgeChamferDistance(Side)
```

```

System.double GetEdgeChamferDistance( 
   System.int Side
)
```

```

System.double GetEdgeChamferDistance( 
   System.int Side
) 
```

#### Parameters

*Side*
:   Feature direction (see **Remarks**)

#### Return Value

Edge chamfer distance

Remarks

Set the Side parameter to 0 or 1. For angle-distance chamfers, set side to 0.

Example

[Get Edge Chamfer Distances (C#)](Get_Edge_Chamfer_Distances_Example_CSharp.htm)  
[Get Edge Chamfer Distances (VB.NET)](Get_Edge_Chamfer_Distances_Example_VBNET.htm)  
[Get Edge Chamfer Distances (VBA)](Get_Edge_Chamfer_Distances_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IChamferFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2.md)  
[IChamferFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2_members.md)  
[IChamferFeatureData2::SetEdgeChamferDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~SetEdgeChamferDistance.md)
