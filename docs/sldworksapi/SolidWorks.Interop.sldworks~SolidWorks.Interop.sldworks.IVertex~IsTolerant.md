# IsTolerant Method (IVertex)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~IsTolerant`

Gets whether a vertex is tolerant and its tolerance value.
Gets whether a vertex is tolerant and its tolerance value.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsTolerant( _
   ByRef Tolerance As System.Double _
) As System.Boolean
```

```

Dim instance As IVertex
Dim Tolerance As System.Double
Dim value As System.Boolean
 
value = instance.IsTolerant(Tolerance)
```

```

System.bool IsTolerant( 
   out System.double Tolerance
)
```

```

System.bool IsTolerant( 
   [Out] System.double Tolerance
) 
```

#### Parameters

*Tolerance*
:   Vertex tolerance or gap in meters

#### Return Value

True if tolerant, false if not tolerant

Remarks

If the tolerance (or gap) between common vertices in a part:

- is greater than 1/2 of the session precision (i.e., > 5.0E-9 mm), then each vertex is tolerant, and this method returns true.
- is less than or equal to 1/2 of the session precision (i.e., <= 5.0E-9 mm), then each vertex is exact and not tolerant, and this method returns false.

Traverse part body vertices and use this method to find the maximum vertex gap (tolerance) in a part, which can also be found using the **Tools > Check** dialog in the SOLIDWORKS user interface.

Example

[Get Maximum Edge and Vertex Gaps (VBA)](Get_Maximum_Edge_and_Vertex_Gaps_Example_VB.htm)  
[Get Maximum Edge and Vertex Gaps (VB.NET)](Get_Maximum_Edge_and_Vertex_Gaps_Example_VBNET.htm)  
[Get Maximum Edge and Vertex Gaps (C#)](Get_Maximum_Edge_and_Vertex_Gaps_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IVertex Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md)  
[IVertex Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex_members.md)  
[IEdge::IsTolerant](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IsTolerant.md)
