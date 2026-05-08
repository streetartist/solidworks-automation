# VPeriodicity Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData~VPeriodicity`

Gets whether the surface is periodic in the V direction.
Gets whether the surface is periodic in the V direction.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property VPeriodicity As System.Boolean
```

```

Dim instance As IBSurfParamData
Dim value As System.Boolean
 
value = instance.VPeriodicity
```

```

System.bool VPeriodicity {get;}
```

```

property System.bool VPeriodicity {
   System.bool get();
}
```

#### Property Value

True if surface is periodic in V direction, false if not

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
[IBSurfParamData::UPeriodicity Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData~UPeriodicity.md)
