# IGetUnits Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetUnits`

Gets the current unit settings, fraction base, fraction value, and significant digits.
Gets the current unit settings, fraction base, fraction value, and significant digits.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetUnits() As System.Short
```

```

Dim instance As IModelDoc2
Dim value As System.Short
 
value = instance.IGetUnits()
```

```

System.short IGetUnits()
```

```

System.short IGetUnits(); 
```

#### Return Value

- in-process, unmanaged C++: Pointer to an array of 5 shorts (see **Remarks**)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

The format of the returned data is an array of shorts:

[ LengthUnit, FractionBase, FractionValue, SignificantDigits, RoundToFraction ]

where:

- LengthUnit =  current model units as defined in [swLengthUnit\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLengthUnit_e.html).
- FractionBase =  decimal or fraction as defined in [swFractionDisplay\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFractionDisplay_e.html); fractional units are only valid if the model units are set to swINCHES or swFEETINCHES.
- FractionValue = denominator value if using fractional units.
- SignificantDigits =  significant digits if using decimal units.
- RoundToFraction =  flag denoting whether or not to round to the fraction; for example, if 4 was the denominator value and the actual value was .27, it is rounded to .25

You can also use [IModelDoc2::LengthUnit](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~LengthUnit.md), which provides access to the LengthUnit parameter.

Example

[Get and Set Units (C++)](Get_and_Set_Units_Example_CPlusPlus_COM.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::GetAngularUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetAngularUnits.md)  
[IModelDoc2::GetUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetUnits.md)  
[IModelDoc2::IGetAngularUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetAngularUnits.md)  
[IModelDoc2::IGetUserUnit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetUserUnit.md)  
[IModelDoc2::GetUserUnit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetUserUnit.md)  
[IModelDoc2::ISetAngularUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ISetAngularUnits.md)  
[IModelDoc2::SetAngularUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetAngularUnits.md)  
[IModelDoc2::SetUnits Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetUnits.md)
