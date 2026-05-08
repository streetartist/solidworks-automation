# ResolutionControl Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~ResolutionControl`

Gets and sets the quality of the resolution of the fill-surface feature.
Gets and sets the quality of the resolution of the fill-surface feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ResolutionControl As System.Integer
```

```

Dim instance As IFillSurfaceFeatureData
Dim value As System.Integer
 
instance.ResolutionControl = value
 
value = instance.ResolutionControl
```

```

System.int ResolutionControl {get; set;}
```

```

property System.int ResolutionControl {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Valid values: 1, 2, and 3 (see **Remarks**)

Remarks

Adjusting the quality of the resolution is only available for patches that are not optimized. See [IFillSurfaceFeatureData::OptimizeSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~OptimizeSurface.md) for details.

Specifying a higher value:

- Increases the number of patches defining the surface
- Improves the quality of the surface profile
- Increases processing time
- Increases the size of the file

Example

[Insert Fill-surface Feature (C#)](Insert_Fill-surface_Feature_Example_CSharp.htm)  
[Insert Fill-surface Feature (VB.NET)](Insert_Fill-surface_Feature_Example_VBNET.htm)  
[Insert Fill-surface Feature (VBA)](Insert_Fill-surface_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFillSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData.md)  
[IFillSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData_members.md)
