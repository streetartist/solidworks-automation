# D1Curves Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~D1Curves`

Gets or sets the curves for Direction 1 for this boundary feature.
Gets or sets the curves for Direction 1 for this boundary feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property D1Curves As System.Object
```

```

Dim instance As IBoundaryBossFeatureData
Dim value As System.Object
 
instance.D1Curves = value
 
value = instance.D1Curves
```

```

System.object D1Curves {get; set;}
```

```

property System.Object^ D1Curves {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of curves for Direction 1 (see **Remarks**)

Remarks

[Sketch curves](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md), [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md), or [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) can be used to create the boundary feature. Boundary features are

created based on the order of the curve selection.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Example

[Insert Boundary Feature (C#)](Insert_Boundary_Feature_Example_CSharp.htm)  
[Insert Boundary Feature (VB.NET)](Insert_Boundary_Feature_Example_VBNET.htm)  
[Insert Boundary Feature (VBA)](Insert_Boundary_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBoundaryBossFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData.md)  
[IBoundaryBossFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData_members.md)  
[IBoundaryBossFeatureData::D1CurveInfluence Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~D1CurveInfluence.md)  
[IBoundaryBossFeatureData::D2CurveInfluence Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~D2CurveInfluence.md)  
[IBoundaryBossFeatureData::D2Curves Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~D2Curves.md)  
[IBoundaryBossFeatureData::TrimByD1 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~TrimByD1.md)  
[IBoundaryBossFeatureData::GetTangentInfluence Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetTangentInfluence.md)  
[IBoundaryBossFeatureData::SetTangentInfluence Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~SetTangentInfluence.md)
