# ResetAllHandles Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~ResetAllHandles`

Resets all handles to their initial state.
Resets all [handles](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle.md) to their initial state.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ResetAllHandles() 
```

```

Dim instance As ISketchSpline
 
instance.ResetAllHandles()
```

```

void ResetAllHandles()
```

```

void ResetAllHandles(); 
```

#### Return Value

Use [SplineHandle::Reset](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~Reset.md) to reset one handle to its initial state.

Example

[Set Spline Tangency and Curvature Controls (VBA)](Set_Spline_Tangency_and_Curvature_Controls_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchSpline Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.md)  
[ISketchSpline Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline_members.md)  
[ISketchSpline::GetSplineHandleCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetSplineHandleCount.md)  
[ISketchSpline::GetSplineHandles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetSplineHandles.md)  
[ISketchSpline::IGetSplineHandles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~IGetSplineHandles.md)  
[ISketchSpline::ShowSplineHandles Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~ShowSplineHandles.md)
