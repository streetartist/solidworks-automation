# IGetNormalVector Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc~IGetNormalVector`

Gets the normal to the arc.
Gets the normal to the arc.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetNormalVector() As System.Double
```

```

Dim instance As ISketchArc
Dim value As System.Double
 
value = instance.IGetNormalVector()
```

```

System.double IGetNormalVector()
```

```

System.double IGetNormalVector(); 
```

#### Return Value

- in-process, unmanaged C++: Pointer to an array of 3 doubles (x,y,z), which represents the unit vector normal to the arc

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchArc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc.md)  
[ISketchArc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc_members.md)  
[ISketchArc::GetNormalVector Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc~GetNormalVector.md)
