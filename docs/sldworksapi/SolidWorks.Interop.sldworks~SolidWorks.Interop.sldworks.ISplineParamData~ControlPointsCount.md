# ControlPointsCount Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~ControlPointsCount`

Gets and sets the number of control points in the spline.
Gets and sets the number of control points in the spline.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ControlPointsCount As System.Integer
```

```

Dim instance As ISplineParamData
Dim value As System.Integer
 
instance.ControlPointsCount = value
 
value = instance.ControlPointsCount
```

```

System.int ControlPointsCount {get; set;}
```

```

property System.int ControlPointsCount {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Number of control points

Remarks

The number of control points must be greater than or equal to the [order](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~Order.md) of the spline.

Example

[Get BCurve Spline Points (C#)](Get_BCurve_Spline_Points_Example_CSharp.htm)  
[Get BCurve Spline Points (VB.NET)](Get_BCurve_Spline_Points_Example_VBNET.htm)  
[Get BCurve Spline Points (VBA)](Get_BCurve_Spline_Points_Example_VB.htm)  
[Get Spline's Parameters (C#)](Get_Spline's_Parameters_Example_CSharp.htm)  
[Get Spline's Parameters (VB.NET)](Get_Spline's_Parameters_Example_VBNET.htm)  
[Get Spline's Parameters (VBA)](Get_Spline's_Parameters_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISplineParamData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData.md)  
[ISplineParamData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData_members.md)  
[ISplineParamData::GetControlPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~GetControlPoints.md)  
[ISplineParamData::IGetControlPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~IGetControlPoints.md)
