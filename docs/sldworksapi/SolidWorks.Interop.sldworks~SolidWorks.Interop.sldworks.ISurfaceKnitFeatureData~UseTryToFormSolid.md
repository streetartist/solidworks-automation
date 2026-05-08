# UseTryToFormSolid Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData~UseTryToFormSolid`

Gets or sets whether to try to form a solid body when creating the Surface-Knit feature.
Gets or sets whether to try to form a solid body when creating the Surface-Knit feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UseTryToFormSolid As System.Boolean
```

```

Dim instance As ISurfaceKnitFeatureData
Dim value As System.Boolean
 
instance.UseTryToFormSolid = value
 
value = instance.UseTryToFormSolid
```

```

System.bool UseTryToFormSolid {get; set;}
```

```

property System.bool UseTryToFormSolid {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to true to form a solid body, false to not

Remarks

If [ISurfaceKnitFeatureData::UseGapFilters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData~UseGapFilters.md) is true, then this property is automatically enabled or disabled depending on whether a solid body can be created from the input bodies.

If you set this property to true, then [knit tolerance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData~KnitTolerance.md) is automatically updated so that the Surface-Knit feature can be created as a solid body.

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
