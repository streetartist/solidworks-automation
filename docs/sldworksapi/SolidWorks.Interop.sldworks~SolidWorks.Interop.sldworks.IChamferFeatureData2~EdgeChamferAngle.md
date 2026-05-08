# EdgeChamferAngle Property (IChamferFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~EdgeChamferAngle`

Gets or sets the angle on the edge of the chamfer feature.
Gets or sets the angle on the edge of the chamfer feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property EdgeChamferAngle As System.Double
```

```

Dim instance As IChamferFeatureData2
Dim value As System.Double
 
instance.EdgeChamferAngle = value
 
value = instance.EdgeChamferAngle
```

```

System.double EdgeChamferAngle {get; set;}
```

```

property System.double EdgeChamferAngle {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Chamfer angle of the edge of the chamfer feature

Remarks

This method is relevant only for an angle-distance type of chamfer.

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
[IChamferFeatureData2::Type Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~Type.md)
