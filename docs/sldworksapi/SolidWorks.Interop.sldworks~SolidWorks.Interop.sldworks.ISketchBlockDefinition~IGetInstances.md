# IGetInstances Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetInstances`

Gets all of the block instances of this block definition.
Gets all of the block instances of this block definition.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetInstances( _
   ByVal Count As System.Integer _
) As SketchBlockInstance
```

```

Dim instance As ISketchBlockDefinition
Dim Count As System.Integer
Dim value As SketchBlockInstance
 
value = instance.IGetInstances(Count)
```

```

SketchBlockInstance IGetInstances( 
   System.int Count
)
```

```

SketchBlockInstance^ IGetInstances( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of block instances

#### Return Value

- in-process, unmanaged C++: Pointer to an array of all of the [block instances](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.md)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Call [ISketchBlockDefinition::GetInstanceCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetInstanceCount.md) before calling this method to get the value of Count.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.md)  
[ISketchBlockDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition_members.md)  
[ISketchBlockDefinition::GetInstances Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetInstances.md)
