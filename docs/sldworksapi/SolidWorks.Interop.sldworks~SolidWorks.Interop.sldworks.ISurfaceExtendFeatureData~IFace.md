# IFace Property (ISurfaceExtendFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData~IFace`

Gets or sets the end-condition face for this surface-extend feature.
Gets or sets the end-condition face for this surface-extend feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property IFace As Face2
```

```

Dim instance As ISurfaceExtendFeatureData
Dim value As Face2
 
instance.IFace = value
 
value = instance.IFace
```

```

Face2 IFace {get; set;}
```

```

property Face2^ IFace {
   Face2^ get();
   void set (    Face2^ value);
}
```

#### Property Value

End-condition [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurfaceExtendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData.md)  
[ISurfaceExtendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData_members.md)  
[ISurfaceExtendFeatureData::Face Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData~Face.md)
