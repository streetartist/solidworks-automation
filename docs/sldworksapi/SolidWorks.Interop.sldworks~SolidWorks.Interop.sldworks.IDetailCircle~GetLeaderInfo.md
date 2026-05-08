# GetLeaderInfo Method (IDetailCircle)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~GetLeaderInfo`

Gets the leader information for this detail circle.
Gets the leader information for this detail circle.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetLeaderInfo() As System.Object
```

```

Dim instance As IDetailCircle
Dim value As System.Object
 
value = instance.GetLeaderInfo()
```

```

System.object GetLeaderInfo()
```

```

System.Object^ GetLeaderInfo(); 
```

#### Return Value

Array (see **Remarks**)

Remarks

There can be 0, 1 or 2 lines in the leader line. If the GTol is not attached, there are 0 lines. Otherwise, leaders can use a straight leaderline (1 line) or a bent leaderline (2 lines). Your applications must infer the number of leader lines based on [IGtol::IsAttached](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IsAttached.md) and [IGtol::HasExtraLeader](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~HasExtraLeader.md).

- IsAttached() == false implies no leaderline, therefore, no leaderline points (PointCount=0).
- HasExtraLeader() == false means that this is a straight leaderline, therefore, 1 line (PointCount=2)
- HasExtraLeader() == True means that this is a bent leaderline, therefore, 2 lines (PointCount=3)

Format of return information is the following array of doubles:

- retval[0] = X-coordinate of first leader point
- retval[1] = Y-coordinate of first leader point
- retval[2] = Z-coordinate of first leader point
- retval[3] = X-coordinate of second leader point
- retval[4] = Y-coordinate of second leader point
- retval[5] = Z-coordinate of second leader point
- retval[6] = X-coordinate of third leader point
- retval[7] = Y-coordinate of third leader point
- retval[8] = Z-coordinate of third leader point

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDetailCircle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle.md)  
[IDetailCircle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle_members.md)  
[IDetailCircle::IGetLeaderInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~IGetLeaderInfo.md)
