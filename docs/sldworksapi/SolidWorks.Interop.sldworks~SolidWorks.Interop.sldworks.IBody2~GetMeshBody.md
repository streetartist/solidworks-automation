# GetMeshBody Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetMeshBody`

Gets the mesh body associated with this body.
Gets the mesh body associated with this body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetMeshBody() As System.Object
```

```

Dim instance As IBody2
Dim value As System.Object
 
value = instance.GetMeshBody()
```

```

System.object GetMeshBody()
```

```

System.Object^ GetMeshBody(); 
```

#### Return Value

[IMeshBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeshBody.md)

Remarks

This method is valid only if [IBody2::IsMeshBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IsMeshBody.md) is true.

Example

See the [IFacet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFacet.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)
