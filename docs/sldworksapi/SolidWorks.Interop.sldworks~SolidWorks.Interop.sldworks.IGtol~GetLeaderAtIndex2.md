# GetLeaderAtIndex2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetLeaderAtIndex2`

Gets information about the specified leader on this GTol.
Gets information about the specified leader on this GTol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetLeaderAtIndex2( _
   ByVal Index As System.Integer _
) As System.Object
```

```

Dim instance As IGtol
Dim Index As System.Integer
Dim value As System.Object
 
value = instance.GetLeaderAtIndex2(Index)
```

```

System.object GetLeaderAtIndex2( 
   System.int Index
)
```

```

System.Object^ GetLeaderAtIndex2( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Index of the leader

#### Return Value

Array (see **Remarks**)

Remarks

A GTol can have a straight leader (1 segment) or a bent leader (2 segments), or it might have a perpendicular leader, which can have either 2 or 3 segments, depending on the situation. The returned array contains the point information to define the leader. It contains the x,y,z coordinates for each vertex in the leader. It can contain up to 12 doubles (4 sets of x,y,z values).

Examine the return value to determine the number of items in the leader coordinate information. The size of the array is either 6 (1 segments), 9 (2 segments), or 12 (3 segments).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md)  
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.md)  
[IGtol::GetLeaderCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetLeaderCount.md)  
[IGtol::GetLeaderInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetLeaderInfo.md)  
[IGtol::IGetLeaderAtIndex2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetLeaderAtIndex2.md)  
[IGtol::IGetLeaderInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetLeaderInfo.md)  
[IGtol::SetLeader Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetLeader.md)  
[IGtol::GetLeaderSide Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetLeaderSide.md)  
[IGtol::IGetLineAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetLineAtIndex.md)
