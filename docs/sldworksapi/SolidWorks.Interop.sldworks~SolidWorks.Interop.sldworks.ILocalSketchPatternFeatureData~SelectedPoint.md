# SelectedPoint Property (ILocalSketchPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData~SelectedPoint`

Gets or sets the selected point for this sketch-driven component pattern feature.
Gets or sets the selected point for this sketch-driven component pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SelectedPoint As SketchPoint
```

```

Dim instance As ILocalSketchPatternFeatureData
Dim value As SketchPoint
 
instance.SelectedPoint = value
 
value = instance.SelectedPoint
```

```

SketchPoint SelectedPoint {get; set;}
```

```

property SketchPoint^ SelectedPoint {
   SketchPoint^ get();
   void set (    SketchPoint^ value);
}
```

#### Property Value

[Point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md)

Remarks

This property is valid only if [ILocalSketchPatternFeatureData::ReferencePoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData~ReferencePoint.md) is set to [swLocalSketchPatternReferencePoint\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLocalSketchPatternReferencePoint_e.html).swLocalSketchPatternSelectedPoint.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILocalSketchPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData.md)  
[ILocalSketchPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData_members.md)  
[ILocalSketchPatternFeatureData::GetReferencePointType Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData~GetReferencePointType.md)
