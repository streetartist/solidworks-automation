# Sense Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveParamData~Sense`

Gets whether the curve and edge are in the same direction.
Gets whether the curve and edge are in the same direction.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Sense As System.Boolean
```

```

Dim instance As ICurveParamData
Dim value As System.Boolean
 
value = instance.Sense
```

```

System.bool Sense {get;}
```

```

property System.bool Sense {
   System.bool get();
}
```

#### Property Value

True if curve and edge are in the same direction, false if not

Remarks

If this method returns False, then the curve and edge are in opposite directions. In that case, [ICurveParamData::StartPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveParamData~StartPoint.md) corresponds to the end of the edge, [ICurveParamData::EndPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveParamData~EndPoint.md) corresponds to the start of the edge.

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
[ICurveParamData::UMaxValue Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveParamData~UMaxValue.md)  
[ICurveParamData::UMinValue Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveParamData~UMinValue.md)
