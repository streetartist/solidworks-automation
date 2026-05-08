# ReferencePoint Property (ILocalSketchPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData~ReferencePoint`

Gets or sets the type of reference point for this sketch-driven component pattern feature.
Gets or sets the type of reference point for this sketch-driven component pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ReferencePoint As System.Integer
```

```

Dim instance As ILocalSketchPatternFeatureData
Dim value As System.Integer
 
instance.ReferencePoint = value
 
value = instance.ReferencePoint
```

```

System.int ReferencePoint {get; set;}
```

```

property System.int ReferencePoint {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Type of reference point as defined in [swLocalSketchPatternReferencePoint\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLocalSketchPatternReferencePoint_e.html)

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

Example

[Create Local Sketch-driven Pattern (C#)](Create_Local_Sketch-driven_Pattern_Example_CSharp.htm)  
[Create Local Sketch-driven Pattern (VB.NET)](Create_Local_Sketch-driven_Pattern_Example_VBNET.htm)  
[Create Local Sketch-driven Pattern (VBA)](Create_Local_Sketch-driven_Pattern_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILocalSketchPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData.md)  
[ILocalSketchPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData_members.md)  
[ILocalSketchPatternFeatureData::GetReferencePointType Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData~GetReferencePointType.md)  
[ILocalSketchPatternFeatureData::SelectedPoint Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData~SelectedPoint.md)
