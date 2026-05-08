# IGetConstraints Method (ISketchPath)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath~IGetConstraints`

Gets the names of the constraints in this sketch path.
Gets the names of the constraints in this sketch path.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetConstraints( _
   ByVal Count As System.Integer _
) As System.String
```

```

Dim instance As ISketchPath
Dim Count As System.Integer
Dim value As System.String
 
value = instance.IGetConstraints(Count)
```

```

System.string IGetConstraints( 
   System.int Count
)
```

```

System.String^ IGetConstraints( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of sketch constraints

#### Return Value

- in-process, unmanaged C++: Pointer to an array of sketch constraints

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [ISketchPath::GetConstraintsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath~GetConstraintsCount.md) to get the value of count.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchPath Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath.md)  
[ISketchPath Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath_members.md)  
[ISketchPath::GetConstraints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath~GetConstraints.md)
