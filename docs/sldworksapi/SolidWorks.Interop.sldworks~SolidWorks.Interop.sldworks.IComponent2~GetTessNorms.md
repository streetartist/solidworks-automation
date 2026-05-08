# GetTessNorms Method (IComponent2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetTessNorms`

Gets the normal vector for each of the triangles, which make up the shaded picture tessellation for the component.
Gets the normal vector for each of the triangles, which make up the shaded picture tessellation for the component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTessNorms() As System.Object
```

```

Dim instance As IComponent2
Dim value As System.Object
 
value = instance.GetTessNorms()
```

```

System.object GetTessNorms()
```

```

System.Object^ GetTessNorms(); 
```

#### Return Value

Object of type SafeArray of floats (see **Remarks**)

Remarks

Tessellation information is available only when the component is loaded as lightweight.

The format of retval is:

- float x, y, z - first point's unit normal
- float x, y, z - second point's unit normal
- float x, y, z - third point's unit normal

for the set of triangles for the component.

The total size of the data is [ 9 x sizeof(float) x (number of triangles) ].

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IComponent2::IGetTessNorms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetTessNorms.md)
