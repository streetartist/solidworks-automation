# IGetComponents Method (IBomTableAnnotation)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~IGetComponents`

Obsolete. Superseded by IBomTableAnnotation::IGetComponents2.
Obsolete. Superseded by [IBomTableAnnotation::IGetComponents2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~IGetComponents2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetComponents( _
   ByVal RowIndex As System.Integer, _
   ByVal Count As System.Integer _
) As Component2
```

```

Dim instance As IBomTableAnnotation
Dim RowIndex As System.Integer
Dim Count As System.Integer
Dim value As Component2
 
value = instance.IGetComponents(RowIndex, Count)
```

```

Component2 IGetComponents( 
   System.int RowIndex,
   System.int Count
)
```

```

Component2^ IGetComponents( 
   System.int RowIndex,
   System.int Count
) 
```

#### Parameters

*RowIndex*
:   Row in the BOM table where to get the components; 0-based index

*Count*
:   Number of components in the specified row

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) in the specified row

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [IBomTableAnnotation::GetComponentsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetComponentsCount.md) to get the value of Count.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.md)  
[IBomTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation_members.md)  
[IBomTableAnnotation::GetComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetComponents.md)
