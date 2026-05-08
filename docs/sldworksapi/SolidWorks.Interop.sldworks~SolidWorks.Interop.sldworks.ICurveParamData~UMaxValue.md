# UMaxValue Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveParamData~UMaxValue`

Gets the maximum U parameter value.
Gets the maximum U parameter value.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property UMaxValue As System.Double
```

```

Dim instance As ICurveParamData
Dim value As System.Double
 
value = instance.UMaxValue
```

```

System.double UMaxValue {get;}
```

```

property System.double UMaxValue {
   System.double get();
}
```

#### Property Value

Maximum U parameter value

Remarks

The minimum U parameter must always be smaller than the maximum U parameter.

If the curve and edge are in opposite directions ([ICurveParamData::Sense](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveParamData~Sense.md) returns false) and the minimum U parameter is larger than the maximum U parameter, then the parameters are in negative parameter space. For example, if ICurveParamData::Sense is false, minimum U parameter is 10, and maximum U parameter is 5, then [ICurveParamData::UMinValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveParamData~UMinValue.md) = -10 and ICurveParamData::UMaxValue = -5. To normalize the values in positive parameter space, swap the two U parameter values and then negate them, so that the values of the minimum U parameter is 5 and the maximum U parameter is 10.

If the curve is closed and the curve starts and ends at the same point, then ICurveParamData::UMinValue and ICurveParamData::UMaxValue are a period apart.

Example

[Get Edge Curve Parameterization (C#)](Get_Edge_Curve_Parameterization_Example_CSharp.htm)  
[Get Edge Curve Parameterization (VB.NET)](Get_Edge_Curve_Parameterization_Example_VBNET.htm)  
[Get Edge Curve Parameterization (VBA)](Get_Edge_Curve_Parameterization_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICurveParamData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveParamData.md)  
[ICurveParamData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveParamData_members.md)
