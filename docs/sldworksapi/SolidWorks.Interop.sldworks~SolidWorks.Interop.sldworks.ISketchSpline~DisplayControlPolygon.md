# DisplayControlPolygon Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~DisplayControlPolygon`

Gets or sets whether to add a control polygon to this spline.
Gets or sets whether to add a control polygon to this spline.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DisplayControlPolygon As System.Boolean
```

```

Dim instance As ISketchSpline
Dim value As System.Boolean
 
instance.DisplayControlPolygon = value
 
value = instance.DisplayControlPolygon
```

```

System.bool DisplayControlPolygon {get; set;}
```

```

property System.bool DisplayControlPolygon {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to add a control polygon, false to not

Remarks

To add a control polygon, set [ISldWorks::SetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceToggle.md) swSketchShowSplineControlPolygon to True.

If the spline is not smooth after dragging a node of the control polygon, use [ISketchSpline::RelaxSpline](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~RelaxSpline.md) to smoothen its shape.

Example

[Get and Set Spline Properties (VBA)](Get_and_Set_Spline_Properties_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchSpline Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.md)  
[ISketchSpline Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline_members.md)
