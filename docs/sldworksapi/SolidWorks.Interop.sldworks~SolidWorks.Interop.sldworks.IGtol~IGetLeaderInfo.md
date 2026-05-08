# IGetLeaderInfo Method (IGtol)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetLeaderInfo`

Gets information describing the layout of the GTol leader lines.
Gets information describing the layout of the GTol leader lines.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetLeaderInfo( _
   ByRef PointCount As System.Integer _
) As System.Double
```

```

Dim instance As IGtol
Dim PointCount As System.Integer
Dim value As System.Double
 
value = instance.IGetLeaderInfo(PointCount)
```

```

System.double IGetLeaderInfo( 
   out System.int PointCount
)
```

```

System.double IGetLeaderInfo( 
   [Out] System.int PointCount
) 
```

#### Parameters

*PointCount*
:   Number of (x,y,z) points returned in the array

#### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

There can be 0, 1 or 2 lines with the leader line. If the GTol is not attached, then there are 0 lines. Otherwise, the GTol can have a straight leaderline (1 line) or a bent leaderline (2 lines). The caller must infer the number of leader lines based on [IGtol::IsAttached](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IsAttached.md) and [IGtol::HasExtraLeader](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~HasExtraLeader.md).

- IGtol::IsAttached() == false implies no leaderline; therefore, there are no leaderline points (PointCount=0).
- IGtol::HasExtraLeader() == false means that this is a straight leaderline; therefore, there is 1 line (PointCount=2).
- IGtol::HasExtraLeader() == True means that this is a bent leaderline; therefore, there are 2 lines (PointCount=3).

The format of return information is the following array of doubles:

*retval*[0] = X-coordinate of first leader point

*retval*[1] = Y-coordinate of first leader point

*retval*[2] = Z-coordinate of first leader point

*retval*[3] = X-coordinate of second leader point

*retval*[4] = Y-coordinate of second leader point

*retval*[5] = Z-coordinate of second leader point

*retval*[6] = X-coordinate of third leader point

*retval*[7] = Y-coordinate of third leader point

*retval*[8] = Z-coordinate of third leader point

Use [IGtol::GetLeaderCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetLeaderCount.md) to see how many leaders are on the [IGTol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md) object.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md)  
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.md)  
[IGtol::GetLeaderAtIndex2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetLeaderAtIndex2.md)  
[IGtol::GetLeaderCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetLeaderCount.md)  
[IGtol::GetLeaderInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetLeaderInfo.md)  
[IGtol::GetLeaderSide Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetLeaderSide.md)  
[IGtol::IGetLeaderAtIndex2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetLeaderAtIndex2.md)  
[IGtol::IGetLineAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetLineAtIndex.md)  
[IGtol::SetLeader Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetLeader.md)
