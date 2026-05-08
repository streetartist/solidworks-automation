# UKnots Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData~UKnots`

Gets the knot vector in the U direction.
Gets the knot vector in the U direction.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property UKnots As System.Object
```

```

Dim instance As IBSurfParamData
Dim value As System.Object
 
value = instance.UKnots
```

```

System.object UKnots {get;}
```

```

property System.Object^ UKnots {
   System.Object^ get();
}
```

#### Property Value

Array of knot doubles

Remarks

Returned array contains ([control-point column count](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData~ControlPointColumnCount.md) + [U order](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData~UOrder.md)) knot values. If the surface is periodic in the U direction, then data is converted and returned in a non-periodic form with additional knots added to the surface ends.

Example

[Get B-Spline Surface Parameterization Data (C#)](Get_B-Spline_Surface_Parameterization_Data_Example_CSharp.htm)  
[Get B-Spline Surface Parameterization Data (VB.NET)](Get_B-Spline_Surface_Parameterization_Data_Example_VBNET.htm)  
[Get B-Spline Surface Parameterization Data (VBA)](Get_B-Spline_Surface_Parameterization_Data_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBSurfParamData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData.md)  
[IBSurfParamData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData_members.md)  
[IBSurfParamData::VKnots Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData~VKnots.md)
