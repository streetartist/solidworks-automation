# GetLeaderAtIndex Method (ISFSymbol)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetLeaderAtIndex`

Gets information about the specified leader on this surface finish symbol.
Gets information about the specified leader on this surface finish symbol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetLeaderAtIndex( _
   ByVal Index As System.Integer _
) As System.Object
```

```

Dim instance As ISFSymbol
Dim Index As System.Integer
Dim value As System.Object
 
value = instance.GetLeaderAtIndex(Index)
```

```

System.object GetLeaderAtIndex( 
   System.int Index
)
```

```

System.Object^ GetLeaderAtIndex( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Index of leader

#### Return Value

Array of doubles (see **Remarks**)

Remarks

There can be 0, 1 or 2 lines used with the leader line. If the surface-finish sysmbol is not attached then, there are 0 lines; otherwise, you can have a straight leaderline (1 line) or a bent leaderline (2 lines). You must infer the number of leader lines based on [ISFSymbol::IsAttached](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~IsAttached.md) and [ISFSymbol::HasExtraLeader](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~HasExtraLeader.md).

- ISFSymbol::IsAttached == false implies no leaderline and no leaderline points (PointCount=0).
- ISFSymbol::HasExtraLeader == false means that this is a straight leaderline and 1 line (PointCount=2)
- ISFSymbol::HasExtraLeader == true means that this is a bent leaderline and 2 lines (PointCount=3)

Format of return information is the following array of doubles:

|  |  |
| --- | --- |
|  | retval[0] = x-coordinate of first leader point |
|  | retval[1] = y-coordinate of first leader point |
|  | retval[2] = z-coordinate of first leader point |
|  |  |
|  | retval[3] = x-coordinate of second leader point |
|  | retval[4] = y-coordinate of second leader point |
|  | retval[5] = z-coordinate of second leader point |
|  |  |
|  | retval[6] = x-coordinate of third leader point |
|  | retval[7] = y-coordinate of third leader point |
|  | retval[8] = z-coordinate of third leader point |

Use [ISFSymbol::GetLeaderCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetLeaderCount.md) to see how many leaders there are on the [ISFSymbol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.md) object.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISFSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.md)  
[ISFSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol_members.md)  
[ISFSymbol::IGetLeaderAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~IGetLeaderAtIndex.md)
