# IFindTwoEdgeMaxDeviation Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IFindTwoEdgeMaxDeviation`

Finds the maximum distance between two edges.
Finds the maximum distance between two edges.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IFindTwoEdgeMaxDeviation( _
   ByVal PEdge1 As Edge, _
   ByVal PEdge2 As Edge _
) As System.Double
```

```

Dim instance As IModeler
Dim PEdge1 As Edge
Dim PEdge2 As Edge
Dim value As System.Double
 
value = instance.IFindTwoEdgeMaxDeviation(PEdge1, PEdge2)
```

```

System.double IFindTwoEdgeMaxDeviation( 
   Edge PEdge1,
   Edge PEdge2
)
```

```

System.double IFindTwoEdgeMaxDeviation( 
   Edge^ PEdge1,
   Edge^ PEdge2
) 
```

#### Parameters

*PEdge1*
:   First [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)

*PEdge2*
:   Second [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)

#### Return Value

Maximum distance between the two edges

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)  
[IModeler::FindTwoEdgeMaxDeviation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~FindTwoEdgeMaxDeviation.md)
