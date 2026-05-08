# IGetComponents2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~IGetComponents2`

Gets the components in the specified row for the specified configuration in this BOM table annotation.
Gets the components in the specified row for the specified configuration in this BOM table annotation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetComponents2( _
   ByVal RowIndex As System.Integer, _
   ByVal Configuration As System.String, _
   ByVal Count As System.Integer _
) As Component2
```

```

Dim instance As IBomTableAnnotation
Dim RowIndex As System.Integer
Dim Configuration As System.String
Dim Count As System.Integer
Dim value As Component2
 
value = instance.IGetComponents2(RowIndex, Configuration, Count)
```

```

Component2 IGetComponents2( 
   System.int RowIndex,
   System.string Configuration,
   System.int Count
)
```

```

Component2^ IGetComponents2( 
   System.int RowIndex,
   System.String^ Configuration,
   System.int Count
) 
```

#### Parameters

*RowIndex*
:   Row in the BOM table where to get the components; 0-based index

*Configuration*
:   Configuration for which to count components in top-level only BOMs; specify an empty string for parts only and indented BOMs

*Count*
:   Number of components in the specified row

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) in the specified row for the specified configuration

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [IBomTableAnnotation::GetComponentsCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetComponentsCount2.md) to get the value of Count.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.md)  
[IBomTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation_members.md)  
[IBomTableAnnotation::GetComponents2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetComponents2.md)
