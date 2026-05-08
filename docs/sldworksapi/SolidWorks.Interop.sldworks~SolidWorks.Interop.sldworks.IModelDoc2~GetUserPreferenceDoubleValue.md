# GetUserPreferenceDoubleValue Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetUserPreferenceDoubleValue`

Obsolete. Superseded by IModelDocExtension::GetUserPreferenceDouble.
Obsolete. Superseded by [IModelDocExtension::GetUserPreferenceDouble](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetUserPreferenceDouble.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetUserPreferenceDoubleValue( _
   ByVal UserPreferenceValue As System.Integer _
) As System.Double
```

```

Dim instance As IModelDoc2
Dim UserPreferenceValue As System.Integer
Dim value As System.Double
 
value = instance.GetUserPreferenceDoubleValue(UserPreferenceValue)
```

```

System.double GetUserPreferenceDoubleValue( 
   System.int UserPreferenceValue
)
```

```

System.double GetUserPreferenceDoubleValue( 
   System.int UserPreferenceValue
) 
```

#### Parameters

*UserPreferenceValue*
:   Value as defined in [swUserPreferenceDoubleValue\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUserPreferenceDoubleValue_e.html)

#### Return Value

Numeric value of the user preference specified in UserPreferenceValue

Remarks

This method is equivalent to interactively getting document properties in the SOLIDWORKS product. See [System Options and Document Properties](sldworksapiprogguide.chm::/overview/System_Options_and_Document_Properties.htm) for details.

If you want to retrieve the current, minimum, and maximum values for a document user preference, use [IModelDoc2::GetUserPreferenceDoubleValueRange](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetUserPreferenceDoubleValueRange.md). Be sure to read that method's **Remarks** section because its implementation is limited.

Example

[Get and Set Material Density (VBA)](Get_and_Set_Material_Density_Example_VB.htm)  
[Get Mass Properties of Assembly Component (VBA)](Get_Mass_Properties_of_Assembly_Component_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
