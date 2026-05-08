# IGetWitnessLine Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetWitnessLine`

Gets the extension line that connects the leader of this geometric tolerance with the entity that is being dimensioned.
Gets the extension line that connects the leader of this geometric tolerance with the entity that is being dimensioned.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetWitnessLine() As System.Double
```

```

Dim instance As IGtol
Dim value As System.Double
 
value = instance.IGetWitnessLine()
```

```

System.double IGetWitnessLine()
```

```

System.double IGetWitnessLine(); 
```

#### Return Value

- in-process, unmanaged C++: Pointer to array of six doubles (see **Remarks**)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

As you drag a geometric tolerance leader off an entity, SOLIDWORKS dynamically builds a witness or extension line that connects the leader to the entity.

The return value is the following array of six doubles:

[ startPt[3], endPt[3] ]

where:

- startPt[3] = x,y,z start point coordinates of the witness line
- endPt[3] = x,y,z end point coordinates of the witness line

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md)  
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.md)  
[IGtol::GetWitnessLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetWitnessLine.md)
