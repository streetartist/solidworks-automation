# ShowSplineHandles Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~ShowSplineHandles`

Gets or sets whether to show the handles for this spline.
Gets or sets whether to show the [handles](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle.md) for this spline.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ShowSplineHandles As System.Boolean
```

```

Dim instance As ISketchSpline
Dim value As System.Boolean
 
instance.ShowSplineHandles = value
 
value = instance.ShowSplineHandles
```

```

System.bool ShowSplineHandles {get; set;}
```

```

property System.bool ShowSplineHandles {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to show spline handles, false to not

Remarks

If setting this property to True, then use [IModelDoc2::WindowRedraw](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~WindowRedraw.md) after to see the spline handles.

Example

[Get and Set Spline Properties (VBA)](Get_and_Set_Spline_Properties_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchSpline Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.md)  
[ISketchSpline Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline_members.md)  
[ISketchSpline::GetSplineHandleCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetSplineHandleCount.md)  
[ISketchSpline::GetSplineHandles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetSplineHandles.md)  
[ISketchSpline::IGetSplineHandles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~IGetSplineHandles.md)  
[ISketchSpline::ResetAllHandles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~ResetAllHandles.md)
