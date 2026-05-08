# AddTangencyControl Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~AddTangencyControl`

Adds a new handle to help control the tangency of this spline.
Adds a new handle to help control the tangency of this spline.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddTangencyControl( _
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
 
value = instance.AddTangencyControl(XPos, YPos, ZPos)
```

```

SplineHandle AddTangencyControl( 
   System.double XPos,
   System.double YPos,
   System.double ZPos
)
```

```

SplineHandle^ AddTangencyControl( 
   System.double XPos,
   System.double YPos,
   System.double ZPos
) 
```

#### Parameters

*XPos*
:   x coordinate of the new handle

*YPos*
:   y coordinate of the new handle

*ZPos*
:   z coordinate of the new handle

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
[ISketchSpline::AddCurvatureControl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~AddCurvatureControl.md)  
[ISketchSpline::GetSplineHandleCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetSplineHandleCount.md)  
[ISketchSpline::GetSplineHandles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetSplineHandles.md)  
[ISketchSpline::IGetSplineHandles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~IGetSplineHandles.md)  
[ISketchSpline::ResetAllHandles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~ResetAllHandles.md)  
[ISketchSpline::ShowSplineHandles Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~ShowSplineHandles.md)  
[ISplineHandle::TangentDriving Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~TangentDriving.md)  
[ISplineHandle::TangentMagnitude Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~TangentMagnitude.md)  
[ISplineHandle::TangentPolarDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~TangentPolarDirection.md)  
[ISplineHandle::TangentRadialDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~TangentRadialDirection.md)
