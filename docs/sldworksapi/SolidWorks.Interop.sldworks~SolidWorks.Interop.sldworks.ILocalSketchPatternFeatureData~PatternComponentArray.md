# PatternComponentArray Property (ILocalSketchPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData~PatternComponentArray`

Gets or sets the components to pattern for this sketch-driven component pattern feature.
Gets or sets the components to pattern for this sketch-driven component pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PatternComponentArray As System.Object
```

```

Dim instance As ILocalSketchPatternFeatureData
Dim value As System.Object
 
instance.PatternComponentArray = value
 
value = instance.PatternComponentArray
```

```

System.object PatternComponentArray {get; set;}
```

```

property System.Object^ PatternComponentArray {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of [components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILocalSketchPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData.md)  
[ILocalSketchPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData_members.md)  
[ILocalSketchPatternFeatureData::GetPatternComponentCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData~GetPatternComponentCount.md)
