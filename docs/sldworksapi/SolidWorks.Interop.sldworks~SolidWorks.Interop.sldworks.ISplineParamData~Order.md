# Order Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~Order`

Gets and sets the number of nearby control points that influence any given point on the curve.
Gets and sets the number of nearby control points that influence any given point on the curve.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Order As System.Integer
```

```

Dim instance As ISplineParamData
Dim value As System.Integer
 
instance.Order = value
 
value = instance.Order
```

```

System.int Order {get; set;}
```

```

property System.int Order {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

The degree of the spline polynomial + 1

Remarks

|  |  |  |
| --- | --- | --- |
| **A spline of order...** | **is represented by a ...** | **of degree...** |
| 2 | linear polynomial | 1 |
| 3 | quadratic polynomial | 2 |
| 4 | cubic polynomial | 3 |

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
[ISplineParamData::GetSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~GetSegments.md)  
[ISplineParamData::IGetSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~IGetSegments.md)
