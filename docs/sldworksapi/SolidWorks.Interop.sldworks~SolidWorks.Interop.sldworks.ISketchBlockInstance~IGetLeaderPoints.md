# IGetLeaderPoints Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~IGetLeaderPoints`

Gets the coordinate information for the leader on this block instance.
Gets the coordinate information for the leader on this block instance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetLeaderPoints() As System.Double
```

```

Dim instance As ISketchBlockInstance
Dim value As System.Double
 
value = instance.IGetLeaderPoints()
```

```

System.double IGetLeaderPoints()
```

```

System.double IGetLeaderPoints(); 
```

#### Return Value

- in-process, unmanaged C++: Pointer to an array containing leader point information (see **Remarks**)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

For the COM interface, you must specify an array size of 9. Depending on the number of points in the leader, this array might only be partially filled upon return from the API. For the OLE Automation interface, the returned SafeArray is sized appropriately for the number of points returned.

You must determine the number of points in the leader to use the data returned by this method. The number of points is a function of the number of segments in the leader. The leader line can have one or two segments depending on whether it is straight or bent. Use [ISketchBlockInstnace::GetLeaderStyle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetLeaderStyle.md) to determine the number of points in the leader.

|  |  |
| --- | --- |
| If SketchBlockInstance::GetLeaderStyle returns... | Then the number of points equals... |
| swNO\_LEADER | 0 |
| swSTRAIGHT | 2 |
| swBENT | 3 |

 

The format of the return array is:

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

[ISketchBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.md)  
[ISketchBlockInstance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance_members.md)  
[ISketchBlockInstance::GetLeaderPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetLeaderPoints.md)  
[ISketchBlockInstance::SetLeader Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~SetLeader.md)
