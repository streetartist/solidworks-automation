# SetUserPreferenceDoubleValue Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetUserPreferenceDoubleValue`

Obsolete. Superseded by IModelDocExtension::SetUserPreferenceDouble.
Obsolete. Superseded by [IModelDocExtension::SetUserPreferenceDouble](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetUserPreferenceDouble.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetUserPreferenceDoubleValue( _
   ByVal UserPreferenceValue As System.Integer, _
   ByVal Value As System.Double _
) As System.Boolean
```

```

Dim instance As IModelDoc2
Dim UserPreferenceValue As System.Integer
Dim Value As System.Double
Dim value As System.Boolean
 
value = instance.SetUserPreferenceDoubleValue(UserPreferenceValue, Value)
```

```

System.bool SetUserPreferenceDoubleValue( 
   System.int UserPreferenceValue,
   System.double Value
)
```

```

System.bool SetUserPreferenceDoubleValue( 
   System.int UserPreferenceValue,
   System.double Value
) 
```

#### Parameters

*UserPreferenceValue*
:   User preference value as defined in [swUserPreferenceDoubleValue\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUserPreferenceDoubleValue_e.html)

*Value*
:   Numeric value to give to the user preference specified in UserPreferenceValue

#### Return Value

True if the user preference is set successfully, false if not

Remarks

This method is equivalent to interactively setting document properties in the SOLIDWORKS software. See [System Options and Document Properties](sldworksapiprogguide.chm::/overview/System_Options_and_Document_Properties.htm) for details.

Example

[Get and Set Material Density (VBA)](Get_and_Set_Material_Density_Example_VB.htm)  
[Get Excel Cell Value for Density (VBA)](Get_Excel_Cell_Value_for_Density_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
