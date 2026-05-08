# FindTwoEdgeMaxDeviation Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~FindTwoEdgeMaxDeviation`

Finds the maximum distance between two edges.
Finds the maximum distance between two edges.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function FindTwoEdgeMaxDeviation( _
   ByVal LpEdge1 As System.Object, _
   ByVal LpEdge2 As System.Object _
) As System.Double
```

```

Dim instance As IModeler
Dim LpEdge1 As System.Object
Dim LpEdge2 As System.Object
Dim value As System.Double
 
value = instance.FindTwoEdgeMaxDeviation(LpEdge1, LpEdge2)
```

```

System.double FindTwoEdgeMaxDeviation( 
   System.object LpEdge1,
   System.object LpEdge2
)
```

```

System.double FindTwoEdgeMaxDeviation( 
   System.Object^ LpEdge1,
   System.Object^ LpEdge2
) 
```

#### Parameters

*LpEdge1*
:   First [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)

*LpEdge2*
:   Second [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)

#### Return Value

Maximum distance between the two edges

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)  
[IModeler::IFindTwoEdgeMaxDeviation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IFindTwoEdgeMaxDeviation.md)
