# GetComponentsCount Method (IBomTableAnnotation)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetComponentsCount`

Obsolete. Superseded by IBomTableAnnotation::GetComponentsCount2.
Obsolete. Superseded by [IBomTableAnnotation::GetComponentsCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetComponentsCount2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetComponentsCount( _
   ByVal RowIndex As System.Integer _
) As System.Integer
```

```

Dim instance As IBomTableAnnotation
Dim RowIndex As System.Integer
Dim value As System.Integer
 
value = instance.GetComponentsCount(RowIndex)
```

```

System.int GetComponentsCount( 
   System.int RowIndex
)
```

```

System.int GetComponentsCount( 
   System.int RowIndex
) 
```

#### Parameters

*RowIndex*
:   Row in the BOM table where to get the number of components; 0-based index

#### Return Value

Number of components in the specified row

Remarks

Call this method before calling [IBomTableAnnotation::IGetComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~IGetComponents.md) to determine the size of the array for that method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.md)  
[IBomTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation_members.md)  
[IBomTableAnnotation::GetComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetComponents.md)
