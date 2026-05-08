# StartPoint Property (ICurveParamData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveParamData~StartPoint`

Gets the x, y, and z coordinates for the start point of the curve.
Gets the x, y, and z coordinates for the start point of the curve.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property StartPoint As System.Object
```

```

Dim instance As ICurveParamData
Dim value As System.Object
 
value = instance.StartPoint
```

```

System.object StartPoint {get;}
```

```

property System.Object^ StartPoint {
   System.Object^ get();
}
```

#### Property Value

Array of three doubles

Remarks

If [ICurveParamData::Sense](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveParamData~Sense.md) returns false, then the curve and edge are in opposite directions. In that case, start point corresponds to the end of the edge, and [ICurveParamData::EndPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveParamData~EndPoint.md) corresponds to the start of the edge.

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
