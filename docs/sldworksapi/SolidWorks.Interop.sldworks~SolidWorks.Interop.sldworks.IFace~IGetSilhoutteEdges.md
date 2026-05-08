# IGetSilhoutteEdges Method (IFace)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace~IGetSilhoutteEdges`

Obsolete. Superseded by IFace2::IGetSilhoutteEdges.
Obsolete. Superseded by [IFace2::IGetSilhoutteEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetSilhoutteEdges.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetSilhoutteEdges( _
   ByRef Root As System.Double, _
   ByRef Normal As System.Double _
) As System.IntPtr
```

```

Dim instance As IFace
Dim Root As System.Double
Dim Normal As System.Double
Dim value As System.IntPtr
 
value = instance.IGetSilhoutteEdges(Root, Normal)
```

```

System.IntPtr IGetSilhoutteEdges( 
   ref System.double Root,
   ref System.double Normal
)
```

```

System.IntPtr IGetSilhoutteEdges( 
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
