# GetAllCustomProperties Method (IBomTableAnnotation)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetAllCustomProperties`

Gets the list of available custom properties that can be used for a custom properties column in this BOM table annotation.
Gets the list of available custom properties that can be used for a custom properties column in this BOM table annotation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAllCustomProperties() As System.Object
```

```

Dim instance As IBomTableAnnotation
Dim value As System.Object
 
value = instance.GetAllCustomProperties()
```

```

System.object GetAllCustomProperties()
```

```

System.Object^ GetAllCustomProperties(); 
```

#### Return Value

Array of strings of available custom properties

Remarks

To get the number of custom properties, use [IBomTableAnnotation::GetAllCustomPropertiesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetAllCustomPropertiesCount.md).

The list of available custom properties includes all of the items in the BOM table, which includes items from the file summary items and file custom properties that have been set.

Example

[Get Available Custom Properties for BOM Table (VBA)](Get_Available_Custom_Properties_for_BOM_Table_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.md)  
[IBomTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation_members.md)  
[IBomTableAnnotation::IGetAllCustomProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~IGetAllCustomProperties.md)  
[IBomTableAnnotation::GetColumnCustomProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetColumnCustomProperty.md)
