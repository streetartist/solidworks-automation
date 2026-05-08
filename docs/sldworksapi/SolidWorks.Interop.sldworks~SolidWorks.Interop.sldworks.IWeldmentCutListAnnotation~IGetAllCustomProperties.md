# IGetAllCustomProperties Method (IWeldmentCutListAnnotation)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation~IGetAllCustomProperties`

Gets the list of available custom properties that could be used for a custom properties column in this weldment cut list table annotation.
Gets the list of available custom properties that could be used for a custom properties column in this weldment cut list table annotation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetAllCustomProperties( _
   ByVal Count As System.Integer _
) As System.String
```

```

Dim instance As IWeldmentCutListAnnotation
Dim Count As System.Integer
Dim value As System.String
 
value = instance.IGetAllCustomProperties(Count)
```

```

System.string IGetAllCustomProperties( 
   System.int Count
)
```

```

System.String^ IGetAllCustomProperties( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of available custom properties

#### Return Value

- in-process, unmanaged C++: Pointer to an array of strings of available custom properties

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [IWeldmentCutListAnnotation::GetAllCustomPropertiesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation~GetAllCustomPropertiesCount.md) to get Count.

The list of available custom properties includes all of the items in the weldment cut list table, which includes items from the file summary items and file custom properties that have been set.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWeldmentCutListAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation.md)  
[IWeldmentCutListAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation_members.md)  
[IWeldmentCutListAnnotation::GetAllCustomProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation~GetAllCustomProperties.md)  
[IWeldmentCutListAnnotation::GetColumnCustomProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation~GetColumnCustomProperty.md)  
[IWeldmentCutListAnnotation::SetColumnCustomProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation~SetColumnCustomProperty.md)
