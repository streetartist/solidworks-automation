# UPeriodicity Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData~UPeriodicity`

Gets whether the surface is periodic in the U direction.
Gets whether the surface is periodic in the U direction.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property UPeriodicity As System.Boolean
```

```

Dim instance As IBSurfParamData
Dim value As System.Boolean
 
value = instance.UPeriodicity
```

```

System.bool UPeriodicity {get;}
```

```

property System.bool UPeriodicity {
   System.bool get();
}
```

#### Property Value

True if surface is periodic in U direction, false if not

Remarks

If a surface is periodic in one direction (that is, cylinder, cone, torus (apple and lemon shapes), spheres), then U is the periodic direction.

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
[IBSurfParamData::VPeriodicity Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData~VPeriodicity.md)
