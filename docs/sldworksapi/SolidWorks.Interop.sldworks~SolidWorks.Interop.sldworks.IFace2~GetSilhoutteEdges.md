# GetSilhoutteEdges Method (IFace2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetSilhoutteEdges`

Obsolete. Superseded by IFace2::GetSilhoutteEdgesVB.
Obsolete. Superseded by [IFace2::GetSilhoutteEdgesVB](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetSilhoutteEdgesVB.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSilhoutteEdges( _
   ByRef Root As System.Double, _
   ByRef Normal As System.Double _
) As System.Object
```

```

Dim instance As IFace2
Dim Root As System.Double
Dim Normal As System.Double
Dim value As System.Object
 
value = instance.GetSilhoutteEdges(Root, Normal)
```

```

System.object GetSilhoutteEdges( 
   ref System.double Root,
   ref System.double Normal
)
```

```

System.Object^ GetSilhoutteEdges( 
   System.double% Root,
   System.double% Normal
) 
```

#### Parameters

*Root*

*Normal*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)  
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.md)
