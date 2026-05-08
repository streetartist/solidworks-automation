# IGetLeaderAtIndex2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetLeaderAtIndex2`

Gets information about the specified leader on this GTol.
Gets information about the specified leader on this GTol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetLeaderAtIndex2( _
   ByVal Index As System.Integer, _
   ByRef PointCount As System.Integer _
) As System.Double
```

```

Dim instance As IGtol
Dim Index As System.Integer
Dim PointCount As System.Integer
Dim value As System.Double
 
value = instance.IGetLeaderAtIndex2(Index, PointCount)
```

```

System.double IGetLeaderAtIndex2( 
   System.int Index,
   out System.int PointCount
)
```

```

System.double IGetLeaderAtIndex2( 
   System.int Index,
   [Out] System.int PointCount
) 
```

#### Parameters

*Index*
:   Index of the leader

*PointCount*
:   Number of (x,y,z) points returned in the array

#### Return Value

- in-process, unmanaged C++: Pointer to array of doubles (see **Remarks**)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

A GTol can have a straight leader (1 segment) or a bent leader (2 segments), or it might have a perpendicular leader, which can have either 2 or 3 segments, depending on the situation. The returned array contains the point information to define the leader. It contains the x,y,z coordinates for each vertex in the leader. It can contain up to 12 doubles (4 sets of x,y,z values).

Because the return value is passed into this method, it should be dimensioned to 12 before this method is called to allow for the maximum number of items that can be returned (4 segments). Upon return from the API, the PointCount argument contains the actual number of points stored in the array. Multiply this number by 3 to determine the number of array items actually used.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md)  
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.md)  
[IGtol::GetLeaderAtIndex2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetLeaderAtIndex2.md)  
[IGtol::GetLeaderCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetLeaderCount.md)  
[IGtol::GetLeaderSide Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetLeaderSide.md)  
[IGtol::IGetLeaderInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetLeaderInfo.md)  
[IGtol::SetLeader Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetLeader.md)
