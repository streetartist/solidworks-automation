# GetTessTriStripNorms Method (IComponent2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetTessTriStripNorms`

Gets the normal vector for each of the triangles, which make up the shaded picture tessellation for this component.
Gets the normal vector for each of the triangles, which make up the shaded picture tessellation for this component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTessTriStripNorms() As System.Object
```

```

Dim instance As IComponent2
Dim value As System.Object
 
value = instance.GetTessTriStripNorms()
```

```

System.object GetTessTriStripNorms()
```

```

System.Object^ GetTessTriStripNorms(); 
```

#### Return Value

Array containing the tri-strip normals

Remarks

Tessellation information is available only when the component is loaded as lightweight.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IComponent2::IGetTessTriStripNorms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetTessTriStripNorms.md)
