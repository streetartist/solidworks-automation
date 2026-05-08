# IGetRenderMaterials Method (IComponent2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetRenderMaterials`

Obsolete. Superseded by IComponent2::GetRenderMaterials2.
Obsolete. Superseded by [IComponent2::GetRenderMaterials2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetRenderMaterials2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetRenderMaterials( _
   ByVal Count As System.Integer _
) As RenderMaterial
```

```

Dim instance As IComponent2
Dim Count As System.Integer
Dim value As RenderMaterial
 
value = instance.IGetRenderMaterials(Count)
```

```

RenderMaterial IGetRenderMaterials( 
   System.int Count
)
```

```

RenderMaterial^ IGetRenderMaterials( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of appearances

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [appearances](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [IComponent2::GetRenderMaterialsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetRenderMaterialsCount.md) to get the value of Count.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IComponent2::GetRenderMaterials Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetRenderMaterials.md)
