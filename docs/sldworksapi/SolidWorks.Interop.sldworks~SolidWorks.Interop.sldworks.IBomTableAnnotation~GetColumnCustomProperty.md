# GetColumnCustomProperty Method (IBomTableAnnotation)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetColumnCustomProperty`

Gets the custom property used to fill the values in a specified user-defined column.
Gets the custom property used to fill the values in a specified user-defined column.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetColumnCustomProperty( _
   ByVal Index As System.Integer _
) As System.String
```

```

Dim instance As IBomTableAnnotation
Dim Index As System.Integer
Dim value As System.String
 
value = instance.GetColumnCustomProperty(Index)
```

```

System.string GetColumnCustomProperty( 
   System.int Index
)
```

```

System.String^ GetColumnCustomProperty( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Column from which to get the custom property

#### Return Value

Custom property used to fill the values in this user-defined column

Remarks

This method will return an empty string if the column is not a user-defined column.

To get the list of custom properties, use [IBomTableAnnotation::GetAllCustomProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetAllCustomProperties.md) or [IBomTableAnnotation::IGetAllCustomProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~IGetAllCustomProperties.md). The list of possible custom properties includes all of the items in the BOM table, which includes items from the file summary items and file custom properties that have been set.

Example

[Get Custom Properties for BOM Table Columns (VBA)](Get_Custom_Properties_for_BOM_Table_Columns_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.md)  
[IBomTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation_members.md)  
[IBomTableAnnotation::GetAllCustomPropertiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetAllCustomPropertiesCount.md)  
[IBomTableAnnotation::SetColumnCustomProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~SetColumnCustomProperty.md)
