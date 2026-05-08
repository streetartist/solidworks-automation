# CurvatureDensity Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CurvatureDensity`

Gets or sets the scaling factor by which to adjust the density of the curvature combs for this spline.
Gets or sets the scaling factor by which to adjust the density of the curvature combs for this spline.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CurvatureDensity As System.Integer
```

```

Dim instance As ISketchManager
Dim value As System.Integer
 
instance.CurvatureDensity = value
 
value = instance.CurvatureDensity
```

```

System.int CurvatureDensity {get; set;}
```

```

property System.int CurvatureDensity {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Curvature density of the curvature combs for this spline; valid values from 0 - 100

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)  
[ISketchManager::CurvatureScale Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CurvatureScale.md)  
[ISketchSpline::ShowCurvatureCombs Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~ShowCurvatureCombs.md)
