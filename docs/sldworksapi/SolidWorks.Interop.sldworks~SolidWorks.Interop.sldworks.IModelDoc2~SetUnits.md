# SetUnits Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetUnits`

Sets the units used by the end-user for the model.
Sets the units used by the end-user for the model.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetUnits( _
   ByVal UType As System.Short, _
   ByVal FractBase As System.Short, _
   ByVal FractDenom As System.Short, _
   ByVal SigDigits As System.Short, _
   ByVal RoundToFraction As System.Boolean _
) 
```

```

Dim instance As IModelDoc2
Dim UType As System.Short
Dim FractBase As System.Short
Dim FractDenom As System.Short
Dim SigDigits As System.Short
Dim RoundToFraction As System.Boolean
 
instance.SetUnits(UType, FractBase, FractDenom, SigDigits, RoundToFraction)
```

```

void SetUnits( 
   System.short UType,
   System.short FractBase,
   System.short FractDenom,
   System.short SigDigits,
   System.bool RoundToFraction
)
```

```

void SetUnits( 
   System.short UType,
   System.short FractBase,
   System.short FractDenom,
   System.short SigDigits,
   System.bool RoundToFraction
) 
```

#### Parameters

*UType*
:   Model units as defined in [swLengthUnit\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLengthUnit_e.html)

*FractBase*
:   Decimal or fraction as defined in [swFractionDisplay\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFractionDisplay_e.html)

*FractDenom*
:   Denominator of the smallest inch fraction to be used, for example, 64 for 1/64; valid only if FractBase is set to swFRACTION (see **Remarks**)

*SigDigits*
:   Significant digits; valid only if FractBase is set to swDECIMAL

*RoundToFraction*
:   Flag denoting whether or not to round to the fraction; for example, if 4 is the denominator value given in FractDenom and the actual value is 0.27, it is rounded to 0.25

Remarks

Fractional units are only valid if UType is set to swINCHES or swFEETINCHES.

Example

' VBA  
' 1. Open a document in SOLIDWORKS.  
' 2. Run the macro below to set inch units with  
'     a fractional base of 16 and no rounding.

Dim swApp As SldWorks.SldWorks  
Dim Part As SldWorks.ModelDoc2  
Option Explicit  
Sub main()  
   Set swApp = Application.SldWorks  
   Set Part = swApp.ActiveDoc  
   Part.**SetUnits** swINCHES, swFRACTION, 16, 0, False  
End Sub

Example

[Get and Set Units (C++)](Get_and_Set_Units_Example_CPlusPlus_COM.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::GetUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetUnits.md)  
[IModelDoc2::IGetUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetUnits.md)  
[IModelDoc2::GetAngularUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetAngularUnits.md)  
[IModelDoc2::GetUserUnit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetUserUnit.md)  
[IModelDoc2::IGetAngularUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetAngularUnits.md)  
[IModelDoc2::IGetUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetUnits.md)  
[IModelDoc2::IGetUserUnit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetUserUnit.md)  
[IModelDoc2::ISetAngularUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ISetAngularUnits.md)  
[IModelDoc2::SetAngularUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetAngularUnits.md)
