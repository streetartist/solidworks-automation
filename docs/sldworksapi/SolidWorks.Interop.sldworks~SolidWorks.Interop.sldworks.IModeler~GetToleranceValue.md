# GetToleranceValue Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~GetToleranceValue`

Gets the current tolerance value of the given tolerance ID.
Gets the current tolerance value of the given tolerance ID.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetToleranceValue( _
   ByVal ToleranceID As System.Integer _
) As System.Double
```

```

Dim instance As IModeler
Dim ToleranceID As System.Integer
Dim value As System.Double
 
value = instance.GetToleranceValue(ToleranceID)
```

```

System.double GetToleranceValue( 
   System.int ToleranceID
)
```

```

System.double GetToleranceValue( 
   System.int ToleranceID
) 
```

#### Parameters

*ToleranceID*
:   Type of tolerance that you want to obtain as defined by [swTolerances\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTolerances_e.html)

#### Return Value

Tolerance value for the specified ToleranceID

Example

[Get Length of Spline or Elliptical Edge (VBA)](Get_Length_of_Spline_or_Elliptical_Edge_Example_VB.htm)  
[Get Parameters and Spline Points for Curve (VBA)](Get_Parameters_and_Spline_Points_for_Curve_Example_VB.htm)  
[Get Tolerance (VBA)](Get_Tolerance_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)  
[IModeler::UnsetTolerances Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~UnsetTolerances.md)  
[IModeler::SetToleranceValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~SetToleranceValue.md)
