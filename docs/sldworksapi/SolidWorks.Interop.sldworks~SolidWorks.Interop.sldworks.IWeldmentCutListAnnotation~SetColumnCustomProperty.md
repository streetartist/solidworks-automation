# SetColumnCustomProperty Method (IWeldmentCutListAnnotation)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation~SetColumnCustomProperty`

Sets the custom property of the specified user-defined column.
Sets the custom property of the specified user-defined column.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetColumnCustomProperty( _
   ByVal Index As System.Integer, _
   ByVal CustomProp As System.String _
) As System.Boolean
```

```

Dim instance As IWeldmentCutListAnnotation
Dim Index As System.Integer
Dim CustomProp As System.String
Dim value As System.Boolean
 
value = instance.SetColumnCustomProperty(Index, CustomProp)
```

```

System.bool SetColumnCustomProperty( 
   System.int Index,
   System.string CustomProp
)
```

```

System.bool SetColumnCustomProperty( 
   System.int Index,
   System.String^ CustomProp
) 
```

#### Parameters

*Index*
:   Column for which to get the custom property

*CustomProp*
:   Custom property for this user-defined column

#### Return Value

True if the custom property is set, false if not

Remarks

Use this method to create a user-defined column where each row in the column is automatically filled in with the custom property value for that particular configuration. The default title for the column is the name of the custom property. If the specified custom property is not a valid custom property, then each row in the column remains empty.

 

To create a user-defined column that is not attached to a custom property; for example, you want to fill in each row of the column yourself, use this method with the CustomProp value specified as the title of the column.

 

To get the list of available custom properties, use [IWeldmentCutListAnnotation::GetAllCustomProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation~GetAllCustomProperties.md) or [IWeldmentCustListAnnotation::IGetAllCustomProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation~IGetAllCustomProperties.md). The list of available custom properties includes all of the items in the weldment cut-list table, which includes items from the file summary items and file custom properties that have been set.

 

This method returns false if the column is not a user-defined column, and no action is taken.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWeldmentCutListAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation.md)  
[IWeldmentCutListAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation_members.md)  
[IWeldmentCutListAnnotation::GetColumnCustomProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation~GetColumnCustomProperty.md)
