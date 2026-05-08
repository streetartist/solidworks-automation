# Color Property (ISplineParamData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~Color`

Gets the color used to draw the spline.
Gets the color used to draw the spline.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Color As System.Integer
```

```

Dim instance As ISplineParamData
Dim value As System.Integer
 
value = instance.Color
```

```

System.int Color {get;}
```

```

property System.int Color {
   System.int get();
}
```

#### Property Value

COLORREF value; -1 if not defined

Example

[Get BCurve Spline Points (C#)](Get_BCurve_Spline_Points_Example_CSharp.htm)  
[Get BCurve Spline Points (VB.NET)](Get_BCurve_Spline_Points_Example_VBNET.htm)  
[Get BCurve Spline Points (VBA)](Get_BCurve_Spline_Points_Example_VB.htm)  
[Get P-Spline Parameterization Data (C#)](Get_P-Spline_Parameterization_Data_Example_CSharp.htm)  
[Get P-Spline Parameterization Data (VB.NET)](Get_P-Spline_Parameterization_Data_Example_VBNET.htm)  
[Get P-Spline Parameterization Data (VBA)](Get_P-Spline_Parameterization_Data_Example_VB.htm)  
[Get Spline's Parameters (C#)](Get_Spline's_Parameters_Example_CSharp.htm)  
[Get Spline's Parameters (VB.NET)](Get_Spline's_Parameters_Example_VBNET.htm)  
[Get Spline's Parameters (VBA)](Get_Spline's_Parameters_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISplineParamData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData.md)  
[ISplineParamData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData_members.md)  
[ISplineParamData::LayerOverride Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~LayerOverride.md)  
[ISplineParamData::LineStyle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~LineStyle.md)
