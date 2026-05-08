# IGetAttributes Method (ISketchBlockInstance)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~IGetAttributes`

Gets the attributes for this block instance.
Gets the attributes for this block instance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetAttributes( _
   ByVal Count As System.Integer _
) As Note
```

```

Dim instance As ISketchBlockInstance
Dim Count As System.Integer
Dim value As Note
 
value = instance.IGetAttributes(Count)
```

```

Note IGetAttributes( 
   System.int Count
)
```

```

Note^ IGetAttributes( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of attributes

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [notes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Attributes are notes that have tag names and are not read-only.

Before calling this method, call [ISketchBlockInstance::GetAttributeCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetAttributeCount.md) to get the value for Count.

Use [ISketchBlockInstance::GetAttributeValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetAttributeValue.md) to get attribute's value, or use [ISketchBlockInstance::SetAttributeValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~SetAttributeValue.md) to set an attribute's value.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.md)  
[ISketchBlockInstance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance_members.md)  
[ISketchBlockInstance::GetAttributes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetAttributes.md)  
[ISketchBlockInstance::GetAttributeValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetAttributeValue.md)  
[ISketchBlockInstance::SetAttributeValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~SetAttributeValue.md)
