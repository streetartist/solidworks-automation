# KnitTolerance Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData~KnitTolerance`

Gets or sets the knit tolerance for this Surface-Knit feature.
Gets or sets the knit tolerance for this Surface-Knit feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property KnitTolerance As System.Double
```

```

Dim instance As ISurfaceKnitFeatureData
Dim value As System.Double
 
instance.KnitTolerance = value
 
value = instance.KnitTolerance
```

```

System.double KnitTolerance {get; set;}
```

```

property System.double KnitTolerance {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Knit tolerance (see **Remarks**)

Remarks

[ISurfaceKnitFeatureData::UseGapFilters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData~UseGapFilters.md) must be true for this property to have an effect.

A knit tolerance's:

- lower limit is 0.0001 mm
- upper limit is 0.1 mm

The knit tolerance value should be in a gap range such that:

([Minimum gap](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData~MinValueForGapRange.md)) <= (Knit tolerance) <= MIN(0.1 mm, [Maximum gap](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData~MaxValueForGapRange.md))

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
