# GetColumnCustomProperty Method (IRevisionTableAnnotation)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~GetColumnCustomProperty`

Gets the custom property used for the values in a specified user-defined column.
Gets the custom property used for the values in a specified user-defined column.

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

Dim instance As IRevisionTableAnnotation
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

Custom property used for the values in this user-defined column

Remarks

This method returns a empty string if the column is not a user-defined column.

To get the list of custom properties, use [IRevisonTableAnnotation::GetAllCustomProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~GetAllCustomProperties.md) or [IRevisionTableAnnotation::IGetAllCustomProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~IGetAllCustomProperties.md). The list of available custom properties includes all of the items in the revision table, which includes items from the file summary items and file custom properties that have been set.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRevisionTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation.md)  
[IRevisionTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation_members.md)  
[IRevisionTableAnnotation::GetAllCustomPropertiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~GetAllCustomPropertiesCount.md)  
[IRevisionTableAnnotation::SetColumnCustomProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~SetColumnCustomProperty.md)
