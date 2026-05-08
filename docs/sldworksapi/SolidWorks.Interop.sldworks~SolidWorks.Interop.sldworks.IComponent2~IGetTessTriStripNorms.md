# IGetTessTriStripNorms Method (IComponent2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetTessTriStripNorms`

Gets the normal vector for each of the triangles, which make up the shaded picture tessellation for this component.
Gets the normal vector for each of the triangles, which make up the shaded picture tessellation for this component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetTessTriStripNorms() As System.Single
```

```

Dim instance As IComponent2
Dim value As System.Single
 
value = instance.IGetTessTriStripNorms()
```

```

System.float IGetTessTriStripNorms()
```

```

System.float IGetTessTriStripNorms(); 
```

#### Return Value

- in-process, unmanaged C++: Pointer to an array of floats containing the tri-strip normals

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Tessellation information is available only when the component is loaded as lightweight.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IComponent2::GetTessTriStripNorms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetTessTriStripNorms.md)
