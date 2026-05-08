# CurvatureScale Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CurvatureScale`

Gets or sets the scaling factor by which to adjust the size of the curvature combs for this spline.
Gets or sets the scaling factor by which to adjust the size of the curvature combs for this spline.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CurvatureScale As System.Double
```

```

Dim instance As ISketchManager
Dim value As System.Double
 
instance.CurvatureScale = value
 
value = instance.CurvatureScale
```

```

System.double CurvatureScale {get; set;}
```

```

property System.double CurvatureScale {
   System.double get();
   void set (    System.double value);
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
[ISketchSpline::ShowCurvatureCombs Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~ShowCurvatureCombs.md)  
[ISketchManager::CurvatureDensity Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CurvatureDensity.md)
