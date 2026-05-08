# SurfaceForCut Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData~SurfaceForCut`

Gets or sets the surface to use to cut the solid bodies.
Gets or sets the surface to use to cut the solid bodies.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SurfaceForCut As System.Object
```

```

Dim instance As ISurfaceCutFeatureData
Dim value As System.Object
 
instance.SurfaceForCut = value
 
value = instance.SurfaceForCut
```

```

System.object SurfaceForCut {get; set;}
```

```

property System.Object^ SurfaceForCut {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

[Surface feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) to use to cut the solid bodies

Remarks

To access this interface, you must declare it as SurfCutFeatureData or ISurfCutFeatureData.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurfaceCutFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData.md)  
[ISurfaceCutFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData_members.md)
