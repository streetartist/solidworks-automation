# GetComponentsCount2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetComponentsCount2`

Gets the number of components, the item number, and the part number in the specified row for the specified configuration in this BOM table annotation.
Gets the number of components, the item number, and the part number in the specified row for the specified configuration in this BOM table annotation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetComponentsCount2( _
   ByVal RowIndex As System.Integer, _
   ByVal Configuration As System.String, _
   ByRef ItemNumber As System.String, _
   ByRef PartNumber As System.String _
) As System.Integer
```

```

Dim instance As IBomTableAnnotation
Dim RowIndex As System.Integer
Dim Configuration As System.String
Dim ItemNumber As System.String
Dim PartNumber As System.String
Dim value As System.Integer
 
value = instance.GetComponentsCount2(RowIndex, Configuration, ItemNumber, PartNumber)
```

```

System.int GetComponentsCount2( 
   System.int RowIndex,
   System.string Configuration,
   out System.string ItemNumber,
   out System.string PartNumber
)
```

```

System.int GetComponentsCount2( 
   System.int RowIndex,
   System.String^ Configuration,
   [Out] System.String^ ItemNumber,
   [Out] System.String^ PartNumber
) 
```

#### Parameters

*RowIndex*
:   Row in the BOM table where to get the number of components; 0-based index

*Configuration*
:   Configuration for which to count components in top-level only BOMs; specify an empty string for parts only and indented BOMs

*ItemNumber*
:   Item number of the specified row

*PartNumber*
:   Part number of the specified row

#### Return Value

Number of components in the specified row for the specified configuration

Remarks

Call this method before calling [IBomTableAnnotation::IGetComponents2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~IGetComponents2.md) to determine the size of the array for that method.

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
[IBomTableAnnotation::GetComponents2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetComponents2.md)
