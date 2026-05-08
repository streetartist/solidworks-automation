# IGetLeaderAtIndex Method (ICustomSymbol)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomSymbol~IGetLeaderAtIndex`

Obsolete. Superseded by INote::IGetLeaderAtIndex.
Obsolete. Superseded by [INote::IGetLeaderAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetLeaderAtIndex.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetLeaderAtIndex( _
   ByVal Index As System.Integer, _
   ByRef PointCount As System.Integer _
) As System.Double
```

```

Dim instance As ICustomSymbol
Dim Index As System.Integer
Dim PointCount As System.Integer
Dim value As System.Double
 
value = instance.IGetLeaderAtIndex(Index, PointCount)
```

```

System.double IGetLeaderAtIndex( 
   System.int Index,
   out System.int PointCount
)
```

```

System.double IGetLeaderAtIndex( 
   System.int Index,
   [Out] System.int PointCount
) 
```

#### Parameters

*Index*

*PointCount*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICustomSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomSymbol.md)  
[ICustomSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomSymbol_members.md)
