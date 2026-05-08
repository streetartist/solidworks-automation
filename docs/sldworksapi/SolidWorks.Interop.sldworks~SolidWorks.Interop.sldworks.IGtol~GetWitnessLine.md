# GetWitnessLine Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetWitnessLine`

Gets the extension line that connects the leader of this geometric tolerance with the entity being dimensioned.
Gets the extension line that connects the leader of this geometric tolerance with the entity being dimensioned.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetWitnessLine() As System.Object
```

```

Dim instance As IGtol
Dim value As System.Object
 
value = instance.GetWitnessLine()
```

```

System.object GetWitnessLine()
```

```

System.Object^ GetWitnessLine(); 
```

#### Return Value

An array of six doubles (see **Remarks**)

Remarks

As you drag a geometric tolerance leader off an entity, SOLIDWORKS dynamically builds a witness or extension line that connects the leader to the entity.

The return value is the following array of six doubles:

[ startPt[3], endPt[3] ]

where:

- startPt[3] = x,y,z start point coordinates of the witness line
- endPt[3] = x,y,z end point coordinates of the witness line

Example

[Get GTol Witness Line (VBA)](Get_GTol_Witness_Line_Example_VB.htm)  
[Get GTol Witness Line (VB.NET)](Get_GTol_Witness_Line_Example_VBNET.htm)  
[Get GTol Witness Line (C#)](Get_GTol_Witness_Line_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md)  
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.md)  
[IGtol::IGetWitnessLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetWitnessLine.md)
