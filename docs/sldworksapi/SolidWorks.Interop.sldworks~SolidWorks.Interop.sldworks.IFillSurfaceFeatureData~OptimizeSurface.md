# OptimizeSurface Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~OptimizeSurface`

Gets or sets whether or not to optimize the patch.
Gets or sets whether or not to optimize the patch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property OptimizeSurface As System.Boolean
```

```

Dim instance As IFillSurfaceFeatureData
Dim value As System.Boolean
 
instance.OptimizeSurface = value
 
value = instance.OptimizeSurface
```

```

System.bool OptimizeSurface {get; set;}
```

```

property System.bool OptimizeSurface {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True for optimized patch, false for non-optimized patch

Remarks

You can only adjust the quality of the resolution of a patch when the patch is not optimized. See [IFillSurfaceFeatureData::ResolutionControl](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~ResolutionControl.md) for details.

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
