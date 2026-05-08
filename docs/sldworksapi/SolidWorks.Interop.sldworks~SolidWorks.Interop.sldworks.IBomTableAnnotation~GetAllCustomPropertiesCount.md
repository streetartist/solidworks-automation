# GetAllCustomPropertiesCount Method (IBomTableAnnotation)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetAllCustomPropertiesCount`

Gets the number of items in the list of available custom properties that can be used for a custom properties column in this BOM table annotation.
Gets the number of items in the list of available custom properties that can be used for a custom properties column in this BOM table annotation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAllCustomPropertiesCount() As System.Integer
```

```

Dim instance As IBomTableAnnotation
Dim value As System.Integer
 
value = instance.GetAllCustomPropertiesCount()
```

```

System.int GetAllCustomPropertiesCount()
```

```

System.int GetAllCustomPropertiesCount(); 
```

#### Return Value

Number of available custom properties

Remarks

Call this method before calling [IBomTableAnnotation::IGetAllCustomProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~IGetAllCustomProperties.md).

The list of possible custom properties includes all of the items in the BOM table, which includes items from the file summary items and file custom properties that have been set.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.md)  
[IBomTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation_members.md)  
[IBomTableAnnotation::GetAllCustomProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetAllCustomProperties.md)  
[IBomTableAnnotation::SetColumnCustomProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~SetColumnCustomProperty.md)
