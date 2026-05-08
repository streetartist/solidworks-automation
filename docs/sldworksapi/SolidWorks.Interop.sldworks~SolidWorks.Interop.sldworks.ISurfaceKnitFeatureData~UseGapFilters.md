# UseGapFilters Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData~UseGapFilters`

Gets or sets whether to use gap filters for this Surface-Knit feature.
Gets or sets whether to use gap filters for this Surface-Knit feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UseGapFilters As System.Boolean
```

```

Dim instance As ISurfaceKnitFeatureData
Dim value As System.Boolean
 
instance.UseGapFilters = value
 
value = instance.UseGapFilters
```

```

System.bool UseGapFilters {get; set;}
```

```

property System.bool UseGapFilters {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to use gap filters, false to not

Remarks

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
[ISurfaceKnitFeatureData::KnitTolerance Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData~KnitTolerance.md)  
[ISurfaceKnitFeatureData::MaxValueForGapRange Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData~MaxValueForGapRange.md)  
[ISurfaceKnitFeatureData::MinValueForGapRange Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData~MinValueForGapRange.md)
