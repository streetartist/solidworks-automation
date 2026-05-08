# GetModelPathNamesCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetModelPathNamesCount`

Gets the number of model pathnames in the specified row of this BOM table annotation.
Gets the number of model pathnames in the specified row of this BOM table annotation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetModelPathNamesCount( _
   ByVal RowIndex As System.Integer _
) As System.Integer
```

```

Dim instance As IBomTableAnnotation
Dim RowIndex As System.Integer
Dim value As System.Integer
 
value = instance.GetModelPathNamesCount(RowIndex)
```

```

System.int GetModelPathNamesCount( 
   System.int RowIndex
)
```

```

System.int GetModelPathNamesCount( 
   System.int RowIndex
) 
```

#### Parameters

*RowIndex*
:   Row in the BOM table; 0-based index

#### Return Value

Number of model pathnames in the specified row

Remarks

Call this method before calling [IBomTableAnnotation::IGetModelPathNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~IGetModelPathNames.md) to determine the size of the array for that method.

Example

[Get Model Pathnames in BOM Table (C#)](Get_Model_Path_Names_in_BOM_Table_Example_CSharp.htm)  
[Get Model Pathnames in BOM Table (VB.NET)](Get_Model_Path_Names_in_BOM_Table_Example_VBNET.htm)  
[Get Model Pathnames in BOM Table (VBA)](Get_Model_Path_Names_in_BOM_Table_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.md)  
[IBomTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation_members.md)  
[IBomTableAnnotation::GetModelPathNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetModelPathNames.md)
