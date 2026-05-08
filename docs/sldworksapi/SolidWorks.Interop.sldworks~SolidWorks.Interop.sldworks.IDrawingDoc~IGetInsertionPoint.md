# IGetInsertionPoint Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IGetInsertionPoint`

Gets the current insertion (pick) point in a drawing.
Gets the current insertion (pick) point in a drawing.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetInsertionPoint() As System.Double
```

```

Dim instance As IDrawingDoc
Dim value As System.Double
 
value = instance.IGetInsertionPoint()
```

```

System.double IGetInsertionPoint()
```

```

System.double IGetInsertionPoint(); 
```

#### Return Value

- in-process, unmanaged C++: Pointer to an array of 3 doubles (x,y,z)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Example

You might want to use [ISelectionMgr::IGetSelectionPointInSketchSpace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IGetSelectionPointInSketchSpace2.md) to handle multiple selections.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc::GetInsertionPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetInsertionPoint.md)
