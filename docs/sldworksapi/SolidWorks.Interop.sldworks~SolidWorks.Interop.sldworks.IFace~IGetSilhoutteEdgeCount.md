# IGetSilhoutteEdgeCount Method (IFace)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace~IGetSilhoutteEdgeCount`

Obsolete. Superseded by IFace2::IGetSilhoutteEdgeCount.
Obsolete. Superseded by [IFace2::IGetSilhoutteEdgeCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetSilhoutteEdgeCount.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetSilhoutteEdgeCount( _
   ByRef Root As System.Double, _
   ByRef Normal As System.Double _
) As System.Integer
```

```

Dim instance As IFace
Dim Root As System.Double
Dim Normal As System.Double
Dim value As System.Integer
 
value = instance.IGetSilhoutteEdgeCount(Root, Normal)
```

```

System.int IGetSilhoutteEdgeCount( 
   ref System.double Root,
   ref System.double Normal
)
```

```

System.int IGetSilhoutteEdgeCount( 
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

[IFace Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace.md)  
[IFace Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace_members.md)
