# RemoveInnerLoops Method (IFace)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace~RemoveInnerLoops`

Obsolete. Superseded by IFace2::RemoveInnterLoops.
Obsolete. Superseded by [IFace2::RemoveInnterLoops](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~RemoveInnerLoops.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function RemoveInnerLoops( _
   ByVal NumOfLoops As System.Integer, _
   ByVal InnerLoopsIn As System.Object _
) As System.Object
```

```

Dim instance As IFace
Dim NumOfLoops As System.Integer
Dim InnerLoopsIn As System.Object
Dim value As System.Object
 
value = instance.RemoveInnerLoops(NumOfLoops, InnerLoopsIn)
```

```

System.object RemoveInnerLoops( 
   System.int NumOfLoops,
   System.object InnerLoopsIn
)
```

```

System.Object^ RemoveInnerLoops( 
   System.int NumOfLoops,
   System.Object^ InnerLoopsIn
) 
```

#### Parameters

*NumOfLoops*

*InnerLoopsIn*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFace Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace.md)  
[IFace Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace_members.md)
