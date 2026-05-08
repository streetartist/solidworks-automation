# ShowCurvatureCombs Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~ShowCurvatureCombs`

Gets or sets whether to show curvature combs.
Gets or sets whether to show curvature combs.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ShowCurvatureCombs As System.Boolean
```

```

Dim instance As ISketchSpline
Dim value As System.Boolean
 
instance.ShowCurvatureCombs = value
 
value = instance.ShowCurvatureCombs
```

```

System.bool ShowCurvatureCombs {get; set;}
```

```

property System.bool ShowCurvatureCombs {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to show curvature combs, false to not

Remarks

Use [ISketchManager::CurvatureScale](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CurvatureScale.md) to adjust the size of all of the curvature combs of this spline.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchSpline Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.md)  
[ISketchSpline Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline_members.md)  
[ISketchManager::CurvatureDensity Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CurvatureDensity.md)  
[ISketchSpline::AddCurvatureControl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~AddCurvatureControl.md)  
[ISketchHandle::CurvatureControlled Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~CurvatureControlled.md)  
[ISketchHandle::RadiusOfCurvature Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~RadiusOfCurvature.md)
