# AddCurvatureControl Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~AddCurvatureControl`

Adds a curvature control pointer to this spline.
Adds a curvature control pointer to this spline.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddCurvatureControl( _
   ByVal XPos As System.Double, _
   ByVal YPos As System.Double, _
   ByVal ZPos As System.Double _
) As SplineHandle
```

```

Dim instance As ISketchSpline
Dim XPos As System.Double
Dim YPos As System.Double
Dim ZPos As System.Double
Dim value As SplineHandle
 
value = instance.AddCurvatureControl(XPos, YPos, ZPos)
```

```

SplineHandle AddCurvatureControl( 
   System.double XPos,
   System.double YPos,
   System.double ZPos
)
```

```

SplineHandle^ AddCurvatureControl( 
   System.double XPos,
   System.double YPos,
   System.double ZPos
) 
```

#### Parameters

*XPos*
:   x coordinate for the pointer

*YPos*
:   y coordinate for the pointer

*ZPos*
:   z coordinate for the pointer

#### Return Value

[Spline handle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle.md)

Example

[Set Spline Tangency and Curvature Controls (VBA)](Set_Spline_Tangency_and_Curvature_Controls_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchSpline Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.md)  
[ISketchSpline Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline_members.md)  
[ISketchSpline::AddTangencyControl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~AddTangencyControl.md)  
[ISketchSpline::GetSplineHandleCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetSplineHandleCount.md)  
[ISketchSpline::GetSplineHandles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetSplineHandles.md)  
[ISketchSpline::IGetSplineHandles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~IGetSplineHandles.md)  
[ISketchSpline::ResetAllHandles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~ResetAllHandles.md)  
[ISketchSpline::ShowCurvatureCombs Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~ShowCurvatureCombs.md)  
[ISketchSpline::ShowSplineHandles Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~ShowSplineHandles.md)  
[ISplineHandle::Curvature Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~Curvature.md)  
[ISplineHandle::CurvatureControlled Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~CurvatureControlled.md)  
[ISplineHandle::RadiusOfCurvature Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~RadiusOfCurvature.md)
