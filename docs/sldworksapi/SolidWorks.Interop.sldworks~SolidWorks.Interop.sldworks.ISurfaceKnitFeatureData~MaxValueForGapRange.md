# MaxValueForGapRange Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData~MaxValueForGapRange`

Gets or sets the maximum gap range for this Surface-Knit feature.
Gets or sets the maximum gap range for this Surface-Knit feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property MaxValueForGapRange As System.Double
```

```

Dim instance As ISurfaceKnitFeatureData
Dim value As System.Double
 
instance.MaxValueForGapRange = value
 
value = instance.MaxValueForGapRange
```

```

System.double MaxValueForGapRange {get; set;}
```

```

property System.double MaxValueForGapRange {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Maximum gap range; valid values are from 0.01 mm to 1 mm

Remarks

[ISurfaceKnitFeatureData::UseGapFilters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData~UseGapFilters.md) must be true for this property to have an effect.

Maximum gap should be in the range of [ISurfaceKnitFeatureData::KnitTolerance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData~KnitTolerance.md) to 1 mm.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Example

[Create Knit Surface Feature (VB.NET)](Create_Surface_Knit_Feature_Example_VBNET.htm)  
[Create Knit Surface Feature (VBA)](Create_Surface_Knit_Feature_Example_VB6.htm)  
[Create Knit Surface Feature (C#)](Create_Surface_Knit_Feature_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurfaceKnitFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData.md)  
[ISurfaceKnitFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData_members.md)  
[ISurfaceKnitFeatureData::MinValueForGapRange Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData~MinValueForGapRange.md)
