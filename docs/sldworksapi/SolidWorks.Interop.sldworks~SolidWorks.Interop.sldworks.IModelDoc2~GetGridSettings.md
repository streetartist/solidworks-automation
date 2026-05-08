# GetGridSettings Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetGridSettings`

Gets the current grid settings.
Gets the current grid settings.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetGridSettings() As System.Object
```

```

Dim instance As IModelDoc2
Dim value As System.Object
 
value = instance.GetGridSettings()
```

```

System.object GetGridSettings()
```

```

System.Object^ GetGridSettings(); 
```

#### Return Value

Current grid settings (see **Remarks**)

Remarks

The return format is the following array of doubles:

[ dispGrid, gridSpacing, snap, dotStyle, nMajor, nMinor, angleSnap, angleUnit, minorAuto ]

where:

- dispGrid - can be interpreted as a BOOLEAN: True if grid displayed, false otherwise
- gridSpacing - snap distance
- snap - can be interpreted as a BOOLEAN: True if snap to grid is on, false otherwise
- dotStyle - can be interpreted as a BOOLEAN: True if dotted grids, false otherwise
- nMajor - number of minors in major
- nMinor - number of snaps in minor
- angleSnap - can be interpreted as a BOOLEAN: True if snap to angle is on, false otherwise
- angleUnit - value of angle to which to snap
- minorAuto - an be interpreted as a BOOLEAN: True if the minor grids are set automatically, false otherwise

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::GridOptions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GridOptions.md)  
[IModelDoc2::ToolsGrid Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ToolsGrid.md)
