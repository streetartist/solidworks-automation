# GetColumnCustomProperty Method (IWeldmentCutListAnnotation)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation~GetColumnCustomProperty`

Gets the custom property for the specified user-defined column.
Gets the custom property for the specified user-defined column.

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

Dim instance As IWeldmentCutListAnnotation
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
:   Column for which to get the custom property

#### Return Value

Custom property for this user-defined column

Remarks

This method returns an empty string if the column is not a user-defined column.

To get the list of custom properties, use [IWeldmentCutListAnnotation::GetAllCustomProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation~GetAllCustomProperties.md) or [IWeldmentCutListAnnotation::IGetAllCustomProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation~IGetAllCustomProperties.md). The list of possible custom properties includes all of the items in the weldment cut list annotation table, which includes items from the file summary items and file custom properties that have been set.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWeldmentCutListAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation.md)  
[IWeldmentCutListAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation_members.md)  
[IWeldmentCutListAnnotation::SetColumnCustomProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation~SetColumnCustomProperty.md)  
[IWeldmentCutListAnnotation::GetAllCustomPropertiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation~GetAllCustomPropertiesCount.md)
