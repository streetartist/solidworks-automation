# GetComponents Method (IBomTableAnnotation)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetComponents`

Obsolete. Superseded by IBomTableAnnotation::GetComponents2.
Obsolete. Superseded by [IBomTableAnnotation::GetComponents2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetComponents2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetComponents( _
   ByVal RowIndex As System.Integer _
) As System.Object
```

```

Dim instance As IBomTableAnnotation
Dim RowIndex As System.Integer
Dim value As System.Object
 
value = instance.GetComponents(RowIndex)
```

```

System.object GetComponents( 
   System.int RowIndex
)
```

```

System.Object^ GetComponents( 
   System.int RowIndex
) 
```

#### Parameters

*RowIndex*
:   Row in the BOM table where to get the components; 0-based index

#### Return Value

Array of [components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) in the specified row

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.md)  
[IBomTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation_members.md)  
[IBomTableAnnotation::GetComponentsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetComponentsCount.md)  
[IBomTableAnnotation::IGetComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~IGetComponents.md)
