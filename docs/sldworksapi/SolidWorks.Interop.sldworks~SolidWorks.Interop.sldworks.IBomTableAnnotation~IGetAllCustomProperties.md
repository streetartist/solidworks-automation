# IGetAllCustomProperties Method (IBomTableAnnotation)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~IGetAllCustomProperties`

Gets the list of available custom properties that can be used for a custom properties column in this BOM table annotation.
Gets the list of available custom properties that can be used for a custom properties column in this BOM table annotation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetAllCustomProperties( _
   ByVal Count As System.Integer _
) As System.String
```

```

Dim instance As IBomTableAnnotation
Dim Count As System.Integer
Dim value As System.String
 
value = instance.IGetAllCustomProperties(Count)
```

```

System.string IGetAllCustomProperties( 
   System.int Count
)
```

```

System.String^ IGetAllCustomProperties( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of available custom properties

#### Return Value

- in-process, unmanaged C++: Pointer to an array of strings of available custom properties

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

To get the number of custom properties, use [IBomTableAnnotation::GetAllCustomPropertiesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetAllCustomPropertiesCount.md).

The list of available custom properties includes all of the items in the BOM table, which includes items from the file summary items and file custom properties that have been set.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.md)  
[IBomTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation_members.md)  
[IBomTableAnnotation::GetAllCustomProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetAllCustomProperties.md)  
[IBomTableAnnotation::GetColumnCustomProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetColumnCustomProperty.md)
