# GridOptions Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GridOptions`

Obsolete. Superseded by ISketchManager::SetGridOptions.
Obsolete. Superseded by [ISketchManager::SetGridOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SetGridOptions.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GridOptions( _
   ByVal DispGrid As System.Boolean, _
   ByVal GridSpacing As System.Double, _
   ByVal Snap As System.Boolean, _
   ByVal DotStyle As System.Boolean, _
   ByVal NMajor As System.Short, _
   ByVal NMinor As System.Short, _
   ByVal Align2edge As System.Boolean, _
   ByVal AngleSnap As System.Boolean, _
   ByVal AngleUnit As System.Double, _
   ByVal MinorAuto As System.Boolean _
) 
```

```

Dim instance As IModelDoc2
Dim DispGrid As System.Boolean
Dim GridSpacing As System.Double
Dim Snap As System.Boolean
Dim DotStyle As System.Boolean
Dim NMajor As System.Short
Dim NMinor As System.Short
Dim Align2edge As System.Boolean
Dim AngleSnap As System.Boolean
Dim AngleUnit As System.Double
Dim MinorAuto As System.Boolean
 
instance.GridOptions(DispGrid, GridSpacing, Snap, DotStyle, NMajor, NMinor, Align2edge, AngleSnap, AngleUnit, MinorAuto)
```

```

void GridOptions( 
   System.bool DispGrid,
   System.double GridSpacing,
   System.bool Snap,
   System.bool DotStyle,
   System.short NMajor,
   System.short NMinor,
   System.bool Align2edge,
   System.bool AngleSnap,
   System.double AngleUnit,
   System.bool MinorAuto
)
```

```

void GridOptions( 
   System.bool DispGrid,
   System.double GridSpacing,
   System.bool Snap,
   System.bool DotStyle,
   System.short NMajor,
   System.short NMinor,
   System.bool Align2edge,
   System.bool AngleSnap,
   System.double AngleUnit,
   System.bool MinorAuto
) 
```

#### Parameters

*DispGrid*
:   True to display the grid, false to not

*GridSpacing*
:   Snap distance

*Snap*
:   True to snap to grid, false to not

*DotStyle*
:   True for dotted grids, false for not

*NMajor*
:   Number of minors in major

*NMinor*
:   Number of snaps in minor

*Align2edge*
:   True if to align to an edge, false to not

*AngleSnap*
:   True to snap to angle, false to not

*AngleUnit*
:   Value of angle to which to snap

*MinorAuto*
:   True if the minor grids are to be set automatically, false if not

Remarks

The Align2edge argument aligns the grid with the currently selected edge. If Align2edge is set to True, then you must have selected an edge.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::GetGridSettings Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetGridSettings.md)  
[IModelDoc2::ToolsGrid Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ToolsGrid.md)
