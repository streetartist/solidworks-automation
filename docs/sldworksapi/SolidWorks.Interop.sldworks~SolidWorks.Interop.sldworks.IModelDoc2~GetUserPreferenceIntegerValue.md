# GetUserPreferenceIntegerValue Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetUserPreferenceIntegerValue`

Obsolete. Superseded by IModelDocExtension::GetUserPreferenceInteger.
Obsolete. Superseded by [IModelDocExtension::GetUserPreferenceInteger](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetUserPreferenceInteger.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetUserPreferenceIntegerValue( _
   ByVal UserPreferenceValue As System.Integer _
) As System.Integer
```

```

Dim instance As IModelDoc2
Dim UserPreferenceValue As System.Integer
Dim value As System.Integer
 
value = instance.GetUserPreferenceIntegerValue(UserPreferenceValue)
```

```

System.int GetUserPreferenceIntegerValue( 
   System.int UserPreferenceValue
)
```

```

System.int GetUserPreferenceIntegerValue( 
   System.int UserPreferenceValue
) 
```

#### Parameters

*UserPreferenceValue*
:   Value as defined in [swUserPreferenceIntegerValue\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUserPreferenceIntegerValue_e.html)

#### Return Value

Numeric value associated with the specified UserPreferenceValue

Remarks

This method is equivalent to interactively getting document properties in the SOLIDWORKS product. See [System Options and Document Properties](sldworksapiprogguide.chm::/overview/System_Options_and_Document_Properties.htm) for details.

Example

[Get Material Properties (VBA)](Get_Material_Properties_Example_VB.htm)  
[Make Part Transparent (VBA)](Make_Part_Transparent_Example_VB.htm)  
[Save Document as TIFF (VBA)](Save_As_Tiff_Example_VB.htm)  
[Set Grid Lines (VBA)](Set_Grid_Lines_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
