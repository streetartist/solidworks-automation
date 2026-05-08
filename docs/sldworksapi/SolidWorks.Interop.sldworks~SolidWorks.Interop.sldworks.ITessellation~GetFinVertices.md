# GetFinVertices Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetFinVertices`

Gets the IDs of the two vertices that correspond to a fin.
Gets the IDs of the two vertices that correspond to a fin.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFinVertices( _
   ByVal FinId As System.Integer _
) As System.Object
```

```

Dim instance As ITessellation
Dim FinId As System.Integer
Dim value As System.Object
 
value = instance.GetFinVertices(FinId)
```

```

System.object GetFinVertices( 
   System.int FinId
)
```

```

System.Object^ GetFinVertices( 
   System.int FinId
) 
```

#### Parameters

*FinId*
:   Fin ID of the fin from which you want to return the vertices IDs

#### Return Value

Array of two longs or two integers (see [Long vs. Integer](sldworksapiprogguide.chm::/overview/Long_vs_Integer.htm)) describing the vertices IDs of a fin

Example

[Tessellate a Body (C#)](Tessellate_a_Body_Example_CSharp.htm)  
[Tessellate a Body (VB.NET)](Tessellate_a_Body_Example_VBNET.htm)  
[Tessellate a Body (VBA)](Tessellate_a_Body_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.md)  
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.md)  
[ITessellation::IGetFinVertices Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetFinVertices.md)
