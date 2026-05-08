# GetComponents2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetComponents2`

Gets the components in the specified row for the specified configuration in this BOM table annotation.
Gets the components in the specified row for the specified configuration in this BOM table annotation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetComponents2( _
   ByVal RowIndex As System.Integer, _
   ByVal Configuration As System.String _
) As System.Object
```

```

Dim instance As IBomTableAnnotation
Dim RowIndex As System.Integer
Dim Configuration As System.String
Dim value As System.Object
 
value = instance.GetComponents2(RowIndex, Configuration)
```

```

System.object GetComponents2( 
   System.int RowIndex,
   System.string Configuration
)
```

```

System.Object^ GetComponents2( 
   System.int RowIndex,
   System.String^ Configuration
) 
```

#### Parameters

*RowIndex*
:   Row in the BOM table where to get the components; 0-based index

*Configuration*
:   Configuration for which to get components in top-level only BOMs; specify an empty string for parts only and indented BOMs

#### Return Value

Array of [components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) in the specified row for the specified configuration

Example

[Get Components in Each BOM Table Row (VBA)](Get_Components_in_Each_BOM_Table_Row_VB.htm)  
[Get Components in Each BOM Table Row (VB.NET)](Get_Components_in_Each_BOM_Table_Row_Example_VBNET.htm)  
[Get Components in Each BOM Table Row (C#)](Get_Components_in_Each_BOM_Table_Row_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.md)  
[IBomTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation_members.md)  
[IBomTableAnnotation::GetComponentsCount2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetComponentsCount2.md)  
[IBomTableAnnotation::IGetComponents2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~IGetComponents2.md)
