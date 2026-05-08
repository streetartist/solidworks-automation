# GetChamferUnits Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetChamferUnits`

Gets the local units of measurement for a chamfer display dimension.
Gets the local units of measurement for a chamfer display dimension.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetChamferUnits( _
   ByRef LengthUnit As System.Integer, _
   ByRef AngularUnit As System.Integer _
) As System.Boolean
```

```

Dim instance As IDisplayDimension
Dim LengthUnit As System.Integer
Dim AngularUnit As System.Integer
Dim value As System.Boolean
 
value = instance.GetChamferUnits(LengthUnit, AngularUnit)
```

```

System.bool GetChamferUnits( 
   out System.int LengthUnit,
   out System.int AngularUnit
)
```

```

System.bool GetChamferUnits( 
   [Out] System.int LengthUnit,
   [Out] System.int AngularUnit
) 
```

#### Parameters

*LengthUnit*
:   Unit of length as defined in [swLengthUnit\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLengthUnit_e.html)

*AngularUnit*
:   Unit of angle as defined in [swAngleUnit\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAngleUnit_e.html)

#### Return Value

True if successful, false if not

Remarks

The unit display setting of a chamfer display dimension is controlled by a value stored in one of two places: on the owning document or on the individual display dimension. Use [IDisplayDimension::GetUseDocUnits](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUseDocUnits.md) to determine whether the units settings are local or from the owning document. If IDisplayDimension::GetUseDocUnits returns true, then the units settings are from the owning document, and this API returns -1 for both length and angle units of measurement.

Local unit information for a chamfer display dimension is in force when Override Units is selected on the Other tab of the dimension's PropertyManager page. If Override Units is selected, then this API returns units as defined in swLengthUnit\_e (length measurement) and swAngleUnit\_e (angle measurement).

Example

[Get Chamfer Display Dimension (C#)](Get_Chamfer_Display_Dimension_Example_CSharp.htm)  
[Get Chamfer Display Dimension (VB.NET)](Get_Chamfer_Display_Dimension_Example_VBNET.htm)  
[Get Chamfer Display Dimension (VBA)](Get_Chamfer_Display_Dimension_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::GetUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUnits.md)  
[IDisplayDimension::ChamferPrecision Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ChamferPrecision.md)
