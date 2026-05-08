# IGetFinVertices Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetFinVertices`

Gets the IDs of the two vertices that correspond to a fin.
Gets the IDs of the two vertices that correspond to a fin.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetFinVertices( _
   ByVal FinId As System.Integer _
) As System.Integer
```

```

Dim instance As ITessellation
Dim FinId As System.Integer
Dim value As System.Integer
 
value = instance.IGetFinVertices(FinId)
```

```

System.int IGetFinVertices( 
   System.int FinId
)
```

```

System.int IGetFinVertices( 
   System.int FinId
) 
```

#### Parameters

*FinId*
:   Fin ID of the fin from which you want to return the vertices

#### Return Value

- in-process, unmanaged C++: Pointer to an array of two longs or integers describing the vertices IDs of a fin

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.md)  
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.md)  
[ITessellate::GetFinVertices Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetFinVertices.md)
