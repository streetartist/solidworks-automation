# Periodic Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~Periodic`

Gets and sets the periodicity of the spline.
Gets and sets the periodicity of the spline.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Periodic As System.Integer
```

```

Dim instance As ISplineParamData
Dim value As System.Integer
 
instance.Periodic = value
 
value = instance.Periodic
```

```

System.int Periodic {get; set;}
```

```

property System.int Periodic {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

0 if an open spline, 1 if a closed spline

Remarks

The [number of knots](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~KnotPointsCount.md) in the spline depends on the periodicity of the spline:

|  |  |
| --- | --- |
| **If this method returns...** | **Then the number of knots is...** |
| 1 | [ControlPointsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~ControlPointsCount.md) + 1 |
| 0 | [ControlPointsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~ControlPointsCount.md) + [Order](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~Order.md) |

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
