# GetUserPreferenceStringValue Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetUserPreferenceStringValue`

Obsolete. Superseded by IModelDocExtension::GetUserPreferenceString.
Obsolete. Superseded by [IModelDocExtension::GetUserPreferenceString](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetUserPreferenceString.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetUserPreferenceStringValue( _
   ByVal UserPreference As System.Integer _
) As System.String
```

```

Dim instance As IModelDoc2
Dim UserPreference As System.Integer
Dim value As System.String
 
value = instance.GetUserPreferenceStringValue(UserPreference)
```

```

System.string GetUserPreferenceStringValue( 
   System.int UserPreference
)
```

```

System.String^ GetUserPreferenceStringValue( 
   System.int UserPreference
) 
```

#### Parameters

*UserPreference*
:   Value as defined in [swUserPreferenceStringValue\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUserPreferenceStringValue_e.html)

#### Return Value

String value of UserPreference

Remarks

This method is equivalent to interactively getting document properties in the SOLIDWORKS product. See [System Options and Document Properties](sldworksapiprogguide.chm::/overview/System_Options_and_Document_Properties.htm) for details.

Example

[Get Transform of Coordinate System (VB.NET)](Get_Transform_of_Coordinate_System_Example_VB.NET.htm)  
[Get Coordinate System Transform (VBA)](Get_Coordinate_System_Transform_Example_VB.htm)  
[Save Rollbacked Part as Parasolid File (VBA)](Save_Roll_Backed_Part_as_Parasolid_File_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
